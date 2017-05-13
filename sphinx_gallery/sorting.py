# -*- coding: utf-8 -*-
r"""
Sorters for Sphinx Galleries
============================

Classes to define how objects are sorted within galleries.
"""

import os.path as op


class ExplicitOrderKey(object):
    """Explicitly order a list of strings."""
    def __init__(self, ordered_list):
        if not isinstance(ordered_list, list):
            raise ValueError('ordered_list must be a list')
        self.ordered_list = ordered_list

    def __call__(self, item):
        if item in self.ordered_list:
            # Return that item's explicit position as a string
            # add 000 so it's at the front in case we have numbered folders
            return '000' + str(self.ordered_list.index(item))
        elif not op.exists(op.join(item, 'README.txt')):
            # We're skipping this folder anyway
            return item
        else:
            raise ValueError('If you use an explicit folder ordering, you '
                             'must specify all folders. Explicit order not '
                             'found for {}'.format(item))
