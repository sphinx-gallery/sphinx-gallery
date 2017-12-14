# -*- coding: utf-8 -*-
r"""
Study a Bokeh plot
==================

Capture a Bokeh figure

Only need to define which object is the figure
"""
# Created: Fri Nov 24 16:39:45 2017
# Author: Óscar Nájera
# License: 3-clause BSD
from __future__ import division, absolute_import, print_function


import numpy as np
from bokeh.plotting import figure

N = 500
x = np.linspace(0, 10, N)
y = np.linspace(0, 10, N)
p = figure(x_range=(0, 10), y_range=(0, 10))

# must give a vector of image data for image parameter
p = figure(plot_width=400, plot_height=400)
p.line(x, np.sin(x) / x)
p.line(x, np.sin(-2 * x) / x, color='red')

# sphx_glr_capture_bokeh = p
