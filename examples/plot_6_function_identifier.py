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
from sphinx_gallery.backreferences import identify_names
from sphinx_gallery.py_source_parser import split_code_and_text_blocks

filename = os.__file__.replace('.pyc', '.py')
_, script_blocks = split_code_and_text_blocks(filename)
names = identify_names(script_blocks)
figheight = len(names) + .5

fontsize = 12.5

# %%
# Sphinx-Gallery examines both the executed code itself, as well as the
# documentation blocks (such as this one, or the top-level one),
# to find backreferences. This means that by writing :obj:`numpy.sin`
# and :obj:`numpy.exp` here, a backreference will be created even though
# they are not explicitly used in the code. This is useful in particular when
# functions return classes -- if you add them to the documented blocks of
# examples that use them, they will be shown in the backreferences.
#
# Also note that global variables of the script have intersphinx references
# added to them automatically (e.g., ``fig`` and ``fig.text`` below).

fig = plt.figure(figsize=(7.5, 8))

for i, (name, obj) in enumerate(names.items()):
    fig.text(0.55, (float(len(names)) - 0.5 - i) / figheight,
             name,
             ha="right",
             size=fontsize,
             transform=fig.transFigure,
             bbox=dict(boxstyle='square', fc="w", ec="k"))
    fig.text(0.6, (float(len(names)) - 0.5 - i) / figheight,
             obj[0]["module"],
             ha="left",
             size=fontsize,
             transform=fig.transFigure,
             bbox=dict(boxstyle='larrow,pad=0.1', fc="w", ec="k"))

plt.draw()
