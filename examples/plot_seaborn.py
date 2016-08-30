# -*- coding: utf-8 -*-
r"""
Using Seaborn
=============

A example from their website

"""
# Author: Michael Waskom
# License: BSD 3 clause

from __future__ import division, absolute_import, print_function

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white")

df = sns.load_dataset("iris")

g = sns.PairGrid(df, diag_sharey=False)
g.map_lower(sns.kdeplot, cmap="Blues_d")
g.map_upper(plt.scatter)
g.map_diag(sns.kdeplot, lw=3)
