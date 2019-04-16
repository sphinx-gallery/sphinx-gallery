# -*- coding: utf-8 -*-
r"""
Test source parser
==================


"""
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import division, absolute_import, print_function

import os.path as op
import pytest
import sphinx_gallery.py_source_parser as sg


def test_get_docstring_and_rest(unicode_sample, tmpdir):
    docstring, rest, lineno = sg.get_docstring_and_rest(unicode_sample)
    assert u'Únicode' in docstring
    assert u'heiß' in rest
    # degenerate
    fname = op.join(str(tmpdir), 'temp')
    with open(fname, 'w') as fid:
        fid.write('print("hello")\n')
    with pytest.raises(ValueError, match='Could not find docstring'):
        sg.get_docstring_and_rest(fname)
