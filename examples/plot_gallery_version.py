# -*- coding: utf-8 -*-
"""
===========================
Sphinx-Gallery introduction
===========================

A cartoon like plot to present Sphinx-Gallery using itself to display its
version.
"""

# Code source: Óscar Nájera
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt
import sphinxgallery

np.random.seed(32)
def layers(n, m):
    """
    Return *n* random Gaussian mixtures, each of length *m*.
    """
    def bump(a):
        x = 1 / (.1 + np.random.random())
        y = 2 * np.random.random() - .3
        z = 13 / (.1 + np.random.random())
        for i in range(m):
            w = (i / float(m) - y) * z
            a[i] += x * np.exp(-w * w)
    a = np.zeros((m, n))
    for i in range(n):
        for j in range(12):
            bump(a[:, i])
    return np.abs(a)

try:
    plt.xkcd()
except:
    pass
finally:
    fig = plt.figure()
    plt.xticks([])
    plt.yticks([])

    plt.annotate(
        'Introducing Sphinx-Gallery ' + sphinxgallery.__version__,
        xy=(12, 4), arrowprops=dict(arrowstyle='->'), xytext=(15, -4))

    d = layers(3, 100)
    plt.stackplot(range(100), d.T, baseline='wiggle')

plt.show()