# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
r"""
Test Sphinx-Gallery
"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import codecs
import os
import sys
import re
import shutil
import pytest
from sphinx.application import Sphinx
from sphinx.errors import ExtensionError
from sphinx_gallery.gen_rst import MixedEncodingStringIO
from sphinx_gallery import sphinx_compatibility
from sphinx_gallery.gen_gallery import (check_duplicate_filenames,
                                        collect_gallery_files)
from sphinx_gallery.utils import _TempDir


@pytest.fixture
def conf_file(request):
    env = request.node.get_marker('conf_file')
    kwargs = env.kwargs if env else {}
    result = {
        'content': "",
    }
    result.update(kwargs)

    return result


@pytest.fixture
def tempdir():
    """
    temporary directory that wrapped with `path` class.
    this fixture is for compat with old test implementation.
    """
    return _TempDir()


@pytest.fixture
def config_app(tempdir, conf_file):
    _fixturedir = os.path.join(os.path.dirname(__file__), 'testconfs')
    srcdir = os.path.join(tempdir, "config_test")
    shutil.copytree(_fixturedir, srcdir)
    shutil.copytree(os.path.join(_fixturedir, "src"),
                    os.path.join(tempdir, "examples"))

    with open(os.path.join(srcdir, "conf.py"), "w") as conffile:
        conffile.write(conf_file['content'])

    app = Sphinx(srcdir, srcdir, os.path.join(srcdir, "_build"),
                 os.path.join(srcdir, "_build", "toctree"),
                 "html", warning=MixedEncodingStringIO())

    sphinx_compatibility._app = app
    return app


@pytest.mark.conf_file(content="""
import os
import sphinx_gallery
extensions = ['sphinx_gallery.gen_gallery']
# General information about the project.
project = u'Sphinx-Gallery <Tests>'""")
def test_default_config(config_app):
    """Test the default Sphinx-Gallery configuration is loaded

    if only the extension is added to Sphinx"""

    cfg = config_app.config
    assert cfg.project == "Sphinx-Gallery <Tests>"
    # no duplicate values allowed The config is present already
    with pytest.raises(ExtensionError) as excinfo:
        config_app.add_config_value('sphinx_gallery_conf', 'x', True)
    assert 'already present' in str(excinfo.value)


@pytest.mark.conf_file(content="""
import os
import sphinx_gallery
extensions = ['sphinx_gallery.gen_gallery']
# General information about the project.
project = u'Sphinx-Gallery <Tests>'

sphinx_gallery_conf = {
    'examples_dirs': 'src',
    'gallery_dirs': 'ex',
}""")
def test_no_warning_simple_config(config_app):
    """Testing that no warning is issued with a simple config.

    The simple config only specifies input (examples_dirs) and output
    (gallery_dirs) directories.
    """

    cfg = config_app.config
    assert cfg.project == "Sphinx-Gallery <Tests>"
    build_warn = config_app._warning.getvalue()
    assert build_warn == ''


@pytest.mark.conf_file(content="""
import os
import sphinx_gallery
extensions = ['sphinx_gallery.gen_gallery']
# General information about the project.
project = u'Sphinx-Gallery <Tests>'

sphinx_gallery_conf = {
    'mod_example_dir' : os.path.join('modules', 'gen'),
    'examples_dirs': 'src',
    'gallery_dirs': 'ex',
}""")
def test_config_old_backreferences_conf(config_app):
    """Testing Deprecation warning message against old backreference config

    In this case the user is required to update the mod_example_dir config
    variable Sphinx-Gallery should notify the user and also silently update
    the old config to the new one. """

    cfg = config_app.config
    assert cfg.project == "Sphinx-Gallery <Tests>"
    assert cfg.sphinx_gallery_conf['backreferences_dir'] == os.path.join(
        'modules', 'gen')
    build_warn = config_app._warning.getvalue()

    assert "WARNING:" in build_warn
    assert "deprecated" in build_warn
    assert "Support for 'mod_example_dir' will be removed" in build_warn


@pytest.mark.conf_file(content="""
import os
import sphinx_gallery
extensions = ['sphinx_gallery.gen_gallery']
# General information about the project.
project = u'Sphinx-Gallery <Tests>'

