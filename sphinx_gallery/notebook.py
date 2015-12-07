# -*- coding: utf-8 -*-
r"""
============================
Parser for Jupyter notebooks
============================

Class that holds the Ipython notebook information

"""
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import division, absolute_import, print_function
import nbformat
import os

NOTEBOOK_SKELETON = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 2",
            "language": "python2",
            "name": "python2"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 2
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython2",
            "version": "2.7.10"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 0
}


class Notebook(object):
    """Ipython notebook object

    Constructs the file cell-by-cell and writes it at the end"""

    def __init__(self, file_name, target_dir):
        """Declare the skeleton of the notebook

        Parameters
        ----------
        file_name : str
            original script file name, .py extension will be renamed
        target_dir: str
            directory where notebook file is to be saved
        """

        self.file_name = file_name.replace('.py', '.ipynb')
        self.write_file = os.path.join(target_dir, self.file_name)
        self.work_notebook = nbformat.from_dict(NOTEBOOK_SKELETON)
        self.add_code_cell("%matplotlib inline")

    def add_code_cell(self, code):
        """Add a code cell to the notebook

        Parameters
        ----------
        code : str
            Cell content
        """
        code_cell = nbformat.from_dict({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {"collapsed": False},
            "outputs": [],
            "source": [code]
            })
        self.work_notebook["cells"].append(code_cell)

    def add_markdown_cell(self, text):
        """Add a markdown cell to the notebook

        Parameters
        ----------
        code : str
            Cell content
        """
        markdown_cell = nbformat.from_dict({
            "cell_type": "markdown",
            "metadata": {},
            "source": [text]
        })
        self.work_notebook["cells"].append(markdown_cell)

    def save_file(self):
        """Saves the notebook to a file"""
        nbformat.write(self.work_notebook, self.write_file)
