# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
RST file generator
==================

Generate the rst files for the examples by iterating over the python
example files.

Files that generate images should start with 'plot'

"""
# Don't use unicode_literals here (be explicit with u"..." instead) otherwise
# tricky errors come up with exec(code_blocks, ...) calls
from __future__ import division, print_function, absolute_import
from time import time
import codecs
import glob
import hashlib
import os
import re
import shutil
import subprocess
import sys
import traceback
import warnings


# Try Python 2 first, otherwise load from Python 3
try:
    # textwrap indent only exists in python 3
    from textwrap import indent
except ImportError:
    def indent(text, prefix, predicate=None):
        """Adds 'prefix' to the beginning of selected lines in 'text'.

        If 'predicate' is provided, 'prefix' will only be added to the lines
        where 'predicate(line)' is True. If 'predicate' is not provided,
        it will default to adding 'prefix' to all non-empty lines that do not
        consist solely of whitespace characters.
        """
        if predicate is None:
            def predicate(line):
                return line.strip()

        def prefixed_lines():
            for line in text.splitlines(True):
                yield (prefix + line if predicate(line) else line)
        return ''.join(prefixed_lines())

from io import StringIO

try:
    # make sure that the Agg backend is set before importing any
    # matplotlib
    import matplotlib
    matplotlib.use('agg')
    matplotlib_backend = matplotlib.get_backend()

    if matplotlib_backend != 'agg':
        mpl_backend_msg = (
            "Sphinx-Gallery relies on the matplotlib 'agg' backend to "
            "render figures and write them to files. You are "
            "currently using the {} backend. Sphinx-Gallery will "
            "terminate the build now, because changing backends is "
            "not well supported by matplotlib. We advise you to move "
            "sphinx_gallery imports before any matplotlib-dependent "
            "import. Moving sphinx_gallery imports at the top of "
            "your conf.py file should fix this issue")

        raise ValueError(mpl_backend_msg.format(matplotlib_backend))

    import matplotlib.pyplot as plt
except ImportError:
    # this script can be imported by nosetest to find tests to run: we should
    # not impose the matplotlib requirement in that case.
    pass

from . import glr_path_static
from .backreferences import write_backreferences, _thumbnail_div
from .downloads import CODE_DOWNLOAD
from .py_source_parser import (get_docstring_and_rest,
                               split_code_and_text_blocks)

from .notebook import jupyter_notebook, save_notebook

try:
    basestring
except NameError:
    basestring = str
    unicode = str


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

    # When called from a local terminal seaborn needs it in Python3
    def isatty(self):
        self.file1.isatty()


class MixedEncodingStringIO(StringIO):
    """Helper when both ASCII and unicode strings will be written"""

    def write(self, data):
        if not isinstance(data, unicode):
            data = data.decode('utf-8')
        StringIO.write(self, data)


###############################################################################
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


# This one could contain unicode
CODE_OUTPUT = u""".. rst-class:: sphx-glr-script-out

 Out::

