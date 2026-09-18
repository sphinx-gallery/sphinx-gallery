"""Utilities.

Miscellaneous utilities.
"""

# Author: Eric Larson
# License: 3-clause BSD

import contextlib
import hashlib
import json
import os
import re
import subprocess
import zipfile
from functools import partial
from pathlib import Path
from shutil import copyfile, move
from typing import (
    Any,
    Callable,
    ContextManager,
    Iterator,
    Literal,
    Sequence,
    Tuple,
    TypedDict,
)

import sphinx.util

try:
    from sphinx.util.display import status_iterator  # noqa: F401
except Exception:  # Sphinx < 6
    from sphinx.util import status_iterator  # noqa: F401

from .typing import GalleryConfig, PathLikeStr

logger = sphinx.util.logging.getLogger("sphinx-gallery")

WARNING_TYPE = "sphinx_gallery"
"""Warning ``type`` for every warning Sphinx-Gallery emits.

Pass it together with a ``subtype`` naming the kind of problem::

    logger.warning("...", type=WARNING_TYPE, subtype="config")

Readers can then silence a kind of warning with ``suppress_warnings =
["sphinx_gallery.config"]`` in their ``conf.py``, or all of ours with
``["sphinx_gallery"]``. Keep the subtypes documented in
``doc/configuration.rst`` in sync with the ones used here.
"""


class _WriteKwargs(TypedDict):
    """Text writing kwargs for builtins.open."""

    encoding: str
    newline: str


_W_KW: _WriteKwargs = {"encoding": "utf-8", "newline": "\n"}


def _single_threaded() -> ContextManager:
    """Run a block of native code without leaving a thread pool behind.

    Sphinx forks its parallel read and write workers -- ``get_context("fork")`` is
    hardcoded in ``sphinx/util/parallel.py`` -- and ``fork()`` only clones the calling
    thread. An OpenMP worker thread that is alive in the Sphinx process at that moment
    is therefore lost in the child, while the OpenMP runtime still believes it exists;
    the next parallel region in that child blocks forever in the OpenMP join barrier.
    Since Sphinx Gallery declares itself ``parallel_read_safe``, any BLAS call it makes
    in the Sphinx process on its own behalf must not leave such a thread behind.

    Capping the thread pools for the duration of the call means no OpenMP team is ever
    created, so there is nothing for a later ``fork()`` to lose. This is a no-op when
    ``threadpoolctl`` is not installed; the deadlock only shows up with a threaded BLAS
    (notably MKL), so a fallback that silently does nothing is acceptable.
    """
    try:
        import threadpoolctl
    except ImportError:
        return contextlib.nullcontext()
    return threadpoolctl.threadpool_limits(limits=1)


