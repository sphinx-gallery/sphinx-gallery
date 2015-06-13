# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Generate the rst files for the examples by iterating over the python
example files.

Files that generate images should start with 'plot'

"""
from __future__ import division, print_function, absolute_import
from time import time
import os
import re
import shutil
import traceback
import sys
import subprocess
import warnings
from . import glr_path_static
from .backreferences import write_backreferences, _thumbnail_div


# Try Python 2 first, otherwise load from Python 3
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

try:
    basestring
except NameError:
    basestring = str

import token
import tokenize
import numpy as np

try:
    # make sure that the Agg backend is set before importing any
    # matplotlib
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
except ImportError:
    # this script can be imported by nosetest to find tests to run: we should
    # not impose the matplotlib requirement in that case.
    pass


###############################################################################

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


###############################################################################
RST_TEMPLATE = """

.. _example_%(short_fname)s:

%(docstring)s\n
"""

PLOT_OUT_TEMPLATE = """
%(image_list)s

%(stdout)s

**Total running time of the example:** %(time_elapsed) .2f seconds
(%(time_m) .0f minutes %(time_s) .2f seconds)\n\n"""


CODE_DOWNLOAD = """**Python source code:** :download:`%(fname)s <%(fname)s>`\n"""

# The following strings are used when we have several pictures: we use
# an html div tag that our CSS uses to turn the lists into horizontal
# lists.
HLIST_HEADER = """
.. rst-class:: sphx-glr-horizontal

"""

HLIST_IMAGE_TEMPLATE = """
    *

      .. image:: /%s
            :scale: 47
"""

SINGLE_IMAGE = """
.. image:: /%s
    :align: center
"""

CODE_OUTPUT = """**Script output**:\n
.. rst-class:: sphx-glr-script-out

  ::

    {0}\n"""

def extract_docstring(filename):
    """ Extract a module-level docstring, if any
    """

    _, (srow, erow), first_text = split_code_and_text_blocks(filename)[0]

    paragraphs = first_text.split('\n\n')
    if len(first_text) > 1:
        first_par = re.sub('\n', ' ', paragraphs[1])
        first_par = ((first_par[:95] + '...')
                     if len(first_par) > 95 else first_par)
    else:
        raise ValueError("Docstring not found by gallery.\n"
                         "Please check the layout of your"
                         " example file:\n {}\n and make sure"
                         " it's correct".format(filename))

    return eval(first_text), first_par, erow


def analyze_blocks(source_file):
    """Return starting line numbers of code and text blocks
    Returns
    -------
    block_edges : list of int
        Line number for the start of each block and last line
    """
    block_edges = []
    with open(source_file) as f:
        token_iter = tokenize.generate_tokens(f.readline)
        for token_tuple in token_iter:
            t_id, t_str, (srow, scol), (erow, ecol), src_line = token_tuple
            tok_name = token.tok_name[t_id]
            if tok_name == 'STRING' and scol == 0:
                # Add one point to line after text (for later slicing)
                block_edges.extend((srow, erow+1))

    if not block_edges:  # no text blocks
        raise ValueError("Docstring not found by gallery.\n"
                         "Please check the layout of your"
                         " example file:\n {}\n and make sure"
                         " it's correct".format(source_file))
    else:
        # append last line if missig
        if not block_edges[-1] == erow:  # iffy: I'm using end state of loop
            block_edges.append(erow)

    return block_edges


def split_code_and_text_blocks(source_file):
    """Return list with source file separated into code and text blocks.
    Returns
    -------
    blocks : list of (label, (start, end+1), content)
        List where each element is a tuple with the label ('text' or 'code'),
        the (start, end+1) line numbers, and content string of block.
    """
    block_edges = analyze_blocks(source_file)

    with open(source_file) as f:
        source_lines = f.readlines()

    # Every other block should be a text block
    blocks = []
    slice_ranges = zip(block_edges[:-1], block_edges[1:])
    for i, (start, end) in enumerate(slice_ranges):
        block_label = 'text' if i % 2 == 0 else 'code'
        # subtract 1 from indices b/c line numbers start at 1, not 0
        content = ''.join(source_lines[start-1:end-1])
        blocks.append((block_label, (start, end), content))
    return blocks


def extract_line_count(filename, target_dir):
    """Extract the line count of a file"""
    example_file = os.path.join(target_dir, filename)
    lines = open(example_file).readlines()
    start_row = 0
    if lines and lines[0].startswith('#!'):
        lines.pop(0)
        start_row = 1
    line_iterator = iter(lines)
    tokens = tokenize.generate_tokens(lambda: next(line_iterator))
    check_docstring = True
    erow_docstring = 0
    for tok_type, _, _, (erow, _), _ in tokens:
        tok_type = token.tok_name[tok_type]
        if tok_type in ('NEWLINE', 'COMMENT', 'NL', 'INDENT', 'DEDENT'):
            continue
        elif (tok_type == 'STRING') and check_docstring:
            erow_docstring = erow
            check_docstring = False
    return erow_docstring+1+start_row, erow+1+start_row


def line_count_sort(file_list, target_dir):
    """Sort the list of examples by line-count"""
    new_list = [x for x in file_list if x.endswith('.py')]
    unsorted = np.zeros(shape=(len(new_list), 2))
    unsorted = unsorted.astype(np.object)
    for count, exmpl in enumerate(new_list):
        docstr_lines, total_lines = extract_line_count(exmpl, target_dir)
        unsorted[count][1] = total_lines - docstr_lines
        unsorted[count][0] = exmpl
    index = np.lexsort((unsorted[:, 0].astype(np.str),
                        unsorted[:, 1].astype(np.float)))
    if not len(unsorted):
        return []
    return np.array(unsorted[index][:, 0]).tolist()


def generate_dir_rst(src_dir, target_dir, gallery_conf,
                     plot_gallery, seen_backrefs):
    """Generate the rst file for an example directory"""
    if not os.path.exists(os.path.join(src_dir, 'README.txt')):
        print(80 * '_')
        print('Example directory %s does not have a README.txt file' %
              src_dir)
        print('Skipping this directory')
        print(80 * '_')
        return ""  # because string is an expected return type

    fhindex = open(os.path.join(src_dir, 'README.txt')).read()
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    sorted_listdir = [fname for fname in sorted(os.listdir(src_dir)) if fname.endswith('py')]
    for fname in sorted_listdir:
        generate_file_rst(fname, target_dir, src_dir, plot_gallery)
        new_fname = os.path.join(src_dir, fname)
        _, snippet, _ = extract_docstring(new_fname)
        write_backreferences(seen_backrefs, gallery_conf,
                             target_dir, fname, snippet)

        fhindex += _thumbnail_div(target_dir, fname, snippet)
        fhindex += """

