# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Testing the rst files generator
"""
from __future__ import division, absolute_import, print_function
import sphinxgallery.gen_rst as sg
from nose.tools import assert_equals


def test_split_code_and_text_blocks():
    """Test if a known example file gets properly split"""

    blocks = sg.split_code_and_text_blocks('examples/just_code.py')

    assert_equals(blocks[0][0], 'text')
    assert_equals(blocks[0][1], (2, 11))
    assert_equals(blocks[1][0], 'code')
    assert_equals(blocks[1][1], (11, 16))
