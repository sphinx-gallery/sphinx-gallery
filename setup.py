# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Installer Sphinx extension for gallery generator
"""

import codecs
import os
from setuptools import setup, find_packages
import sphinx_gallery

# get the long and short descriptions from the README
with codecs.open('README.rst', mode='r', encoding='utf-8') as f:
    long_description = f.read()

description, in_ = '', False
for line in long_description.splitlines():
    if not in_:
        if len(line) and not line.startswith(('.', '=', ' ')) and \
                line != 'Sphinx-Gallery':
            in_ = True
    if in_:
        if len(line) == 0:
            break
        else:
            description += line + ' '
description = description.strip()

# Get the requirements from requirements.txt and environment
with open('requirements.txt', 'r') as fid:
    install_requires = [line.strip() for line in fid if line.strip()]

setup(
    name="sphinx-gallery",
    description=description,  # noqa: E501, analysis:ignore
    long_description=long_description,
    long_description_content_type='text/x-rst',
    version=sphinx_gallery.__version__,
    packages=find_packages(),
    package_data={'sphinx_gallery': [
        '_static/gallery*.css',
        '_static/no_image.png',
        '_static/broken_example.png',
        '_static/binder_badge_logo.svg'
    ]},
    scripts=['bin/copy_sphinxgallery.sh', 'bin/sphx_glr_python_to_jupyter.py'],
    url="https://sphinx-gallery.github.io",
    author="Óscar Nájera",
    author_email='najera.oscar@gmail.com',
    install_requires=install_requires,
    python_requires='>=3.5',
    license='3-clause BSD',
    classifiers=['Intended Audience :: Developers',
                 'Development Status :: 4 - Beta',
                 'Framework :: Sphinx :: Extension',
                 'Programming Language :: Python',
                 ],
)
