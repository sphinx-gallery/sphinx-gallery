"""
Force plots to be displayed on separate lines
=============================================
This example demonstrates how the visualisation of multiple plots produced from a single
code block can be controlled. The default behaviour is to stack plots side-by-side,
however this can be overridden to display each plot created by the code block on a
separate line, preserving their size.

There are two config options to control this behaviour:

- a file-wide ``sphinx_gallery_multi_image`` variable
- a code block-specific ``sphinx_gallery_multi_image_block`` variable

Setting these variables to ``"single"`` will force plots to be displayed on separate
lines. Default behaviour is to treat these variables as being set to ``"multi"``.

Below we demonstrate how the file-wide ``sphinx_gallery_multi_image`` variable can be
used to display plots on separate lines.
"""

# Code source: Thomas S. Binns
# License: BSD 3 clause
# sphinx_gallery_tags = ["matplotlib","image","split-plots"]

# sphinx_gallery_multi_image = "single"

import matplotlib.pyplot as plt
import numpy as np

# %%

# Plots will be shown on separate lines

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.pcolormesh(np.random.randn(100, 100))

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.pcolormesh(np.random.randn(100, 100))

########################################################################################
# Now, we show how the ``sphinx_gallery_multi_image_block`` variable can be used to
# control the behaviour for a specific code block, here reverting to the default
# behaviour of stacking plots side-by-side.

# %%

# sphinx_gallery_multi_image_block = "multi"
# ↑↑↑ Return to default behaviour for just this cell

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.pcolormesh(np.random.randn(100, 100))

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.pcolormesh(np.random.randn(100, 100))
