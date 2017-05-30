# -*- coding: utf-8 -*-
"""
Backwards-compatility shims for Sphinx
======================================

"""
from __future__ import division, absolute_import, print_function

from distutils.version import LooseVersion

import sphinx
import sphinx.util


# This gets set when the extension is initialized.
_app = None


def _app_status_iterator(iterable, summary, **kwargs):
    global _app

    color = kwargs.pop('color', None)
    if color is not None:
        kwargs['colorfunc'] = getattr(sphinx.util.console, color)

    for item in _app.status_iterator(iterable, summary, **kwargs):
        yield item


if LooseVersion(sphinx.__version__) >= '1.6':
    status_iterator = sphinx.util.status_iterator
else:
    status_iterator = _app_status_iterator
