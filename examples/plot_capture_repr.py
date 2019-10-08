# -*- coding: utf-8 -*-
r"""
Capturing output representations
================================

This example demonstrates how the configuration ``capture_repr``
(:ref:`capture_repr`) works. The setting used to build this Sphinx-Gallery
documentation is ``capture_repr: ('_repr_html_', '__repr__')``. The output that
is captured with this setting can be observed in this example. Differences in
outputs that would be captured with other ``capture_repr`` tuples is also
explained.
"""
#%%
# Nothing is captured for the code block above because no data is directed to
# standard output and the last statement is not an expression.

# example 1
a = 2
b = 10

#%%
# If you did wish to capture the value of ``b``, you would need to use:

# example 2
a = 2
b = 10
b   # this is an expression

#%%
# Technically, Sphinx-Gallery first attempts to capture the ``_repr_html_``
# of ``b`` as this is the first 'representation' method in the ``capture_repr``
# tuple. As this method does not exist for ``b``, Sphinx-Gallery moves on to
# try and capture the ``__repr__`` method, which is second in the tuple. This
# does exist for ``b`` so it is captured and included above. 
# 
# A pandas dataframe is used in the code block below to provide an example of
# an expression with a ``_repr_html_`` method. 

# example 3
import pandas as pd

df = pd.DataFrame(data = {'col1': [1, 2], 'col2': [3, 4]})
df

#%%
# The pandas dataframe ``df`` has both a ``__repr__`` and ``_repr_html_``
# method. As ``_repr_html_`` appears first in the ``capture_repr`` tuple, the
# ``_repr_html_`` is captured in preference.
#
# For the example below, the last statement is an expression and there is
# standard output data:

# example 4
print('Hello world')
a + b

#%%
# ``print()`` outputs to standard output, which is always captured. The
# string ``'Hello world'`` is thus captured. A 'representation' of the last
# expression is also captured. Again, since this expression does not have a
# ``_repr_html_`` method, the ``__repr__`` method is captured.
#
# The ``capture_repr`` configuration
# ##################################
#
# The ``capture_repr`` configuration is an empty tuple by default. With this
# setting, only data directed to standard output is captured. Thus, output
# would only be captured for example 4.
# 
# Adding 'representations' to the ``capture_repr`` tuple would direct
# Sphinx-Gallery to capture a 'representation' of the last statement, only if
# it is an expression. In examples 2, 3 and 4, the last statement is an
# expression. If the ``capture_repr`` configuration was *not* an empty tuple,
# Sphinx-Gallery would attempt to capture a 'representation' of the last
# expression for these examples. This would be performed according to the order
# that the ' ' methods are given in the tuple, with
# preference given to earlier methods.
#
# If no 'representation' in the ``capture_repr`` tuple is present for a last
# expression, nothing would be captured. For example, if the the configuration
# was set to ``'capture_repr': ('_repr_html_')`` nothing would be captured for
# example 2 as ``b`` does not have a ``_repr_html_``.
