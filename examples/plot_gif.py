# -*- coding: utf-8 -*-
"""
==============================================
Embedding an image file that was saved to disk
==============================================

If you wish to save an image to disk (e.g., if you create a GIF) and wish to
embed it in your documentation, you may do so with the `image_files` scraper.

This example creates a GIF using Matplotlib that is saved to disk with the
``FuncAnimation`` class. The created image file will be embedded in the
documentation just after the cell that created the file. This behavior is
enabled with the `image_files` value in the `image_scapers` configuration. See
:ref:`image_scrapers` for more information.

This example was modified from `this blog post by
Eli Bendersky <https://eli.thegreenplace.net/2016/drawing-animated-gifs-with-matplotlib/>`_.
"""

# Code source: Chris Holdgraf, Eli Bendersky
# License: BSD 3 clause

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

###############################################################################
# Create our figure
# =================
#
# First we'll create the figure for our animation. We'll use a simple scatter
# plot with a line plotted on top.

fig, ax = plt.subplots()
fig.set_tight_layout(True)

# Plot a scatter that persists (isn't redrawn) and the initial line.
x = np.arange(0, 20, 0.1)
ax.scatter(x, x + np.random.normal(0, 3.0, len(x)))
line, = ax.plot(x, x - 5, 'r-', linewidth=2)


def update(ii):
    label = 'timestep {0}'.format(ii)
    # Update the line and the axes (with a new xlabel). Return a tuple of
    # "artists" that have to be redrawn for this frame.
    line.set_ydata(x - 5 + ii)
    ax.set_xlabel(label)
    return line, ax


###############################################################################
# Create the animation
# ====================
#
# FuncAnimation will call the 'update' function for each frame. Here,
# we animate over 10 frames, with an interval of 200ms between frames.
# Once this animation is saved to disk, Sphinx-gallery will embed it in the
# documentation.

anim = FuncAnimation(fig, update, frames=np.arange(0, 10), interval=500)
anim.save('line.gif', dpi=40, writer='pillow')

###############################################################################
# .. note::
#    Sphinx-gallery will only display an image file if it has been modified
#    since the execution of the Python file. It will not display a pre-existing
#    image file (though you can always refer to these by directly embedding
#    them in your rST).
