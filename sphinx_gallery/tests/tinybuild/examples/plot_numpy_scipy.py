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
import matplotlib
import matplotlib.pyplot as plt

t = np.arange(1001) / 1000.
win = firwin(1001, 0.05)
plt.plot(t, win)
orig_dpi = 80. if matplotlib.__version__[0] < '2' else 100.
assert plt.rcParams['figure.dpi'] == orig_dpi
plt.rcParams['figure.dpi'] = 70.
assert plt.rcParams['figure.dpi'] == 70.
