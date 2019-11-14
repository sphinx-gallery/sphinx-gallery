# -*- coding: utf-8 -*-
"""
Introductory example - Plotting sin
===================================

This is a general example demonstrating a Matplotlib plot output, embedded
rST, the use of math notation and cross-linking to other examples. It would be
useful to compare the :download:`source Python file <plot_1_sin.py>` with the
output below.

Example files should start with a header docstring. Anything before the
docstring is ignored by Sphinx-Gallery and will not appear in the rendered
output, nor will it be executed. This docstring requires an rST header, used
at the title of the example and to correctly build reference links.

Once you close the docstring you will be writing Python code. This code gets
executed by Sphinx-Gallery and any output, including plots will be captured.
You can also alternate between code blocks and text blocks that provide
explanations about the code.

To include displayed math notation, use the directive ``.. math::`` and to
include inline math notation use ``:math:``. For example, we wish to plot the
following function:

.. math::

    x \\rightarrow \\sin(x)

Here the function :math:`\\sin` is evaluated at each point the variable
:math:`x` is defined. When writting latex in a Python string, ensure that you
escape the backslashes or use a raw docstring. You do not need to do
this in text blocks (see below).
"""

# Code source: Óscar Nájera
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('$x$')
plt.ylabel('$\sin(x)$')
# To avoid matplotlib text output
plt.show()

#%%
# To include embedded rST, use a line of ``#`` symbols that spans >= 20 columns
# or ``#%%`` between your rST and your code (see :ref:`embedding_rst`). This
# separates your example into distinct text and code blocks. You can continue
# writing code below the rST:

print('this example shows a sin plot')

#%%
# Latex syntax in the text blocks does not require backslashes to be escaped:
#
# .. math::
#    \sin
#
# Cross referencing
# ^^^^^^^^^^^^^^^^^
#
# You can refer to an example from any part of the documentation,
# including from other examples. Sphinx-Gallery automatically creates reference
# labels for each example. The label consists of the ``.py`` file name,
# prefixed with ``sphx_glr_`` and the name of the
# folder(s) the example is in. In this case, the example is in
# ``auto_examples``, the ``gallery_dirs`` (see
# :ref:`configure_and_use_sphinx_gallery`), then the subdirectory ``no_output``
# (since the example is within a sub-gallery). The file name of the example is
# ``plot_syntaxerror.py``. We can thus cross-link to the example 'SyntaxError'
# using:
# ``:ref:`sphx_glr_auto_examples_no_output_plot_syntaxerror.py\```.
#
# .. seealso::
#     :ref:`sphx_glr_auto_examples_no_output_plot_syntaxerror.py` for a
#     an example with an error.
