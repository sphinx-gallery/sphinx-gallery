"""
Testing backreferences
----------------------

This example runs after plot_future_statements.py (alphabetical ordering within
subsection) and should be unaffected by the ``__future__`` import in
plot_future_statements.py. We should eventually update this script to actually
test this... we require Python 3 nowadays so the ``__future__`` statements there
don't do anything. So for now let's repurpose this to look at some
backreferences. We should probably also change the filename in another PR!

A cross-reference carrying an intersphinx inventory prefix, such as
:obj:`sphinx_gallery:sphinx_gallery.sorting.ExplicitOrder`, becomes a backreference
whose name contains a colon -- which is not a legal filename character on Windows.
"""

# sphinx_gallery_thumbnail_path = '_static_nonstandard/demo.png'

from sphinx_gallery.scrapers import clean_modules, figure_rst
from sphinx_gallery.sorting import ExplicitOrder

ExplicitOrder([])  # must actually be used to become a backref target!

assert 3 / 2 == 1.5
assert figure_rst([], "") == ""
assert clean_modules(dict(reset_modules=[]), "", "before") is None
