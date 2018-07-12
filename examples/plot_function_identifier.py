# -*- coding: utf-8 -*-
"""
Identifying function names in a script
======================================

This demonstrates how Sphinx-Gallery identifies names function to figure out
which functions are called in the script and to which module do they belong.

It uses both the code itself, as well as the docstrings (such as this one),
as adding a reference to :func:`numpy.sin` and :func:`numpy.exp` will create
proper backreferences even if they are not explicitly used. This is useful
in particular when functions return classes -- if you add them to the docstring
of the example that calls them, they will be shown in the backreferences.
"""

# Code source: Óscar Nájera
# License: BSD 3 clause

import os
import matplotlib.pyplot as plt
import sphinx_gallery.backreferences as spback


filename = spback.__file__.replace('.pyc', '.py')
names = spback.identify_names(filename)
figheight = len(names) + .5

fontsize = 20
fig = plt.figure(figsize=(7.5, 8))

for i, (name, obj) in enumerate(names.items()):
    fig.text(0.55, (float(len(names)) - 0.5 - i) / figheight,
             name,
             ha="right",
             size=fontsize,
             transform=fig.transFigure,
             bbox=dict(boxstyle='square', fc="w", ec="k"))
    fig.text(0.6, (float(len(names)) - 0.5 - i) / figheight,
             obj["module"],
             ha="left",
             size=fontsize,
             transform=fig.transFigure,
             bbox=dict(boxstyle='larrow', fc="w", ec="k"))
#
plt.draw()
plt.show()
