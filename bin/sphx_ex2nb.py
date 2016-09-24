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
from sphinx_gallery.notebook import Notebook

parser = argparse.ArgumentParser(
    description='Sphinx-Gallery Notebook converter')
parser.add_argument('file', nargs='+',
                    help='Input Python file script to convert. '
                    'Supports multiple files and shell wildcards'
                    ' (e.g. *.py)')


def main():
    args = parser.parse_args()

    for src_file in args.file:
        file_name = os.path.basename(src_file)
        blocks = sg.split_code_and_text_blocks(src_file)
        print('Converting {0}'.format(src_file))
        example_nb = Notebook(file_name, '.', blocks)
        example_nb.save_file()


if __name__ == '__main__':
    main()
