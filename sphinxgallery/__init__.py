"""Sphinx Gallery
"""
import os
def _path_static():
    """Returns path to packaged static files"""
    return os.path.abspath(os.path.dirname(__file__))+'/_static'
