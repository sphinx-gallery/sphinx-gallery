# -*- coding: utf-8 -*-
"""
Using Unicode everywhere 🤗
===========================

This example demonstrates how to include non-ASCII characters, mostly emoji 🎉
to stress test the build and test environments that parse the example files.
"""
from __future__ import unicode_literals

# 🎉 👍
# Code source: Óscar Nájera
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 20
plt.rcParams["font.monospace"] = ["DejaVu Sans Mono"]
plt.rcParams["font.family"] = "monospace"

plt.figure()
x = np.random.randn(100) * 2 + 1
y = np.random.randn(100) * 6 + 3
s = np.random.rand(*x.shape) * 800 + 500
plt.scatter(x, y, s, marker=r'$\oint$')
x = np.random.randn(60) * 7 - 4
y = np.random.randn(60) * 3 - 2
s = s[:x.size]
plt.scatter(x, y, s, alpha=0.5, c='g', marker=r'$\clubsuit$')
plt.xlabel('⇒')
plt.ylabel('⇒')
plt.title('♲' * 10)
print('Std out capture 😎')
# To avoid matplotlib text output
plt.show()

# %%
# Debug fonts
print(plt.rcParams)
