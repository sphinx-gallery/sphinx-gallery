"""Dummy module whose API is deliberately never used by any example.

Together with :mod:`sphinx_gallery._dummy.unused_b` this gives the API usage graph
a deep, tie-heavy set of unused entries like a real project's, which is what
``test_rebuild_deterministic`` needs to detect ordering bugs. Keep these unused.
"""


class UnusedAlpha:
    """Unused class for exercising the API usage graph."""

    def one(self):
        """Do nothing."""

    def two(self):
        """Do nothing."""

    def three(self):
        """Do nothing."""


class UnusedBeta:
    """Unused class for exercising the API usage graph."""

    def one(self):
        """Do nothing."""

    def two(self):
        """Do nothing."""

    def three(self):
        """Do nothing."""


class UnusedGamma:
    """Unused class for exercising the API usage graph."""

    def one(self):
        """Do nothing."""

    def two(self):
        """Do nothing."""

    def three(self):
        """Do nothing."""
