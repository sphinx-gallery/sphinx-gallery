# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Testing the rst files generator
"""
from __future__ import division, absolute_import, print_function
from sphinxgallery import Path
import sphinxgallery.docs_resolv as sg
import tempfile
import sys
from nose.tools import assert_equals


def test_shelve():
    """Test if shelve can be caches information
    retrieved after file is deleted"""
    test_string = 'test information'
    tmp_cache = Path(tempfile.mkdtemp())
    with tempfile.NamedTemporaryFile('w') as fid:
        fid.write(test_string)
        fid.seek(0)

        # recovers data from temporary file and caches it in the shelve
        # use Path class in name to test bug, shelve only accepts str as key
        file_data = sg.get_data(Path(fid.name), tmp_cache)

        # tests recovered data matches
        assert_equals(file_data, test_string)

    # test if cached data is available after temporary file has vanished
    assert_equals(sg.get_data(fid.name, tmp_cache), test_string)

    # shelve keys need to be str in python 2, deal with unicode input
    if sys.version_info[0] == 2:
        unicode_name = unicode(fid.name)
        assert_equals(sg.get_data(unicode_name, tmp_cache), test_string)
