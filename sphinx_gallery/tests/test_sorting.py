# -*- coding: utf-8 -*-
r"""
Tests for sorting keys on gallery sections
==========================================

"""
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import division, absolute_import, print_function
import pytest


def test_ExplicitOrderStrict_sorting_key():
    """Test ExplicitOrderStrict"""
    from sphinx_gallery.sorting import ExplicitOrderStrict

    all_folders = ['e', 'f', 'd', 'c', '01b', 'a']
    explicit_folders = ['f', 'd']
    key = ExplicitOrderStrict(explicit_folders)
    sorted_folders = sorted(["d", "f"], key=key)
    assert sorted_folders == explicit_folders

    # Test fails on wrong input
    with pytest.raises(ValueError) as excinfo:
        ExplicitOrderStrict('nope')
    excinfo.match("ExplicitOrderStrict sorting key takes a list")

    # Test missing folder
    with pytest.raises(ValueError) as excinfo:
        sorted_folders = sorted(all_folders, key=key)
    excinfo.match('If you use an explicit folder ordering')
