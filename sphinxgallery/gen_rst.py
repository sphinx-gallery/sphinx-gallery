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
import ast
import token
import tokenize
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
CODE_DOWNLOAD = """**Total running time of the script:**
({0:.0f} minutes {1:.3f} seconds)\n\n
\n**Download Python source code:** :download:`{2} <{2}>`\n"""

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


def split_code_and_text_blocks(source_file):
    """Return list with source file separated into code and text blocks.

    Returns
    -------
    blocks : list of (label, content)
        List where each element is a tuple with the label ('text' or 'code'),
        and content string of block.
    """

    with open(source_file) as f:
        source_lines = f.read()

    doc_string = ast.get_docstring(ast.parse(source_lines))

    blocks = [('text', doc_string)]
    # Remove from source_lines the docstring
    end_doc = [m.end() for m in re.finditer('"""', source_lines)][1]
    source_lines = source_lines[end_doc:]

    blocks.append(('code', source_lines))

    blocks = [s for s in blocks if s[-1].strip() != '']
    newblocks = []
    for block_label, content in blocks:
        if block_label == 'text':
            newblocks.append(('text', content))
        if block_label == 'code':
            pattern = re.compile('^#{20,}.*\s((?:^#.*\s)*)', flags=re.M)
            split_block = re.split(pattern, content)
            for split_code_block in split_block:
                if split_code_block is None or split_code_block.strip() == '':
                    continue
                elif split_code_block.startswith('#'):
                    sub_pat = re.compile('^# |^#', flags=re.M)
                    coment_block = re.sub(sub_pat, '', split_code_block)
                    newblocks.append(('text', coment_block))
                else:
                    newblocks.append(('code', split_code_block))
    return newblocks


def codestr2rst(codestr):
    """Return reStructuredText code block from code string"""
    code_directive = "\n.. code-block:: python\n\n"
    indented_block = '    ' + codestr.replace('\n', '\n    ')
    return code_directive + indented_block


def text2string(content):
    """Returns a string without the extra triple quotes"""
    try:
        return ast.literal_eval(content)+'\n'
    except:
        return content


def extract_intro(filename):
    """ Extract the first paragraph of module-level docstring. max:95 char"""

    first_text = split_code_and_text_blocks(filename)[0][-1]

    paragraphs = first_text.split('\n\n')
    if len(first_text) > 1:
        first_par = re.sub('\n', ' ', paragraphs[1])
        first_par = ((first_par[:95] + '...')
                     if len(first_par) > 95 else first_par)
    else:
        raise ValueError("Missing first paragraph."
                         "Please check the layout of your"
                         " example file:\n {}\n and make sure"
                         " it's correct.".format(filename))

    return first_par


def _plots_are_current(src_file, image_file):
    """Test existence of image file and later touch time to source script"""

    first_image_file = image_file.format(1)
    needs_replot = (not os.path.exists(first_image_file) or
              os.stat(first_image_file).st_mtime <= os.stat(src_file).st_mtime)
    return not needs_replot


def save_figures(image_path, fig_count):
    """Save all open matplotlib figures of the example code-block

    Parameters
    ----------
    image_path : str
        Path where plots are saved (format string which accepts figure number)
    fig_count : int
        Previous figure number count. Figure number add from this number

    Returns
    -------
    list of strings containing the full path to each figure
    """
    figure_list = []

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

        current_fig = image_path.format(fig_count + fig_mngr.num)
        fig.savefig(current_fig, **kwargs)
        figure_list.append(current_fig)
    return figure_list


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


def save_thumbnail(image_path, base_image_name):
    """Save the thumbnail image"""
    first_image_file = image_path.format(1)
    thumb_dir = os.path.join(os.path.dirname(first_image_file), 'thumb')
    if not os.path.exists(thumb_dir):
        os.makedirs(thumb_dir)

    thumb_file = os.path.join(thumb_dir,
                              'sphx_glr_%s_thumb.png' % base_image_name)

    if os.path.exists(first_image_file):
        scale_image(first_image_file, thumb_file, 400, 280)
    elif not os.path.exists(thumb_file):
        # create something to replace the thumbnail
        scale_image(os.path.join(glr_path_static(), 'no_image.png'),
                    thumb_file, 200, 140)


