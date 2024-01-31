# Author: Óscar Nájera
# License: 3-clause BSD
r"""Tests for sorting keys on gallery (sub)sections."""

import os.path as op
import pytest

from sphinx.errors import ConfigError
from sphinx_gallery.sorting import (
    ExplicitOrder,
    NumberOfCodeLinesSortKey,
    FileNameSortKey,
    FileSizeSortKey,
    ExampleTitleSortKey,
    FunctionSortKey,
)


def test_ExplicitOrder_sorting_key():
    """Test ExplicitOrder."""
    all_folders = ["e", "f", "d", "c", "01b", "a"]
    explicit_folders = ["f", "d"]
    key = ExplicitOrder(explicit_folders)
    sorted_folders = sorted(["d", "f"], key=key)
    assert sorted_folders == explicit_folders

    # Test fails on wrong input
    with pytest.raises(ConfigError) as excinfo:
        ExplicitOrder("nope")
    excinfo.match("ExplicitOrder sorting key takes a list")

    # Test missing folder
    with pytest.raises(ConfigError) as excinfo:
        sorted_folders = sorted(all_folders, key=key)
    excinfo.match("If you use an explicit folder ordering")

    # str(obj) stability for sphinx non-rebuilds
    assert str(key).startswith("<ExplicitOrder : ")
    assert str(key) == str(ExplicitOrder(explicit_folders))
    assert str(key) != str(ExplicitOrder(explicit_folders[::-1]))
    src_dir = op.dirname(__file__)
    for klass, type_ in (
        (NumberOfCodeLinesSortKey, int),
        (FileNameSortKey, str),
        (FileSizeSortKey, int),
        (ExampleTitleSortKey, str),
    ):
        sorter = klass(src_dir)
        assert str(sorter) == f"<{klass.__name__}>"
        out = sorter(op.basename(__file__))
        assert isinstance(out, type_), type(out)


def test_Function_sorting_key():
    data = [(1, 0), (3, 2), (5, 4), (7, 6), (9, 8)]

    def f(x):
        return x[0] * x[1]

    sorter = FunctionSortKey(f)
    assert str(sorter).startswith("FunctionSortKey")
    assert sorted(data, key=f) == sorted(data, key=sorter)

    sorter_repr = FunctionSortKey(f, "f(x,y) = x*y")
    assert str(sorter_repr).startswith("f(x,y) = x*y")
    assert sorted(data, key=sorter_repr) == sorted(data, key=sorter)
