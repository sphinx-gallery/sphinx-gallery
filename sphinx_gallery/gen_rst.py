# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
==================
RST file generator
==================

Generate the rst files for the examples by iterating over the python
example files.

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
from .backreferences import write_backreferences, _thumbnail_div
from .source_parser import get_docstring_and_rest, split_code_and_text_blocks
from .notebook import jupyter_notebook, save_notebook
from .write_rst import rst_notebook
from .save_images import scale_image
from .execute_blocks import execute_script_blocks

# TODO lua/else
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


def extract_intro(filename, lang='python'):
    """ Extract the first paragraph of module-level docstring. max:95 char"""

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
        write_backreferences(seen_backrefs, gallery_conf,
                             target_dir, fname, intro)
        this_entry = _thumbnail_div(build_target_dir, fname, intro) + """

.. toctree::
   :hidden:

   /%s/%s\n""" % (build_target_dir, fname[:-3])
        entries_text.append((amount_of_code, this_entry))

    # sort to have the smallest entries in the beginning
    entries_text.sort()

    fhindex = gallery_rst(src_dir, entries_text)

    return fhindex, computation_times


def gallery_rst(src_dir, entries_text):
    """Generates the rst text of a gallery given the entries

    Parameters
    ----------
    src_dir : path to the gallery sources
    entries_text : list of 2-tuples
        tuples contain the amount_of_code of the example
        and the thumbnail div element

    Returns:
    str : Content of the gallery
    """

    with open(os.path.join(src_dir, 'README.txt')) as fid:
        fhindex = fid.read()
    # Add empty lines to avoid bug in issue #165
    fhindex += "\n\n"

    for _, entry_text in entries_text:
        fhindex += entry_text

    # clear at the end of the section
    fhindex += """.. raw:: html\n
    <div style='clear:both'></div>\n\n"""

    return fhindex


def prepare_execution_env(fname, target_dir, src_dir, gallery_conf, lang='python'):
    image_dir = os.path.join(target_dir, 'images')
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    base_image_name = os.path.splitext(fname)[0]
    image_fname = 'sphx_glr_' + base_image_name + '_{0:03}.png'
    image_path_template = os.path.join(image_dir, image_fname)

    src_file = os.path.normpath(os.path.join(src_dir, fname))
    filename_pattern = gallery_conf.get('filename_pattern')
    execute_script = re.search(filename_pattern, src_file) and gallery_conf[
        'plot_gallery'] and lang == 'python'
    return {'execute_script': execute_script, 'fig_count': 0,
            'image_path': image_path_template, 'src_file': src_file}


def generate_file_rst(fname, target_dir, src_dir, gallery_conf, lang='python'):
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
    script_blocks = split_code_and_text_blocks(src_file, lang)
    amount_of_code = sum([len(bcontent)
                          for blabel, bcontent in script_blocks
                          if blabel == 'code'])

    if md5sum_is_current(example_file):
        return amount_of_code, 0

    block_vars = prepare_execution_env(
        fname, target_dir, src_dir, gallery_conf, lang)
    if block_vars['execute_script']:
        print('Executing file %s' % src_file)
    executed_blocks, time_elapsed = execute_script_blocks(
        script_blocks, block_vars, gallery_conf)

    # Writes md5 checksum if example has build correctly
    # not failed and was initially meant to run(no-plot shall not cache md5sum)
    if block_vars['execute_script']:
        with open(example_file + '.md5', 'w') as file_checksum:
            file_checksum.write(get_md5sum(example_file))

    save_thumbnail(block_vars["image_path"], src_file, gallery_conf)
    write_fname = os.path.relpath(example_file, gallery_conf['src_dir'])
    rst_fname = os.path.splitext(example_file)[0] + '.rst'
    with codecs.open(rst_fname, mode='w', encoding='utf-8') as f:
        f.write(rst_notebook(executed_blocks, write_fname, time_elapsed, lang))

    if lang == 'python':
        save_notebook(jupyter_notebook(script_blocks),
                      example_file.replace('.py', '.ipynb'))

    if block_vars['execute_script']:
        print("{0} ran in : {1:.2g} seconds\n".format(src_file, time_elapsed))

    return amount_of_code, time_elapsed
