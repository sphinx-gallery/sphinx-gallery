"""
Repr test
=========
Test repr and the sphinx_gallery_dummy_image config.
"""


# sphinx_gallery_dummy_image=2
class A:
    def _repr_html_(self):
        return '<p><b>This should print<b></p>'


A()
