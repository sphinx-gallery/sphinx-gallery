"""
Matplotlib animation support
============================

Show a Matplotlib animation, which should end up nicely embedded below.

In order to enable support for animations ``'matplotlib_animations'``
must be set to ``True`` in the sphinx gallery
:ref:`configuration <image_scrapers>`.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Adapted from
# https://matplotlib.org/gallery/animation/basic_example.html


def _update_line(num):
    line.set_data(data[..., :num])
    return line,


fig, ax = plt.subplots()
data = np.random.RandomState(0).rand(2, 25)
line, = ax.plot([], [], 'r-')
ax.set(xlim=(0, 1), ylim=(0, 1))
ani = animation.FuncAnimation(fig, _update_line, 25, interval=100, blit=True)