.. toctree::
   :hidden:

   /%s/%s\n""" % (target_dir, fname[:-3])


# clear at the end of the section
    fhindex += """.. raw:: html\n
    <div style='clear:both'></div>\n\n"""

    return fhindex


def scale_image(in_fname, out_fname, max_width, max_height):
    """Scales an image with the same aspect ratio centered in an
       image with a given max_width and max_height
       if in_fname == out_fname the image can only be scaled down
    """
    # local import to avoid testing dependency on PIL:
    try:
        from PIL import Image
    except ImportError:
        import Image
    img = Image.open(in_fname)
    width_in, height_in = img.size
    scale_w = max_width / float(width_in)
    scale_h = max_height / float(height_in)

    if height_in * scale_w <= max_height:
        scale = scale_w
    else:
        scale = scale_h

    if scale >= 1.0 and in_fname == out_fname:
        return

    width_sc = int(round(scale * width_in))
    height_sc = int(round(scale * height_in))

    # resize the image
    img.thumbnail((width_sc, height_sc), Image.ANTIALIAS)

    # insert centered
    thumb = Image.new('RGB', (max_width, max_height), (255, 255, 255))
    pos_insert = ((max_width - width_sc) // 2, (max_height - height_sc) // 2)
    thumb.paste(img, pos_insert)

    thumb.save(out_fname)
    # Use optipng to perform lossless compression on the resized image if
    # software is installed
    if os.environ.get('SKLEARN_DOC_OPTIPNG', False):
        try:
            subprocess.call(["optipng", "-quiet", "-o", "9", out_fname])
        except Exception:
            warnings.warn('Install optipng to reduce the size of the \
                          generated images')


def execute_script(image_path, src_file, fname, code_block):
    image_dir, image_fname = os.path.split(image_path)
    # The following is a list containing all the figure names
    time_elapsed = 0
    stdout = ''

    # We need to execute the code
    print('plotting %s' % fname)

    plt.close('all')
    cwd = os.getcwd()
    # Redirect output to stdout and
    orig_stdout = sys.stdout

    try:
        # First CD in the original example dir, so that any file
        # created by the example get created in this directory
        os.chdir(os.path.dirname(src_file))
        my_globals = {'pl': plt, '__name__': 'gallery'}
        my_buffer = StringIO()
        my_stdout = Tee(sys.stdout, my_buffer)
        sys.stdout = my_stdout

        t0 = time()
        exec(code_block, my_globals)
        time_elapsed = time() - t0

        sys.stdout = orig_stdout

        my_stdout = my_buffer.getvalue().strip().expandtabs()
        if my_stdout:
            stdout = CODE_OUTPUT.format(my_stdout.replace('\n', '\n    '))
        os.chdir(cwd)
        figure_list = save_figures(image_path)

        # Depending on whether we have one or more figures, we're using a
        # horizontal list or a single rst call to 'image'.
        if len(figure_list) == 1:
            figure_name = figure_list[0]
            image_list = SINGLE_IMAGE % figure_name.lstrip('/')
        else:
            image_list = HLIST_HEADER
            for figure_name in figure_list:
                image_list += HLIST_IMAGE_TEMPLATE % figure_name.lstrip('/')

    except:
        image_list = '%s is not compiling:' % fname
        print(80 * '_')
        print(image_list)
        traceback.print_exc()
        print(80 * '_')
    finally:
        os.chdir(cwd)
        sys.stdout = orig_stdout

    print(" - time elapsed : %.2g sec" % time_elapsed)

    return image_list, time_elapsed, stdout


def save_figures(image_path):
    figure_list = []
    # In order to save every figure we have two solutions :
    # * iterate from 1 to infinity and call plt.fignum_exists(n)
    #   (this requires the figures to be numbered
    #    incrementally: 1, 2, 3 and not 1, 2, 5)
    # * iterate over [fig_mngr.num for fig_mngr in
    #   matplotlib._pylab_helpers.Gcf.get_all_fig_managers()]

    fig_managers = matplotlib._pylab_helpers.Gcf.get_all_fig_managers()
    for fig_mngr in fig_managers:
        # Set the fig_num figure as the current figure as we can't
        # save a figure that's not the current figure.
        fig = plt.figure(fig_mngr.num)
        kwargs = {}
        to_rgba = matplotlib.colors.colorConverter.to_rgba
        for attr in ['facecolor', 'edgecolor']:
            fig_attr = getattr(fig, 'get_' + attr)()
            default_attr = matplotlib.rcParams['figure.' + attr]
            if to_rgba(fig_attr) != to_rgba(default_attr):
                kwargs[attr] = fig_attr

        current_fig = image_path.format(fig_mngr.num)
        fig.savefig(current_fig, **kwargs)
        figure_list.append(current_fig)
    return figure_list


def _plots_are_current(src_file, image_file):
    first_image_file = image_file.format(1)
    needs_replot = (not os.path.exists(first_image_file) or
               os.stat(first_image_file).st_mtime <= os.stat(src_file).st_mtime)
    return not needs_replot


def codestr2rst(codestr):
    """Return reStructuredText code block from code string"""
    code_directive = "\n.. code-block:: python\n\n"
    indented_block = '\t' + codestr.replace('\n', '\n\t')
    return code_directive + indented_block


def generate_file_rst(fname, target_dir, src_dir, plot_gallery):
    """ Generate the rst file for a given example."""

    this_template = RST_TEMPLATE
    short_fname = target_dir.replace(os.path.sep, '_') + '_' + fname
    src_file = os.path.join(src_dir, fname)
    example_file = os.path.join(target_dir, fname)
    shutil.copyfile(src_file, example_file)

    base_image_name = os.path.splitext(fname)[0]
    image_fname = 'sphx_glr_' + base_image_name + '_{0:03}.png'

    image_dir = os.path.join(target_dir, 'images')
    image_path = os.path.join(image_dir, image_fname)
    thumb_dir = os.path.join(image_dir, 'thumb')
    thumb_file = os.path.join(thumb_dir, 'sphx_glr_%s_thumb.png' % base_image_name)
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    if not os.path.exists(thumb_dir):
        os.makedirs(thumb_dir)

    if _plots_are_current(src_file, image_path):
        return

    time_elapsed = 0
#    docstring, short_desc, end_row = extract_docstring(example_file)
    script_blocks = split_code_and_text_blocks(example_file)
    docstring = eval(script_blocks[0][2])
    coderst = codestr2rst(script_blocks[1][2])

    if plot_gallery and fname.startswith('plot'):
        # generate the plot as png image if file name
        # starts with plot and if it is more recent than an
        # existing image.
        image_list, time_elapsed, stdout = execute_script(image_path,
                                                          src_file, fname,
                                                          script_blocks[1][2])
        this_template += PLOT_OUT_TEMPLATE


    # generate thumb file
    first_image_file = image_path.format(1)
    if os.path.exists(first_image_file):
        scale_image(first_image_file, thumb_file, 400, 280)
    elif not os.path.exists(thumb_file):
        # create something to replace the thumbnail
        scale_image(os.path.join(glr_path_static(), 'no_image.png'),
                    thumb_file, 200, 140)


    time_m, time_s = divmod(time_elapsed, 60)
    f = open(os.path.join(target_dir, base_image_name + '.rst'), 'w')
    this_template += CODE_DOWNLOAD + coderst
    f.write(this_template % locals())
    f.flush()
