# -*- coding: utf-8 -*-
# Author: Chris Holdgraf
# License: 3-clause BSD
"""
Testing the binder badge functionality
"""
from __future__ import division, absolute_import, print_function
import os
import tempfile
import sys
from copy import deepcopy

import pytest

from sphinx_gallery.binder import (gen_binder_rst, gen_binder_url,
                                   check_binder_conf)
from sphinx_gallery.utils import _TempDir


def test_binder():
    """Testing binder URL generation and checks."""
    file_path = 'myfile.py'
    conf1 = {'url': 'http://test1.com', 'org': 'org',
             'repo': 'repo', 'branch': 'branch',
             'dependencies': '../requirements.txt'}
    url = gen_binder_url(file_path, conf1)
    assert url == 'http://test1.com/v2/gh/org/repo/branch?filepath=_downloads/myfile.ipynb'

    # Assert filepath prefix is added
    prefix = 'my_prefix/foo'
    conf1['filepath_prefix'] = prefix
    url = gen_binder_url(file_path, conf1)
    assert url == 'http://test1.com/v2/gh/org/repo/branch?filepath={}/_downloads/myfile.ipynb'.format(prefix)
    conf1.pop('filepath_prefix')

    # URL must have http
    with pytest.raises(ValueError) as excinfo:
        conf2 = deepcopy(conf1)
        conf2['url'] = 'test1.com'
        url = check_binder_conf(conf2)

    excinfo.match(r'did not supply a valid url')

    # Assert missing params
    for key in conf1.keys():
        conf3 = deepcopy(conf1)
        conf3.pop(key)
        with pytest.raises(ValueError) as excinfo:
            url = check_binder_conf(conf3)
        excinfo.match(r"binder_conf is missing values for")

    # Dependencies file
    dependency_file_tests = ['requirements_not.txt', 'doc-requirements.txt']
    for ifile in dependency_file_tests:
        with pytest.raises(ValueError) as excinfo:
            conf3 = deepcopy(conf1)
            conf3['dependencies'] = ifile
            url = check_binder_conf(conf3)
        excinfo.match(r"Did not find one of `requirements.txt` or `environment.yml`")

    with pytest.raises(ValueError) as excinfo:
        conf6 = deepcopy(conf1)
        conf6['dependencies'] = {'test': 'test'}
        url = check_binder_conf(conf6)
    excinfo.match(r"`dependencies` value should be a list of strings")

    # Check returns the correct object
    conf4 = check_binder_conf({})
    conf5 = check_binder_conf(None)
    for iconf in [conf4, conf5]:
        assert iconf == {}

    # Assert extra unkonwn params
    with pytest.raises(ValueError) as excinfo:
        conf7 = deepcopy(conf1)
        conf7['foo'] = 'blah'
        url = check_binder_conf(conf7)
    excinfo.match(r"Unknown Binder config key")
