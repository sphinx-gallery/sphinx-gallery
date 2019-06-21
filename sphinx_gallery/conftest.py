"""Helpers for testing."""

import sphinx


def pytest_report_header(config, startdir):
    """Add information to the pytest run header."""
    return 'Sphinx:  %s (%s)' % (sphinx.__version__, sphinx.__file__)
