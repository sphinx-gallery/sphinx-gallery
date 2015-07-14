# -*- coding: utf-8 -*-
"""
========================
Notebook styled examples
========================

The gallery is capable of transforming python files into reStructuredText files
with a notebook structure. In this case, all strings are converted into regular
reStructuredText while all python code is converted in code blocks that are
executed serially and code with output is converted to reStructuredText.

It makes a lot of sense to contrast this output rst file with the
:download:`original python script <plot_notebook.py>` to get better feeling of
the necessary file structure.

Anything before the first python string is ignored by sphinx-gallery and will
not appear in the rst file, nor will it be executed.
The first python string requires an reStructuredText title to name the file and
correctly build the reference links. Then one expects to alternate between
code blocks and comment/string blocks.

Thus keep in mind to always use a single string to introduce all your content
and code blocks. As in this example we start by first writing this module
style docstring, then for the first code block we write the example file author
and script license continued by the import modules instructions.
"""

# Code source: Óscar Nájera
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

##############################################################################
# This code block is executed, although it produces no output. It is now
#possible to again include a new comment string, which is this text. The
#sphinx-gallery parser will assume everything between the strings is code and
#execute it. Keep in mind to always keep your comments always in the same string
#block.
#
#In this example the next block of code produces some plotable data. Code is
#executed, figure is saved and then code is presented next, followed by the
#inlined figure.

x = np.linspace(-np.pi, np.pi, 300)
xx, yy = np.meshgrid(x, x)
z = np.cos(xx) + np.cos(yy)

plt.figure()
plt.imshow(z)
plt.colorbar()
plt.xlabel('$x$')
plt.ylabel('$y$')

###########################################################################
#Again it is possble to continue the discussion with a new python string. This
#time to introduce the next code block generates 2 separate figures.

plt.figure()
plt.imshow(z, cmap=plt.cm.get_cmap('hot'))
plt.figure()
plt.imshow(z, cmap=plt.cm.get_cmap('Spectral'), interpolation='none')

##########################################################################
#There's some subtle differences between strings and comments which I'll
#demonstrate below. (Some of this only makes sense if you look at the
#:download:`raw python script <plot_notebook.py>`)

# Comments in text blocks remain nested in the text.

def dummy():
    """Dummy function to make sure docstrings don't get rendered as text"""
    pass

# Code comments are not strings and are left in code blocks.

# Any string that's not saved to a variable is converted to text.

string = """
Triple-quoted string which tries to break parser but doesn't.
"""

############################################################################
#Finally, I'll call ``show`` at the end just so someone running the python code
#directly will see the plots; this is not necessary for creating the docs.

plt.show()