sphinx_gallery_conf = {
    'backreferences_dir': os.path.join('gen_modules', 'backreferences'),
    'examples_dirs': 'src',
    'gallery_dirs': 'ex',
}""")
def test_config_backreferences(config_app):
    """Test no warning is issued under the new configuration"""

    cfg = config_app.config
    assert cfg.project == "Sphinx-Gallery <Tests>"
    assert cfg.sphinx_gallery_conf['backreferences_dir'] == os.path.join(
        'gen_modules', 'backreferences')
    build_warn = config_app._warning.getvalue()
    assert build_warn == ""


def test_duplicate_files_warn(config_app):
    """Test for a warning when two files with the same filename exist."""
    files = ['./a/file1.py', './a/file2.py', 'a/file3.py', './b/file1.py']
    msg = ("Duplicate file name(s) found. Having duplicate file names "
           "will break some links. List of files: {}")
    m = "['./b/file1.py']" if sys.version_info[0] >= 3 else "[u'./b/file1.py']"

    # No warning because no overlapping names
    check_duplicate_filenames(files[:-1])
    warnings = config_app._warning.getvalue()
    assert warnings == ''

    # Warning because last file is named the same
    check_duplicate_filenames(files)
    warnings = config_app._warning.getvalue()
    assert msg.format(m) in warnings


def _check_order(config_app, key):
    index_fname = os.path.join(config_app.outdir, '..', 'ex', 'index.rst')
    order = list()
    regex = '.*:%s=(.):.*' % key
    with codecs.open(index_fname, 'r', 'utf-8') as fid:
        for line in fid:
            if 'sphx-glr-thumbcontainer' in line:
                order.append(int(re.match(regex, line).group(1)))
    assert len(order) == 3
    assert order == [1, 2, 3]


@pytest.mark.conf_file(content="""
import sphinx_gallery
extensions = ['sphinx_gallery.gen_gallery']
sphinx_gallery_conf = {
    'examples_dirs': 'src',
    'gallery_dirs': 'ex',
}""")
def test_example_sorting_default(config_app):
    """Test sorting of examples by default key (number of code lines)."""
    _check_order(config_app, 'lines')


@pytest.mark.conf_file(content="""
import sphinx_gallery
from sphinx_gallery.sorting import FileSizeSortKey
extensions = ['sphinx_gallery.gen_gallery']
sphinx_gallery_conf = {
    'examples_dirs': 'src',
    'gallery_dirs': 'ex',
    'within_subsection_order': FileSizeSortKey,
}""")
def test_example_sorting_filesize(config_app):
    """Test sorting of examples by filesize."""
    _check_order(config_app, 'filesize')


@pytest.mark.conf_file(content="""
import sphinx_gallery
from sphinx_gallery.sorting import FileNameSortKey
extensions = ['sphinx_gallery.gen_gallery']
sphinx_gallery_conf = {
    'examples_dirs': 'src',
    'gallery_dirs': 'ex',
    'within_subsection_order': FileNameSortKey,
}""")
def test_example_sorting_filename(config_app):
    """Test sorting of examples by filename."""
    _check_order(config_app, 'filename')


@pytest.mark.conf_file(content="""
import sphinx_gallery
from sphinx_gallery.sorting import ExampleTitleSortKey
extensions = ['sphinx_gallery.gen_gallery']
sphinx_gallery_conf = {
    'examples_dirs': 'src',
    'gallery_dirs': 'ex',
    'within_subsection_order': ExampleTitleSortKey,
}""")
def test_example_sorting_title(config_app):
    """Test sorting of examples by title."""
    _check_order(config_app, 'title')


def test_collect_gallery_files(config_app, tmpdir):
    """Test that example files are collected properly."""
    rel_filepaths = ['examples/file1.py',
                     'examples/test.rst',
                     'examples/README.txt',
                     'examples/folder1/file1.py',
                     'examples/folder1/file2.py',
                     'examples/folder2/file1.py',
                     'tutorials/folder1/subfolder/file1.py',
                     'tutorials/folder2/subfolder/subsubfolder/file1.py']

    abs_paths = [tmpdir.join(rp) for rp in rel_filepaths]
    for ap in abs_paths:
        ap.ensure()

    examples_path = tmpdir.join('examples')
    dirs = [examples_path.strpath]
    collected_files = set(collect_gallery_files(dirs))
    expected_files = set(
        [ap.strpath for ap in abs_paths
         if re.search(r'examples.*\.py$', ap.strpath)])

    assert collected_files == expected_files

    tutorials_path = tmpdir.join('tutorials')
    dirs = [examples_path.strpath, tutorials_path.strpath]
    collected_files = set(collect_gallery_files(dirs))
    expected_files = set(
        [ap.strpath for ap in abs_paths if re.search(r'.*\.py$', ap.strpath)])

    assert collected_files == expected_files
