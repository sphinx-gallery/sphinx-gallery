# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Testing the rst files generator
"""
from __future__ import division, absolute_import, print_function
import sphinxgallery.docs_resolv as sg
import tempfile
import sys
from nose.tools import assert_equals


def test_shelve():
    """Test if shelve can be caches information
    retrieved after file is deleted"""
    test_string = 'test information'
    shelve_file = 'shelve_test_file'
    with tempfile.NamedTemporaryFile('w') as fid:
        fid.write(test_string)
        fid.seek(0)

        # recovers data from temporary file and caches it in the shelve
        file_data = sg.get_data(fid.name, shelve_file)
        # tests recovered data matches
        assert_equals(file_data, test_string)

    # test if cached data is available after temporary file has vanished
    assert_equals(sg.get_data(fid.name, shelve_file), test_string)

    # shelve keys need to be str in python 2, deal with unicode input
    if sys.version_info.major == 2:
        unicode_name = unicode(fid.name)
        assert_equals(sg.get_data(unicode_name, shelve_file), test_string)
