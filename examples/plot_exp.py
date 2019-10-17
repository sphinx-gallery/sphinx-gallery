# -*- coding: utf-8 -*-
"""
Plotting the exponential function
=================================

A simple example for ploting two figures of a exponential
function in order to test the autonomy of the gallery
stacking multiple images.
"""

# Code source: Óscar Nájera
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

# You can use modules local to the example being run, here
# we just use a trivial NumPy wrapper
from local_module import N  # = 100


def main():
    x = np.linspace(-1, 2, N)
    y = np.exp(x)

    plt.figure()
    plt.plot(x, y)
    plt.xlabel('$x$')
    plt.ylabel('$\exp(x)$')

    plt.figure()
    plt.plot(x, -np.exp(-x))
    plt.xlabel('$x$')
    plt.ylabel('$-\exp(-x)$')
    # To avoid matplotlib text output
    plt.show()

if __name__ == '__main__':
    main()
