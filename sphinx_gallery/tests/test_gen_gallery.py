# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
r"""
Test Sphinx-Gallery
"""

from __future__ import division, absolute_import, print_function
import sys
import shutil
import os
from collections import namedtuple
import tempfile
import pytest
from six import StringIO, string_types

from docutils import nodes

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx_gallery import gen_gallery

_fixturedir = os.path.join(os.path.dirname(__file__), 'testconfs')

from sphinx.builders.latex import LaTeXBuilder
from sphinx.theming import Theme
from sphinx.ext.autodoc import AutoDirective
from sphinx.pycode import ModuleAnalyzer

from sphinx_gallery import gen_gallery


@pytest.fixture
def tmpdir():
    tempdir = tempfile.mkdtemp()
    print('test tempdir in:', tempdir)
    return tempdir


def test_app(tmpdir):
    app = Sphinx(_fixturedir, _fixturedir, tmpdir, tmpdir, "html")
