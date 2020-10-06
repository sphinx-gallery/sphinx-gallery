"""
Repr test
=========
Test repr.
"""


class A:
    def _repr_html_(self):
        return '<p><b>This should print<b></p>'


A()
