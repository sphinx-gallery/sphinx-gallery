# -*- coding: utf-8 -*-
"""
The Header Docstring
====================

When writting latex in a Python string keep in mind to escape the backslashes
or use a raw docstring

.. math:: \\sin (x)

Closing this string quotes on same line"""


##############################################################################
# Direct first comment
# with second line

import numpy as np

##################################################
A = 1

import matplotlib.pyplot as plt

#####################################
# There is no need to always alternate between code and comment blocks
# Now there is free repetition of both

#############################################
# A block an be split by either a single line of ``#``'s (>=20 columns) or 
# ``#%%``. For compatibility reasons ``# %%`` (with a space) can also be used
# but we recommend only using ``#%%`` for consistency. All future 
# 'block splitters' used in the source ``.py`` document will be ``#%%``.

#%%
# Latex in the comments does not need to be escaped
#
# .. math::
#    \sin

def dummy():
    """This should not be part of a 'text' block'"""

    ######################################
    # Comment inside code to remain here
    pass

# this should not be part of a 'text' block

#%%
#
# ####################################################################
#
# Making a line cut in sphinx

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

"""Free strings are not supported. They remain part of the code"""

#%%
# New lines can be included in your block comments and the parser
# is capable of retaining this significant whitespace to work with sphinx
#
# So the reStructuredText headers survive
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


print('one')

#%%
# Code block separators
####################################################################
# Surrounding a comment line with a line of ``#``'s (like a block splitter)
# above and below (or ``#%%`` on top and a line of ``#``'s below, as we have 
# done here in the source ``.py`` doc) also works and creates a new header for
# that comment block too. Nevertheless to get rich text formatting we advise to
# use RestructuredText syntax in the comment blocks.

print('two')
#%%
#
B = 1

#%%
# End comments
#
# That's all folks !
#
# .. literalinclude:: plot_parse.py
#
#
