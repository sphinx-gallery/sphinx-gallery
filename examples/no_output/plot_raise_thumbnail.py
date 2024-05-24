"""
Example that fails to execute (with a specified thumbnail)
==========================================================

By default, examples with code blocks that raise an error will have the broken
image stamp as their gallery thumbnail. However, this may not be desired, e.g.
if only part of the example is expected to fail and it should not look like the
entire example fails.

In these cases, the `sphinx_gallery_thumbnail_path` variable can be set to
specify a desired thumbnail.
"""

# Code source: Thomas S. Binns
# License: BSD 3 clause
# sphinx_gallery_line_numbers = True

# sphinx_gallery_thumbnail_path = 'auto_examples/no_output/images/sphx_glr_plot_raise_001.png'  # noqa

import numpy as np
import matplotlib.pyplot as plt

plt.pcolormesh(np.random.randn(100, 100))

# %%
# This block will raise an AssertionError

assert False
