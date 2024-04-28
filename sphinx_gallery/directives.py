"""Custom Sphinx directives."""

import os
from pathlib import PurePosixPath, Path
import shutil

from docutils import nodes
from docutils import statemachine
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives import images

from sphinx.errors import ExtensionError


from .backreferences import (
    _thumbnail_div,
    THUMBNAIL_PARENT_DIV,
    THUMBNAIL_PARENT_DIV_CLOSE,
)
from .gen_rst import extract_intro_and_title
from .py_source_parser import split_code_and_text_blocks


class MiniGallery(Directive):
    """Custom directive to insert a mini-gallery.

    The required argument is one or more of the following:

    * fully qualified names of objects
    * pathlike strings to example Python files
    * glob-style pathlike strings to example Python files

    The string list of arguments is separated by spaces.

    The mini-gallery will be the subset of gallery
    examples that make use of that object from that specific namespace

    Options:

    * `add-heading` adds a heading to the mini-gallery.  If an argument is
      provided, it uses that text for the heading.  Otherwise, it uses
      default text.
    * `heading-level` specifies the heading level of the heading as a single
      character.  If omitted, the default heading level is `'^'`.
    """

    required_arguments = 0
    has_content = True
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "add-heading": directives.unchanged,
        "heading-level": directives.single_char_or_unicode,
    }

    def run(self):
        """Generate mini-gallery from backreference and example files."""
        from .gen_rst import _get_callables

        if not (self.arguments or self.content):
            raise ExtensionError("No arguments passed to 'minigallery'")

        # Respect the same disabling options as the `raw` directive
        if (
            not self.state.document.settings.raw_enabled
            or not self.state.document.settings.file_insertion_enabled
        ):
            raise self.warning(f'"{self.name}" directive disabled.')

        # Retrieve the backreferences directory
        config = self.state.document.settings.env.config
        backreferences_dir = config.sphinx_gallery_conf["backreferences_dir"]

        # Retrieve source directory
        src_dir = config.sphinx_gallery_conf["src_dir"]

        # Parse the argument into the individual objects

        obj_list = []

        if self.arguments:
            obj_list.extend([c.strip() for c in self.arguments[0].split()])
        if self.content:
            obj_list.extend([c.strip() for c in self.content])

        lines = []

        # Add a heading if requested
        if "add-heading" in self.options:
            heading = self.options["add-heading"]
            if heading == "":
                if len(obj_list) == 1:
                    heading = f"Examples using ``{obj_list[0]}``"
                else:
                    heading = "Examples using one of multiple objects"
            lines.append(heading)
            heading_level = self.options.get("heading-level", "^")
            lines.append(heading_level * len(heading))

        def has_backrefs(obj):
            path = Path(src_dir, backreferences_dir, f"{obj}.examples")
            return path if (path.is_file() and (path.stat().st_size > 0)) else False

        file_paths = []
        for obj in obj_list:
            if path := has_backrefs(obj):
                file_paths.append((obj, path))
            elif paths := Path(src_dir).glob(obj):
                file_paths.extend([(obj, p) for p in paths])

        if len(file_paths) == 0:
            return []

        lines.append(THUMBNAIL_PARENT_DIV)

        # sort on the str(file_path) but keep (obj, path) pair
        if config.sphinx_gallery_conf["minigallery_sort_order"] is None:
            sortkey = None
        else:
            (sortkey,) = _get_callables(
                config.sphinx_gallery_conf, "minigallery_sort_order"
            )
        for obj, path in sorted(
            set(file_paths),
            key=((lambda x: sortkey(os.path.abspath(x[-1]))) if sortkey else None),
        ):
            if path.suffix == ".examples":
                # Insert the backreferences file(s) using the `include` directive.
                # / is the src_dir for include
                lines.append(
                    f"""\
.. include:: /{path.relative_to(src_dir).as_posix()}
    :start-after: thumbnail-parent-div-open
    :end-before: thumbnail-parent-div-close"""
                )
            else:
                dirs = [
                    (e, g)
                    for e, g in zip(
                        config.sphinx_gallery_conf["examples_dirs"],
                        config.sphinx_gallery_conf["gallery_dirs"],
                    )
                    if (obj.find(e) != -1)
                ]
                if len(dirs) != 1:
                    raise ExtensionError(
                        f"Error in gallery lookup: input={obj}, matches={dirs}, "
                        f"examples={config.sphinx_gallery_conf['examples_dirs']}"
                    )

                example_dir, target_dir = [Path(src_dir, d) for d in dirs[0]]

                # finds thumbnails in subdirs
                target_dir = target_dir / path.relative_to(example_dir).parent
                _, script_blocks = split_code_and_text_blocks(
                    str(path), return_node=False
                )
                intro, title = extract_intro_and_title(str(path), script_blocks[0][1])

                thumbnail = _thumbnail_div(target_dir, src_dir, path.name, intro, title)
                lines.append(thumbnail)

        lines.append(THUMBNAIL_PARENT_DIV_CLOSE)
        text = "\n".join(lines)
        include_lines = statemachine.string2lines(text, convert_whitespace=True)
        self.state_machine.insert_input(include_lines, str(path))

        return []


"""
Image sg for responsive images
"""


class imgsgnode(nodes.General, nodes.Element):
    """Sphinx Gallery image node class."""

    pass


