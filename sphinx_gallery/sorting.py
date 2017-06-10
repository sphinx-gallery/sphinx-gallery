# -*- coding: utf-8 -*-
r"""
Sorters for Sphinx-Gallery subsections
======================================

Sorting key functions for subgallery folders
"""
# Created: Sun May 21 20:38:59 2017
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import division, absolute_import, print_function
import os
import types


class ExplicitOrderStrict(list):
    """Sorting key for all galleries sub sections

    Parameters
    ----------
    ordered_list : list, tuple, types.GeneratorType
        Hold the paths of each gallery subfolder"""

    def __init__(self, ordered_list):
        if not isinstance(ordered_list, (list, tuple, types.GeneratorType)):
            raise ValueError("ExplicitOrderStrict sorting key takes a list, "
                             "tuple or Generator, which hold"
                             "the paths of each gallery subfolder")

        list.__init__(self, (os.path.normpath(path) for path in ordered_list))

    def __call__(self, item):
        if item in self:
            return self.index(item)
        else:
            raise ValueError('If you use an explicit folder ordering, you '
                             'must specify all folders. Explicit order not '
                             'found for {}'.format(item))
