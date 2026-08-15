"""Test utility functions."""

import ast
from pathlib import Path

import pytest

import sphinx_gallery
from sphinx_gallery.utils import (
    WARNING_TYPE,
    _combine_backreferences,
    _read_json,
    _write_json,
)

DOCUMENTED_SUBTYPES = {
    "backreference_missing",
    "config",
    "dependency",
    "duplicate_filename",
    "example_error",
    "file_conf",
    "space_in_filename",
    "thumbnail",
    "url_fetch",
}


def _iter_logger_warning_calls():
    """Yield every ``logger.warning(...)`` call made by the package."""
    for path in sorted(Path(sphinx_gallery.__file__).parent.glob("*.py")):
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "warning"
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "logger"
            ):
                yield f"{path.name}:{node.lineno}", node


def test_warnings_are_suppressible():
    """Every warning must be tagged so users can filter it via `suppress_warnings`."""
    calls = dict(_iter_logger_warning_calls())
    assert len(calls) > 10, "found almost no warnings, has the AST match gone stale?"
    for location, node in calls.items():
        keywords = {kw.arg: kw.value for kw in node.keywords}
        assert "type" in keywords and "subtype" in keywords, (
            f"{location}: pass type=WARNING_TYPE and a subtype, so that readers can "
            "silence this warning with suppress_warnings"
        )
        assert getattr(keywords["type"], "id", None) == "WARNING_TYPE", (
            f"{location}: pass the WARNING_TYPE constant rather than a literal"
        )
        subtype = keywords["subtype"]
        assert isinstance(subtype, ast.Constant), f"{location}: subtype must be literal"
        assert subtype.value in DOCUMENTED_SUBTYPES, (
            f"{location}: unknown subtype {subtype.value!r}, add it to "
            "DOCUMENTED_SUBTYPES and to the table in doc/configuration.rst"
        )


@pytest.mark.parametrize("subtype", sorted(DOCUMENTED_SUBTYPES))
def test_subtypes_documented(subtype):
    """Each subtype is documented, and named as `sphinx_gallery.<subtype>`."""
    doc = Path(sphinx_gallery.__file__).parents[1] / "doc" / "configuration.rst"
    if not doc.is_file():
        pytest.skip("docs not available (installed package)")
    assert f"``{subtype}``" in doc.read_text(encoding="utf-8")
    assert WARNING_TYPE == "sphinx_gallery"


def test_combine_backreferences():
    """Check `_combine_backreferences` works as expected."""
    backrefs_a = {
        "a": [1, 2],
        "b": [11, 12],
    }
    assert _combine_backreferences({}, backrefs_a) == backrefs_a

    backrefs_b = {
        "a": [3, 4],
        "c": [21, 22],
    }
    assert _combine_backreferences(backrefs_a, backrefs_b) == {
        "a": [1, 2, 3, 4],
        "b": [11, 12],
        "c": [21, 22],
    }


def test_read_write_json(tmp_path):
    """Check `_read_json` and `_write_json` work as expected."""
    path = tmp_path / "test"
    data = {
        "object1": ("path/file.py", "first intro", "first title"),
        "object2": ("path2/file2.py", "second intro", "second title"),
    }
    _write_json(path, data, "test_dict")
    # Writing converts tuples to lists
    assert _read_json(path.with_name(path.stem + "test_dict.json")) == {
        key: list(value) for key, value in data.items()
    }
