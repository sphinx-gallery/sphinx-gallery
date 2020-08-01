"""
Using ``sys.argv`` in examples
==============================

This example demonstrates the use of ``sys.argv`` in example ``.py`` files.

By default, all example ``.py`` files will be run by Sphinx-Gallery **without** any
arguments. Notice below that ``sys.argv`` is a list consisting of only the
file name. Further, any arguments added will take on the default value.

This behavior can be changed by using the `reset_argv` option in the sphinx configuration, see :ref:`reset_argv`.

"""

import argparse
import sys

parser = argparse.ArgumentParser(description='Toy parser')
parser.add_argument('--option', default='default',
                    help='a dummy optional argument')
print('sys.argv:', sys.argv)
print('parsed args:', parser.parse_args())
