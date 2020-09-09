"""
Testing future statements across examples
-----------------------------------------

This example runs after plot_future_statements.py (alphabetical ordering within
subsection) and should be unaffected by the __future__ import in
plot_future_statements.py.
"""
# sphinx_gallery_thumbnail_path = '_static_nonstandard/demo.png'

import sys
from sphinx_gallery.sorting import ExplicitOrder

ExplicitOrder([])  # must actually be used to become a backref target!

PY2 = sys.version_info[0] == 2

expected = 1 if PY2 else 1.5
assert 3/2 == expected

# Make sure print is a keyword not a function. Note: need to use exec because
# otherwise you get a SyntaxError on Python 3
if PY2:
    exec('print "test"')
