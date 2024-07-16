"""
Example that fails to execute (with normal thumbnail behaviour)
===============================================================

By default, examples with code blocks that raise an error will have the broken
image stamp as their gallery thumbnail. However, this may not be desired, e.g.
if only part of the example is expected to fail and it should not look like the
entire example fails.

In these cases, the `sphinx_gallery_failing_thumbnail` variable can be set to
``False``, which will change the thumbnail selection to the default behaviour
as for non-failing examples.
"""

# Code source: Thomas S. Binns
# License: BSD 3 clause
# sphinx_gallery_line_numbers = True

# sphinx_gallery_failing_thumbnail = False

import matplotlib.pyplot as plt
import numpy as np

plt.pcolormesh(np.random.randn(100, 100))

# %%
# This block will raise an AssertionError

assert False
