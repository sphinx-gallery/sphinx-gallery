# -*- coding: utf-8 -*-
"""
Utilities
=========

Miscellaneous utilities.
"""
# Author: Eric Larson
# License: 3-clause BSD

from __future__ import division, absolute_import, print_function

import tempfile
from shutil import rmtree
import pytest


class _TempDir(str):
    """Create and auto-destroy temp dir.

    This is designed to be used with testing modules. Instances should be
    defined inside test functions. Instances defined at module level can not
    guarantee proper destruction of the temporary directory.

    When used at module level, the current use of the __del__() method for
    cleanup can fail because the rmtree function may be cleaned up before this
    object (an alternative could be using the atexit module instead).
    """
    # adapted from MNE-Python

    def __new__(self):  # noqa: D105
        new = str.__new__(self, tempfile.mkdtemp(prefix='tmp_sg_tempdir_'))
        return new

    def __init__(self):  # noqa: D102
        self._path = self.__str__()

    def __del__(self):  # noqa: D105
        rmtree(self._path, ignore_errors=True)


@pytest.fixture
def unicode_sample(tmpdir):
    """Return temporary python source file with Unicode in various places"""
    code_str = b"""# -*- coding: utf-8 -*-
'''
\xc3\x9anicode in header
=================

U\xc3\xb1icode in description
'''

# Code source: \xc3\x93scar N\xc3\xa1jera
# License: BSD 3 clause

import os
path = os.path.join('a','b')

a = 'hei\xc3\x9f'  # Unicode string

import sphinx_gallery.back_references as br
br.identify_names

from sphinx_gallery.back_references import identify_names
identify_names

"""

    fname = tmpdir.join("unicode_sample.py")
    fname.write(code_str, 'wb')
    return fname
