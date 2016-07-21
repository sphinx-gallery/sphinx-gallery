# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Installer Sphinx extension for gallery generator
"""

import codecs
from setuptools import setup, find_packages
import sphinx_gallery

with codecs.open('README.rst', mode='r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="sphinx-gallery",
    description="Sphinx extension to automatically generate an examples gallery",
    long_description=long_description,
    version=sphinx_gallery.__version__,
    packages=find_packages(),
    package_data={'sphinx_gallery': ['_static/gallery.css', '_static/no_image.png',
                                     '_static/broken_example.png']},
    scripts=['bin/copy_sphinxgallery.sh'],
    url="https://github.com/sphinx-gallery/sphinx-gallery",
    author="Óscar Nájera",
    author_email='najera.oscar@gmail.com',
    # XXX : don't force requirements in setup.py as it tends to break people
    # install_requires= ['Sphinx', 'matplotlib', 'pillow'],
    install_requires=[],
    setup_requires=['nose>=1.0'],
    license='3-clause BSD',
    classifiers=['Intended Audience :: Developers',
                 'Development Status :: 3 - Alpha',
                 'Framework :: Sphinx :: Extension',
                 'Programming Language :: Python',
                 ],
)
