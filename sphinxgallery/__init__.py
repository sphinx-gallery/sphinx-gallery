"""Sphinx Gallery
"""
import os
__version__ = '0.0.9'

def path_static():
    """Returns path to packaged static files"""
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), '_static')
