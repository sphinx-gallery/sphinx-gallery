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
# Nothing is captured for the code block below with **any** ``capture_repr``
# tuple because no data is directed to standard output and the last statement
# is not an expression.

a = 2
b = 10

#%%
# The string ``'Hello world'`` would be the only output captured for the code
# block below with **any** ``capture_repr`` tuple. This is because ``print()``
# outputs to standard output, which is always captured and the last statement
# is not an expression. The 'representation' methods, if present in the
# configuration tuple, are only captured if the last statement is an expression.

print('Hello world')
a = 'Hello'
b = 'world'

#%%
# For the code block below, nothing would be output if ``capture_repr`` was an
# empty tuple because nothing is output to standard output. However, if the
# tuple was not empty, a 'representation' would be captured because the last
# statement is an expression. In our case, Sphinx-Gallery would first attempt
# to capture the ``'_repr_html_'`` method as this is first in the tuple. Since
# ``a + b`` does not have a ``'_repr_html_``, Sphinx-Gallery then attempts to
# capture ``'__repr__'`` as this is second in the tuple. This exists for the
# expression and is thus what is captured. 

a = 2
b = 3
a + b

#%%
# A pandas dataframe is used in the code block below to provide an example of
# an expression with a ``_repr_html_`` method. The pandas dataframe ``df`` has
# both a ``__repr__`` and ``_repr_html_`` method. As ``_repr_html_`` appears
# first in the ``capture_repr`` tuple, the ``_repr_html_`` is captured and
# rendered in the built documentation.

import pandas as pd

df = pd.DataFrame(data = {'col1': [1, 2], 'col2': [3, 4]})
df



