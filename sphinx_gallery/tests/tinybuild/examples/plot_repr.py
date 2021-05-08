"""
Repr test
=========
Test repr and the sphinx_gallery_dummy_images config.
"""


# sphinx_gallery_dummy_images=2
class A:
    def _repr_html_(self):
        return '<p><b>This should print<b></p>'


A()
