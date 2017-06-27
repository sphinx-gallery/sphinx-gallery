# -*- coding: utf-8 -*-
r"""
Sorters for Sphinx Galleries
============================

Classes to define how objects are sorted within galleries.
"""

import os


class ExplicitOrderKey(object):
    """Explicitly order a list of strings."""
    def __init__(self, dict_ordered):
        if not isinstance(dict_ordered, dict):
            raise ValueError('dict_ordered must be a dictionary')
        if not all(isinstance(ii, list) for ii in dict_ordered.values()):
            raise ValueError('All values of dict_ordered must be a list.')
        self.dict_ordered = dict_ordered
        self.active_list = None
        self.active_key = None

    def activate_key(self, key):
        if key is None:
            self.active_list = []
            self.active_key = None
        elif key not in self.dict_ordered.keys():
            raise ValueError('key must be one of {}, found {}'.format(
                list(self.dict_ordered.keys()), key))
        else:
            self.active_list = self.dict_ordered[key]
            self.active_key = key

    def __call__(self, item):
        if self.active_key is None:
            return item
        if item in self.active_list:
            # Return that item's explicit position as a string
            # add 000 so it's at the front in case we have numbered folders
            return '000' + str(self.active_list.index(item))
        elif any(item.endswith(ii) for ii in ['.py', '.txt', '.DS_Store']):
            # This will be skipped anyway.
            return item
        else:
            raise ValueError('If you use an explicit folder ordering, you\n'
                             'must specify all folders within a given\n'
                             'examples folder. Explicit order not found for\n'
                             'root: {}, item: {}'.format(self.active_key, item))
