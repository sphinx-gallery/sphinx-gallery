# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
r"""
Test Sphinx-Gallery
"""

from __future__ import division, absolute_import, print_function

import os
import tempfile


import pytest
from sphinx.application import Sphinx
from sphinx.errors import ExtensionError

from sphinx_gallery.gen_rst import MixedEncodingStringIO

_fixturedir = os.path.join(os.path.dirname(__file__), 'testconfs')


@pytest.fixture
def tmpdir():
    tempdir = tempfile.mkdtemp()
    print('test tempdir in:', tempdir)
    return tempdir


def test_config(tmpdir):
    """Testing warning messages on configuration correctly shown"""

    app = Sphinx(_fixturedir, _fixturedir, tmpdir,
                 tmpdir, "html", warning=MixedEncodingStringIO())
    cfg = app.config
    assert cfg.project == "Sphinx-Gallery <Tests>"
    assert cfg.sphinx_gallery_conf['backreferences_dir'] == os.path.join(
        'modules', 'generated')
    build_warn = app._warning.getvalue()

    assert "Gallery now requires" in build_warn
    assert "'backreferences_dir': False" in build_warn
    assert "DeprecationWarning:" in build_warn
    assert "mod_example_dir" not in build_warn

    # no duplicate values allowed
    with pytest.raises(ExtensionError) as excinfo:
        app.add_config_value('sphinx_gallery_conf', 'x', True)
    assert 'already present' in str(excinfo.value)
