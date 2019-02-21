# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Test the SG pipeline used with Sphinx
"""
from __future__ import division, absolute_import, print_function

import codecs
import os
import os.path as op
import shutil

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
    timings_fname = op.join(out_dir, 'auto_examples',
                            'sg_execution_times.html')
    assert op.isfile(timings_fname)


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


def test_rebuild(tmpdir_factory, sphinx_app):
    # Make sure that examples that haven't been changed aren't run twice.
    # The app has already been run once in the fixture.

    status = sphinx_app._status.getvalue()
    assert "generating gallery for auto_examples..." in status
    generated_modules = os.listdir(os.path.join(sphinx_app.srcdir,
                                                'gen_modules'))
    generated_modules = sorted(os.path.join(sphinx_app.srcdir,
                                            'gen_modules', f)
                               for f in generated_modules)
    generated_mtimes_first = [os.path.getmtime(generated_module)
                              for generated_module in generated_modules]
    not_updated_examples = \
        sphinx_app.config.sphinx_gallery_conf['not_updated_examples']
    assert not_updated_examples == set()  # All examples are updated

    # run a second time, files shouldn't be updated
    temp_dir = (tmpdir_factory.getbasetemp() / 'root').strpath
    src_dir = temp_dir
    conf_dir = temp_dir
    out_dir = op.join(temp_dir, '_build', 'html')
    toctrees_dir = op.join(temp_dir, '_build', 'toctrees')
    with docutils_namespace():
        new_app = Sphinx(src_dir, conf_dir, out_dir, toctrees_dir,
                         buildername='html', status=MixedEncodingStringIO())
        new_app.build(False, [])
    status = new_app._status.getvalue()
    # assert "generating gallery for auto_examples..." not in status
    generated_mtimes_second = [os.path.getmtime(generated_module)
                               for generated_module in generated_modules]
    assert generated_mtimes_first == generated_mtimes_second

    not_updated_examples = \
        new_app.config.sphinx_gallery_conf['not_updated_examples']
    assert not_updated_examples  # not empty