{0}\n"""


SPHX_GLR_SIG = """\n.. rst-class:: sphx-glr-signature

    `Generated by Sphinx-Gallery <http://sphinx-gallery.readthedocs.io>`_\n"""


def codestr2rst(codestr, lang='python'):
    """Return reStructuredText code block from code string"""
    code_directive = "\n.. code-block:: {0}\n\n".format(lang)
    indented_block = indent(codestr, ' ' * 4)
    return code_directive + indented_block


def extract_thumbnail_number(text):
    """ Pull out the thumbnail image number specified in the docstring. """

    # check whether the user has specified a specific thumbnail image
    pattr = re.compile(
        r"^\s*#\s*sphinx_gallery_thumbnail_number\s*=\s*([0-9]+)\s*$",
        flags=re.MULTILINE)
    match = pattr.search(text)

    if match is None:
        # by default, use the first figure created
        thumbnail_number = 1
    else:
        thumbnail_number = int(match.groups()[0])

    return thumbnail_number


def extract_intro(filename):
    """ Extract the first paragraph of module-level docstring. max:95 char"""

    docstring, _ = get_docstring_and_rest(filename)

    # lstrip is just in case docstring has a '\n\n' at the beginning
    paragraphs = docstring.lstrip().split('\n\n')
    if len(paragraphs) > 1:
        first_paragraph = re.sub('\n', ' ', paragraphs[1])
        first_paragraph = (first_paragraph[:95] + '...'
                           if len(first_paragraph) > 95 else first_paragraph)
    else:
        raise ValueError(
            "Example docstring should have a header for the example title "
            "and at least a paragraph explaining what the example is about. "
            "Please check the example file:\n {}\n".format(filename))

    return first_paragraph


def get_md5sum(src_file):
    """Returns md5sum of file"""

    with open(src_file, 'rb') as src_data:
        src_content = src_data.read()

        src_md5 = hashlib.md5(src_content).hexdigest()
    return src_md5


def md5sum_is_current(src_file):
    """Checks whether src_file has the same md5 hash as the one on disk"""

    src_md5 = get_md5sum(src_file)

    src_md5_file = src_file + '.md5'
    if os.path.exists(src_md5_file):
        with open(src_md5_file, 'r') as file_checksum:
            ref_md5 = file_checksum.read()

        return src_md5 == ref_md5

    return False


def save_figures(image_path, execution_path, fig_count, gallery_conf):
    """Save all open matplotlib figures of the example code-block

    Parameters
    ----------
    image_path : str
        Path where plots are saved (format string which accepts figure number)
    execution_path : str
        Path where the example script was executed.
    fig_count : int
        Previous figure number count. Figure number add from this number
    gallery_conf : dict
        Contains the configuration of Sphinx-Gallery
    Returns
    -------
    images_rst : str
        rst code to embed the images in the document
    fig_num : int
        number of figures saved
    """
    figure_list = []

    for fig_num in plt.get_fignums():
        # Set the fig_num figure as the current figure as we can't
        # save a figure that's not the current figure.
        fig = plt.figure(fig_num)
        kwargs = {}
        to_rgba = matplotlib.colors.colorConverter.to_rgba
        for attr in ['facecolor', 'edgecolor']:
            fig_attr = getattr(fig, 'get_' + attr)()
            default_attr = matplotlib.rcParams['figure.' + attr]
            if to_rgba(fig_attr) != to_rgba(default_attr):
                kwargs[attr] = fig_attr

        current_fig = image_path.format(fig_count + fig_num)
        fig.savefig(current_fig, **kwargs)
        figure_list.append(current_fig)

    if gallery_conf.get('find_mayavi_figures', False):
        from mayavi import mlab
        e = mlab.get_engine()
        last_matplotlib_fig_num = fig_count + len(figure_list)
        total_fig_num = last_matplotlib_fig_num + len(e.scenes)
        mayavi_fig_nums = range(last_matplotlib_fig_num + 1, total_fig_num + 1)

        for scene, mayavi_fig_num in zip(e.scenes, mayavi_fig_nums):
            current_fig = image_path.format(mayavi_fig_num)
            mlab.savefig(current_fig, figure=scene)
            # make sure the image is not too large
            scale_image(current_fig, current_fig, 850, 999)
            figure_list.append(current_fig)
        mlab.close(all=True)

    if gallery_conf.get('find_saved_figures', False):
        png_paths = glob.glob(os.sep.join([execution_path, '*.png']))
        cur_count = len(figure_list)
        for fig_num, path in enumerate(png_paths, start=1):
            current_fig = image_path.format(fig_count + fig_num + cur_count)
            shutil.move(path, current_fig)
            figure_list.append(current_fig)

    return figure_rst(figure_list, gallery_conf['src_dir'])


def figure_rst(figure_list, sources_dir):
    """Given a list of paths to figures generate the corresponding rst

    Depending on whether we have one or more figures, we use a
    single rst call to 'image' or a horizontal list.

    Parameters
    ----------
    figure_list : list of str
        Strings are the figures' absolute paths
    sources_dir : str
        absolute path of Sphinx documentation sources

    Returns
    -------
    images_rst : str
        rst code to embed the images in the document
    fig_num : int
        number of figures saved
    """

    figure_paths = [os.path.relpath(figure_path, sources_dir)
                    for figure_path in figure_list]
    figure_paths = [figure_name.replace(os.sep, '/').lstrip('/')
                    for figure_name in figure_list]
    images_rst = ""
    if len(figure_paths) == 1:
        figure_name = figure_paths[0]
        images_rst = SINGLE_IMAGE % figure_name
    elif len(figure_paths) > 1:
        images_rst = HLIST_HEADER
        for figure_name in figure_paths:
            images_rst += HLIST_IMAGE_TEMPLATE % figure_name

    return images_rst, len(figure_list)


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


def save_thumbnail(image_path_template, src_file, gallery_conf):
    """Save the thumbnail image"""
    # read specification of the figure to display as thumbnail from main text
    _, content = get_docstring_and_rest(src_file)
    thumbnail_number = extract_thumbnail_number(content)
    thumbnail_image_path = image_path_template.format(thumbnail_number)

    thumb_dir = os.path.join(os.path.dirname(thumbnail_image_path), 'thumb')
    if not os.path.exists(thumb_dir):
        os.makedirs(thumb_dir)

    base_image_name = os.path.splitext(os.path.basename(src_file))[0]
    thumb_file = os.path.join(thumb_dir,
                              'sphx_glr_%s_thumb.png' % base_image_name)

    if src_file in gallery_conf['failing_examples']:
        broken_img = os.path.join(glr_path_static(), 'broken_example.png')
        scale_image(broken_img, thumb_file, 200, 140)

    elif os.path.exists(thumbnail_image_path):
        scale_image(thumbnail_image_path, thumb_file, 400, 280)

    elif not os.path.exists(thumb_file):
        # create something to replace the thumbnail
        default_thumb_file = os.path.join(glr_path_static(), 'no_image.png')
        default_thumb_file = gallery_conf.get("default_thumb_file",
                                              default_thumb_file)
        scale_image(default_thumb_file, thumb_file, 200, 140)


def generate_dir_rst(src_dir, target_dir, gallery_conf, seen_backrefs):
    """Generate the gallery reStructuredText for an example directory"""
    if not os.path.exists(os.path.join(src_dir, 'README.txt')):
        print(80 * '_')
        print('Example directory %s does not have a README.txt file' %
              src_dir)
        print('Skipping this directory')
        print(80 * '_')
        return "", []  # because string is an expected return type

    with open(os.path.join(src_dir, 'README.txt')) as fid:
        fhindex = fid.read()
    # Add empty lines to avoid bug in issue #165
    fhindex += "\n\n"

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    sorted_listdir = [fname for fname in sorted(os.listdir(src_dir))
                      if fname.endswith('.py')]
    entries_text = []
    computation_times = []
    build_target_dir = os.path.relpath(target_dir, gallery_conf['src_dir'])
    for fname in sorted_listdir:
        amount_of_code, time_elapsed = \
            generate_file_rst(fname, target_dir, src_dir, gallery_conf)
        computation_times.append((time_elapsed, fname))
        new_fname = os.path.join(src_dir, fname)
        intro = extract_intro(new_fname)
        this_entry = _thumbnail_div(build_target_dir, fname, intro) + """

