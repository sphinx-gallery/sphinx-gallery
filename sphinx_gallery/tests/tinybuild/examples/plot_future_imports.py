"""
Test __future__ imports across cells
------------------------------------

This example tests that __future__ imports works across cells.
"""

from __future__ import division
from __future__ import print_function
import matplotlib

####################
# Dummy section, with :func:`sphinx_gallery.backreferences.identify_names` ref.

assert 3/2 == 1.5
print(3/2, end='')

# testing reset of mpl
assert matplotlib.rcParams['figure.dpi'] == 100.
matplotlib.rcParams['figure.dpi'] = 90.
assert matplotlib.rcParams['figure.dpi'] == 90.
