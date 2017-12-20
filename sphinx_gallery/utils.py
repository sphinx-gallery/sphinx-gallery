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


def replace_py_ipynb(fname):
    """Replace .py extension in filename by .ipynb"""
    fname_prefix, extension = fname.rsplit('.', 1)
    if extension != 'py':
        raise ValueError(
            "Unrecognized file extension, expected '.py', got {!r}".format(
                fname))

    new_extension = 'ipynb'
    return '{}.{}'.format(fname_prefix, new_extension)
