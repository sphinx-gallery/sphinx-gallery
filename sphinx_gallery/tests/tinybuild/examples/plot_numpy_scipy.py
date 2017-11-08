"""
======================
Link to other packages
======================

Use :mod:`sphinx_gallery` to link to other packages, like
:mod:`numpy`, :mod:`scipy.signal`, and :mod:`matplotlib.pyplot`.

FYI this gallery uses :obj:`sphinx_gallery.sorting.FileNameSortKey`.
"""

import numpy as np
from scipy.signal import firwin
import matplotlib.pyplot as plt

t = np.arange(1001) / 1000.
win = firwin(1001, 0.05)
plt.plot(t, win)
assert plt.rcParams['figure.dpi'] == 100.
plt.rcParams['figure.dpi'] = 80.
assert plt.rcParams['figure.dpi'] == 80.
