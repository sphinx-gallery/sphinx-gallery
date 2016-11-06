# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
r"""
Testing the Jupyter notebook parser
"""

from __future__ import division, absolute_import, print_function
import json
import tempfile
from nose.tools import assert_equal
import sphinx_gallery.gen_rst as sg
from sphinx_gallery.notebook import rst2md, jupyter_notebook, save_notebook


def test_latex_conversion():
    """Latex parsing from rst into Jupyter Markdown"""
    double_inline_rst = r":math:`T<0` and :math:`U>0`"
    double_inline_jmd = r"$T<0$ and $U>0$"
    assert_equal(double_inline_jmd, rst2md(double_inline_rst))

    align_eq = r"""
.. math::
   \mathcal{H} &= 0 \\
   \mathcal{G} &= D"""

    align_eq_jmd = r"""
\begin{align}\mathcal{H} &= 0 \\
   \mathcal{G} &= D\end{align}"""
    assert_equal(align_eq_jmd, rst2md(align_eq))


def test_convert():
    """Test ReST conversion"""
    rst = """hello

.. contents::
    :local:

This is :math:`some` math :math:`stuff`.

.. note::
    Interpolation is a linear operation that can be performed also on
    Raw and Epochs objects.

.. warning::
    Go away

For more details on interpolation see the page :ref:`channel_interpolation`.
.. _foo: bar

.. image:: foobar
  :alt: me
  :whatever: you
"""

    markdown = """hello

This is $some$ math $stuff$.

<div class="alert alert-info"><h4>Note</h4><p>Interpolation is a linear operation that can be performed also on
    Raw and Epochs objects.</p></div>

<div class="alert alert-danger"><h4>Warning</h4><p>Go away</p></div>

For more details on interpolation see the page `channel_interpolation`.

![me](foobar)
"""  # noqa
    assert_equal(rst2md(rst), markdown)


def test_jupyter_notebook():
    """Test that written ipython notebook file corresponds to python object"""
    blocks = sg.split_code_and_text_blocks('tutorials/plot_parse.py')
    example_nb = jupyter_notebook(blocks)

    with tempfile.NamedTemporaryFile('w') as nb_file:
        save_notebook(example_nb, nb_file.name)
        with open(nb_file.name, "r") as fname:
            assert_equal(json.load(fname), example_nb)
