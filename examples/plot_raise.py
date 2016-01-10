# -*- coding: utf-8 -*-
"""
=============================
Example that fails to execute
=============================

When scripts fail their gallery thumbnail is replaced with the broken
image stamp. Thus allowing easy identification in the gallery display.

You also get the python traceback of the failed code block
"""

iae

###############################################################################
# Sphinx gallery as it executes scripts by block will continue
# evaluating the script after exceptions, but there is no warranty
# figure ordering will continue to match block's code. Anyway when the
# script is broken, you should try to fix it first.

# Code source: Óscar Nájera
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

plt.pcolormesh(np.random.randn(100, 100))


###############################################################################
# Here is another error raising Block

plt.plot('Strings are not a valid argument for the plot function')
