# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Testing the rst files generator
"""
from __future__ import division, absolute_import, print_function
import sphinx_gallery.docs_resolv as sg
import os
import tempfile
import sys
from nose.tools import assert_equal


def test_shelve():
    """Test if shelve can be caches information
    retrieved after file is deleted"""
    test_string = 'test information'
    tmp_cache = tempfile.mkdtemp()
    # Don't use context manager for NamedTemporaryFile here:
    # "Whether the name can be used to open the file a second time, while the
    # named temporary file is still open, varies across platforms (it can be
    # so used on Unix; it cannot on Windows NT or later)
    with tempfile.NamedTemporaryFile('w', delete=False) as fid:
        fid.write(test_string)

    try:
        # recovers data from temporary file and caches it in the shelve
        file_data = sg.get_data(fid.name, tmp_cache)
        # tests recovered data matches
        assert_equal(file_data, test_string)
    finally:
        os.remove(fid.name)

    # test if cached data is available after temporary file has vanished
    assert_equal(sg.get_data(fid.name, tmp_cache), test_string)

    # shelve keys need to be str in python 2, deal with unicode input
    if sys.version_info[0] == 2:
        unicode_name = unicode(fid.name)
        assert_equal(sg.get_data(unicode_name, tmp_cache), test_string)
