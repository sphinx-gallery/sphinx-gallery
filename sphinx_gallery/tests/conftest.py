# -*- coding: utf-8 -*-
"""
Pytest fixtures
"""
from __future__ import division, absolute_import, print_function

import collections

import pytest

import sphinx
from sphinx_gallery import (docs_resolv, gen_gallery, gen_rst, utils,
                            sphinx_compatibility, py_source_parser)


def pytest_report_header(config, startdir):
    """Add information to the pytest run header."""
    return 'Sphinx:  %s (%s)' % (sphinx.__version__, sphinx.__file__)


Params = collections.namedtuple('Params', 'args kwargs')


class FakeSphinxApp:
    def __init__(self):
        self.calls = collections.defaultdict(list)

    def status_iterator(self, *args, **kwargs):
        self.calls['status_iterator'].append(Params(args, kwargs))
        for it in args[0]:
            yield it

    def warning(self, *args, **kwargs):
        self.calls['warning'].append(Params(args, kwargs))

    def warn(self, *args, **kwargs):
        self.calls['warn'].append(Params(args, kwargs))

    def info(self, *args, **kwargs):
        self.calls['info'].append(Params(args, kwargs))

    def verbose(self, *args, **kwargs):
        self.calls['verbose'].append(Params(args, kwargs))

    def debug(self, *args, **kwargs):
        self.calls['debug'].append(Params(args, kwargs))


@pytest.fixture
def gallery_conf(tmpdir):
    """Set up a test sphinx-gallery configuration."""
    app = utils.Bunch()
    app.config = dict(source_suffix={'.rst': None})
    gallery_conf = gen_gallery._complete_gallery_conf(
        {}, str(tmpdir), True, False, app=app)
    gallery_conf.update(examples_dir=str(tmpdir), gallery_dir=str(tmpdir))
    return gallery_conf


@pytest.fixture
def fakesphinxapp():
    orig_app = sphinx_compatibility._app
    sphinx_compatibility._app = app = FakeSphinxApp()
    try:
        yield app
    finally:
        sphinx_compatibility._app = orig_app


@pytest.fixture
def log_collector():
    orig_dr_logger = docs_resolv.logger
    orig_gg_logger = gen_gallery.logger
    orig_gr_logger = gen_rst.logger
    orig_ps_logger = py_source_parser.logger
    app = FakeSphinxApp()
    docs_resolv.logger = app
    gen_gallery.logger = app
    py_source_parser.logger = app
    gen_rst.logger = app
    try:
        yield app
    finally:
        docs_resolv.logger = orig_dr_logger
        gen_gallery.logger = orig_gg_logger
        gen_rst.logger = orig_gr_logger
        py_source_parser.logger = orig_ps_logger


@pytest.fixture
def unicode_sample(tmpdir):
    """Return temporary python source file with Unicode in various places"""
    code_str = b"""# -*- coding: utf-8 -*-
'''
\xc3\x9anicode in header
=================

U\xc3\xb1icode in description
'''

# Code source: \xc3\x93scar N\xc3\xa1jera
# License: BSD 3 clause

import os
path = os.path.join('a','b')

a = 'hei\xc3\x9f'  # Unicode string

import sphinx_gallery.back_references as br
br.identify_names

from sphinx_gallery.back_references import identify_names
identify_names

"""

    fname = tmpdir.join("unicode_sample.py")
    fname.write(code_str, 'wb')
    return fname.strpath
