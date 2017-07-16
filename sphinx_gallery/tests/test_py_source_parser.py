# -*- coding: utf-8 -*-
r"""
Test source parser
==================


"""
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import division, absolute_import, print_function
import sphinx_gallery.py_source_parser as sg


def test_get_docstring_and_rest():

    docstring, rest = sg.get_docstring_and_rest(
        'sphinx_gallery/tests/unicode.sample')
    assert u'Únicode' in docstring
    assert u'heiß' in rest
