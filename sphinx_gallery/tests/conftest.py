# -*- coding: utf-8 -*-
"""
Pytest fixtures
"""
from __future__ import division, absolute_import, print_function

import collections

import pytest

import sphinx_gallery.sphinx_compatibility


Params = collections.namedtuple('Params', 'args kwargs')


class FakeSphinxApp:
    def __init__(self):
        self.calls = collections.defaultdict(list)

    def status_iterator(self, *args, **kwargs):
        self.calls['status_iterator'].append(Params(args, kwargs))
        yield


@pytest.fixture
def fakesphinxapp():
    orig_app = sphinx_gallery.sphinx_compatibility._app
    sphinx_gallery.sphinx_compatibility._app = app = FakeSphinxApp()
    try:
        yield app
    finally:
        sphinx_gallery.sphinx_compatibility._app = orig_app
