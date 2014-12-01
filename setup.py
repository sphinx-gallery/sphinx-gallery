# -*- coding: utf-8 -*-
"""
Installer Sphinx extension for gallery generator
"""
# TODO
# - Remove setup tools and use python standard distutils
# - Automatic online deployment CI and website
# - Default CSS themening
# - Sample gallery with documentation

from setuptools import setup, find_packages


setup(
    name="sphinx_gallery",
    description="Sphinx extension to automatically generate an examples gallery",
    version="0.0.1",
    packages=find_packages(),
    url="https://github.com/sphinx-gallery/sphinx-gallery",
    author="Óscar Nájera",
    author_email='najera.oscar@gmail.com',
    install_requires=['Sphinx', 'matplotlib', 'pillow', 'scikit-learn'],
    setup_requires=['nose>=1.0']
)
