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
from types import GeneratorType


class ExplicitOrderStrict(list):
    def __init__(self, ordered_list):
        if not isinstance(ordered_list, (list, tuple, set, GeneratorType)):
            raise ValueError("ExplicitOrderStrict sorting key takes a list "
                             "tuple, set or Generator of strings, which hold"
                             "the path of all gallery subfolders")

        list.__init__(self, ordered_list)

    def __call__(self, item):
        if item in self:
            return self.index(item)
        else:
            raise ValueError('If you use an explicit folder ordering, you '
                             'must specify all folders. Explicit order not '
                             'found for {}'.format(item))
