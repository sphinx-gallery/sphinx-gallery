# -*- coding: utf-8 -*-
"""
Installer Sphinx extension for gallery generator
"""
# TODO
# - Remove setup tools and use python standard distutils
# - Automatic online deployment CI and website
# - Sample gallery with documentation

from setuptools import setup, find_packages


setup(
    name="sphinxgallery",
    description="Sphinx extension to automatically generate an examples gallery",
    version="0.0.2",
    packages=find_packages(),
    package_data={'sphinxgallery': ['_static/gallery.css', '_static/no_image.png']},
    url="https://github.com/sphinx-gallery/sphinx-gallery",
    author="Óscar Nájera",
    author_email='najera.oscar@gmail.com',
    install_requires=['scipy', 'Sphinx', 'matplotlib', 'pillow', 'scikit-learn', 'numpy'],
    setup_requires=['nose>=1.0']
)
