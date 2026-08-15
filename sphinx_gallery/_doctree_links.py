# License: 3-clause BSD
"""Doctree-based code link embedding.

A Sphinx post-transform rewrites each example code block into pygments-token
inline nodes and wraps identified names in resolved ``reference`` nodes. Link
targets come from the local py domain and intersphinx inventories, so links
work in every HTML builder (html, dirhtml, ...) with no post-processing of
built pages.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import TYPE_CHECKING, Any, Iterator, NamedTuple

from docutils import nodes
from pygments.lexers import get_lexer_by_name
from pygments.token import STANDARD_TYPES, Name, Operator
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util.nodes import make_refnode

from .utils import _read_json

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.builders import Builder
    from sphinx.environment import BuildEnvironment

    from .typing import GalleryConfig


def _sanitize_css_class(s: str) -> str:
    for x in "~!@$%^&*()+=,./';:\"?><[]\\{}|`#":
        s = s.replace(x, "-")
    return s


class code_links_block(nodes.General, nodes.TextElement):
    """A highlighted code block with reference nodes embedded per-token.

    Sphinx only renders the children of a ``literal_block`` when its
    ``rawsource`` differs from its text -- otherwise it re-highlights the
    rawsource with pygments and drops the children (``SkipNode``), which would
    silently throw every link away:
    https://github.com/sphinx-doc/sphinx/blob/v9.1.0/sphinx/writers/html5.py#L622-L624

    Rather than rely on that, we swap in a node of our own and render the
    ``div.highlight`` wrapper that ``visit_literal_block`` would have emitted.
    """


def visit_code_links_block_html(self: Any, node: code_links_block) -> None:
    """Open the same wrapper markup pygments/Sphinx would have produced."""
    lang = _sanitize_css_class(node["lang"])
    self.body.append(
        f'<div class="highlight-{lang} notranslate"><div class="highlight"><pre>'
    )


def depart_code_links_block_html(self: Any, node: code_links_block) -> None:
    """Close the highlight wrapper markup."""
    self.body.append("</pre></div></div>\n")


def _load_code_obj(
    env: BuildEnvironment, docname: str
) -> dict[str, list[dict[str, Any]]] | None:
    """Return the identify_names candidate dict for a gallery doc, or None."""
    path = Path(env.srcdir, f"{docname}.codeobj.json")
    if not path.is_file():
        return None
    try:
        return _read_json(path)
    except Exception:  # e.g. truncated by an interrupted build
        return None


class _Lookup(NamedTuple):
    """Where a name was found: a local document, an external URI, or nowhere."""

    docname: str | None
    node_id: str | None
    uri: str | None
    objtype: str | None  # None when the name was not found at all
    aliased: bool


class _Resolver:
    """Resolve fully qualified names via the py domain and intersphinx."""

    def __init__(
        self,
        env: BuildEnvironment,
        builder: Builder,
        docname: str,
        gallery_conf: GalleryConfig,
    ) -> None:
        self.env = env
        self.builder = builder
        self.docname = docname
        self.prefer_full = gallery_conf["prefer_full_module"]
        try:
            from sphinx.ext.intersphinx import InventoryAdapter

            self.inventory = InventoryAdapter(env).main_inventory
        except ImportError:
            self.inventory = {}
        self._cache: dict[str, _Lookup] = {}

    def _lookup(self, target: str) -> _Lookup:
        """Find a fully qualified name in the py domain, then in intersphinx."""
        entry = self.env.domains["py"].objects.get(target)
        if entry is not None:
            # an aliased entry is the ``:canonical:`` (often private) location of
            # an object documented elsewhere, so it is only a fallback -- the py
            # domain prefers the canonical entry the same way:
            # https://github.com/sphinx-doc/sphinx/blob/v9.1.0/sphinx/domains/python/__init__.py#L1239-L1244
            return _Lookup(
                docname=entry.docname,
                node_id=entry.node_id,
                uri=None,
                objtype=f"py:{entry.objtype}",
                aliased=getattr(entry, "aliased", False),
            )
        for objtype, mapping in self.inventory.items():
            if objtype.startswith("py:") and target in mapping:
                item = mapping[target]
                # Sphinx 8.2+ hands out _InventoryItem, older versions a tuple
                uri = getattr(item, "uri", None)
                if uri is None:
                    uri = item[2]
                return _Lookup(None, None, str(uri), objtype, False)
        return _Lookup(None, None, None, None, False)

    def resolve(self, cobjs: list[dict[str, Any]]) -> dict[str, Any] | None:
        """Try candidate (module, name) pairs in order; return link info."""
        fallback = None
        for cobj in cobjs:
            modnames = [cobj["module_short"], cobj["module"]]
            full_name = f"{cobj['module']}.{cobj['name']}"
            if any(re.search(p, full_name) for p in self.prefer_full):
                # prefer_full_module changes where we *resolve* (gh-947); local
                # links keep the short label below, like the old resolver did
                modnames = modnames[::-1]
            for modname in dict.fromkeys(modnames):
                if modname == "builtins":
                    target = cobj["name"]
                else:
                    target = f"{modname}.{cobj['name']}"
                if target not in self._cache:
                    self._cache[target] = self._lookup(target)
                found = self._cache[target]
                if found.objtype is None:  # not documented anywhere we know of
                    continue
                # label local objects with the shortest module path even when
                # only documented under a deeper one (gh-1364)
                internal = found.docname is not None
                label = cobj["module_short"] if internal else modname
                # builtins are named bare in the tooltip, as the Python docs
                # and the inventory entry itself do
                if label == "builtins":
                    title = cobj["name"]
                else:
                    title = f"{label}.{cobj['name']}"
                css = ["sphx-glr-backref-module-" + _sanitize_css_class(label)]
                css.append(
                    "sphx-glr-backref-type-" + _sanitize_css_class(found.objtype)
                )
                if "py:class" in found.objtype and not cobj["is_class"]:
                    css.append("sphx-glr-backref-instance")
                link = {"found": found, "title": title, "classes": css}
                if not found.aliased:
                    return link
                # keep looking: a later candidate may name the object by the
                # public module it is actually documented under
                fallback = fallback or link
        return fallback

    def reference(
        self, link: dict[str, Any], children: list[nodes.Node]
    ) -> nodes.reference:
        """Build the reference node for a link returned by :meth:`resolve`."""
        found: _Lookup = link["found"]
        if found.docname is not None:
            # make_refnode also handles a target on this very page, which needs
            # a bare ``refid`` rather than a URI pointing back at ourselves
            ref = make_refnode(
                self.builder,
                self.docname,
                found.docname,
                found.node_id,
                children,
                title=link["title"],
            )
        else:
            ref = nodes.reference(
                "",
                "",
                *children,
                internal=False,
                refuri=found.uri,
                reftitle=link["title"],
            )
        ref["classes"] += link["classes"]
        return ref


def _pygments_class(ttype: Any) -> str:
    """Return the CSS class pygments' HTML formatter gives a token type.

    Ported from the private ``pygments.formatters.html._get_ttype_class``, which
    is what ``HtmlFormatter`` itself uses, so that a token unknown to
    ``STANDARD_TYPES`` gets the same compound class (e.g. ``n-Foo``) as it would
    in a stock highlighted block:
    https://github.com/pygments/pygments/blob/2.20.0/pygments/formatters/html.py#L57-L66
    """
    short = STANDARD_TYPES.get(ttype)
    if short:
        return short
    suffix = ""
    while short is None:
        suffix = "-" + ttype[-1] + suffix
        ttype = ttype.parent
        short = STANDARD_TYPES.get(ttype)
    return short + suffix


def _token_node(ttype: Any, text: str) -> nodes.Node:
    """Convert one pygments token to a docutils node."""
    short = _pygments_class(ttype)
    if not short:  # the root Token type, which pygments leaves unwrapped
        return nodes.Text(text)
    return nodes.inline(text, text, classes=[short])


def _dotted_chain(tokens: list[tuple[Any, str]], i: int) -> Iterator[tuple[str, int]]:
    """Yield the dotted-name prefixes starting at ``tokens[i]``, longest first.

    For ``mne.filter.create_filter`` this yields the whole chain, then
    ``mne.filter``, then ``mne``, each with the number of tokens it spans, so
    the caller can link the longest prefix that actually resolves.
    """
    parts = [tokens[i][1]]
    spans = [1]
    # step over the "." of each ``.name`` that continues the chain
    for j in range(i + 1, len(tokens) - 1, 2):
        if tokens[j] != (Operator, ".") or tokens[j + 1][0] not in Name:
            break
        parts.append(tokens[j + 1][1])
        spans.append(spans[-1] + 2)
    for k in range(len(parts), 0, -1):
        yield ".".join(parts[:k]), spans[k - 1]


def _tokenize_and_link(
    code: str,
    lang: str,
    code_obj: dict[str, list[dict[str, Any]]],
    resolver: _Resolver,
) -> Iterator[nodes.Node]:
    """Yield docutils nodes for ``code``, linking names found in ``code_obj``."""
    lexer = get_lexer_by_name(
        "python" if lang in ("default", "python3") else lang.lower()
    )
    tokens = list(lexer.get_tokens(code))
    linked_through = -1  # last index already emitted as part of a link
    prev_token = None  # last non-whitespace token, to spot attribute access
    for i, (ttype, text) in enumerate(tokens):
        if i <= linked_through:
            continue  # a dotted name we already linked swallowed this token
        link = n_tok = None
        # only start a chain at a name that is not itself an attribute: the
        # ``b`` of ``a().b`` continues the preceding expression, so linking it
        # on its own would point at some unrelated top-level ``b``
        if ttype in Name and prev_token != (Operator, "."):
            for written, span in _dotted_chain(tokens, i):
                if written in code_obj:
                    link = resolver.resolve(code_obj[written])
                    if link is not None:
                        n_tok = span
                        break
        if link is not None and n_tok is not None:
            children = [_token_node(tt, tx) for tt, tx in tokens[i : i + n_tok]]
            yield resolver.reference(link, children)
            linked_through = i + n_tok - 1
            prev_token = tokens[linked_through]
        else:
            if text.strip():
                prev_token = (ttype, text)
            yield _token_node(ttype, text)


def _split_lines(node: nodes.Node) -> Iterator[nodes.Node]:
    """Split one token node into a node per line it spans.

    A line number can only be inserted *between* top-level nodes, so a token
    covering several lines (a triple-quoted string, say) has to become one node
    per line first. References are atomic: a dotted name never spans lines.
    """
    if isinstance(node, nodes.reference):
        yield node
        return
    classes = node["classes"] if isinstance(node, nodes.inline) else None
    for segment in node.astext().splitlines(keepends=True):
        if classes is None:
            yield nodes.Text(segment)
        else:
            yield nodes.inline(segment, segment, classes=classes)


def _add_linenos(children: list[nodes.Node], start: int) -> list[nodes.Node]:
    """Interleave pygments-style inline line-number nodes into a token stream.

    Replicates ``HtmlFormatter(linenos="inline")``, which prepends a
    ``span.linenos`` to every line with the number right-justified to the width
    of the last one:
    https://github.com/pygments/pygments/blob/2.20.0/pygments/formatters/html.py#L687
    """
    total = sum(node.astext().count("\n") for node in children)
    width = len(str(start + max(total - 1, 0)))
    out: list[nodes.Node] = []
    lineno = start
    at_line_start = True
    for node in children:
        for piece in _split_lines(node):
            if at_line_start:
                number = str(lineno).rjust(width)
                out.append(nodes.inline(number, number, classes=["linenos"]))
                lineno += 1
            out.append(piece)
            at_line_start = piece.astext().endswith("\n")
    return out


class CodeLinksTransform(SphinxPostTransform):
    """Embed documentation links into gallery example code blocks."""

    default_priority = 5
    formats = ("html",)

    def run(self, **kwargs: Any) -> None:
        """Rewrite python code blocks of gallery docs with embedded links."""
        gallery_conf = self.config.sphinx_gallery_conf
        docname = self.env.path2doc(self.document["source"])
        if docname is None:
            return
        code_obj = _load_code_obj(self.env, docname)
        if not code_obj:
            return
        # Sphinx 9 deprecated SphinxPostTransform.app in favor of env._app
        app = getattr(self.env, "_app", None) or self.app
        resolver = _Resolver(self.env, app.builder, docname, gallery_conf)
        for block in list(self.document.findall(nodes.literal_block)):
            lang = block.get("language", "")
            if lang.lower() not in ("python", "python3", "default", "ipython3"):
                continue
            code = block.rawsource
            children = list(_tokenize_and_link(code, lang, code_obj, resolver))
            if block.get("linenos"):
                lineno_start = block.get("highlight_args", {}).get("linenostart", 1)
                children = _add_linenos(children, lineno_start)
            new = code_links_block(lang=lang)
            new["classes"] = block.get("classes", [])
            new += children
            block.replace_self(new)


def setup_doctree_links(app: Sphinx) -> None:
    """Register the doctree-based link embedding machinery."""
    app.add_node(
        code_links_block,
        html=(visit_code_links_block_html, depart_code_links_block_html),
    )
    app.add_post_transform(CodeLinksTransform)
