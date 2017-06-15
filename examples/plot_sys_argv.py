"""
Using ``sys.argv`` in examples
==============================

Note that your example will be run by sphinx-gallery without arguments.
"""

import argparse
import sys

parser = argparse.ArgumentParser(description='Toy parser')
parser.add_argument('--option', default='default',
                    help='a dummy optional argument')
print('sys.argv:', sys.argv)
print('parsed args:', parser.parse_args())
