# Author: Óscar Nájera
# License: 3-clause BSD
"""Link resolver objects."""

import gzip
import json
import os
import posixpath
import re
import shelve
import urllib.parse as urllib_parse
import urllib.request as urllib_request
from io import BytesIO
from pathlib import Path
from urllib.error import HTTPError, URLError

import sphinx.util
from sphinx.errors import ExtensionError
from sphinx.search import js_index

from .utils import _W_KW, _replace_md5, status_iterator

logger = sphinx.util.logging.getLogger("sphinx-gallery")


def _get_data(url):
    """Get data over http(s) or from a local file."""
    if urllib_parse.urlparse(url).scheme in ("http", "https"):
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"  # noqa: E501
        headers = {"User-Agent": user_agent}
        req = urllib_request.Request(url, None, headers)
        resp = urllib_request.urlopen(req)
        encoding = resp.headers.get("content-encoding", "plain")
        data = resp.read()
        if encoding == "gzip":
            data = gzip.GzipFile(fileobj=BytesIO(data)).read()
        elif encoding != "plain":
            raise ExtensionError(f"unknown encoding {encoding!r}")
        data = data.decode("utf-8")
    else:
        with open(url, mode="r", encoding="utf-8") as fid:
            data = fid.read()

    return data


def get_data(url, gallery_dir):
    """Persistent dictionary usage to retrieve the search indexes."""
    cached_file = os.path.join(gallery_dir, "searchindex")
    search_index = shelve.open(cached_file)
    if url in search_index:
        data = search_index[url]
    else:
        data = _get_data(url)
        search_index[url] = data
    search_index.close()

    return data


def parse_sphinx_docopts(index):
    """Parse the Sphinx index for documentation options.

    Parameters
    ----------
    index : str
        The Sphinx index page

    Returns
    -------
    docopts : dict
        The documentation options from the page.
    """
    pos = index.find("var DOCUMENTATION_OPTIONS")
    if pos < 0:
        pos = index.find("const DOCUMENTATION_OPTIONS")  # Sphinx 7.2+
    if pos < 0:
        raise ExtensionError("Documentation options could not be found in index.")
    pos = index.find("{", pos)
    if pos < 0:
        raise ExtensionError("Documentation options could not be found in index.")
    endpos = index.find("};", pos)
    if endpos < 0:
        raise ExtensionError("Documentation options could not be found in index.")
    block = index[pos + 1 : endpos].strip()
    docopts = {}
    for line in block.splitlines():
        key, value = line.split(":", 1)
        key = key.strip().strip('"')

        value = value.strip()
        if value[-1] == ",":
            value = value[:-1].rstrip()
        if value[0] in "\"'":
            value = value[1:-1]
        elif value == "false":
            value = False
        elif value == "true":
            value = True
        else:
            try:
                value = int(value)
            except ValueError:
                # In Sphinx 1.7.5, URL_ROOT is a JavaScript fragment.
                # Ignoring this entry since URL_ROOT is not used
                # elsewhere.
                # https://github.com/sphinx-gallery/sphinx-gallery/issues/382
                continue

        docopts[key] = value

    return docopts


