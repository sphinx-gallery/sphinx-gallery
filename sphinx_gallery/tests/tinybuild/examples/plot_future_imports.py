"""
Test __future__ imports across cells
------------------------------------

This example tests that __future__ imports works across cells.
"""

from __future__ import division
from __future__ import print_function

####################
# Dummy section
assert 3/2 == 1.5
print(3/2, end='')
