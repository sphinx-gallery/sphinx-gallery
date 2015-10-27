# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Testing the rst files generator
"""
from __future__ import division, absolute_import, print_function
import tempfile

import sphinx_gallery.gen_rst as sg
from nose.tools import assert_equal, assert_false
import ast


def test_split_code_and_text_blocks():
    """Test if a known example file gets properly split"""

    blocks = sg.split_code_and_text_blocks('examples/just_code.py')

    assert_equal(blocks[0][0], 'text')
    assert_equal(blocks[1][0], 'code')


def test_bug_cases_of_notebook_syntax():
    """Test over the known requirements of supported syntax in the
    notebook styled comments"""

    with open('sphinx_gallery/tests/reference_parse.txt') as reference:
        ref_blocks = ast.literal_eval(reference.read())
        blocks = sg.split_code_and_text_blocks('tutorials/plot_parse.py')

        assert_equal(blocks, ref_blocks)


def test_direct_comment_after_docstring():
    # For more details see
    # https://github.com/sphinx-gallery/sphinx-gallery/pull/49
    with tempfile.NamedTemporaryFile('w') as f:
        f.write('\n'.join(['"Docstring"',
                           '# and now comes the module code',
                           '# with a second line of comment',
                           'x, y = 1, 2',
                           '']))
        f.flush()

        result = sg.split_code_and_text_blocks(f.name)

    expected_result = [
        ('text', 'Docstring'),
        ('code', '\n'.join(['# and now comes the module code',
                            '# with a second line of comment',
                            'x, y = 1, 2',
                            '']))]
    assert_equal(result, expected_result)


def test_codestr2rst():
    """Test the correct translation of a code block into rst"""
    output = sg.codestr2rst('print("hello world")')
    reference = """
.. code-block:: python

    print("hello world")"""
    assert_equal(reference, output)


def test_extract_intro():
    with tempfile.NamedTemporaryFile('w') as f:
        f.write('\n'.join(['"""'
                           'Docstring header',
                           '================',
                           '',
                           'This is the description of the example',
                           'which goes on and on',
                           '',
                           '',
                           'And this is a second paragraph',
                           '"""',
                           '',
                           '# and now comes the module code',
                           'x, y = 1, 2']))

        f.flush()

        result = sg.extract_intro(f.name)
        assert_false('Docstring' in result)
        assert_equal(
            result,
            'This is the description of the example which goes on and on')
        assert_false('second paragraph' in result)