class SphinxDocLinkResolver:
    """Resolve documentation links using searchindex.js generated by Sphinx.

    Parameters
    ----------
    doc_url : str
        The base URL of the project website.
    relative : bool
        Return relative links (only useful for links to documentation of this
        package).
    """

    def __init__(self, config, doc_url, gallery_dir, relative=False):
        self.config = config
        self.doc_url = doc_url
        self.gallery_dir = gallery_dir
        self.relative = relative
        self._link_cache = {}

        if isinstance(doc_url, Path):
            index_url = os.path.join(doc_url, "index.html")
            searchindex_url = os.path.join(doc_url, "searchindex.js")
            docopts_url = os.path.join(doc_url, "_static", "documentation_options.js")
        else:
            if relative:
                raise ExtensionError(
                    "Relative links are only supported for local "
                    "URLs (doc_url cannot be absolute)"
                )
            index_url = doc_url + "/"
            searchindex_url = doc_url + "/searchindex.js"
            docopts_url = doc_url + "/_static/documentation_options.js"

        # detect if we are using relative links on a Windows system
        if os.name.lower() == "nt" and isinstance(doc_url, Path):
            if not relative:
                raise ExtensionError(
                    "You have to use relative=True for the local"
                    " package on a Windows system."
                )
            self._is_windows = True
        else:
            self._is_windows = False

        # Download and find documentation options. As of Sphinx 1.7, these
        # options are now kept in a standalone file called
        # 'documentation_options.js'. Since SphinxDocLinkResolver can be called
        # not only for the documentation which is being built but also ones
        # that are being referenced, we need to try and get the index page
        # first and if that doesn't work, check for the
        # documentation_options.js file.
        index = get_data(index_url, gallery_dir)
        if "var DOCUMENTATION_OPTIONS" in index:
            self._docopts = parse_sphinx_docopts(index)
        else:
            docopts = get_data(docopts_url, gallery_dir)
            self._docopts = parse_sphinx_docopts(docopts)

        # download and initialize the search index
        sindex = get_data(searchindex_url, gallery_dir)
        self._searchindex = js_index.loads(sindex)

    def _get_index_match(self, first, second):
        try:
            match = self._searchindex["objects"][first]
        except KeyError:
            return None
        else:
            if isinstance(match, dict):
                try:
                    match = match[second]
                except KeyError:
                    return None
            elif isinstance(match, (list, tuple)):  # Sphinx 5.0.0 dev
                try:
                    for item in match:
                        if item[4] == second:
                            match = item[:4]
                            break
                    else:
                        return None
                except Exception:
                    return None
        return match

    def _get_link_type(self, cobj, use_full_module=False):
        """Get a valid link and type_, False if not found."""
        module_type = "module" if use_full_module else "module_short"
        first, second = cobj[module_type], cobj["name"]
        match = self._get_index_match(first, second)
        if match is None and "." in second:  # possible class attribute
            first, second = second.split(".", 1)
            first = ".".join([cobj[module_type], first])
            match = self._get_index_match(first, second)
        if match is None:
            link = type_ = None
        else:
            fname_idx = match[0]
            objname_idx = str(match[1])
            anchor = match[3]
            type_ = self._searchindex["objtypes"][objname_idx]

            fname = self._searchindex["filenames"][fname_idx]
            # In 1.5+ Sphinx seems to have changed from .rst.html to only
            # .html extension in converted files. Find this from the options.
            ext = self._docopts.get("FILE_SUFFIX", ".rst.html")
            fname = os.path.splitext(fname)[0] + ext
            if self._is_windows:
                fname = fname.replace("/", "\\")
                link = os.path.join(self.doc_url, fname)
            else:
                link = posixpath.join(self.doc_url, fname)

            fullname = ".".join([first, second])
            if anchor == "":
                anchor = fullname
            elif anchor == "-":
                anchor = self._searchindex["objnames"][objname_idx][1] + "-" + fullname

            link = link + "#" + anchor

        return link, type_

    def resolve(self, cobj, this_url, return_type=False):
        """Resolve the link to the documentation, returns None if not found.

        Parameters
        ----------
        cobj : Dict[str, Any]
            Dict with information about the "code object" for which we are
            resolving a link.

                - cobj['name'] : function or class name (str)
                - cobj['module'] : module name (str)
                - cobj['module_short'] : shortened module name (str)
                - cobj['is_class'] : whether object is class (bool)
                - cobj['is_explicit'] : whether object is an explicit
                  backreference (referred to by sphinx markup) (bool)
        this_url: str
            URL of the current page. Needed to construct relative URLs
            (only used if relative=True in constructor).
        return_type : bool
            If True, return the type as well.

        Returns
        -------
        link : str or None
            The link (URL) to the documentation.
        type_ : str
            The type. Only returned if return_type is True.
        """
        full_name = cobj["module_short"] + "." + cobj["name"]
        if full_name not in self._link_cache:
            # we don't have it cached
            use_full_module = False
            for pattern in self.config["prefer_full_module"]:
                if re.search(pattern, cobj["module"] + "." + cobj["name"]):
                    use_full_module = True
                    break
            self._link_cache[full_name] = self._get_link_type(cobj, use_full_module)
        link, type_ = self._link_cache[full_name]

        if self.relative and link is not None:
            link = os.path.relpath(link, start=this_url)
            if self._is_windows:
                # replace '\' with '/' so it on the web
                link = link.replace("\\", "/")

            # for some reason, the relative link goes one directory too high up
            link = link[3:]

        return (link, type_) if return_type else link


