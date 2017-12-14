# -*- coding: utf-8 -*-
r"""
Test source parser
==================


"""
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import division, absolute_import, print_function
import sphinx_gallery.py_source_parser as sg


def test_get_docstring_and_rest(unicode_sample):

    docstring, rest, lineno = sg.get_docstring_and_rest(unicode_sample)
    assert u'Únicode' in docstring
    assert u'heiß' in rest
