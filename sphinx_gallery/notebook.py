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
from copy import deepcopy
import json
import os
import re

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

def rst2md(text):
    """Converts the RST text from the examples docstrigs and comments
    into markdown text for the IPython notebooks"""

    top_heading = re.compile(r'^=+$\s^([\w\s]+)^=+$', flags=re.M)
    text = re.sub(top_heading, r'# \1', text)

    math_eq = re.compile(r'^\.\. math::((?:.+)?(?:\n+^  .+)*)', flags=re.M)
    text = re.sub(math_eq,
                  lambda match: r'$${0}$$'.format(match.group(1).strip()),
                  text)
    inline_math = re.compile(r':math:`(.+)`')
    text = re.sub(inline_math, r'$\1$', text)

    return text

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
        self.work_notebook = deepcopy(NOTEBOOK_SKELETON)
        self.add_code_cell("%matplotlib inline")

    def add_code_cell(self, code):
        """Add a code cell to the notebook

        Parameters
        ----------
        code : str
            Cell content
        """

        code_cell = {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {"collapsed": False},
            "outputs": [],
            "source": [code.strip()]
            }
        self.work_notebook["cells"].append(code_cell)

    def add_markdown_cell(self, text):
        """Add a markdown cell to the notebook

        Parameters
        ----------
        code : str
            Cell content
        """
        markdown_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": [rst2md(text)]
        }
        self.work_notebook["cells"].append(markdown_cell)

    def save_file(self):
        """Saves the notebook to a file"""
        with open(self.write_file, 'w') as out_nb:
            json.dump(self.work_notebook, out_nb, indent=2)