.. toctree::
   :hidden:

   /%s\n""" % os.path.join(build_target_dir, fname[:-3]).replace(os.sep, '/')
        entries_text.append((amount_of_code, this_entry))

        if gallery_conf['backreferences_dir']:
            write_backreferences(seen_backrefs, gallery_conf,
                                 target_dir, fname, intro)

    # sort to have the smallest entries in the beginning
    entries_text.sort()

    for _, entry_text in entries_text:
        fhindex += entry_text

    # clear at the end of the section
    fhindex += """.. raw:: html\n
    <div style='clear:both'></div>\n\n"""

    return fhindex, computation_times


def execute_code_block(code_block, example_globals,
                       block_vars, gallery_conf):
    """Executes the code block of the example file"""
    time_elapsed = 0
    stdout = ''

    # If example is not suitable to run, skip executing its blocks
    if not block_vars['execute_script']:
        return stdout, time_elapsed

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

        t_start = time()
        # don't use unicode_literals at the top of this file or you get
        # nasty errors here on Py2.7
        exec(code_block, example_globals)
        time_elapsed = time() - t_start

        sys.stdout = orig_stdout

        my_stdout = my_buffer.getvalue().strip().expandtabs()
        # raise RuntimeError
        if my_stdout:
            stdout = CODE_OUTPUT.format(indent(my_stdout, u' ' * 4))
        os.chdir(cwd)
        images_rst, fig_num = save_figures(
            block_vars['image_path'],
            os.path.dirname(src_file),
            block_vars['fig_count'],
            gallery_conf)

    except Exception:
        formatted_exception = traceback.format_exc()

        fail_example_warning = 80 * '_' + '\n' + \
            '%s failed to execute correctly:' % src_file + \
            formatted_exception + 80 * '_' + '\n'
        warnings.warn(fail_example_warning)

        fig_num = 0
        images_rst = codestr2rst(formatted_exception, lang='pytb')

        # Breaks build on first example error
        # XXX This check can break during testing e.g. if you uncomment the
        # `raise RuntimeError` by the `my_stdout` call, maybe use `.get()`?
        if gallery_conf['abort_on_example_error']:
            raise
        # Stores failing file
        gallery_conf['failing_examples'][src_file] = formatted_exception
        block_vars['execute_script'] = False

    finally:
        os.chdir(cwd)
        sys.stdout = orig_stdout

    code_output = u"\n{0}\n\n{1}\n\n".format(images_rst, stdout)
    block_vars['fig_count'] += fig_num

    return code_output, time_elapsed


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


def generate_file_rst(fname, target_dir, src_dir, gallery_conf):
    """Generate the rst file for a given example.

    Returns
    -------
    amount_of_code : int
        character count of the corresponding python script in file
    time_elapsed : float
        seconds required to run the script
    """

    src_file = os.path.normpath(os.path.join(src_dir, fname))
    example_file = os.path.join(target_dir, fname)
    shutil.copyfile(src_file, example_file)
    script_blocks = split_code_and_text_blocks(src_file)
    amount_of_code = sum([len(bcontent)
                          for blabel, bcontent in script_blocks
                          if blabel == 'code'])

    if md5sum_is_current(example_file):
        return amount_of_code, 0

    image_dir = os.path.join(target_dir, 'images')
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    base_image_name = os.path.splitext(fname)[0]
    image_fname = 'sphx_glr_' + base_image_name + '_{0:03}.png'
    build_image_dir = os.path.relpath(image_dir, gallery_conf['src_dir'])
    image_path_template = os.path.join(image_dir, image_fname)

    ref_fname = os.path.relpath(example_file, gallery_conf['src_dir'])
    ref_fname = ref_fname.replace(os.path.sep, '_')
    example_rst = """\n\n.. _sphx_glr_{0}:\n\n""".format(ref_fname)

    filename_pattern = gallery_conf.get('filename_pattern')
    execute_script = re.search(filename_pattern, src_file) and gallery_conf[
        'plot_gallery']
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

    # A simple example has two blocks: one for the
    # example introduction/explanation and one for the code
    is_example_notebook_like = len(script_blocks) > 2
    time_elapsed = 0
    block_vars = {'execute_script': execute_script, 'fig_count': 0,
                  'image_path': image_path_template, 'src_file': src_file}
    if block_vars['execute_script']:
        print('Executing file %s' % src_file)
    for blabel, bcontent in script_blocks:
        if blabel == 'code':
            code_output, rtime = execute_code_block(bcontent,
                                                    example_globals,
                                                    block_vars,
                                                    gallery_conf)

            time_elapsed += rtime

            if is_example_notebook_like:
                example_rst += codestr2rst(bcontent) + '\n'
                example_rst += code_output
            else:
                example_rst += code_output
                if 'sphx-glr-script-out' in code_output:
                    # Add some vertical space after output
                    example_rst += "\n\n|\n\n"
                example_rst += codestr2rst(bcontent) + '\n'

        else:
            example_rst += bcontent + '\n\n'

    clean_modules()

    # Writes md5 checksum if example has build correctly
    # not failed and was initially meant to run(no-plot shall not cache md5sum)
    if block_vars['execute_script']:
        with open(example_file + '.md5', 'w') as file_checksum:
            file_checksum.write(get_md5sum(example_file))

    save_thumbnail(image_path_template, src_file, gallery_conf)

    time_m, time_s = divmod(time_elapsed, 60)
    example_nb = jupyter_notebook(script_blocks)
    save_notebook(example_nb, example_file.replace('.py', '.ipynb'))
    with codecs.open(os.path.join(target_dir, base_image_name + '.rst'),
                     mode='w', encoding='utf-8') as f:
        example_rst += "**Total running time of the script:**" \
                       " ({0: .0f} minutes {1: .3f} seconds)\n\n".format(
                           time_m, time_s)
        example_rst += CODE_DOWNLOAD.format(fname,
                                            fname.replace('.py', '.ipynb'))
        example_rst += SPHX_GLR_SIG
        f.write(example_rst)

    if block_vars['execute_script']:
        print("{0} ran in : {1:.2g} seconds\n".format(src_file, time_elapsed))

    return amount_of_code, time_elapsed
