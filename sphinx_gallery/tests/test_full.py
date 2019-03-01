# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Test the SG pipeline used with Sphinx
"""
from __future__ import division, absolute_import, print_function

import codecs
from distutils.version import LooseVersion
import os
import os.path as op
import shutil
import sys

from sphinx.application import Sphinx
from sphinx.util.docutils import docutils_namespace
from sphinx_gallery.gen_rst import MixedEncodingStringIO

import pytest


@pytest.fixture(scope='module')
def sphinx_app(tmpdir_factory):
    temp_dir = (tmpdir_factory.getbasetemp() / 'root').strpath
    src_dir = op.join(op.dirname(__file__), 'tinybuild')

    def ignore(src, names):
        return ('_build', 'gen_modules', 'auto_examples')

    shutil.copytree(src_dir, temp_dir, ignore=ignore)
    # For testing iteration, you can get similar behavior just doing `make`
    # inside the tinybuild directory
    src_dir = temp_dir
    conf_dir = temp_dir
    out_dir = op.join(temp_dir, '_build', 'html')
    toctrees_dir = op.join(temp_dir, '_build', 'toctrees')
    # Avoid warnings about re-registration, see:
    # https://github.com/sphinx-doc/sphinx/issues/5038
    with docutils_namespace():
        app = Sphinx(src_dir, conf_dir, out_dir, toctrees_dir,
                     buildername='html', status=MixedEncodingStringIO())
        # need to build within the context manager
        # for automodule and backrefs to work
        app.build(False, [])
    return app


def test_timings(sphinx_app):
    """Test that a timings page is created."""
    out_dir = sphinx_app.outdir
    src_dir = sphinx_app.srcdir
    # local folder
    timings_rst = op.join(src_dir, 'auto_examples',
                          'sg_execution_times.rst')
    assert op.isfile(timings_rst)
    with open(timings_rst, 'rb') as fid:
        content = fid.read().decode('utf-8')
    assert ':ref:`sphx_glr_auto_examples_plot_numpy_matplotlib.py`' in content
    parenthetical = '(``%s``)' % ('plot_numpy_matplotlib.py',)
    assert parenthetical in content
    # HTML output
    timings_html = op.join(out_dir, 'auto_examples',
                           'sg_execution_times.html')
    assert op.isfile(timings_html)
    with open(timings_html, 'rb') as fid:
        content = fid.read().decode('utf-8')
    assert 'href="plot_numpy_matplotlib.html' in content
    # printed
    status = sphinx_app._status.getvalue()
    assert '- examples/plot_numpy_matplotlib.py: ' in status


def test_junit(sphinx_app, tmpdir):
    out_dir = sphinx_app.outdir
    junit_file = op.join(out_dir, 'sphinx-gallery', 'junit-results.xml')
    assert op.isfile(junit_file)
    with open(junit_file, 'rb') as fid:
        contents = fid.read().decode('utf-8')
    assert contents.startswith('<?xml')
    assert 'errors="0" failures="0"' in contents
    assert 'tests="5"' in contents
    assert 'expected example failure' in contents
    assert '<failure message' not in contents
    src_dir = sphinx_app.srcdir
    new_src_dir = op.join(str(tmpdir), 'src')
    shutil.copytree(src_dir, new_src_dir)
    del src_dir
    new_out_dir = op.join(new_src_dir, '_build', 'html')
    new_toctree_dir = op.join(new_src_dir, '_build', 'toctrees')
    passing_fname = op.join(new_src_dir, 'examples',
                            'plot_numpy_matplotlib.py')
    failing_fname = op.join(new_src_dir, 'examples',
                            'plot_future_imports_broken.py')
    shutil.move(passing_fname, passing_fname + '.temp')
    shutil.move(failing_fname, passing_fname)
    shutil.move(passing_fname + '.temp', failing_fname)
    with docutils_namespace():
        app = Sphinx(new_src_dir, new_src_dir, new_out_dir,
                     new_toctree_dir,
                     buildername='html', status=MixedEncodingStringIO())
        # need to build within the context manager
        # for automodule and backrefs to work
        with pytest.raises(ValueError, match='Here is a summary of the '):
            app.build(False, [])
    junit_file = op.join(new_out_dir, 'sphinx-gallery', 'junit-results.xml')
    assert op.isfile(junit_file)
    with open(junit_file, 'rb') as fid:
        contents = fid.read().decode('utf-8')
    assert 'errors="0" failures="2"' in contents
    assert 'tests="5"' in contents
    if LooseVersion(sys.version) >= LooseVersion('3'):
        assert '<failure message="RuntimeError: Forcing' in contents
    else:
        assert '<failure message="SyntaxError: invalid' in contents
    assert 'Passed even though it was marked to fail' in contents


def test_run_sphinx(sphinx_app):
    """Test basic outputs."""
    out_dir = sphinx_app.outdir
    out_files = os.listdir(out_dir)
    assert 'index.html' in out_files
    assert 'auto_examples' in out_files
    generated_examples_dir = op.join(out_dir, 'auto_examples')
    assert op.isdir(generated_examples_dir)
    status = sphinx_app._status.getvalue()
    assert 'executed 3 out of 4' in status
    assert 'after excluding 0' in status


def test_embed_links_and_styles(sphinx_app):
    """Test that links and styles are embedded properly in doc."""
    out_dir = sphinx_app.outdir
    examples_dir = op.join(out_dir, 'auto_examples')
    assert op.isdir(examples_dir)
    example_files = os.listdir(examples_dir)
    assert 'plot_numpy_matplotlib.html' in example_files
    example_file = op.join(examples_dir, 'plot_numpy_matplotlib.html')
    with codecs.open(example_file, 'r', 'utf-8') as fid:
        lines = fid.read()
    # ensure we've linked properly
    assert '#module-matplotlib.colors' in lines
    assert 'matplotlib.colors.is_color_like' in lines
    assert '#module-numpy' in lines
    assert 'numpy.arange.html' in lines
    assert '#module-matplotlib.pyplot' in lines
    assert 'pyplot.html' in lines
    try:
        import memory_profiler  # noqa, analysis:ignore
    except ImportError:
        assert "memory usage" not in lines
    else:
        assert "memory usage" in lines
    # CSS styles
    assert 'class="sphx-glr-signature"' in lines
    assert 'class="sphx-glr-timing"' in lines


def test_backreferences(sphinx_app):
    """Test backreferences."""
    out_dir = sphinx_app.outdir
    mod_file = op.join(out_dir, 'gen_modules', 'sphinx_gallery.sorting.html')
    with codecs.open(mod_file, 'r', 'utf-8') as fid:
        lines = fid.read()
    assert 'ExplicitOrder' in lines  # in API doc
    assert 'plot_second_future_imports.html' in lines  # backref via code use
    assert 'FileNameSortKey' in lines  # in API doc
    assert 'plot_numpy_matplotlib.html' in lines  # backref via :class: in str
    mod_file = op.join(out_dir, 'gen_modules',
                       'sphinx_gallery.backreferences.html')
    with codecs.open(mod_file, 'r', 'utf-8') as fid:
        lines = fid.read()
    assert 'identify_names' in lines  # in API doc
    assert 'plot_future_imports.html' in lines  # backref via doc block