def _handle_http_url_error(e, msg="fetching"):
    if isinstance(e, HTTPError):
        error_msg = f"{msg} {e.url}: {e.code} ({e.msg})"
    elif isinstance(e, URLError):
        error_msg = f"{msg}: {e.reason}"
    logger.warning(
        "The following {} has occurred {}".format(type(e).__name__, error_msg)
    )


def _sanitize_css_class(s):
    for x in "~!@$%^&*()+=,./';:\"?><[]\\{}|`#":
        s = s.replace(x, "-")
    return s


def _get_intersphinx_inventory(app):
    """
    Get the mapping between module names and intersphinx inventories.

    In some cases, intersphinx inventories may provide documentation for modules _other_
    than the one given by the intersphinx_mapping key (e.g., the Python inventory
    contains documentation for all standard library modules, or Matplotlib contains
    several `mpl_toolkits`` modules), so this checks py:module for all inventories and
    adds that additional module mapping.
    """
    if inventory := getattr(app.env, "sg_intersphinx_inventory", None):
        return inventory

    # Make a copy of the inventories, because this dict is created by intersphinx and we
    # don't want to break whatever assumptions it has made about it.
    intersphinx_inv_orig = getattr(app.env, "intersphinx_named_inventory", dict())
    intersphinx_inv = intersphinx_inv_orig.copy()
    for module_name, inventory in intersphinx_inv_orig.items():
        documented_modules = {
            qualname.split(".")[0] for qualname in inventory.get("py:module", dict())
        }
        for other_module_name in documented_modules - {module_name}:
            intersphinx_inv[other_module_name] = inventory

    app.env.sg_intersphinx_inventory = intersphinx_inv
    return intersphinx_inv


# Whatever mechanism is used for writing here should be paired with reading in
# _embed_code_links
def _write_code_obj(target_file, example_code_obj):
    codeobj_fname = target_file.with_name(target_file.stem + ".codeobj.json.new")
    with open(codeobj_fname, "w", **_W_KW) as fid:
        json.dump(
            example_code_obj,
            fid,
            sort_keys=True,
            ensure_ascii=False,
            indent=1,
            check_circular=False,
        )
    _replace_md5(codeobj_fname, check="json")


