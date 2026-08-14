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
from typing import TYPE_CHECKING, Any, Iterator

from docutils import nodes
from pygments.lexers import get_lexer_by_name
from pygments.token import STANDARD_TYPES, Name, Operator
from sphinx.transforms.post_transforms import SphinxPostTransform

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
    """A highlighted code block with reference nodes embedded per-token."""


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
        self._cache: dict[str, tuple[str | None, str | None, bool, bool]] = {}

    def _lookup(self, target: str) -> tuple[str | None, str | None, bool, bool]:
        """Return (uri, objtype, internal, aliased) for a fully qualified name."""
        entry = self.env.domains["py"].objects.get(target)
        if entry is not None:
            uri = self.builder.get_relative_uri(self.docname, entry.docname)
            # an aliased entry is the ``:canonical:`` (often private) location of
            # an object documented elsewhere, so it is only a fallback
            aliased = getattr(entry, "aliased", False)
            return f"{uri}#{entry.node_id}", f"py:{entry.objtype}", True, aliased
        for objtype, mapping in self.inventory.items():
            if objtype.startswith("py:") and target in mapping:
                item = mapping[target]
                # Sphinx 8.2+ _InventoryItem vs older plain tuple
                uri = getattr(item, "uri", None)
                if uri is None:
                    uri = item[2]
                return str(uri), objtype, False, False
        return None, None, False, False

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
                uri, objtype, internal, aliased = self._cache[target]
                if uri is None or objtype is None:
                    continue
                # label local objects with the shortest module path even when
                # only documented under a deeper one (gh-1364)
                label = cobj["module_short"] if internal else modname
                # builtins are named bare in the tooltip, as the Python docs
                # and the inventory entry itself do
                if label == "builtins":
                    title = cobj["name"]
                else:
                    title = f"{label}.{cobj['name']}"
                css = ["sphx-glr-backref-module-" + _sanitize_css_class(label)]
                css.append("sphx-glr-backref-type-" + _sanitize_css_class(objtype))
                if "py:class" in objtype and not cobj["is_class"]:
                    css.append("sphx-glr-backref-instance")
                link = {
                    "uri": uri,
                    "title": title,
                    "classes": css,
                    "internal": internal,
                }
                if not aliased:
                    return link
                # keep looking: a later candidate may name the object by the
                # public module it is actually documented under
                fallback = fallback or link
        return fallback


def _token_node(ttype: Any, text: str) -> nodes.Node:
    """Convert one pygments token to a docutils node."""
    short = STANDARD_TYPES.get(ttype, "")
    while not short and ttype.parent is not None:
        ttype = ttype.parent
        short = STANDARD_TYPES.get(ttype, "")
    if not short:
        return nodes.Text(text)
    return nodes.inline(text, text, classes=[short])


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
    i = 0
    prev_significant = None
    while i < len(tokens):
        ttype, text = tokens[i]
        # a linkable chain starts at a Name token not preceded by a "."
        starts_chain = ttype in Name and not (prev_significant == (Operator, "."))
        if starts_chain:
            # gather the maximal dotted chain: Name (. Name)*
            parts, spans = [text], [1]
            j = i
            while (
                j + 2 < len(tokens)
                and tokens[j + 1] == (Operator, ".")
                and tokens[j + 2][0] in Name
            ):
                parts.append(tokens[j + 2][1])
                spans.append(spans[-1] + 2)
                j += 2
            # longest prefix of the chain that identifies and resolves wins
            link = n_tok = None
            for k in range(len(parts), 0, -1):
                written = ".".join(parts[:k])
                if written in code_obj:
                    link = resolver.resolve(code_obj[written])
                    if link is not None:
                        n_tok = spans[k - 1]
                        break
            if link is not None and n_tok is not None:
                ref = nodes.reference(
                    "",
                    "",
                    internal=link["internal"],
                    refuri=link["uri"],
                    reftitle=link["title"],
                    classes=link["classes"],
                )
                for tt, tx in tokens[i : i + n_tok]:
                    ref += _token_node(tt, tx)
                yield ref
                prev_significant = tokens[i + n_tok - 1]
                i += n_tok
                continue
        if text.strip():
            prev_significant = (ttype, text)
        yield _token_node(ttype, text)
        i += 1


def _add_linenos(children: list[nodes.Node], start: int) -> list[nodes.Node]:
    """Interleave pygments-style inline line-number nodes into a token stream.

    Replicates ``HtmlFormatter(linenos="inline")``: a ``span.linenos`` at each
    line start, numbers right-justified to the width of the last line number.
    Multi-line tokens (e.g. triple-quoted strings) are split per line so the
    number node can sit between the segments at the top level.
    """
    total = sum(node.astext().count("\n") for node in children)
    width = len(str(start + max(total - 1, 0)))
    out: list[nodes.Node] = []
    state = {"line": start, "at_start": True}

    def emit_lineno() -> None:
        txt = str(state["line"]).rjust(width)
        out.append(nodes.inline(txt, txt, classes=["linenos"]))
        state["line"] += 1
        state["at_start"] = False

    def emit(text: str, classes: list[str] | None = None) -> None:
        for seg in text.splitlines(keepends=True):
            if state["at_start"]:
                emit_lineno()
            if classes is None:
                out.append(nodes.Text(seg))
            else:
                out.append(nodes.inline(seg, seg, classes=classes))
            if seg.endswith("\n"):
                state["at_start"] = True

    for node in children:
        if isinstance(node, nodes.Text):
            emit(node.astext())
        elif isinstance(node, nodes.reference):
            # references never contain newlines (dotted-name chains only)
            if state["at_start"]:
                emit_lineno()
            out.append(node)
        else:
            assert isinstance(node, nodes.inline)
            emit(node.astext(), classes=node["classes"])
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
