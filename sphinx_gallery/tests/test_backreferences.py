# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Testing the rst files generator
"""
from __future__ import division, absolute_import, print_function
import os
import sphinx_gallery.backreferences as sg
from nose.tools import assert_equal


def test_thumbnail_div():
    """Test if the thumbnail div generates the correct string"""

    html_div = sg._thumbnail_div('fake_dir', 'test_file.py', 'test formating')

    reference = r"""
.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="test formating">

.. only:: html

    .. figure:: /fake_dir{0}images{0}thumb{0}sphx_glr_test_file_thumb.png

        :ref:`sphx_glr_fake_dir_test_file.py`

.. raw:: html

    </div>
""".format(os.sep)

    assert_equal(html_div, reference)


def test_backref_thumbnail_div():
    """Test if the thumbnail div generates the correct string"""

    html_div = sg._thumbnail_div('fake_dir', 'test_file.py', 'test formating',
                                 is_backref=True)

    reference = """
.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="test formating">

.. only:: html

    .. figure:: /fake_dir{0}images{0}thumb{0}sphx_glr_test_file_thumb.png

        :ref:`sphx_glr_fake_dir_test_file.py`

.. raw:: html

    </div>

.. only:: not html

    * :ref:`sphx_glr_fake_dir_test_file.py`
""".format(os.sep)

    assert_equal(html_div, reference)
