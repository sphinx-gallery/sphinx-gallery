# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Testing the rst files generator
"""
from __future__ import division, absolute_import, print_function
import sphinxgallery.docs_resolv as sg
import tempfile
from nose.tools import assert_equals


def _get_data(fid, shelve_file, test_string):
    data = sg.get_data(fid, shelve_file)
    assert_equals(data, test_string)


def test_shelve():
    test_string = 'test information'
    shelve_file = 'shelve_file'
    with tempfile.NamedTemporaryFile() as fid:
        try:
            fid.write(test_string)
        except TypeError:
            fid.write(test_string.encode())

        fid.seek(0)
        _get_data(fid.name, shelve_file, test_string)

    _get_data(fid.name, shelve_file, test_string)
    try:
        _get_data(unicode(fid.name), shelve_file, test_string)
    except NameError:
        pass
