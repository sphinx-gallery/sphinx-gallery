# -*- coding: utf-8 -*-
r"""
Parser for Jupyter notebooks
============================

Class that holds the Jupyter notebook information

"""
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import division, absolute_import, print_function
from functools import partial
import argparse
import json
import re
import sys
import copy
import os
import codecs

from .py_source_parser import split_code_and_text_blocks
from .utils import replace_py_ipynb


def jupyter_notebook_skeleton():
    """Returns a dictionary with the elements of a Jupyter notebook"""
    py_version = sys.version_info
    notebook_skeleton = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python " + str(py_version[0]),
                "language": "python",
                "name": "python" + str(py_version[0])
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": py_version[0]
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython" + str(py_version[0]),
                "version": '{0}.{1}.{2}'.format(*sys.version_info[:3])
            }
        },
        "nbformat": 4,
        "nbformat_minor": 0
    }
    return notebook_skeleton


def directive_fun(match, directive):
    """Helper to fill in directives"""
    directive_to_alert = dict(note="info", warning="danger")
    return ('<div class="alert alert-{0}"><h4>{1}</h4><p>{2}</p></div>'
            .format(directive_to_alert[directive], directive.capitalize(),
                    match.group(1).strip()))


def rst2md(text):
    """Converts the RST text from the examples docstrings and comments
    into markdown text for the Jupyter notebooks"""

    top_heading = re.compile(r'^=+$\s^([\w\s-]+)^=+$', flags=re.M)
    text = re.sub(top_heading, r'# \1', text)

    math_eq = re.compile(r'^\.\. math::((?:.+)?(?:\n+^  .+)*)', flags=re.M)
    text = re.sub(math_eq,
                  lambda match: r'\begin{{align}}{0}\end{{align}}'.format(
                      match.group(1).strip()),
                  text)
    inline_math = re.compile(r':math:`(.+?)`', re.DOTALL)
    text = re.sub(inline_math, r'$\1$', text)

    directives = ('warning', 'note')
    for directive in directives:
        directive_re = re.compile(r'^\.\. %s::((?:.+)?(?:\n+^  .+)*)'
                                  % directive, flags=re.M)
        text = re.sub(directive_re,
                      partial(directive_fun, directive=directive), text)

    links = re.compile(r'^ *\.\. _.*:.*$\n', flags=re.M)
    text = re.sub(links, '', text)

    refs = re.compile(r':ref:`')
    text = re.sub(refs, '`', text)

    contents = re.compile(r'^\s*\.\. contents::.*$(\n +:\S+: *$)*\n',
                          flags=re.M)
    text = re.sub(contents, '', text)

    images = re.compile(
        r'^\.\. image::(.*$)(?:\n *:alt:(.*$)\n)?(?: +:\S+:.*$\n)*',
        flags=re.M)
    text = re.sub(
        images, lambda match: '![{1}]({0})\n'.format(
            match.group(1).strip(), (match.group(2) or '').strip()), text)

    return text


def jupyter_notebook(script_blocks, gallery_conf):
    """Generate a Jupyter notebook file cell-by-cell

    Parameters
    ----------
    script_blocks : list
        Script execution cells.
    gallery_conf : dict
        The sphinx-gallery configuration dictionary.
    """
    first_cell = gallery_conf.get("first_notebook_cell", "%matplotlib inline")
    work_notebook = jupyter_notebook_skeleton()
    add_code_cell(work_notebook, first_cell)
    fill_notebook(work_notebook, script_blocks)

    return work_notebook


def add_code_cell(work_notebook, code):
    """Add a code cell to the notebook

    Parameters
    ----------
    code : str
        Cell content
    """

    code_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {"collapsed": False},
        "outputs": [],
        "source": [code.strip()]
    }
    work_notebook["cells"].append(code_cell)


def add_markdown_cell(work_notebook, text):
    """Add a markdown cell to the notebook

    Parameters
    ----------
    code : str
        Cell content
    """
    markdown_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [rst2md(text)]
    }
    work_notebook["cells"].append(markdown_cell)


def fill_notebook(work_notebook, script_blocks):
    """Writes the Jupyter notebook cells

    Parameters
    ----------
    script_blocks : list of tuples
    """

    for blabel, bcontent, lineno in script_blocks:
        if blabel == 'code':
            add_code_cell(work_notebook, bcontent)
        else:
            add_markdown_cell(work_notebook, bcontent + '\n')


