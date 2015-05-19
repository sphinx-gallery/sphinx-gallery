# -*- coding: utf-8 -*-
"""
=======================================
Únîcödè support in documentation string
=======================================

In this example we include Unicode characters that are so required this days.✓
"""

# Code source: Óscar Nájera
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt


N = 50
x = np.linspace(-1, 2, 50)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2
for i in range(5):
    plt.scatter(x, -np.cos(i*x), s=area, c=colors, alpha=0.5)
plt.show()