def scale_image(
    in_fname: PathLikeStr,
    out_fname: PathLikeStr,
    max_width: int,
    max_height: int,
) -> None:
    """Scales image centered in image box using `max_width` and `max_height`.

    The same aspect ratio is retained. If `in_fname` == `out_fname` the image can only
    be scaled down.
    """
    # local import to avoid testing dependency on PIL:
    from PIL import Image

    in_fname = Path(in_fname)
    out_fname = Path(out_fname)

    img = Image.open(in_fname)
    # XXX someday we should just try img.thumbnail((max_width, max_height)) ...
    width_in, height_in = img.size
    scale_w = max_width / float(width_in)
    scale_h = max_height / float(height_in)

    if height_in * scale_w <= max_height:
        scale = scale_w
    else:
        scale = scale_h

    if scale >= 1.0 and in_fname == out_fname:
        return

    width_sc = int(round(scale * width_in))
    height_sc = int(round(scale * height_in))

    # resize the image using resize; if using .thumbnail and the image is
    # already smaller than max_width, max_height, then this won't scale up
    # at all (maybe could be an option someday...)
    bicubic = Image.Resampling.BICUBIC
    img = img.resize((width_sc, height_sc), bicubic)
    # img.thumbnail((width_sc, height_sc), Image.BICUBIC)
    # width_sc, height_sc = img.size  # necessary if using thumbnail

    # insert centered
    thumb = Image.new("RGBA", (max_width, max_height), (255, 255, 255, 0))
    pos_insert = ((max_width - width_sc) // 2, (max_height - height_sc) // 2)
    thumb.paste(img, pos_insert)

    try:
        thumb.save(out_fname)
    except OSError:
        # try again, without the alpha channel (e.g., for JPEG)
        thumb.convert("RGB").save(out_fname)


def optipng(fname: Path, args: Tuple = ()) -> None:
    """Optimize a PNG in place.

    Parameters
    ----------
    fname : Path
        The filename. If it ends with '.png', ``optipng -o7 fname`` will
        be run. If it fails because the ``optipng`` executable is not found
        or optipng fails, the function returns.
    args : tuple
        Extra command-line arguments, such as ``['-o7']``.
    """
    if fname.suffix == ".png":
        # -o7 because this is what CPython used
        # https://github.com/python/cpython/pull/8032
        try:
            subprocess.check_call(
                ["optipng"] + list(args) + [fname],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass


def _has_optipng() -> bool:
    try:
        subprocess.check_call(
            ["optipng", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    except FileNotFoundError:
        return False
    else:
        return True


def get_md5sum(src_file: PathLikeStr, mode: Literal["t", "b"] = "b") -> str:
    """Returns md5sum of file.

    Parameters
    ----------
    src_file : str | pathlib.Path
        Filename to get md5sum for.
    mode : 't' or 'b'
        File mode to open file with. When in text mode, universal line endings
        are used to ensure consistency in hashes between platforms.
    """
    assert mode in ("t", "b")
    src_file = Path(src_file)
    if mode == "t":
        # Universal newline mode is intentional here for text mode
        src_content = src_file.read_text(
            errors="surrogateescape", encoding="utf-8"
        ).encode(errors="surrogateescape", encoding="utf-8")
    else:
        src_content = src_file.read_bytes()
    return hashlib.md5(src_content).hexdigest()


def _replace_md5(
    fname_new: PathLikeStr,
    fname_old: PathLikeStr | None = None,
    *,
    method: Literal["move", "copy"] = "move",
    mode: Literal["t", "b"] = "b",
    check: Literal["md5", "json"] = "md5",
) -> bool:
    """Replace ``fname_old`` with ``fname_new``, returning whether it changed."""
    fname_new = Path(fname_new)
    assert method in ("move", "copy")
    if fname_old is None:
        assert fname_new.suffix == ".new"
        fname_old = fname_new.with_suffix("")
    else:
        fname_old = Path(fname_old)
    replace = True
    if fname_old.is_file():
        func: Callable[[Path], Any]
        if check == "md5":  # default
            func = partial(get_md5sum, mode=mode)
        else:
            assert check == "json"

            def func(x):
                return json.loads(x.read_text("utf-8"))

        try:
            equiv = func(fname_old) == func(fname_new)
        except Exception:  # e.g., old JSON file is a problem
            equiv = False
        if equiv:
            replace = False
            if method == "move":
                fname_new.unlink()
        else:
            logger.debug(f"Replacing stale {fname_old} with {fname_new}")
    if replace:
        if method == "move":
            move(fname_new, fname_old)
        else:
            copyfile(fname_new, fname_old)
    assert fname_old.is_file()
    return replace


def iter_gallery_header_filenames(gallery_conf: GalleryConfig) -> Iterator[str]:
    """
    A generator of all possible gallery header filenames.

    We support GALLERY_HEADER.[ext], and for backward-compatibility README.[ext]
    """
    extensions = [".txt"] + sorted(gallery_conf["source_suffix"])
    for ext in extensions:
        for fname in ("GALLERY_HEADER", "README", "readme"):
            yield fname + ext


def check_duplicate_filenames(files: Sequence[PathLikeStr]) -> None:
    """Check for duplicate filenames across gallery directories."""
    # Check whether we'll have duplicates
    used_names = set()
    dup_names = list()

    for this_file in files:
        this_fname = Path(this_file).name
        if this_fname in used_names:
            dup_names.append(this_file)
        else:
            used_names.add(this_fname)

    if len(dup_names) > 0:
        logger.warning(
            "Duplicate example file name(s) found. Having duplicate file "
            "names will break some links. "
            "List of files: %s",
            sorted(str(name) for name in dup_names),
            type=WARNING_TYPE,
            subtype="duplicate_filename",
        )


def check_spaces_in_filenames(files: Sequence[PathLikeStr]) -> None:
    """Check for spaces in filenames across example directories."""
    regex = re.compile(r"[\s]")
    files_with_space = [str(file) for file in files if regex.search(str(file))]
    if files_with_space:
        logger.warning(
            "Example file name(s) with spaces found. Having spaces in "
            "file names will break some links. "
            "List of files: %s",
            sorted(files_with_space),
            type=WARNING_TYPE,
            subtype="space_in_filename",
        )


def _collect_gallery_files(
    examples_dirs: Sequence[PathLikeStr],
    gallery_conf: GalleryConfig,
    check_filenames: bool = False,
) -> list[str]:
    """Collect files with `example_extensions`, accounting for `ignore_pattern`.

    If `check_filenames` we check one level of sub-folders as well as root
    `example_dirs` for gallery example files. We then check for duplicate and
    spaces in full file paths.
    """
    exts = gallery_conf["example_extensions"]
    max_depth = 1 if check_filenames else 0
    files = []
    gallery_header_filenames = list(iter_gallery_header_filenames(gallery_conf))
    for example_dir in examples_dirs:
        example_dir = Path(example_dir)
        for dirpath, _, filenames in os.walk(example_dir):
            # `os.walk` yields paths below `example_dir`, so the number of parts
            # relative to it is the depth
            root = Path(dirpath)
            if len(root.parts) - len(example_dir.parts) > max_depth:
                break
            for filename in filenames:
                if filename in gallery_header_filenames:
                    continue
                if (s := Path(filename).suffix) and s in exts:
                    if re.search(gallery_conf["ignore_pattern"], filename) is None:
                        file = str(root / filename) if check_filenames else filename
                        files.append(file)
    if check_filenames:
        check_duplicate_filenames(files)
        check_spaces_in_filenames(files)
    return files


def zip_files(
    file_list: Sequence[PathLikeStr],
    zipname: PathLikeStr,
    relative_to: PathLikeStr,
    extension: str | None = None,
) -> str:
    """
    Creates a zip file with the given files.

    A zip file named `zipname` will be created containing the files listed in
    `file_list`. The zip file contents will be stored with their paths stripped to be
    relative to `relative_to`.
    """
    zipname = Path(zipname)
    zipname_new = zipname.with_name(zipname.name + ".new")
    with zipfile.ZipFile(zipname_new, mode="w") as zipf:
        for fname in file_list:
            fname = Path(fname)
            if extension is not None:
                fname = fname.with_suffix(extension)
            zipf.write(fname, Path(os.path.relpath(fname, relative_to)).as_posix())
    _replace_md5(zipname_new)
    return str(zipname)


def _has_pypandoc() -> Tuple[bool | None, str | None]:
    """Check if pypandoc package available."""
    try:
        import pypandoc  # noqa

        # Import error raised only when function called
        version = pypandoc.get_pandoc_version()
    except (ImportError, OSError):
        return None, None
    else:
        return True, version


def _has_graphviz() -> bool:
    try:
        import graphviz  # noqa F401
    except ImportError as exc:
        logger.info(
            "`graphviz` Python package required for graphical visualization "
            f"but could not be imported, got: {exc}"
        )
        return False
    try:
        subprocess.check_call(
            ["neato", "-V"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    except FileNotFoundError as exc:
        logger.info(
            "`neato` layout engine required for graphical visualization "
            f"but command-line executable could not be found ({exc})"
        )
        return False
    return True


def _format_toctree(items: list[str], includehidden: bool = False) -> str:
    """Format a toc tree."""
    st = """
.. toctree::
   :hidden:"""
    if includehidden:
        st += """
   :includehidden:
"""
    st += """

   {}\n""".format("\n   ".join(items))

    st += "\n"

    return st


# Should be matched with `_read_json`
def _write_json(target_file: PathLikeStr, to_save: dict, name: str = "") -> None:
    """Write dictionary to JSON file."""
    target_file = Path(target_file)
    codeobj_fname = target_file.with_name(target_file.stem + f"{name}.json.new")
    with open(codeobj_fname, "w", **_W_KW) as fid:
        json.dump(
            to_save,
            fid,
            sort_keys=True,
            ensure_ascii=False,
            indent=1,
            check_circular=False,
        )
    _replace_md5(codeobj_fname, check="json")


def _read_json(json_fname: PathLikeStr) -> Any:
    """Read JSON dictionary from file."""
    return json.loads(Path(json_fname).read_text(encoding="utf-8"))


def _combine_backreferences(dict_a: dict, dict_b: dict | None) -> dict:
    """Combine backreferences dictionaries, joining lists when keys are the same."""
    # `dict_b` is None when `backreferences_dir` config not set
    if isinstance(dict_b, dict):
        for key, value in dict_b.items():
            dict_a.setdefault(key, []).extend(value)
    return dict_a
