"""
Plot exponential
================

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 41)

plt.plot(x, np.exp(x))
# To avoid matplotlib text output
plt.show()
