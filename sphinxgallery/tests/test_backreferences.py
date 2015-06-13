# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Testing the rst files generator
"""
from __future__ import division, absolute_import, print_function
import sphinxgallery.backreferences as sg
from nose.tools import assert_equals


def test_thumbnail_div():
    """Test if the thumbnail div generates the correct string"""

    html_div = sg._thumbnail_div('fake_dir', 'test_file.py', 'test formating')

    reference = """
.. raw:: html

    <div class="sphx-glr-thumbContainer" tooltip="test formating">

.. figure:: /fake_dir/images/thumb/sphx_glr_test_file_thumb.png

    :ref:`example_fake_dir_test_file.py`

.. raw:: html

    </div>
"""

    assert_equals(html_div, reference)
