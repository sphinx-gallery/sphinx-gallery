# -*- coding: utf-8 -*-
"""
Plotting simple sin function
============================

This example consisting of a plot of a sin function, demonstrates the autonomy
of the gallery and show how to link to other examples.

To illustrate how to insert maths in example descriptions,
it corresponds mathematically to the function:

.. math::

    x \\rightarrow \\sin(x)

Here the function :math:`\\sin` is evaluated at each point the variable
:math:`x` is defined.

Note that ``sphinx-gallery`` automatically creates labels for each example
using its filename. You can refer to an example from any part of the
documentation, including from other examples. Below, we refer to
'Plotting simple sin function on a black background'
(``plot_sin_black_background.py``) by prefixing the file
name of the example with ``sphx_glr_`` and the ``gallery_dirs`` (see
:ref:`configure_and_use_sphinx_gallery`). In this case the ``gallery_dirs`` is
``auto_examples/sin_func`` so the full label is:
``sphx_glr_auto_examples_sin_func_plot_sin_black_background.py``.

.. seealso::
    :ref:`sphx_glr_auto_examples_sin_func_plot_sin_black_background.py` for a
    fancier plot
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
