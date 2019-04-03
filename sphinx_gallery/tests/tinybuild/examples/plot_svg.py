"""
============
SVG graphics
============

Make sure we can embed SVG graphics.
"""

import numpy as np
import matplotlib.pyplot as plt

from local_module import N  # N = 1000

t = np.arange(N) / float(N)
win = np.hanning(N)
plt.figure()
plt.plot(t, win, color='r')
plt.text(0, 1, 'svg', size=40, va='top')
