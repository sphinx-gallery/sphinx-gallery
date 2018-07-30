# -*- coding: utf-8 -*-
"""
Identifying function names in a script
======================================

This demonstrates how Sphinx-Gallery identifies function names to figure out
which functions are called in the script and to which module do they belong.
"""

# Code source: Óscar Nájera
# License: BSD 3 clause

import os  # noqa, analysis:ignore
import matplotlib.pyplot as plt
import sphinx_gallery.backreferences as spback

filename = spback.__file__.replace('.pyc', '.py')
names = spback.identify_names(filename)
figheight = len(names) + .5

fontsize = 20

###############################################################################
# Sphinx-Gallery examines both the executed code itself, as well as the
# documentation blocks (such as this one, or the top-level one),
# to find backreferences. This means that by writing :obj:`numpy.sin`
# and :obj:`numpy.exp` here, a backreference will be created even though
# they are not explicitly used in the code. This is useful in particular when
# functions return classes -- if you add them to the documented blocks of
# examples that use them, they will be shown in the backreferences.

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
