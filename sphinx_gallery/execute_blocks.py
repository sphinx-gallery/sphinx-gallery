# -*- coding: utf-8 -*-
r"""
Excecute blocks
===============
"""
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import absolute_import, division, print_function

import os
import sys
import traceback
import warnings
from collections import namedtuple
from io import StringIO
from time import time

import matplotlib


matplotlib.use('Agg')
import matplotlib.pyplot as plt
from .write_rst import codestr2rst
from .save_images import save_figures


try:
    basestring
except NameError:
    basestring = str
    unicode = str


class MixedEncodingStringIO(StringIO):
    """Helper when both ASCII and unicode strings will be written"""

    def write(self, data):
        if not isinstance(data, unicode):
            data = data.decode('utf-8')
        StringIO.write(self, data)


class Tee(object):
    """A tee object to redirect streams to multiple outputs"""

    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def write(self, data):
        self.file1.write(data)
        self.file2.write(data)

    def flush(self):
        self.file1.flush()
        self.file2.flush()

    # When called from a local terminal seaborn needs it in Python3
    def isatty(self):
        self.file1.isatty()


exec_block = namedtuple('Execution_block',
                        ["label", "content", "figure_list", "stdout"])


def execute_code_block(block, example_globals,
                       block_vars, gallery_conf):
    """Executes the code block of the example file"""
    stdout = ''

    # If example is not suitable to run, skip executing its blocks
    if not block_vars['execute_script'] or block[0] == 'text':
        return exec_block(block[0], block[1], [], stdout)

    plt.close('all')
    cwd = os.getcwd()
    # Redirect output to stdout and
    orig_stdout = sys.stdout
    src_file = block_vars['src_file']

    try:
        # First cd in the original example dir, so that any file
        # created by the example get created in this directory
        os.chdir(os.path.dirname(src_file))
        my_buffer = MixedEncodingStringIO()
        my_stdout = Tee(sys.stdout, my_buffer)
        sys.stdout = my_stdout

        # don't use unicode_literals at the top of this file or you get
        # nasty errors here on Py2.7
        exec(block[1], example_globals)

        sys.stdout = orig_stdout

        my_stdout = my_buffer.getvalue().strip().expandtabs()
        # raise RuntimeError
        if my_stdout:
            stdout = my_stdout
        os.chdir(cwd)
        fig_list = save_figures(block_vars['image_path'], block_vars['fig_count'],
                                gallery_conf)

    except Exception:
        formatted_exception = traceback.format_exc()

        fail_example_warning = 80 * '_' + '\n' + \
            '%s failed to execute correctly:' % src_file + \
            formatted_exception + 80 * '_' + '\n'
        warnings.warn(fail_example_warning)

        fig_list = []
        stdout = codestr2rst(formatted_exception, lang='pytb')

        # Breaks build on first example error
        # XXX This check can break during testing e.g. if you uncomment the
        # `raise RuntimeError` by the `my_stdout` call, maybe use `.get()`?
        if gallery_conf['abort_on_example_error']:
            raise
        # Stores failing file
        gallery_conf['failing_examples'][src_file] = formatted_exception
        block_vars['execute_script'] = False

    finally:
        fig_num = len(fig_list)
        os.chdir(cwd)
        sys.stdout = orig_stdout

    block_vars['fig_count'] += fig_num

    return exec_block(block[0], block[1], fig_list, stdout)


def clean_modules():
    """Remove "unload" seaborn from the name space

    After a script is executed it can load a variety of setting that one
    does not want to influence in other examples in the gallery."""

    # Horrible code to 'unload' seaborn, so that it resets
    # its default when is load
    # Python does not support unloading of modules
    # https://bugs.python.org/issue9072
    for module in list(sys.modules.keys()):
        if 'seaborn' in module:
            del sys.modules[module]

    # Reset Matplotlib to default
    plt.rcdefaults()


def execute_script_blocks(script_blocks, block_vars, gallery_conf):
    """Executes all scripts blocks and returns a list of its output"""
    t_start = time()

    example_globals = {
        # A lot of examples contains 'print(__doc__)' for example in
        # scikit-learn so that running the example prints some useful
        # information. Because the docstring has been separated from
        # the code blocks in sphinx-gallery, __doc__ is actually
        # __builtin__.__doc__ in the execution context and we do not
        # want to print it
        '__doc__': '',
        # Examples may contain if __name__ == '__main__' guards
        # for in example scikit-learn if the example uses multiprocessing
        '__name__': '__main__',
    }
    executed_blocks = [execute_code_block(block, example_globals,
                                          block_vars, gallery_conf)
                       for block in script_blocks]

    clean_modules()

    time_elapsed = time() - t_start

    return executed_blocks, time_elapsed
