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
    app = Sphinx(src_dir, conf_dir, out_dir, toctrees_dir, buildername='html')
    app.build(False, [])
    return app


def test_run_sphinx(sphinx_app):
    out_dir = sphinx_app.outdir
    out_files = os.listdir(out_dir)
    assert 'index.html' in out_files
    assert 'auto_examples' in out_files
    generated_examples_dir = op.join(out_dir, 'auto_examples')
    assert op.isdir(generated_examples_dir)


def test_embed_links(sphinx_app):
    """Test that links are embedded properly in doc."""
    out_dir = sphinx_app.outdir
    examples_dir = op.join(out_dir, 'auto_examples')
    assert op.isdir(examples_dir)
    example_files = os.listdir(examples_dir)
    assert 'plot_numpy_scipy.html' in example_files
    example_file = op.join(examples_dir, 'plot_numpy_scipy.html')
    with codecs.open(example_file, 'r', 'utf-8') as fid:
        lines = fid.read()
    # ensure we've linked properly
    assert '#module-scipy.signal' in lines
    assert 'scipy.signal.firwin.html' in lines
    assert '#module-numpy' in lines
    assert 'numpy.arange.html' in lines
    # assert '#module-matplotlib.pyplot' in lines
    # assert 'pyplot.html' in lines
