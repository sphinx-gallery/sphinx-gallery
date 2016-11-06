#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
Sphinx Gallery Notebook converter
=================================

Exposes the Sphinx-Gallery Notebook rederer to directly convert Python
scripts into Jupyter Notebooks.

"""
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import division, absolute_import, print_function
import argparse
import os

import sphinx_gallery.gen_rst as sg
from sphinx_gallery.notebook import jupyter_notebook, save_notebook

parser = argparse.ArgumentParser(
    description='Sphinx-Gallery Notebook converter')
parser.add_argument('python_src_file', nargs='+',
                    help='Input Python file script to convert. '
                    'Supports multiple files and shell wildcards'
                    ' (e.g. *.py)')


def main():
    args = parser.parse_args()

    for src_file in args.python_src_file:
        blocks = sg.split_code_and_text_blocks(src_file)
        print('Converting {0}'.format(src_file))
        example_nb = jupyter_notebook(blocks)
        save_notebook(example_nb, src_file.replace('.py', '.ipynb'))


if __name__ == '__main__':
    main()
