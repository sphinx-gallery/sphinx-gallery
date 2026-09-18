"""
Sphinx Gallery
==============

"""

import os
from importlib.metadata import PackageNotFoundError, version

try:
    # Set at build time by setuptools-scm from the git tags, so there is no
    # version to bump by hand. Dev versions have "dev" in them, stable ones do
    # not; doc/conf.py makes use of this to set the version drop-down.
    __version__ = version("sphinx-gallery")
except PackageNotFoundError:  # not installed, e.g. run from a source tree
    __version__ = "0.0.dev0"


def glr_path_static() -> str:
    """Returns path to packaged static files"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "_static"))
