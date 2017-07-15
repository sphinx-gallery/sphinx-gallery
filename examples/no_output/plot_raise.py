# -*- coding: utf-8 -*-
"""
Example that fails to execute
=============================

When scripts fail their gallery thumbnail is replaced with the broken
image stamp. Thus allowing easy identification in the gallery display.

You also get the python traceback of the failed code block
"""

# Code source: Óscar Nájera
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

plt.pcolormesh(np.random.randn(100, 100))

###############################################################################
# This next block will raise a NameError

iae

###############################################################################
# Sphinx gallery will stop executing the remaining code blocks after
# the exception has occurred in the example script. Nevertheless the
# html will still render all the example annotated text and
# code blocks, but no output will be shown.

###############################################################################
# Here is another error raising block but will not be executed

plt.plot('Strings are not a valid argument for the plot function')
