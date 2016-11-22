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
import copy
import json
import tempfile
import re
import os
import nose
import shutil
import warnings
import zipfile
from nose.tools import assert_equal, assert_false, assert_true

import sphinx_gallery.gen_rst as sg
from sphinx_gallery import gen_gallery, gen_rst, notebook, downloads
import matplotlib.pylab as plt  # Import gen_rst first to enable 'Agg' backend.

CONTENT = '''
"""
Docstring header
================

This is the description of the example
which goes on and on, Óscar


And this is a second paragraph
"""

# and now comes the module code
import logging
import sys
x, y = 1, 2
print(u"Óscar output") # need some code output
logger = logging.getLogger()
logger.setLevel(logging.INFO)
lh = logging.StreamHandler(sys.stdout)
lh.setFormatter(logging.Formatter("log:%(message)s"))
logger.addHandler(lh)
logger.info(u"Óscar")
print(r"$\\langle n_\\uparrow n_\\downarrow \\rangle$")
'''.replace('\r\n', '\n').split('\n')


FIGURE_CONTENT = '''
"""
Docstring header
================

Description.
"""

from mayavi import mlab
import matplotlib.pyplot as plt

###############################################################################
# Section 1

from mayavi import mlab
fig = mlab.figure()
mlab.draw()
fig2 = plt.figure()
assert len(mlab.get_engine().scenes) == 1
assert plt.fignum_exists(fig2.number)

###############################################################################
# Section 2

assert len(mlab.get_engine().scenes) == 1  # shall not be closed
assert plt.fignum_exists(fig2.number)

###############################################################################
# Section 3

mlab.close(all=True)
plt.close('all')
assert len(mlab.get_engine().scenes) == 0
assert not plt.fignum_exists(fig2.number)
fig = mlab.figure()
fig2 = plt.figure()
assert len(mlab.get_engine().scenes) == 1
assert plt.fignum_exists(fig2.number)
'''.replace('\r\n', '\n').split('\n')


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
    with tempfile.NamedTemporaryFile('w', delete=False) as f:
        f.write('\n'.join(['"Docstring"',
                           '# and now comes the module code',
                           '# with a second line of comment',
                           'x, y = 1, 2',
                           '']))

    try:
        result = sg.split_code_and_text_blocks(f.name)
    finally:
        os.remove(f.name)

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
    with tempfile.NamedTemporaryFile('wb', delete=False) as f:
        f.write('\n'.join(CONTENT).encode('utf-8'))
    try:
        result = sg.extract_intro(f.name)
    finally:
        os.remove(f.name)
    assert_false('Docstring' in result)
    want = 'This is the description of the example which goes on and on, Óscar'
    assert_equal(result, want)
    assert_false('second paragraph' in result)


def test_md5sums():
    """Test md5sum check functions work on know file content"""

    with tempfile.NamedTemporaryFile('w', delete=False) as f:
        f.write('Local test\n')
    try:
        file_md5 = sg.get_md5sum(f.name)
        # verify correct md5sum
        assert_equal('ea8a570e9f3afc0a7c3f2a17a48b8047', file_md5)
        # False because is a new file
        assert_false(sg.md5sum_is_current(f.name))
        # Write md5sum to file to check is current
        with open(f.name + '.md5', 'w') as file_checksum:
            file_checksum.write(file_md5)
        assert_true(sg.md5sum_is_current(f.name))
    finally:
        os.remove(f.name)
    os.remove(f.name + '.md5')


def build_test_configuration(**kwargs):
    """Sets up a test sphinx-gallery configuration"""

    gallery_conf = copy.deepcopy(gen_gallery.DEFAULT_GALLERY_CONF)
    gallery_conf.update(examples_dir=tempfile.mkdtemp(),
                        gallery_dir=tempfile.mkdtemp())
    gallery_conf.update(kwargs)

    return gallery_conf


def test_fail_example():
    """Test that failing examples are only executed until failing block"""

    gallery_conf = build_test_configuration(filename_pattern='raise.py')

    failing_code = CONTENT + ['#' * 79,
                              'First_test_fail', '#' * 79, 'second_fail']

    with codecs.open(os.path.join(gallery_conf['examples_dir'], 'raise.py'),
                     mode='w', encoding='utf-8') as f:
        f.write('\n'.join(failing_code))

    with warnings.catch_warnings(record=True) as w:
        sg.generate_file_rst('raise.py', gallery_conf['gallery_dir'],
                             gallery_conf['examples_dir'], gallery_conf)
    assert_equal(len(w), 1)
    assert_true(all(x in str(w[0].message)
                    for x in ['_' * 10, "'First_test_fail' is not defined"]))

    # read rst file and check if it contains traceback output

    with codecs.open(os.path.join(gallery_conf['gallery_dir'], 'raise.rst'),
                     mode='r', encoding='utf-8') as f:
        ex_failing_blocks = f.read().count('pytb')
        if ex_failing_blocks == 0:
            raise ValueError('Did not run into errors in bad code')
        elif ex_failing_blocks > 1:
            raise ValueError('Did not stop executing script after error')