def generate_dir_rst(src_dir, target_dir, gallery_conf, seen_backrefs):
    """Generate the gallery reStructuredText for an example directory"""
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
    sorted_listdir = [fname for fname in sorted(os.listdir(src_dir))
                                if fname.endswith('py')]
    for fname in sorted_listdir:
        generate_file_rst(fname, target_dir, src_dir)
        new_fname = os.path.join(src_dir, fname)
        intro = extract_intro(new_fname)
        write_backreferences(seen_backrefs, gallery_conf,
                             target_dir, fname, intro)

        fhindex += _thumbnail_div(target_dir, fname, intro)
        fhindex += """

.. toctree::
   :hidden:

   /%s/%s\n""" % (target_dir, fname[:-3])


    # clear at the end of the section
    fhindex += """.. raw:: html\n
    <div style='clear:both'></div>\n\n"""

    return fhindex


def execute_script(code_block, example_globals, image_path, fig_count, src_file):
    """Executes the code block of the example file"""
    time_elapsed = 0
    stdout = ''

    # We need to execute the code
    print('plotting code blocks in %s' % src_file)

    plt.close('all')
    cwd = os.getcwd()
    # Redirect output to stdout and
    orig_stdout = sys.stdout

    try:
        # First cd in the original example dir, so that any file
        # created by the example get created in this directory
        os.chdir(os.path.dirname(src_file))
        my_buffer = StringIO()
        my_stdout = Tee(sys.stdout, my_buffer)
        sys.stdout = my_stdout

        t_start = time()
        exec(code_block, example_globals)
        time_elapsed = time() - t_start

        sys.stdout = orig_stdout

        my_stdout = my_buffer.getvalue().strip().expandtabs()
        if my_stdout:
            stdout = CODE_OUTPUT.format(my_stdout.replace('\n', '\n    '))
        os.chdir(cwd)
        figure_list = save_figures(image_path, fig_count)

        # Depending on whether we have one or more figures, we're using a
        # horizontal list or a single rst call to 'image'.
        if len(figure_list) == 1:
            figure_name = figure_list[0]
            image_list = SINGLE_IMAGE % figure_name.lstrip('/')
        else:
            image_list = HLIST_HEADER
            for figure_name in figure_list:
                image_list += HLIST_IMAGE_TEMPLATE % figure_name.lstrip('/')

    except Exception:
        image_list = '%s is not compiling:' % src_file
        print(80 * '_')
        print(image_list)
        traceback.print_exc()
        print(80 * '_')
    finally:
        os.chdir(cwd)
        sys.stdout = orig_stdout

    print(" - time elapsed : %.2g sec" % time_elapsed)
    code_output = "\n{0}\n\n{1}\n\n".format(image_list, stdout)

    return code_output, time_elapsed, fig_count + len(figure_list)


def generate_file_rst(fname, target_dir, src_dir):
    """ Generate the rst file for a given example."""

    src_file = os.path.join(src_dir, fname)
    example_file = os.path.join(target_dir, fname)
    shutil.copyfile(src_file, example_file)

    image_dir = os.path.join(target_dir, 'images')
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    base_image_name = os.path.splitext(fname)[0]
    image_fname = 'sphx_glr_' + base_image_name + '_{0:03}.png'
    image_path = os.path.join(image_dir, image_fname)

    if _plots_are_current(src_file, image_path):
        return

    time_elapsed = 0
    script_blocks = split_code_and_text_blocks(example_file)

    ref_fname = example_file.replace(os.path.sep, '_')
    example_rst = """\n\n.. _sphx_glr_{0}:\n\n""".format(ref_fname)

    if not fname.startswith('plot'):
        convert_func = dict(code=codestr2rst, text=text2string)
        for blabel, bcontent in script_blocks:
            example_rst += convert_func[blabel](bcontent)+'\n'
    else:
        example_globals = {}
        fig_count = 0
        for blabel, bcontent in script_blocks:
            if blabel == 'code':
                code_output, rtime, fig_count = execute_script(bcontent,
                                                               example_globals,
                                                               image_path,
                                                               fig_count,
                                                               src_file)

                time_elapsed += rtime
                # Single example style
                if len(script_blocks) == 2:
                    example_rst += code_output
                    example_rst += codestr2rst(bcontent)+'\n'
                # Notebook style
                else:
                    example_rst += codestr2rst(bcontent)+'\n'
                    example_rst += code_output
            else:
                example_rst += text2string(bcontent)+'\n'

    save_thumbnail(image_path, base_image_name)

    time_m, time_s = divmod(time_elapsed, 60)
    with open(os.path.join(target_dir, base_image_name + '.rst'), 'w') as f:
        example_rst += CODE_DOWNLOAD.format(time_m, time_s, fname)
        f.write(example_rst)
