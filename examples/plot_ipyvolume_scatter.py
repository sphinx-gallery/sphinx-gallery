"""
Scatter
=======

This example doesn't do much, it just makes a simple plot
"""
import ipyvolume as ipv
import numpy as np
N = 1000
x, y, z = np.random.normal(0, 1, (3, N))
fig = ipv.figure()
ipv.scatter(x, y, z)
ipv.show()