def test_pattern_matching():
    """Test if only examples matching pattern are executed"""

    gallery_conf = build_test_configuration(
        filename_pattern=re.escape(os.sep) + 'plot_0')

    code_output = ('\n Out::\n'
                   '\n'
                   '    Óscar output\n'
                   '    log:Óscar\n'
                   '    $\\langle n_\\uparrow n_\\downarrow \\rangle$\n\n'
                   )
    # create three files in tempdir (only one matches the pattern)
    fnames = ['plot_0.py', 'plot_1.py', 'plot_2.py']
    for fname in fnames:
        with codecs.open(os.path.join(gallery_conf['examples_dir'], fname),
                         mode='w', encoding='utf-8') as f:
            f.write('\n'.join(CONTENT))
        # generate rst file
        sg.generate_file_rst(fname, gallery_conf['gallery_dir'],
                             gallery_conf['examples_dir'], gallery_conf)
        # read rst file and check if it contains code output
        rst_fname = os.path.splitext(fname)[0] + '.rst'
        with codecs.open(os.path.join(gallery_conf['gallery_dir'], rst_fname),
                         mode='r', encoding='utf-8') as f:
            rst = f.read()
        if re.search(gallery_conf['filename_pattern'],
                     os.path.join(gallery_conf['gallery_dir'], rst_fname)):
            assert_true(code_output in rst)
        else:
            assert_false(code_output in rst)


def test_ipy_notebook():
    """Test that written ipython notebook file corresponds to python object"""
    with tempfile.NamedTemporaryFile('w+', delete=False) as f:
        example_nb = notebook.Notebook(f.name, os.path.dirname(f.name))
    try:
        blocks = sg.split_code_and_text_blocks('tutorials/plot_parse.py')

        for blabel, bcontent in blocks:
            if blabel == 'code':
                example_nb.add_code_cell(bcontent)
            else:
                example_nb.add_markdown_cell(sg.text2string(bcontent))

        example_nb.save_file()
        with open(f.name, 'r') as f:
            assert_equal(json.load(f), example_nb.work_notebook)
    finally:
        os.remove(f.name)


def test_thumbnail_number():
    # which plot to show as the thumbnail image
    for test_str in ['# sphinx_gallery_thumbnail_number= 2',
                     '# sphinx_gallery_thumbnail_number=2',
                     '#sphinx_gallery_thumbnail_number = 2',
                     '    # sphinx_gallery_thumbnail_number=2']:
        with tempfile.NamedTemporaryFile('w', delete=False) as f:
            f.write('\n'.join(['"Docstring"', test_str]))
        try:
            _, content = sg.get_docstring_and_rest(f.name)
        finally:
            os.remove(f.name)
        thumbnail_number = sg.extract_thumbnail_number(content)
        assert_equal(thumbnail_number, 2)


def test_save_figures():
    """Test file naming when saving figures. Requires mayavi."""
    try:
        from mayavi import mlab
    except ImportError:
        raise nose.SkipTest('Mayavi not installed')
    mlab.options.offscreen = True
    examples_dir = tempfile.mkdtemp()

    gallery_conf = {'find_mayavi_figures': True}
    mlab.test_plot3d()
    plt.plot(1, 1)
    fname_template = os.path.join(examples_dir, 'image{0}.png')
    fig_list, _ = sg.save_figures(fname_template, 0, gallery_conf)
    assert_equal(len(fig_list), 2)
    assert_true(fig_list[0].endswith('image1.png'))
    assert_true(fig_list[1].endswith('image2.png'))
    gen_rst.clean_modules(gallery_conf)
    # everything closed properly
    assert_true(all(plt.fignum_exists(ii) is False for ii in range(10)))
    assert_equal(len(mlab.get_engine().scenes), 0)

    mlab.test_plot3d()
    plt.plot(1, 1)
    fig_list, _ = sg.save_figures(fname_template, 2, gallery_conf)
    assert_equal(len(fig_list), 2)
    assert_true(fig_list[0].endswith('image3.png'))
    assert_true(fig_list[1].endswith('image4.png'))
    gen_rst.clean_modules(gallery_conf)
    shutil.rmtree(examples_dir)

    # test full pipeline
    gallery_conf = build_test_configuration(
        filename_pattern=re.escape(os.sep) + 'plot_0')
    gallery_conf['find_mayavi_figures'] = True
    with codecs.open(os.path.join(gallery_conf['examples_dir'], 'plot_0.py'),
                     mode='w', encoding='utf-8') as f:
        f.write('\n'.join(FIGURE_CONTENT))
    sg.generate_file_rst('plot_0.py', gallery_conf['gallery_dir'],
                         gallery_conf['examples_dir'], gallery_conf)
    assert_true(all(plt.fignum_exists(ii) is False for ii in range(10)))
    assert_equal(len(mlab.get_engine().scenes), 0)
    # read rst file and check if it contains code output
    rst_fname = os.path.splitext('plot_0.py')[0] + '.rst'
    with codecs.open(os.path.join(gallery_conf['gallery_dir'], rst_fname),
                     mode='r', encoding='utf-8') as f:
        rst = f.read()
    assert_true('AssertionError' not in rst, msg=rst)
    # check image count, should be four total: 2 in Section 1, 0 in 2, 2 in 3
    sections = rst.split('\nSection ')
    assert_equal(len(sections), 4)
    assert_equal(sections[1].count('.. image::'), 2)
    assert_equal(sections[2].count('.. image::'), 0)
    assert_equal(sections[3].count('.. image::'), 2)


def test_zip_notebooks():
    """Test generated zipfiles are not corrupt"""
    gallery_conf = build_test_configuration(examples_dir='examples')
    examples = downloads.list_downloadable_sources(
        gallery_conf['examples_dir'])
    zipfilepath = downloads.python_zip(examples, gallery_conf['gallery_dir'])
    zipf = zipfile.ZipFile(zipfilepath)
    check = zipf.testzip()
    if check:
        raise OSError("Bad file in zipfile: {0}".format(check))


# TODO: test that broken thumbnail does appear when needed
# TODO: test that examples are not executed twice
# TODO: test that examples are executed after a no-plot and produce
#       the correct image in the thumbnail