class ImageSg(images.Image):
    """Implements a directive to allow an optional hidpi image.

    Meant to be used with the `image_srcset` configuration option.

    e.g.::

        .. image-sg:: /plot_types/basic/images/sphx_glr_bar_001.png
            :alt: bar
            :srcset: /plot_types/basic/images/sphx_glr_bar_001.png,
                     /plot_types/basic/images/sphx_glr_bar_001_2_00x.png 2.00x
            :class: sphx-glr-single-img

    The resulting html is::

        <img src="sphx_glr_bar_001_hidpi.png"
            srcset="_images/sphx_glr_bar_001.png,
                    _images/sphx_glr_bar_001_2_00x.png 2x",
            alt="bar"
            class="sphx-glr-single-img" />
    """

    has_content = False
    required_arguments = 1
    optional_arguments = 3
    final_argument_whitespace = False
    option_spec = {
        "srcset": directives.unchanged,
        "class": directives.class_option,
        "alt": directives.unchanged,
    }

    def run(self):
        """Update node contents."""
        image_node = imgsgnode()

        imagenm = self.arguments[0]
        image_node["alt"] = self.options.get("alt", "")
        image_node["class"] = self.options.get("class", None)

        # we would like uri to be the highest dpi version so that
        # latex etc will use that.  But for now, lets just make
        # imagenm

        image_node["uri"] = imagenm
        image_node["srcset"] = self.options.get("srcset", None)

        return [image_node]


def _parse_srcset(st):
    """Parse st."""
    entries = st.split(",")
    srcset = {}
    for entry in entries:
        spl = entry.strip().split(" ")
        if len(spl) == 1:
            srcset[0] = spl[0]
        elif len(spl) == 2:
            mult = spl[1][:-1]
            srcset[float(mult)] = spl[0]
        else:
            raise ExtensionError('srcset argument "{entry}" is invalid.')
    return srcset


def visit_imgsg_html(self, node):
    """Handle HTML image tag depending on 'srcset' configuration.

    If 'srcset' is not `None`, copy images, generate image html tag with 'srcset'
    and add to HTML `body`. If 'srcset' is `None` run `visit_image` on `node`.
    """
    if node["srcset"] is None:
        self.visit_image(node)
        return

    imagedir, srcset = _copy_images(self, node)

    # /doc/examples/subd/plot_1.rst
    docsource = self.document["source"]
    # /doc/
    # make sure to add the trailing slash:
    srctop = os.path.join(self.builder.srcdir, "")
    # examples/subd/plot_1.rst
    relsource = os.path.relpath(docsource, srctop)
    # /doc/build/html
    desttop = os.path.join(self.builder.outdir, "")
    # /doc/build/html/examples/subd
    dest = os.path.join(desttop, relsource)

    # ../../_images/ for dirhtml and ../_images/ for html
    imagerel = os.path.relpath(imagedir, os.path.dirname(dest))
    if self.builder.name == "dirhtml":
        imagerel = os.path.join("..", imagerel, "")
    else:  # html
        imagerel = os.path.join(imagerel, "")

    if "\\" in imagerel:
        imagerel = imagerel.replace("\\", "/")
    # make srcset str.  Need to change all the prefixes!
    srcsetst = ""
    for mult in srcset:
        nm = os.path.basename(srcset[mult][1:])
        # ../../_images/plot_1_2_0x.png
        relpath = imagerel + nm
        srcsetst += f"{relpath}"
        if mult == 0:
            srcsetst += ", "
        else:
            srcsetst += f" {mult:1.2f}x, "
    # trim trailing comma and space...
    srcsetst = srcsetst[:-2]

    # make uri also be relative...
    nm = os.path.basename(node["uri"][1:])
    uri = imagerel + nm

    alt = node["alt"]
    if node["class"] is not None:
        classst = node["class"][0]
        classst = f'class = "{classst}"'
    else:
        classst = ""

    html_block = f'<img src="{uri}" srcset="{srcsetst}" alt="{alt}"' + f" {classst}/>"
    self.body.append(html_block)


def visit_imgsg_latex(self, node):
    """Copy images, set node[uri] to highest resolution image and call `visit_image`."""
    if node["srcset"] is not None:
        imagedir, srcset = _copy_images(self, node)
        maxmult = -1
        # choose the highest res version for latex:
        for key in srcset.keys():
            maxmult = max(maxmult, key)
        node["uri"] = str(PurePosixPath(srcset[maxmult]).name)

    self.visit_image(node)


def _copy_images(self, node):
    srcset = _parse_srcset(node["srcset"])

    # where the sources are.  i.e. myproj/source
    srctop = self.builder.srcdir

    # copy image from source to imagedir.  This is
    # *probably* supposed to be done by a builder but...
    # ie myproj/build/html/_images
    imagedir = os.path.join(self.builder.imagedir, "")
    imagedir = PurePosixPath(self.builder.outdir, imagedir)

    os.makedirs(imagedir, exist_ok=True)

    # copy all the sources to the imagedir:
    for mult in srcset:
        abspath = PurePosixPath(srctop, srcset[mult][1:])
        shutil.copyfile(abspath, imagedir / abspath.name)

    return imagedir, srcset


def depart_imgsg_html(self, node):
    """HTML depart node visitor function."""
    pass


def depart_imgsg_latex(self, node):
    """LaTeX depart node visitor function."""
    self.depart_image(node)


def imagesg_addnode(app):
    """Add `imgsgnode` to Sphinx app with visitor functions for HTML and LaTeX."""
    app.add_node(
        imgsgnode,
        html=(visit_imgsg_html, depart_imgsg_html),
        latex=(visit_imgsg_latex, depart_imgsg_latex),
    )
