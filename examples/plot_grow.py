# -*- coding: utf-8 -*-
"""
===================================
Ploting simple exponential function
===================================

A simple example of the plot of a exponential function
in order to test the autonomy of the gallery
"""

# Code source: Óscar Nájera
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 2, 100)
y = np.exp(x)

plt.plot(x,y)
plt.xlabel('$x$')
plt.ylabel('$exp(x)$')
plt.show()
