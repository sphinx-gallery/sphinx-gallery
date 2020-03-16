# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Test the SG pipeline used with Sphinx
"""
from __future__ import division, absolute_import, print_function

import codecs
from io import StringIO
import os
import os.path as op
import re
import shutil
import sys
import time

import numpy as np
from numpy.testing import assert_allclose

from sphinx.application import Sphinx
from sphinx.util.docutils import docutils_namespace
from sphinx_gallery.utils import _get_image, scale_image

import pytest

N_TOT = 6
N_FAILING = 1
N_GOOD = N_TOT - N_FAILING
N_RST = 14 + N_TOT
N_RST = '(%s|%s)' % (N_RST, N_RST - 1)  # AppVeyor weirdness


@pytest.fixture(scope='module')
def sphinx_app(tmpdir_factory, req_mpl, req_pil):
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
                     buildername='html', status=StringIO(),
                     warning=StringIO())
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
    with codecs.open(timings_rst, 'r', 'utf-8') as fid:
        content = fid.read()
    assert ':ref:`sphx_glr_auto_examples_plot_numpy_matplotlib.py`' in content
    parenthetical = '(``%s``)' % ('plot_numpy_matplotlib.py',)
    assert parenthetical in content
    # HTML output
    timings_html = op.join(out_dir, 'auto_examples',
                           'sg_execution_times.html')
    assert op.isfile(timings_html)
    with codecs.open(timings_html, 'r', 'utf-8') as fid:
        content = fid.read()
    assert 'href="plot_numpy_matplotlib.html' in content
    # printed
    status = sphinx_app._status.getvalue()
    fname = op.join('examples', 'plot_numpy_matplotlib.py')
    assert ('- %s: ' % fname) in status


def test_junit(sphinx_app, tmpdir):
    out_dir = sphinx_app.outdir
    junit_file = op.join(out_dir, 'sphinx-gallery', 'junit-results.xml')
    assert op.isfile(junit_file)
    with codecs.open(junit_file, 'r', 'utf-8') as fid:
        contents = fid.read()
    assert contents.startswith('<?xml')
    assert 'errors="0" failures="0"' in contents
    assert 'tests="%d"' % (N_TOT,) in contents
    assert 'local_module' not in contents  # it's not actually run as an ex
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
    failing_fname = op.join(new_src_dir, 'examples', 'future',
                            'plot_future_imports_broken.py')
    shutil.move(passing_fname, passing_fname + '.temp')
    shutil.move(failing_fname, passing_fname)
    shutil.move(passing_fname + '.temp', failing_fname)
    with docutils_namespace():
        app = Sphinx(new_src_dir, new_src_dir, new_out_dir,
                     new_toctree_dir,
                     buildername='html', status=StringIO())
        # need to build within the context manager
        # for automodule and backrefs to work
        with pytest.raises(ValueError, match='Here is a summary of the '):
            app.build(False, [])
    junit_file = op.join(new_out_dir, 'sphinx-gallery', 'junit-results.xml')
    assert op.isfile(junit_file)
    with codecs.open(junit_file, 'r', 'utf-8') as fid:
        contents = fid.read()
    assert 'errors="0" failures="2"' in contents
    assert 'tests="2"' in contents  # this time we only ran the two stale files
    assert '<failure message="RuntimeError: Forcing' in contents
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
    assert 'executed %d out of %d' % (N_GOOD, N_TOT) in status
    assert 'after excluding 0' in status
    # intentionally have a bad URL in references
    warning = sphinx_app._warning.getvalue()
    want = '.*fetching .*wrong_url.*404.*'
    assert re.match(want, warning, re.DOTALL) is not None, warning


def test_thumbnail_path(sphinx_app, tmpdir):
    """Test sphinx_gallery_thumbnail_path."""
    # Make sure our thumbnail matches what it should be
    fname_orig = op.join(
        sphinx_app.srcdir, '_static', 'demo.png')
    fname_thumb = op.join(
        sphinx_app.outdir, '_images',
        'sphx_glr_plot_second_future_imports_thumb.png')
    fname_new = str(tmpdir.join('new.png'))
    scale_image(fname_orig, fname_new,
                *sphinx_app.config.sphinx_gallery_conf["thumbnail_size"])
    Image = _get_image()
    orig = np.asarray(Image.open(fname_thumb))
    new = np.asarray(Image.open(fname_new))
    assert new.shape == orig.shape
    corr = np.corrcoef(new.ravel(), orig.ravel())[0, 1]
    assert corr > 0.99


def test_image_formats(sphinx_app):
    """Test Image format support."""
    generated_examples_dir = op.join(sphinx_app.outdir, 'auto_examples')
    generated_examples_index = op.join(generated_examples_dir, 'index.html')
    with codecs.open(generated_examples_index, 'r', 'utf-8') as fid:
        html = fid.read()
    thumb_fnames = ['../_images/sphx_glr_plot_svg_thumb.svg',
                    '../_images/sphx_glr_plot_numpy_matplotlib_thumb.png']
    for thumb_fname in thumb_fnames:
        file_fname = op.join(generated_examples_dir, thumb_fname)
        assert op.isfile(file_fname)
        want_html = 'src="%s"' % (thumb_fname,)
        assert want_html in html
    for ex, ext in (('plot_svg', 'svg'),
                    ('plot_numpy_matplotlib', 'png'),
                    ):
        html_fname = op.join(generated_examples_dir, '%s.html' % ex)
        with codecs.open(html_fname, 'r', 'utf-8') as fid:
            html = fid.read()
        img_fname = '../_images/sphx_glr_%s_001.%s' % (ex, ext)
        file_fname = op.join(generated_examples_dir, img_fname)
        assert op.isfile(file_fname)
        want_html = 'src="%s"' % (img_fname,)
        assert want_html in html


def test_embed_links_and_styles(sphinx_app):
    """Test that links and styles are embedded properly in doc."""
    out_dir = sphinx_app.outdir
    src_dir = sphinx_app.srcdir
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
    assert 'class="sphx-glr-backref-module-matplotlib-colors sphx-glr-backref-type-py-function">' in lines  # noqa: E501
    assert '#module-numpy' in lines
    assert 'numpy.arange.html' in lines
    assert 'class="sphx-glr-backref-module-numpy sphx-glr-backref-type-py-function">' in lines  # noqa: E501
    assert '#module-matplotlib.pyplot' in lines
    assert 'pyplot.html' in lines
    assert 'matplotlib.figure.Figure.html#matplotlib.figure.Figure.tight_layout' in lines  # noqa: E501
    assert 'matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot' in lines
    assert 'matplotlib_configuration_api.html#matplotlib.RcParams' in lines
    assert 'stdtypes.html#list' in lines
    assert 'warnings.html#warnings.warn' in lines
    assert 'itertools.html#itertools.compress' in lines
    assert 'numpy.ndarray.html' in lines
    # see issue 617
    id_names = re.search(
        r'sphinx_gallery.backreferences.html#sphinx[_,-]gallery[.,-]backreferences[.,-]identify[_,-]names', # noqa: E501
        lines
    )
    assert id_names is not None
    # instances have an extra CSS class
    assert 'class="sphx-glr-backref-module-matplotlib-figure sphx-glr-backref-type-py-class sphx-glr-backref-instance"><span class="n">x</span></a>' in lines  # noqa: E501
    assert 'class="sphx-glr-backref-module-matplotlib-figure sphx-glr-backref-type-py-class"><span class="n">Figure</span></a>' in lines  # noqa: E501
    # gh-587: no classes that are only marked as module without type
    assert re.search(r'"sphx-glr-backref-module-\S*"', lines) is None
    assert 'class="sphx-glr-backref-module-sphinx_gallery-backreferences sphx-glr-backref-type-py-function"><span class="n">sphinx_gallery</span><span class="o">.</span><span class="n">backreferences</span><span class="o">.</span><span class="n">identify_names</span></a>' in lines  # noqa: E501
    # gh-587: np.random.RandomState links properly
    # NumPy has had this linked as numpy.random.RandomState and
    # numpy.random.mtrand.RandomState so we need regex...
    assert re.search(r'\.html#numpy\.random\.(mtrand\.?)RandomState" title="numpy\.random\.(mtrand\.?)RandomState" class="sphx-glr-backref-module-numpy-random(-mtrand?) sphx-glr-backref-type-py-class"><span class="n">np</span>', lines) is not None  # noqa: E501
    assert re.search(r'\.html#numpy\.random\.(mtrand\.?)RandomState" title="numpy\.random\.(mtrand\.?)RandomState" class="sphx-glr-backref-module-numpy-random(-mtrand?) sphx-glr-backref-type-py-class sphx-glr-backref-instance"><span class="n">rng</span></a>', lines) is not None  # noqa: E501
    # gh-587: methods of classes in the module currently being documented
    # issue 617 (regex '-'s)
    # instance
    dummy_class_inst = re.search(
        r'sphinx_gallery.backreferences.html#sphinx[_,-]gallery[.,-]backreferences[.,-][D,d]ummy[C,c]lass" title="sphinx_gallery.backreferences.DummyClass" class="sphx-glr-backref-module-sphinx_gallery-backreferences sphx-glr-backref-type-py-class sphx-glr-backref-instance"><span class="n">dc</span>', # noqa: E501
        lines
    )
    assert dummy_class_inst is not None
    # class
    dummy_class_class = re.search(
        r'sphinx_gallery.backreferences.html#sphinx[_,-]gallery[.,-]backreferences[.,-][D,d]ummy[C,c]lass" title="sphinx_gallery.backreferences.DummyClass" class="sphx-glr-backref-module-sphinx_gallery-backreferences sphx-glr-backref-type-py-class"><span class="n">sphinx_gallery</span><span class="o">.</span><span class="n">backreferences</span><span class="o">.</span><span class="n">DummyClass</span>', # noqa: E501
        lines
    )
    assert dummy_class_class is not None
    # method
    dummy_class_meth = re.search(
        r'sphinx_gallery.backreferences.html#sphinx[_,-]gallery[.,-]backreferences[.,-][D,d]ummy[C,c]lass[.,-]run" title="sphinx_gallery.backreferences.DummyClass.run" class="sphx-glr-backref-module-sphinx_gallery-backreferences sphx-glr-backref-type-py-method"><span class="n">dc</span><span class="o">.</span><span class="n">run</span>', # noqa: E501
        lines
    )
    assert dummy_class_meth is not None
    # property (Sphinx 2+ calls it a method rather than attribute, so regex)
    dummy_class_prop = re.compile(r'sphinx_gallery.backreferences.html#sphinx[_,-]gallery[.,-]backreferences[.,-][D,d]ummy[C,c]lass[.,-]prop" title="sphinx_gallery.backreferences.DummyClass.prop" class="sphx-glr-backref-module-sphinx_gallery-backreferences sphx-glr-backref-type-py-(attribute|method)"><span class="n">dc</span><span class="o">.</span><span class="n">prop</span>') # noqa: E501
    assert dummy_class_prop.search(lines) is not None

    try:
        import memory_profiler  # noqa, analysis:ignore
    except ImportError:
        assert "memory usage" not in lines
    else:
        assert "memory usage" in lines

    # CSS styles
    assert 'class="sphx-glr-signature"' in lines
    assert 'class="sphx-glr-timing"' in lines
    for kind in ('python', 'jupyter'):
        assert 'class="sphx-glr-download sphx-glr-download-%s docutils container"' % kind in lines  # noqa:E501

    # highlight language
    fname = op.join(src_dir, 'auto_examples', 'plot_numpy_matplotlib.rst')
    assert op.isfile(fname)
    with codecs.open(fname, 'r', 'utf-8') as fid:
        rst = fid.read()
    assert '.. code-block:: python3\n' in rst

    # warnings
    want_warn = (r'.*plot_numpy_matplotlib\.py:[0-9][0-9]: RuntimeWarning: '
                 r'This warning should show up in the output.*')
    assert re.match(want_warn, lines, re.DOTALL) is not None
    sys.stdout.write(lines)

    example_file = op.join(examples_dir, 'plot_pickle.html')
    with codecs.open(example_file, 'r', 'utf-8') as fid:
        lines = fid.read()
    assert 'joblib.Parallel.html' in lines


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
    assert 'NameFinder' in lines  # in API doc
    assert 'plot_future_imports.html' in lines  # backref via doc block


@pytest.mark.parametrize('rst_file, example_used_in', [
    ('sphinx_gallery.backreferences.identify_names.examples', 'plot_numpy_matplotlib'),
    ('sphinx_gallery.sorting.ExplicitOrder.examples', 'plot_second_future_imports'),
])
def test_backreferences_examples(sphinx_app, rst_file, example_used_in):
    """Test linking to mini-galleries using backreferences_dir."""
    backref_dir = sphinx_app.srcdir
    examples_rst = op.join(backref_dir, 'gen_modules', 'backreferences',
                           rst_file)
    with codecs.open(examples_rst, 'r', 'utf-8') as fid:
        lines = fid.read()
    assert example_used_in in lines


def _assert_mtimes(list_orig, list_new, different=(), ignore=()):
    assert ([op.basename(x) for x in list_orig] ==
            [op.basename(x) for x in list_new])
    for orig, new in zip(list_orig, list_new):
        if op.basename(orig) in different:
            assert np.abs(op.getmtime(orig) - op.getmtime(new)) > 0.1
        elif op.basename(orig) not in ignore:
            assert_allclose(op.getmtime(orig), op.getmtime(new),
                            atol=1e-3, rtol=1e-20, err_msg=op.basename(orig))


def test_rebuild(tmpdir_factory, sphinx_app):
    # Make sure that examples that haven't been changed aren't run twice.

    #
    # First run completes in the fixture.
    #
    status = sphinx_app._status.getvalue()
    lines = [line for line in status.split('\n') if 'removed' in line]
    want = '.*%s added, 0 changed, 0 removed.*' % (N_RST,)
    assert re.match(want, status, re.MULTILINE | re.DOTALL) is not None, lines
    want = '.*targets for 2 source files that are out of date$.*'
    lines = [line for line in status.split('\n') if 'out of date' in line]
    assert re.match(want, status, re.MULTILINE | re.DOTALL) is not None, lines
    lines = [line for line in status.split('\n') if 'on MD5' in line]
    want = ('.*executed %d out of %d.*after excluding 0 files.*based on MD5.*'
            % (N_GOOD, N_TOT))
    assert re.match(want, status, re.MULTILINE | re.DOTALL) is not None, lines
    old_src_dir = (tmpdir_factory.getbasetemp() / 'root_old').strpath
    shutil.copytree(sphinx_app.srcdir, old_src_dir)
    generated_modules_0 = sorted(
        op.join(old_src_dir, 'gen_modules', f)
        for f in os.listdir(op.join(old_src_dir, 'gen_modules'))
        if op.isfile(op.join(old_src_dir, 'gen_modules', f)))
    generated_backrefs_0 = sorted(
        op.join(old_src_dir, 'gen_modules', 'backreferences', f)
        for f in os.listdir(op.join(old_src_dir, 'gen_modules',
                                    'backreferences')))
    generated_rst_0 = sorted(
        op.join(old_src_dir, 'auto_examples', f)
        for f in os.listdir(op.join(old_src_dir, 'auto_examples'))
        if f.endswith('.rst'))
    generated_pickle_0 = sorted(
        op.join(old_src_dir, 'auto_examples', f)
        for f in os.listdir(op.join(old_src_dir, 'auto_examples'))
        if f.endswith('.pickle'))
    copied_py_0 = sorted(
        op.join(old_src_dir, 'auto_examples', f)
        for f in os.listdir(op.join(old_src_dir, 'auto_examples'))
        if f.endswith('.py'))
    copied_ipy_0 = sorted(
        op.join(old_src_dir, 'auto_examples', f)
        for f in os.listdir(op.join(old_src_dir, 'auto_examples'))
        if f.endswith('.ipynb'))
    assert len(generated_modules_0) > 0
    assert len(generated_backrefs_0) > 0
    assert len(generated_rst_0) > 0
    assert len(generated_pickle_0) > 0
    assert len(copied_py_0) > 0
    assert len(copied_ipy_0) > 0
    assert len(sphinx_app.config.sphinx_gallery_conf['stale_examples']) == 0
    assert op.isfile(op.join(sphinx_app.outdir, '_images',
                             'sphx_glr_plot_numpy_matplotlib_001.png'))

    #
    # run a second time, no files should be updated
    #

    src_dir = sphinx_app.srcdir
    del sphinx_app  # don't accidentally use it below
    conf_dir = src_dir
    out_dir = op.join(src_dir, '_build', 'html')
    toctrees_dir = op.join(src_dir, '_build', 'toctrees')
    time.sleep(0.1)
    with docutils_namespace():
        new_app = Sphinx(src_dir, conf_dir, out_dir, toctrees_dir,
                         buildername='html', status=StringIO())
        new_app.build(False, [])
    status = new_app._status.getvalue()
    lines = [line for line in status.split('\n') if '0 removed' in line]
    assert re.match('.*[0|1] added, [1-9] changed, 0 removed$.*',
                    status, re.MULTILINE | re.DOTALL) is not None, lines
    want = ('.*executed 0 out of 1.*after excluding %s files.*based on MD5.*'
            % (N_GOOD,))
    assert re.match(want, status, re.MULTILINE | re.DOTALL) is not None
    n_stale = len(new_app.config.sphinx_gallery_conf['stale_examples'])
    assert n_stale == N_GOOD
    assert op.isfile(op.join(new_app.outdir, '_images',
                             'sphx_glr_plot_numpy_matplotlib_001.png'))

    generated_modules_1 = sorted(
        op.join(new_app.srcdir, 'gen_modules', f)
        for f in os.listdir(op.join(new_app.srcdir, 'gen_modules'))
        if op.isfile(op.join(new_app.srcdir, 'gen_modules', f)))
    generated_backrefs_1 = sorted(
        op.join(new_app.srcdir, 'gen_modules', 'backreferences', f)
        for f in os.listdir(op.join(new_app.srcdir, 'gen_modules',
                                    'backreferences')))
    generated_rst_1 = sorted(
        op.join(new_app.srcdir, 'auto_examples', f)
        for f in os.listdir(op.join(new_app.srcdir, 'auto_examples'))
        if f.endswith('.rst'))
    generated_pickle_1 = sorted(
        op.join(new_app.srcdir, 'auto_examples', f)
        for f in os.listdir(op.join(new_app.srcdir, 'auto_examples'))
        if f.endswith('.pickle'))
    copied_py_1 = sorted(
        op.join(new_app.srcdir, 'auto_examples', f)
        for f in os.listdir(op.join(new_app.srcdir, 'auto_examples'))
        if f.endswith('.py'))
    copied_ipy_1 = sorted(
        op.join(new_app.srcdir, 'auto_examples', f)
        for f in os.listdir(op.join(new_app.srcdir, 'auto_examples'))
        if f.endswith('.ipynb'))

    # mtimes for modules
    _assert_mtimes(generated_modules_0, generated_modules_1)

    # mtimes for backrefs (gh-394)
    _assert_mtimes(generated_backrefs_0, generated_backrefs_1)

    # generated RST files
    ignore = (
        # these two should almost always be different, but in case we
        # get extremely unlucky and have identical run times
        # on the one script that gets re-run (because it's a fail)...
        'sg_execution_times.rst',
        'plot_future_imports_broken.rst',
    )
    _assert_mtimes(generated_rst_0, generated_rst_1, ignore=ignore)

    # mtimes for pickles
    _assert_mtimes(generated_pickle_0, generated_pickle_1)

    # mtimes for .py files (gh-395)
    _assert_mtimes(copied_py_0, copied_py_1)

    # mtimes for .ipynb files
    _assert_mtimes(copied_ipy_0, copied_ipy_1)

    #
    # run a third time, changing one file
    #

    time.sleep(0.1)
    fname = op.join(src_dir, 'examples', 'plot_numpy_matplotlib.py')
    with codecs.open(fname, 'r', 'utf-8') as fid:
        lines = fid.readlines()
    with codecs.open(fname, 'w', 'utf-8') as fid:
        for line in lines:
            if line.startswith('FYI this'):
                line = 'A ' + line
            fid.write(line)
    with docutils_namespace():
        new_app = Sphinx(src_dir, conf_dir, out_dir, toctrees_dir,
                         buildername='html', status=StringIO())
        new_app.build(False, [])
    status = new_app._status.getvalue()
    n = '[2|3|4]'
    lines = [line for line in status.split('\n') if 'source files tha' in line]
    want = '.*targets for %s source files that are out of date$.*' % n
    assert re.match(want, status, re.MULTILINE | re.DOTALL) is not None, lines
    want = ('.*executed 1 out of 2.*after excluding %s files.*based on MD5.*'
            % (N_GOOD - 1,))
    assert re.match(want, status, re.MULTILINE | re.DOTALL) is not None
    n_stale = len(new_app.config.sphinx_gallery_conf['stale_examples'])
    assert n_stale == N_GOOD - 1
    assert op.isfile(op.join(new_app.outdir, '_images',
                             'sphx_glr_plot_numpy_matplotlib_001.png'))

    generated_modules_1 = sorted(
        op.join(new_app.srcdir, 'gen_modules', f)
        for f in os.listdir(op.join(new_app.srcdir, 'gen_modules'))
        if op.isfile(op.join(new_app.srcdir, 'gen_modules', f)))
    generated_backrefs_1 = sorted(
        op.join(new_app.srcdir, 'gen_modules', 'backreferences', f)
        for f in os.listdir(op.join(new_app.srcdir, 'gen_modules',
                                    'backreferences')))
    generated_rst_1 = sorted(
        op.join(new_app.srcdir, 'auto_examples', f)
        for f in os.listdir(op.join(new_app.srcdir, 'auto_examples'))
        if f.endswith('.rst'))
    generated_pickle_1 = sorted(
        op.join(new_app.srcdir, 'auto_examples', f)
        for f in os.listdir(op.join(new_app.srcdir, 'auto_examples'))
        if f.endswith('.pickle'))
    copied_py_1 = sorted(
        op.join(new_app.srcdir, 'auto_examples', f)
        for f in os.listdir(op.join(new_app.srcdir, 'auto_examples'))
        if f.endswith('.py'))
    copied_ipy_1 = sorted(
        op.join(new_app.srcdir, 'auto_examples', f)
        for f in os.listdir(op.join(new_app.srcdir, 'auto_examples'))
        if f.endswith('.ipynb'))

    # mtimes for modules
    _assert_mtimes(generated_modules_0, generated_modules_1)

    # mtimes for backrefs (gh-394)
    _assert_mtimes(generated_backrefs_0, generated_backrefs_1)

    # generated RST files
    different = (
        'plot_numpy_matplotlib.rst',
    )
    ignore = (
        # this one should almost always be different, but in case we
        # get extremely unlucky and have identical run times
        # on the one script above that changes...
        'sg_execution_times.rst',
        # this one will not change even though it was retried
        'plot_future_imports_broken.rst',
    )
    if not sys.platform.startswith('win'):  # not reliable on Windows
        _assert_mtimes(generated_rst_0, generated_rst_1, different, ignore)

        # mtimes for pickles
        _assert_mtimes(generated_pickle_0, generated_pickle_1,
                       different=('plot_numpy_matplotlib.codeobj.pickle'))

        # mtimes for .py files (gh-395)
        _assert_mtimes(copied_py_0, copied_py_1,
                       different=('plot_numpy_matplotlib.py'))

        # mtimes for .ipynb files
        _assert_mtimes(copied_ipy_0, copied_ipy_1,
                       different=('plot_numpy_matplotlib.ipynb'))
