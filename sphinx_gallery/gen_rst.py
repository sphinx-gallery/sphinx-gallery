# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
==================
RST file generator
==================

Generate the rst files for a single example file.

Files that generate images should start with 'plot'

"""
# Don't use unicode_literals here (be explicit with u"..." instead) otherwise
# tricky errors come up with exec(code_blocks, ...) calls
from __future__ import absolute_import, division, print_function
import codecs
import hashlib
import os
import re
import shutil


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
from .source_parser import get_docstring_and_rest, split_code_and_text_blocks
from .notebook import jupyter_notebook, save_notebook
from .write_rst import rst_notebook
from .save_images import scale_image
from .execute_blocks import execute_script_blocks


def _extract_thumbnail_number(text):
    """Pull out the thumbnail image number specified in the docstring."""
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


def _get_md5sum(src_file):
    """Return md5sum of file."""
    with open(src_file, 'rb') as src_data:
        src_content = src_data.read()

        src_md5 = hashlib.md5(src_content).hexdigest()
    return src_md5


def _md5sum_is_current(src_file):
    """Check whether src_file has the same md5 hash as the one on disk."""
    src_md5 = _get_md5sum(src_file)

    src_md5_file = src_file + '.md5'
    if os.path.exists(src_md5_file):
        with open(src_md5_file, 'r') as file_checksum:
            ref_md5 = file_checksum.read()

        return src_md5 == ref_md5

    return False


def _save_thumbnail(image_path_template, src_file, gallery_conf):
    """Save the thumbnail image."""
    # read specification of the figure to display as thumbnail from main text
    _, content = get_docstring_and_rest(src_file)
    thumbnail_number = _extract_thumbnail_number(content)
    thumbnail_image_path = image_path_template.format(thumbnail_number)

    # Create thumbnail dir if it doesn't exist
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


def _prepare_execution_env(fname, target_dir, src_dir, gallery_conf,
                           lang='python'):
    """Prepare execution environment for given file and config."""
    # Create images dir if it doesn't exist
    image_dir = os.path.join(target_dir, 'images')
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # Create image template to be formated
    base_image_name = os.path.splitext(fname)[0]
    image_fname = 'sphx_glr_' + base_image_name + '_{0:03}.png'
    image_path_template = os.path.join(image_dir, image_fname)

    # Check if current file has to be executed
    src_file = os.path.join(src_dir, fname)
    filename_pattern = gallery_conf.get('filename_pattern')
    execute_script = (re.search(filename_pattern, src_file) and
                      gallery_conf['plot_gallery'] and
                      lang == 'python')

    return {'execute_script': execute_script,
            'fig_count': 0,
            'image_path': image_path_template,
            'src_file': src_file,
            'lang': lang}


def extract_intro(filename, lang='python'):
    """Extract the first paragraph of module-level docstring. max:95 char."""
    docstring, _ = get_docstring_and_rest(filename, lang)

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


def generate_file_rst(fname, target_dir, src_dir, gallery_conf, lang='python'):
    """Generate the rst file for a given example.

    Returns
    -------
    amount_of_code : int
        character count of the corresponding python script in file
    time_elapsed : float
        seconds required to run the script
    """
    # Copy source file to target directory
    src_file = os.path.normpath(os.path.join(src_dir, fname))
    example_file = os.path.join(target_dir, fname)
    shutil.copyfile(src_file, example_file)

    # Parse source file
    script_blocks = split_code_and_text_blocks(src_file, lang)
    amount_of_code = sum([len(bcontent) for blabel, bcontent in script_blocks
                          if blabel == 'code'])

    # Skip the execution if md5 matches
    if _md5sum_is_current(example_file):
        return amount_of_code, 0

    # Prepare environment and execute the code
    block_vars = _prepare_execution_env(fname, target_dir, src_dir,
                                        gallery_conf, lang)
    if block_vars['execute_script']:
        print('Executing file %s' % src_file)

    executed_blocks, time_elapsed = execute_script_blocks(script_blocks,
                                                          block_vars,
                                                          gallery_conf)

    # Writes md5 checksum if example has build correctly
    # not failed and was initially meant to run(no-plot shall not cache md5sum)
    if block_vars['execute_script']:
        with open(example_file + '.md5', 'w') as file_checksum:
            file_checksum.write(_get_md5sum(example_file))

    _save_thumbnail(block_vars["image_path"], src_file, gallery_conf)

    # Generate RST and save it
    write_fname = os.path.relpath(example_file, gallery_conf['src_dir'])
    rst_fname = os.path.splitext(example_file)[0] + '.rst'

    with codecs.open(rst_fname, mode='w', encoding='utf-8') as f:
        f.write(rst_notebook(executed_blocks, write_fname, time_elapsed, lang))

    # Create jupyter notebook only if language is python
    if lang == 'python':
        save_notebook(jupyter_notebook(script_blocks),
                      example_file.replace('.py', '.ipynb'))

    if block_vars['execute_script']:
        print("{0} ran in : {1:.2g} seconds\n".format(src_file, time_elapsed))

    return amount_of_code, time_elapsed
