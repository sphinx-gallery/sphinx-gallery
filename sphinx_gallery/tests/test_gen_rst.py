# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Testing the rst files generator
"""
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import ast
import codecs
import json
import tempfile
import re
import os
from nose.tools import assert_equal, assert_false, assert_true
import sphinx_gallery.gen_rst as sg
from sphinx_gallery import notebook


CONTENT = ['"""'
           'Docstring header',
           '================',
           '',
           'This is the description of the example',
           'which goes on and on, Óscar',
           '',
           '',
           'And this is a second paragraph',
           '"""',
           '',
           '# and now comes the module code',
           'import logging',
           'import sys',
           'x, y = 1, 2',
           'print(u"Óscar output") # need some code output',
           'logger = logging.getLogger()',
           'logger.setLevel(logging.INFO)',
           'lh = logging.StreamHandler(sys.stdout)',
           'lh.setFormatter(logging.Formatter("log:%(message)s"))',
           'logger.addHandler(lh)',
           'logger.info(u"Óscar")',
           ]


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
    with tempfile.NamedTemporaryFile('wb') as f:
        f.write('\n'.join(CONTENT).encode('utf-8'))
        f.flush()
        result = sg.extract_intro(f.name)
    assert_false('Docstring' in result)
    assert_equal(
        result,
        'This is the description of the example which goes on and on, Óscar')
    assert_false('second paragraph' in result)


def test_md5sums():
    """Test md5sum check functions work on know file content"""

    with tempfile.NamedTemporaryFile('w') as f:
        f.write('Local test\n')
        f.flush()
        file_md5 = sg.get_md5sum(f.name)
        # verify correct md5sum
        assert_equal('ea8a570e9f3afc0a7c3f2a17a48b8047', file_md5)
        # True because is a new file
        assert_true(sg.check_md5sum_change(f.name))
        # False because file has not changed since last check
        assert_false(sg.check_md5sum_change(f.name))

    os.remove(f.name + '.md5')


def test_pattern_matching():
    """Test if only examples matching pattern are executed"""
    examples_dir = tempfile.mkdtemp()
    gallery_dir = tempfile.mkdtemp()

    gallery_conf = {
        'filename_pattern': re.escape(os.sep) + 'plot_0',
        'examples_dirs': examples_dir,
        'gallery_dirs': gallery_dir,
        'plot_gallery': True,
        'mod_example_dir': 'modules/generated',
        'doc_module': (),
        'reference_url': {},
    }

    code_output = '\n Out::\n\n      Óscar output\n    log:Óscar\n\n'
    # create three files in tempdir (only one matches the pattern)
    fnames = ['plot_0.py', 'plot_1.py', 'plot_2.py']
    for fname in fnames:
        with codecs.open(os.path.join(examples_dir, fname), 'w', 'utf-8') as f:
            f.write('\n'.join(CONTENT))
        # generate rst file
        sg.generate_file_rst(fname, gallery_dir, examples_dir, gallery_conf)
        # read rst file and check if it contains code output
        rst_fname = os.path.splitext(fname)[0] + '.rst'
        with codecs.open(os.path.join(gallery_dir, rst_fname),
                         'r', 'utf-8') as f:
            rst = f.read()
        if re.search(gallery_conf['filename_pattern'],
                     os.path.join(gallery_dir, rst_fname)):
            print(code_output)
            print('')
            print(rst)
            assert_true(code_output in rst)
        else:
            assert_false(code_output in rst)


def test_ipy_notebook():
    """Test that written ipython notebook file corresponds to python object"""
    with tempfile.NamedTemporaryFile('w+') as f:
        example_nb = notebook.Notebook(f.name, os.path.dirname(f.name))
        blocks = sg.split_code_and_text_blocks('tutorials/plot_parse.py')

        for blabel, bcontent in blocks:
            if blabel == 'code':
                example_nb.add_code_cell(bcontent)
            else:
                example_nb.add_markdown_cell(sg.text2string(bcontent))

        example_nb.save_file()

        f.flush()
        assert_equal(json.load(f), example_nb.work_notebook)
