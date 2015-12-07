# -*- coding: utf-8 -*-
r"""
Parser for Jupyter notebooks
"""
# Author: Óscar Nájera

from __future__ import division, absolute_import, print_function
import nbformat
import os
import warnings

notebook_skeleton = {
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


class notebook_file(object):
    def __init__(self, file_name, target_dir):
        self.file_name = file_name.replace('.py', '.ipynb')
        self.write_file = os.path.join(target_dir, self.file_name)
        self.work_notebook = nbformat.from_dict(notebook_skeleton)
        self.add_code("%matplotlib inline")

    def add_code(self, code):
        code_cell = nbformat.from_dict({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {"collapsed": False},
            "outputs": [],
            "source": [code]
            })
        self.work_notebook["cells"].append(code_cell)

    def add_markdown(self, text):
        markdown_cell = nbformat.from_dict({
            "cell_type": "markdown",
            "metadata": {},
            "source": [text]
        })
        self.work_notebook["cells"].append(markdown_cell)

    def save_file(self):
        nbformat.write(self.work_notebook, self.write_file)