def save_notebook(work_notebook, write_file):
    """Saves the Jupyter work_notebook to write_file"""
    with open(write_file, 'w') as out_nb:
        json.dump(work_notebook, out_nb, indent=2)


###############################################################################
# Notebook shell utility

def python_to_jupyter_cli(args=None, namespace=None):
    """Exposes the jupyter notebook renderer to the command line

    Takes the same arguments as ArgumentParser.parse_args
    """
    from . import gen_gallery  # To avoid circular import
    parser = argparse.ArgumentParser(
        description='Sphinx-Gallery Notebook converter')
    parser.add_argument('python_src_file', nargs='+',
                        help='Input Python file script to convert. '
                        'Supports multiple files and shell wildcards'
                        ' (e.g. *.py)')
    args = parser.parse_args(args, namespace)

    for src_file in args.python_src_file:
        file_conf, blocks = split_code_and_text_blocks(src_file)
        print('Converting {0}'.format(src_file))
        gallery_conf = copy.deepcopy(gen_gallery.DEFAULT_GALLERY_CONF)
        example_nb = jupyter_notebook(blocks, gallery_conf)
        save_notebook(example_nb, replace_py_ipynb(src_file))


###############################################################################
# Notebook-to-SG Python utility

def convert_ipynb_to_gallery(path_ipynb, folder_out=None):
    """Convert a Jupyter Notebook to a Sphinx-Gallery Python script.

    This is a (somewhat hacky) helper function to enable an
    .ipynb -> .py -> rst conversion within the Sphinx-Gallery workflow. It
    uses Pandoc to convert Jupyter Notebook markdown into a collection of
    Python and rST comment blocks.

    Parameters
    ----------
    path_ipynb : str
        Path to a Jupyter Notebook
    folder_out : str
        Path to an output folder where generated Python files will be placed.

    Outputs
    -------
    path_out : str
        Path to the output Python file.
    """
    try:
        import pypandoc as pdoc
    except ImportError:
        raise ImportError("ipynb to py conversion requires pandoc and pypandoc. "
                          "Please install them and re-run the function.")
    if folder_out is None:
        folder_out = os.path.dirname(path_ipynb)

    # Load the Jupyter Notebook and iterate through a list of its cells
    nb_dict = json.load(codecs.open(path_ipynb, encoding='utf-8'))
    cells = nb_dict['cells']
    python_file = ""
    for ii, cell in enumerate(cells):
        if ii == 0:
            if cell['cell_type'] != 'markdown':
                raise ValueError("The first cell of the Jupyter Notebook must be of"
                                "type 'markdown'. Found type %s" % cell['cell_type'])
            # Generate the rST and embed it in a comment.
            rst_source = _md_to_sg_py(''.join(cell['source']), comment=False)
            rst_source = '"""\n' + rst_source + '\n"""'
            python_file += rst_source
        else:
            if cell['cell_type'] == 'markdown':
                # Convert markdown into rst and add it to our source file
                # First line of comments to designate block
                rst_source = '\n\n\n'
                rst_source += '#' * 70 + '\n'
                rst_source += _md_to_sg_py(''.join(cell['source']))
                python_file += rst_source
            elif cell['cell_type'] == 'code':
                # If code, simply pass through the Python
                for ii, line in enumerate(cell['source']):
                    # Ensure "magics" are commented out
                    if line.startswith('%'):
                        cell['source'][ii] = line.replace('%', '# %', 1)
                    # If `plt.ion` is used, disable it so SG captures plots
                    if 'plt.ion' in line:
                        cell['source'][ii] = '# ' + line
                python_file += '\n\n'
                python_file += ''.join(cell['source'])

    # Write a new file name
    name_ipynb = os.path.basename(path_ipynb)
    path_out = os.path.join(folder_out, name_ipynb.replace('.ipynb', '.py'))
    with codecs.open(path_out, 'w', encoding='utf-8') as ff:
        ff.write(python_file)
    return path_out


def _md_to_sg_py(md, comment=True):
    """Use pandoc to convert markdown to rst."""
    import pypandoc as pdoc
    rst = []

    # Create the rST and add comments to the start of each line
    rst_body = pdoc.convert_text(md, 'rst', 'md')
    for ln in rst_body.split('\n'):
        # Ensure that escape characters are double-escaped for Sphinx
        ln = ln.replace('\\', '\\\\')
        if comment is True:
            ln = '# ' + ln
        rst.append(ln)
    
    rst = '\n'.join(rst)
    return rst


if __name__ == '__main__':
    import sys
    convert_ipynb_to_gallery(sys.argv[-1])