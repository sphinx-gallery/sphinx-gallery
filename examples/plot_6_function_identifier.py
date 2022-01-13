# -*- coding: utf-8 -*-
"""
Identifying function names in a script
======================================

This demonstrates how Sphinx-Gallery identifies the names of functions,
methods, attributes and objects used and classes instantated in the script
using the internal function ``identify_names``. It also determins to which module
they belong. Identified names are turned into code or intersphinx references.
"""

# Code source: Óscar Nájera
# License: BSD 3 clause

import os.path as op  # noqa, analysis:ignore
import matplotlib.pyplot as plt
import sphinx_gallery
from sphinx_gallery.backreferences import identify_names
from sphinx_gallery.py_source_parser import split_code_and_text_blocks

filename = 'plot_6_function_identifier.py'
if not op.exists(filename):
    filename = __file__ if '__file__' in locals() else op.join(op.dirname(
                   sphinx_gallery.__path__[0]), 'examples', filename)

_, script_blocks = split_code_and_text_blocks(filename)

names = identify_names(script_blocks)

# %%
# Sphinx-Gallery examines both the executed code itself, as well as the
# documentation blocks (such as this one, or the top-level one),
# to find backreferences. This means that by writing :obj:`numpy.sin`
# and :obj:`numpy.exp` here, backreferences will be created for them even
# though they are not used in the code. This is useful in particular when
# functions return classes -- if you add them to the documented blocks of
# examples that use them, they will be shown in the backreferences.
#
# The figure below shows the functions as written in the code block on the
# left and the full resolved import path for that function on the right.

fontsize = 12.5
figheight = 3 * len(names) * fontsize / 72
fig, ax = plt.subplots(figsize=(7.5, figheight))
ax.set_visible(False)

for i, (name, obj) in enumerate(names.items(), 1):
    fig.text(0.48, 1 - i / (len(names) + 1),
             name,
             ha="right",
             va="center",
             size=fontsize,
             transform=fig.transFigure,
             bbox=dict(boxstyle='square', fc="w", ec="k"))
    fig.text(0.52, 1 - i / (len(names) + 1),
             obj[0]["module"],
             ha="left",
             va="center",
             size=fontsize,
             transform=fig.transFigure,
             bbox=dict(boxstyle='larrow,pad=0.1', fc="w", ec="k"))

plt.show()
