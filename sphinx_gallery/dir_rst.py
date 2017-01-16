# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
==================
Directory scanner
==================

Scans a directory for files to generate rst and generate them using functions
from gen_rst

Files that generate images should start with 'plot'

"""
import os
from .backreferences import write_backreferences, _thumbnail_div
from .gen_rst import extract_intro, generate_file_rst

# TODO
def generate_dir_rst(src_dir, target_dir, gallery_conf, seen_backrefs):
    """Generate the gallery reStructuredText for an example directory."""
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
