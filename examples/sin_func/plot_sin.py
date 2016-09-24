# -*- coding: utf-8 -*-
"""
Plotting simple sin function
============================

A simple example of the plot of a sin function
in order to test the autonomy of the gallery.

To illustrate how to insert maths in example descriptions,
it corresponds mathematically to the function:

.. math::

    x \\rightarrow \\sin(x)

Here the function :math:`\\sin` is evaluated at each point the variable
:math:`x` is defined.

Note that ``sphinx-gallery`` automatically creates labels for each example from
its filename. You can thus refer to it from any part of the documentation,
including from other examples, as here

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
plt.show()
