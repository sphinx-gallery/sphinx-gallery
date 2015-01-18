# -*- coding: utf-8 -*-
"""
Installer Sphinx extension for gallery generator
"""

from setuptools import setup, find_packages
import sphinxgallery

setup(
    name="sphinx-gallery",
    description="Sphinx extension to automatically generate an examples gallery",
    version=sphinxgallery.__version__,
    packages=find_packages(),
    package_data={'sphinxgallery': ['_static/gallery.css', '_static/no_image.png']},
    url="https://github.com/sphinx-gallery/sphinx-gallery",
    author="Óscar Nájera",
    author_email='najera.oscar@gmail.com',
    install_requires=['Sphinx', 'matplotlib', 'pillow', 'joblib'],
    setup_requires=['nose>=1.0']
)
