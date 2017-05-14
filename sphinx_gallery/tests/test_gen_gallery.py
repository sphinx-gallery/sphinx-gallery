# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
r"""
Test Sphinx-Gallery
"""

from __future__ import division, absolute_import, print_function

import os
import tempfile
import shutil
import pytest
from sphinx.application import Sphinx
from sphinx.errors import ExtensionError
from sphinx_gallery.gen_rst import MixedEncodingStringIO
from sphinx_gallery.gen_gallery import DEFAULT_GALLERY_CONF


@pytest.fixture
def tmpdir():
    tempdir = tempfile.mkdtemp()
    print('test tempdir in:', tempdir)
    return tempdir


def test_default_config(tmpdir):
    """Test the default Sphinx-Gallery configuration is loaded

    if only the extension is added to Sphinx"""

    _fixturedir = os.path.join(os.path.dirname(__file__), 'testconfs')
    srcdir = os.path.join(tmpdir, "config_test")

    shutil.copytree(_fixturedir, srcdir)
    with open(os.path.join(srcdir, "conf.py"), "w") as conffile:
        conffile.write("""
import os
import sphinx_gallery
extensions = ['sphinx_gallery.gen_gallery']
# General information about the project.
project = u'Sphinx-Gallery <Tests>'""")

    app = Sphinx(srcdir, srcdir, os.path.join(srcdir, "_build"),
                 os.path.join(srcdir, "_build", "toctree"),
                 "html", warning=MixedEncodingStringIO())

    cfg = app.config
    assert cfg.project == "Sphinx-Gallery <Tests>"
    # no duplicate values allowed The config is present already
    with pytest.raises(ExtensionError) as excinfo:
        app.add_config_value('sphinx_gallery_conf', 'x', True)
    assert 'already present' in str(excinfo.value)

    assert cfg.sphinx_gallery_conf == DEFAULT_GALLERY_CONF


def test_config_old_backreferences_conf(tmpdir):
    """Testing Deprecation warning message against old backreference config

    In this case the user is required to update the mod_example_dir config
    variable Sphinx-Gallery should notify the user and also silently update
    the old config to the new one. """

    _fixturedir = os.path.join(os.path.dirname(__file__), 'testconfs')
    srcdir = os.path.join(tmpdir, "config_test")

    shutil.copytree(_fixturedir, srcdir)
    with open(os.path.join(srcdir, "conf.py"), "w") as conffile:
        conffile.write("""
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
    app = Sphinx(srcdir, srcdir, os.path.join(srcdir, "_build"),
                 os.path.join(srcdir, "_build", "toctree"),
                 "html", warning=MixedEncodingStringIO())
    cfg = app.config
    assert cfg.project == "Sphinx-Gallery <Tests>"
    assert cfg.sphinx_gallery_conf['backreferences_dir'] == os.path.join(
        'modules', 'gen')
    build_warn = app._warning.getvalue()

    assert "DeprecationWarning:" in build_warn
    assert "Old configuration" in build_warn
    assert "mod_example_dir" in build_warn
    assert "Gallery now requires" in build_warn
    assert "For a quick fix" in build_warn
    assert "'backreferences_dir': False" not in build_warn


def test_config_unset_backreferences(tmpdir):
    """Testing Deprecation warning message against unset backreference config

    In this case the user is notified to update the set the
    backreferences_dir config variable if such feature is to be enabled or
    otherwise to deactivate the feature. Sphinx-Gallery should notify the
    user and also silently setup the old default config value into the new
    config style. """

    _fixturedir = os.path.join(os.path.dirname(__file__), 'testconfs')
    srcdir = os.path.join(tmpdir, "config_test")

    shutil.copytree(_fixturedir, srcdir)
    with open(os.path.join(srcdir, "conf.py"), "w") as conffile:
        conffile.write("""
import sphinx_gallery
extensions = ['sphinx_gallery.gen_gallery']
# General information about the project.
project = u'Sphinx-Gallery <Tests>'

sphinx_gallery_conf = {
    'examples_dirs': 'src',
    'gallery_dirs': 'ex',
}""")
    app = Sphinx(srcdir, srcdir, os.path.join(srcdir, "_build"),
                 os.path.join(srcdir, "_build", "toctree"),
                 "html", warning=MixedEncodingStringIO())
    cfg = app.config
    assert cfg.project == "Sphinx-Gallery <Tests>"
    assert cfg.sphinx_gallery_conf['backreferences_dir'] == os.path.join(
        'modules', 'generated')
    build_warn = app._warning.getvalue()

    assert "Gallery now requires" in build_warn
    assert "'backreferences_dir': False" in build_warn
    assert "DeprecationWarning:" in build_warn
    assert "mod_example_dir" not in build_warn


def test_config_backreferences(tmpdir):
    """Test no warning is issued under the new configuration"""

    _fixturedir = os.path.join(os.path.dirname(__file__), 'testconfs')
    srcdir = os.path.join(tmpdir, "config_test")

    shutil.copytree(_fixturedir, srcdir)
    with open(os.path.join(srcdir, "conf.py"), "w") as conffile:
        conffile.write("""
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

    app = Sphinx(srcdir, srcdir, os.path.join(srcdir, "_build"),
                 os.path.join(srcdir, "_build", "toctree"),
                 "html", warning=MixedEncodingStringIO())

    cfg = app.config
    assert cfg.project == "Sphinx-Gallery <Tests>"
    assert cfg.sphinx_gallery_conf['backreferences_dir'] == os.path.join(
        'gen_modules', 'backreferences')
    build_warn = app._warning.getvalue()
    assert build_warn == ""
