"""
SVG repr test
=============
Test SVG repr capturing and specifying capture_repr in file.

"""

# sphinx_gallery_capture_repr = ('_repr_svg_',)


class B:
    def _repr_svg_(self):
        return """
<svg viewBox="0 0 50 50" xmlns="http://www.w3.org/2000/svg">
<line x1="0" y1="0" x2="50" y2="50" stroke="black" />
</svg>
"""


B()
