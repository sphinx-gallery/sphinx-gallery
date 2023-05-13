"""
Test using _repr_mimebundle_
============================
Test repr capturing via ``_repr_mimebundle_`` and make sure that the
``capture_repr`` ordering is honored as well as ``_repr_mimebundle_``
over other ``_repr_*_`` having precedence.
"""
# sphinx_gallery_capture_repr = ('_repr_svg_', '_repr_html_')
# %%
# First define a class with only an SVG in the MIME bundle


class A:
    def _repr_mimebundle_(self, **kwargs):
        return {"image/svg+xml": """
<svg viewBox="0 0 50 50" xmlns="http://www.w3.org/2000/svg">
<line x1="0" y1="0" x2="50" y2="50" stroke="black" />
</svg>
"""}


A()


# %%
# Then, only a HTML representation, but both ``_repr_html_`` and
# ``_repr_mimebundle_``.
class B:
    def _repr_html_(self):
        return '<p><b>This should not print</b></p>'

    def _repr_mimebundle_(self, **kwargs):
        # Breaking the string here, so one can use the sentence to
        # check the correct HTML output
        return {"text/html": '<p><b>This should'
                             ' actually print</b></p>'}


B()


# %%
# Then, both SVG and HTML. The SVG should be selected based on the order.
class C:
    def _repr_mimebundle_(self, **kwargs):
        return {"image/svg+xml": """
<svg viewBox="0 0 50 50" xmlns="http://www.w3.org/2000/svg">
<line x1="0" y1="0" x2="50" y2="50" stroke="black" />
</svg>
""",
                "text/html": '<p><b>This should not print</b></p>'}


C()


# %%
# Finally, a separate ``_repr_svg_`` that should be selected since
# ``_repr_mimebundle_`` only includes HTML.
class D:
    def _repr_svg_(self):
        return """
    <svg viewBox="0 0 50 50" xmlns="http://www.w3.org/2000/svg">
    <line x1="0" y1="0" x2="50" y2="50" stroke="black" />
    </svg>
    """

    def _repr_mimebundle_(self, **kwargs):
        return {"text/html": '<p><b>This should not print</b></p>'}


D()
