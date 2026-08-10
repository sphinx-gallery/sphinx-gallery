# License: 3-clause BSD
"""Unit tests for doctree-based code link embedding."""

from docutils import nodes

from sphinx_gallery.doctree_links import _add_linenos, _tokenize_and_link


class FakeResolver:
    """Resolve any candidate whose full name is in ``known``."""

    def __init__(self, known):
        self.known = known

    def resolve(self, cobjs):
        """Return link info for the first known candidate, else None."""
        for cobj in cobjs:
            target = f"{cobj['module']}.{cobj['name']}"
            if target in self.known:
                return dict(
                    uri=f"https://example.com/{target}",
                    title=target,
                    classes=["sphx-glr-backref-module-x", "sphx-glr-backref-type-y"],
                    internal=False,
                )
        return None


def _cobj(module, name):
    return dict(
        name=name, module=module, module_short=module, is_class=False, is_explicit=False
    )


CODE = """\
import numpy as np
x = np.arange(3)
s = '''one
two'''
y = np.arange(x.mean())
"""

CODE_OBJ = {
    "np.arange": [_cobj("numpy", "arange")],
    "x.mean": [_cobj("numpy", "ndarray.mean")],
    "x": [_cobj("numpy", "ndarray")],
}


def test_tokenize_and_link():
    """Names resolve to reference nodes; unresolved names stay plain."""
    resolver = FakeResolver({"numpy.arange", "numpy.ndarray"})
    out = list(_tokenize_and_link(CODE, "python", CODE_OBJ, resolver))
    # round-trips the source exactly
    assert "".join(n.astext() for n in out) == CODE
    refs = [n for n in out if isinstance(n, nodes.reference)]
    # x.mean does not resolve, so its longest resolving prefix (x) links
    # and the .mean attribute stays plain
    assert [r.astext() for r in refs] == ["x", "np.arange", "np.arange", "x"]
    ref = refs[1]
    assert ref["refuri"] == "https://example.com/numpy.arange"
    assert ref["reftitle"] == "numpy.arange"
    assert "sphx-glr-backref-module-x" in ref["classes"]
    # tokens within the link keep their pygments classes
    assert ref.children[0].astext() == "np"
    assert ref.children[0]["classes"] == ["n"]
    assert ref.children[1].astext() == "."
    # the attribute after an unresolved chain is not linked
    texts = [n.astext() for n in out if isinstance(n, nodes.inline)]
    assert "mean" in texts


def _classes(n):
    return n.get("classes", []) if isinstance(n, nodes.Element) else []


def test_add_linenos():
    """Line numbers interleave at line starts, padded, honoring the start."""
    resolver = FakeResolver({"numpy.arange"})
    children = list(_tokenize_and_link(CODE, "python", CODE_OBJ, resolver))
    out = _add_linenos(children, start=8)
    linenos = [n for n in out if "linenos" in _classes(n)]
    # 5 source lines (multiline string spans lines 3-4)
    assert [n.astext() for n in linenos] == [" 8", " 9", "10", "11", "12"]
    # stripping the linenos recovers the source
    rest = [n for n in out if "linenos" not in _classes(n)]
    assert "".join(n.astext() for n in rest) == CODE
    # references survive the interleaving
    refs = [n for n in out if isinstance(n, nodes.reference)]
    assert len(refs) == 2  # np.arange twice (only known name here)
    # a mid-line reference is not directly preceded by a line number
    idx = out.index(refs[0])
    assert "linenos" not in _classes(out[idx - 1])  # "x = " sits before it
