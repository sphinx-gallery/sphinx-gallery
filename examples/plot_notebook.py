# -*- coding: utf-8 -*-
"""
========================
Notebook styled examples
========================

The gallery is capable of transforming python files into reStructuredText files
with a notebook structure. In this case all strings are converted into regular
reStructuredText while all python code is converted in code block that are
executed.

It makes a lot of sense to contrast this output rst file with the original
python file to get better feeling of the necesary file structure.

Anything before the first string is ignored by the parser into the rst file.
The first string requires an reStructuredText title to name the file and
correctly build the reference links. Then one expects to alternate between
code blocks and comment/string blocks.

So keep in mind to always use a single string to introduce all your content
and code blocks. As in this example we start by giving the example file author
and license continued by the import modules intructions.
"""

# Code source: Óscar Nájera
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

"""
After that first code block we can again include a new comment string. The
sphinx-gallery parser will assume everything between the strings is code and
execute it.

Next as part of this example one can construct the sample data and the firt
inline plot.
"""

x = np.linspace(-np.pi, np.pi, 300)
xx, yy = np.meshgrid(x, x)
z = np.cos(xx) + np.cos(yy)

plt.figure()
plt.imshow(z)
plt.colorbar()
plt.xlabel('$x$')
plt.ylabel('$y$')

"""
Include a new comment and a new plot
"""
plt.figure()
plt.plot(x, -np.exp(-x))
plt.xlabel('$x$')
plt.ylabel('$-\exp(-x)$')


plt.show()
