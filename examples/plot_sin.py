# -*- coding: utf-8 -*-
"""
===========================
Ploting simple sin function
===========================

A simple example of the plot of a sin function
in order to test the autonomy of the gallery
"""

# Code source: Óscar Nájera
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x,y)
plt.xlabel('$x$')
plt.ylabel('$\sin(x)$')
plt.show()
