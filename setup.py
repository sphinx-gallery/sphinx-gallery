# Author: Óscar Nájera
# License: 3-clause BSD
"""Install Sphinx extension for gallery generator."""

from setuptools import setup

setup(
    scripts=["bin/copy_sphinxgallery.sh", "bin/sphx_glr_python_to_jupyter.py"],
)
