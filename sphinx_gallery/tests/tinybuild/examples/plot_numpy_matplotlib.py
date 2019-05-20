"""
======================
Link to other packages
======================

Use :mod:`sphinx_gallery` to link to other packages, like
:mod:`numpy`, :mod:`matplotlib.colors`, and :mod:`matplotlib.pyplot`.

FYI this gallery uses :obj:`sphinx_gallery.sorting.FileNameSortKey`.
"""

from warnings import warn

import numpy as np
from matplotlib.colors import is_color_like
import matplotlib
import matplotlib.pyplot as plt

from local_module import N  # N = 1000

t = np.arange(N) / float(N)
win = np.hanning(N)
print(is_color_like('r'))
plt.figure()
plt.plot(t, win, color='r')
plt.text(0, 1, 'png', size=40, va='top')
orig_dpi = 80. if matplotlib.__version__[0] < '2' else 100.
assert plt.rcParams['figure.dpi'] == orig_dpi
plt.rcParams['figure.dpi'] = 70.
assert plt.rcParams['figure.dpi'] == 70.
warn('This warning should show up in the output', RuntimeWarning)
