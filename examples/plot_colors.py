# -*- coding: utf-8 -*-
r"""
Colormaps alter your perception
===============================

This example demonstrates a matplotlib plot and rST text embedded between
code blocks.

The function

.. math:: f(x, y) = \sin(x) + \cos(y)

is plotted with different colormaps.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 300)
xx, yy = np.meshgrid(x, x)
z = np.cos(xx) + np.cos(yy)

plt.figure()
plt.imshow(z)

plt.figure()
plt.imshow(z, cmap=plt.cm.get_cmap('hot'))

plt.figure()
plt.imshow(z, cmap=plt.cm.get_cmap('Spectral'),
           interpolation='none')

# To avoid matplotlib text output
plt.show()

################################################
# You can define blocks in your source code
# with interleaving prose.
#

print("This writes to stdout and will be",
      " displayed in the HTML file")
