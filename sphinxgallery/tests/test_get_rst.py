# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Testing the rst files generator
"""
from __future__ import division, absolute_import, print_function
import sphinxgallery.gen_rst as sg
from nose.tools import assert_equals
import ast


def test_split_code_and_text_blocks():
    """Test if a known example file gets properly split"""

    blocks = sg.split_code_and_text_blocks('examples/just_code.py')

    assert_equals(blocks[0][0], 'text')
    assert_equals(blocks[1][0], 'code')


def test_bug_cases_of_notebook_syntax():
    """Test over the known requirements of supported syntax in the
    notebook styled comments"""

    with open('sphinxgallery/tests/reference_parse.txt') as reference:
        ref_blocks = ast.literal_eval(reference.read())
        blocks = sg.split_code_and_text_blocks('tutorials/plot_parse.py')

        assert_equals(blocks, ref_blocks)


def test_codestr2rst():
    """Test the correct translation of a code block into rst"""
    output = sg.codestr2rst('print("hello world")')
    reference = """
.. code-block:: python

    print("hello world")"""
    assert_equals(reference, output)
