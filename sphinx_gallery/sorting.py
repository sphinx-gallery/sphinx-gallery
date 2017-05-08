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


class ExplicitOrderStrict(object):
    def __init__(self, ordered_list):
        if not isinstance(ordered_list, list):
            raise ValueError("Requires a list")

        self.ordered_list = ordered_list

    def __call__(self, item):
        if item in self.ordered_list:
            return self.ordered_list.index(item)
        elif not os.path.exists(os.path.join(item, 'README.txt')):
            # Some folders are not a gallery subsection and are thus
            # Skipped anyway.
            return -1
        else:
            raise ValueError('If you use an explicit folder ordering, you '
                             'must specify all folders. Explicit order not '
                             'found for {}'.format(item))