def _embed_code_links(app, gallery_conf, gallery_dir):
    """Add resolvers for the packages for which we want to show links."""
    doc_resolvers = {}

    src_gallery_dir = os.path.join(app.builder.srcdir, gallery_dir)
    for this_module, url in gallery_conf["reference_url"].items():
        try:
            if url is None:
                doc_resolvers[this_module] = SphinxDocLinkResolver(
                    app.config.sphinx_gallery_conf,
                    Path(app.builder.outdir),
                    src_gallery_dir,
                    relative=True,
                )
            else:
                doc_resolvers[this_module] = SphinxDocLinkResolver(
                    app.config.sphinx_gallery_conf, url, src_gallery_dir
                )

        except (URLError, HTTPError) as e:
            _handle_http_url_error(e)

    html_gallery_dir = os.path.abspath(os.path.join(app.builder.outdir, gallery_dir))

    # patterns for replacement
    link_pattern = '<a href="{link}" title="{title}" class="{css_class}">{text}</a>'
    orig_pattern = '<span class="n">%s</span>'
    period = '<span class="o">.</span>'

    # This could be turned into a generator if necessary, but should be okay
    flat = [
        [dirpath, filename]
        for dirpath, _, filenames in os.walk(html_gallery_dir)
        for filename in filenames
        if filename.endswith(".html")
    ]
    iterator = status_iterator(
        flat,
        f"embedding documentation hyperlinks for {gallery_dir}... ",
        color="fuchsia",
        length=len(flat),
        stringify_func=lambda x: os.path.basename(x[1]),
    )
    intersphinx_inv = _get_intersphinx_inventory(app)
    for dirpath, fname in iterator:
        full_fname = os.path.join(html_gallery_dir, dirpath, fname)
        subpath = dirpath[len(html_gallery_dir) + 1 :]
        json_fname = os.path.join(
            src_gallery_dir, subpath, fname[:-5] + ".codeobj.json"
        )
        if not os.path.exists(json_fname):
            continue

        # we have a json file with the objects to embed links for
        with open(json_fname, "r", encoding="utf-8") as fid:
            example_code_obj = json.load(fid)
        # generate replacement strings with the links
        str_repl = {}
        for name in sorted(example_code_obj):
            cobjs = example_code_obj[name]
            # possible names from identify_names, which in turn gets
            # possibilities from NameFinder.get_mapping
            link = type_ = None
            for cobj in cobjs:
                for modname in (cobj["module_short"], cobj["module"]):
                    this_module = modname.split(".")[0]
                    cname = cobj["name"]

                    # Try doc resolvers first
                    if this_module in doc_resolvers:
                        try:
                            link, type_ = doc_resolvers[this_module].resolve(
                                cobj, full_fname, return_type=True
                            )
                        except (HTTPError, URLError) as e:
                            _handle_http_url_error(
                                e, msg=f"resolving {modname}.{cname}"
                            )

                    # next try intersphinx
                    if this_module == modname == "builtins":
                        this_module = "python"
                    if link is None and this_module in intersphinx_inv:
                        inv = intersphinx_inv[this_module]
                        if modname == "builtins":
                            want = cname
                        else:
                            want = f"{modname}.{cname}"
                        for key, value in inv.items():
                            # only python domain
                            if key.startswith("py") and want in value:
                                link = value[want][2]
                                type_ = key
                                break

                    # differentiate classes from instances
                    is_instance = (
                        type_ is not None
                        and "py:class" in type_
                        and not cobj["is_class"]
                    )

                    if link is not None:
                        # Add CSS classes
                        name_html = period.join(
                            orig_pattern % part for part in name.split(".")
                        )
                        full_function_name = f"{modname}.{cname}"
                        css_class = "sphx-glr-backref-module-" + _sanitize_css_class(
                            modname
                        )
                        if type_ is not None:
                            css_class += (
                                " sphx-glr-backref-type-" + _sanitize_css_class(type_)
                            )
                        if is_instance:
                            css_class += " sphx-glr-backref-instance"
                        str_repl[name_html] = link_pattern.format(
                            link=link,
                            title=full_function_name,
                            css_class=css_class,
                            text=name_html,
                        )
                        break  # loop over possible module names

                if link is not None:
                    break  # loop over cobjs

        # do the replacement in the html file

        # ensure greediness
        names = sorted(str_repl, key=len, reverse=True)
        regex_str = "|".join(re.escape(name) for name in names)
        regex = re.compile(regex_str)

        def substitute_link(match):
            return str_repl[match.group()]

        if len(str_repl) > 0:
            with open(full_fname, "r", encoding="utf-8") as fid:
                lines_in = fid.readlines()
            with open(full_fname, "w", **_W_KW) as fid:
                for line in lines_in:
                    line_out = regex.sub(substitute_link, line)
                    fid.write(line_out)


def embed_code_links(app, exception):
    """Embed hyperlinks to documentation into example code."""
    if exception is not None:
        return

    gallery_conf = app.config.sphinx_gallery_conf
    if not gallery_conf["embed_code_links"]:
        return

    # XXX: Allowlist of builders for which it makes sense to embed
    # hyperlinks inside the example html. Note that the link embedding
    # require searchindex.js to exist for the links to the local doc
    # and there does not seem to be a good way of knowing which
    # builders creates a searchindex.js.
    if app.builder.name not in ["html", "readthedocs"]:
        return

    logger.info("embedding documentation hyperlinks...", color="white")

    gallery_dirs = gallery_conf["gallery_dirs"]
    if not isinstance(gallery_dirs, list):
        gallery_dirs = [gallery_dirs]

    for gallery_dir in gallery_dirs:
        _embed_code_links(app, gallery_conf, gallery_dir)
