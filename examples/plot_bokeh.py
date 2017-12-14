# -*- coding: utf-8 -*-
r"""
Study a Bokeh plot
==================

Capture javascript and HTML
"""
# Created: Fri Nov 24 16:39:45 2017
# Author: Óscar Nájera
# License: 3-clause BSD
from __future__ import division, absolute_import, print_function


import numpy as np
from bokeh.plotting import figure
import bokeh.resources
from bokeh.embed import autoload_static, file_html, components


N = 500
x = np.linspace(0, 10, N)
y = np.linspace(0, 10, N)
p = figure(x_range=(0, 10), y_range=(0, 10))

# must give a vector of image data for image parameter
p = figure(plot_width=400, plot_height=400)
p.line(x, np.sin(x) / x)
p.line(x, np.sin(-2 * x) / x, color='red')

js, script = autoload_static(p, bokeh.resources.CDN, 'te.js')


with open('te.js', 'w') as jsfi:
    jsfi.write(js)


with open('te.html', 'w') as jsfi:
    jsfi.write(script)

script, div = components(p)
with open('all.html', 'w') as jsfi:
    jsfi.write(script)
    jsfi.write('\n')
    jsfi.write(div)
