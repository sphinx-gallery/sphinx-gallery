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
from itertools import compress  # noqa
import matplotlib
import matplotlib.pyplot as plt

from local_module import N  # N = 1000

t = np.arange(N) / float(N)
win = np.hanning(N)
print(is_color_like('r'))
fig, ax = plt.subplots()
ax.plot(t, win, color='r')
ax.text(0, 1, 'png', size=40, va='top')
fig.tight_layout()
orig_dpi = 80. if matplotlib.__version__[0] < '2' else 100.
assert plt.rcParams['figure.dpi'] == orig_dpi
plt.rcParams['figure.dpi'] = 70.
assert plt.rcParams['figure.dpi'] == 70.
listy = [0, 1]
warn('This warning should show up in the output', RuntimeWarning)
compress('abc', [0, 0, 1])
