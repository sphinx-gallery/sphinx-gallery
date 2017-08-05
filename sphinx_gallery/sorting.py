# -*- coding: utf-8 -*-
r"""
Sorters for Sphinx-Gallery subsections
======================================

Sorting key functions for gallery subsection folders
"""
# Created: Sun May 21 20:38:59 2017
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import division, absolute_import, print_function
import os
import types

from .py_source_parser import split_code_and_text_blocks


class ExplicitOrder(object):
    """Sorting key for all galleries subsections

    This requires all folders to be listed otherwise an exception is raised

    Parameters
    ----------
    ordered_list : list, tuple, types.GeneratorType
        Hold the paths of each galleries' subsections

    Raises
    ------
    ValueError
        Wrong input type or Subgallery path missing
    """

    def __init__(self, ordered_list):
        if not isinstance(ordered_list, (list, tuple, types.GeneratorType)):
            raise ValueError("ExplicitOrder sorting key takes a list, "
                             "tuple or Generator, which hold"
                             "the paths of each gallery subfolder")

        self.ordered_list = list(os.path.normpath(path)
                                 for path in ordered_list)

    def __call__(self, item):
        if item in self.ordered_list:
            return self.ordered_list.index(item)
        else:
            raise ValueError('If you use an explicit folder ordering, you '
                             'must specify all folders. Explicit order not '
                             'found for {}'.format(item))


def amount_of_code(src_dir):
    """Sort examples in src_dir by amount of code """
    def sort_files(filename):
        src_file = os.path.normpath(os.path.join(src_dir, filename))
        file_conf, script_blocks = split_code_and_text_blocks(src_file)
        amount_of_code = sum([len(bcontent)
                              for blabel, bcontent, lineno in script_blocks
                              if blabel == 'code'])
        return amount_of_code
    return sort_files


def file_size(src_dir):
    """Sort examples in src_dir by file size"""
    def sort_files(filename):
        src_file = os.path.normpath(os.path.join(src_dir, filename))
        return os.stat(src_file).st_size
    return sort_files
