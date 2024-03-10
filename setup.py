# Author: Óscar Nájera
# License: 3-clause BSD
"""Install Sphinx extension for gallery generator."""

import codecs
from setuptools import setup, find_packages
import sphinx_gallery

# get the long and short descriptions from the README
with codecs.open("README.rst", mode="r", encoding="utf-8") as f:
    long_description = f.read()

description, in_ = "", False
for line in long_description.splitlines():
    if not in_:
        if (
            len(line)
            and not line.startswith((".", "=", " "))
            and line != "Sphinx-Gallery"
        ):
            in_ = True
    if in_:
        if len(line) == 0:
            break
        else:
            description += line + " "
description = description.strip()

# Get the requirements from requirements.txt and environment
with open("requirements.txt") as fid:
    install_requires = [line.strip() for line in fid if line.strip()]

extras_require = {
    "recommender": ["numpy"],
    "show_api_usage": ["graphviz"],
    "show_memory": ["memory_profiler"],
    "jupyterlite": ["jupyterlite_sphinx"],
}

setup(
    name="sphinx-gallery",
    description=description,  # noqa: E501, analysis:ignore
    long_description=long_description,
    long_description_content_type="text/x-rst",
    version=sphinx_gallery.__version__,
    packages=find_packages(),
    package_data={
        "sphinx_gallery": [
            "_static/sg_gallery*.css",
            "_static/no_image.png",
            "_static/broken_example.png",
            "_static/binder_badge_logo.svg",
            "_static/jupyterlite_badge_logo.svg",
        ]
    },
    entry_points={
        "console_scripts": [
            "python_to_jupyter = sphinx_gallery.notebook:python_to_jupyter_cli",
        ],
    },
    url="https://sphinx-gallery.github.io",
    project_urls={
        "Source": "https://github.com/sphinx-gallery/sphinx-gallery",
        "Documentation": "https://sphinx-gallery.github.io",
    },
    author="Óscar Nájera",
    author_email="najera.oscar@gmail.com",
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires=">=3.8",
    license="3-clause BSD",
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "Framework :: Sphinx :: Extension",
        "Programming Language :: Python",
    ],
)
