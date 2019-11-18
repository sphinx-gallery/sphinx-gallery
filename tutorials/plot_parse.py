# -*- coding: utf-8 -*-
"""
Alternating text and code
=========================

Sphinx-Gallery is capable of transforming Python files into rST files
with a notebook structure. For this to be used you need to respect some syntax
rules. This example demonstrates how to alternate text and code blocks and some
edge cases. It was designed to be compared with the
:download:`source Python script <plot_parse.py>`."""


##############################################################################
# This is the first text block and directly follows the header docstring above.

import numpy as np

##################################################

# a block separator (line of #'s) allows you to create two separate code blocks
A = 1

import matplotlib.pyplot as plt

#####################################
# You can easily alternate between code and text blocks **and** separate
# sequential blocks of code (above) and text (below). Note that separated
# text blocks only shows as a new lines between text, in the rendered output.

#############################################
# You can separate blocks using either a single line of ``#``'s (>=20 columns)
# or ``#%%``. For compatibility reasons ``# %%`` (with a space) can also be used
# but we recommend only using ``#%%`` for consistency. All future 
# 'block splitters' used in the source ``.py`` document will be ``#%%``.

def dummy():
    """This should not be part of a 'text' block'"""

    #############################################
    # Comment inside code to remain in code block
    pass

# this should not be part of a 'text' block

#%%
# 
# ####################################################################
#
# The above syntax makes a line cut in Sphinx. Note the space between the first
# ``#`` and the line of ``#``'s.

#%%
# .. warning::
#     The next kind of comments are not supported and become too hard to escape
#     so just don't code like this::
#
#         def dummy2():
#             """Function docstring"""
#         ####################################
#         # This comment 
#         #%%
#         # and this comment inside python indentation
#         # breaks the block structure and is not
#         # supported
#             dummy2
#

"""Free strings are not supported. They will be rendered as a code block"""

#%%
# New lines can be included in your text block and the parser
# is capable of retaining this important whitespace to work with Sphinx.
# Everything after a block splitter and starting with ``#`` then one space,
# is interpreted by Sphinx-Gallery to be a rST text block. Keep your text
# block together using ``#`` and a space at the beginning of each line.
#
# rST header within text block
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print('one')

#%%
#

# another way to separate code blocks shown above
B = 1

#%%
# Last text block.
#
# That's all folks !
#
# .. literalinclude:: plot_parse.py
#
#
