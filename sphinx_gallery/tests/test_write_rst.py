# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
r"""
Testing the rst notebook parser
"""
import sphinx_gallery.write_rst as sg

from nose.tools import assert_equal, assert_false, assert_true


def test_codestr2rst():
    """Test the correct translation of a code block into rst"""
    output = sg.codestr2rst('print("hello world")')
    reference = """
.. code-block:: python

    print("hello world")"""
    assert_equal(reference, output)


def test_figuresrt():
    """Testing rst of images"""
    figure_list = ['sphx_glr_plot_1.png']
    image_rst = sg.figure_rst(figure_list)
    single_image = """
.. image:: /sphx_glr_plot_1.png
    :align: center
"""
    assert_equal(image_rst, single_image)

    image_rst = sg.figure_rst(figure_list + ['second.png'])

    image_list_rst = """
.. rst-class:: sphx-glr-horizontal


    *

      .. image:: /sphx_glr_plot_1.png
            :scale: 47

    *

      .. image:: /second.png
            :scale: 47
"""
    assert_equal(image_rst, image_list_rst)
