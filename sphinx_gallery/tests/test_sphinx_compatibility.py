# -*- coding: utf-8 -*-
"""
Testing the Sphinx compatibility shims
"""
from __future__ import division, absolute_import, print_function

import sphinx.util.console

from sphinx_gallery import sphinx_compatibility


def test_status_iterator(fakesphinxapp):
    for _ in sphinx_compatibility._app_status_iterator([1, 2, 3],
                                                       'summary',
                                                       length=3):
        pass

    assert len(fakesphinxapp.calls['status_iterator']) == 1
    call = fakesphinxapp.calls['status_iterator'][0]
    assert call.args == ([1, 2, 3], 'summary')
    assert 'color' not in call.kwargs
    assert 'colorfunc' not in call.kwargs
    assert call.kwargs['length'] == 3


def test_status_iterator_color(fakesphinxapp):
    for _ in sphinx_compatibility._app_status_iterator([1, 2, 3],
                                                       'summary',
                                                       color='green',
                                                       length=3):
        pass

    assert len(fakesphinxapp.calls['status_iterator']) == 1
    call = fakesphinxapp.calls['status_iterator'][0]
    assert call.args == ([1, 2, 3], 'summary')
    assert 'color' not in call.kwargs
    assert call.kwargs['colorfunc'] == sphinx.util.console.green
    assert call.kwargs['length'] == 3
