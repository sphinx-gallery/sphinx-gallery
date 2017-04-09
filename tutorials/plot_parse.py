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
# And a single line of hashes can split your blocks


###############################################################################
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

######################################################################
#
# ####################################################################
#
# Making a line cut in sphinx

###############################################################################
# .. warning::
#     The next kind of comments are not supported and become to hard to escape
#     so just don't code like this.
#
# .. code-block:: python
#
#     def dummy2():
#         """Function docstring"""
#     ####################################
#     # This comment inside python indentation
#     # breaks the block structure and is not
#     # supported
#         dummy2
#

"""Free strings are not supported they remain part of the code"""

##############################################################################
# New lines can be included in you block comments and the parser
# is capable of retaining this significant whitespace to work with sphinx
#
# So the reStructuredText headers survive
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


print('one')

###############################################################################
# Code block separators
###############################################################################
# Surrounding a comment line with lines of # like a block spliter also
# works and creates a new header for that comment block
# too. Nevertheless to get rich text formatting we advise to use
# RestructuredText syntax in the comment blocks.

print('two')
##################################################
#
B = 1

##############################################################################
# End comments
#
# That's all folks !
#
# .. literalinclude:: plot_parse.py
#
#
