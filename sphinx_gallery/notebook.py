# -*- coding: utf-8 -*-
r"""
Parser for Jupyter notebooks
============================

Class that holds the Jupyter notebook information

"""
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import division, absolute_import, print_function
from collections import defaultdict
from functools import partial
from itertools import count
import argparse
import json
import re
import sys
import copy

from . import sphinx_compatibility
from .py_source_parser import split_code_and_text_blocks
from .utils import replace_py_ipynb

logger = sphinx_compatibility.getLogger('sphinx-gallery')


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


def rst2md(text, heading_levels):
    """Converts the RST text from the examples docstrings and comments
    into markdown text for the Jupyter notebooks

    Parameters
    ----------
    text: str
        RST input to be converted to MD
    heading_levels: dict
        Mapping of heading style ``(over_char, under_char)`` to heading level.
        Note that ``over_char`` is `None` when only underline is present.
    """

    # Characters recommend for use with headings
    # https://docutils.readthedocs.io/en/sphinx-docs/user/rst/quickstart.html#sections
    adornment_characters = "=`:.'\"~^_*+#<>-"
    headings = re.compile(
        r'(?P<pre>\A|^[ \t]*\n)'  # Start of string or blank line above
        r'(?:(?P<over>[{0}])(?P=over)*\n[ \t]*)?'  # Over, with heading space
        r'(?P<heading>\S[^\n]*)\n'  # Heading itself
        r'(?P<under>(?(over)(?P=over)|[{0}]))(?P=under)*$'  # if over make same
        r''.format(adornment_characters),
        flags=re.M)

    text = re.sub(
        headings,
        lambda match: '{1}{0} {2}'.format(
            '#'*heading_levels[match.group('over', 'under')],
            *match.group('pre', 'heading')),
        text)

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
    first_cell = gallery_conf["first_notebook_cell"]
    last_cell = gallery_conf["last_notebook_cell"]
    work_notebook = jupyter_notebook_skeleton()
    if first_cell is not None:
        add_code_cell(work_notebook, first_cell)
    fill_notebook(work_notebook, script_blocks, gallery_conf)
    if last_cell is not None:
        add_code_cell(work_notebook, last_cell)

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


def add_markdown_cell(work_notebook, markdown):
    """Add a markdown cell to the notebook

    Parameters
    ----------
    markdown : str
        Markdown cell content.
    """
    markdown_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [markdown]
    }
    work_notebook["cells"].append(markdown_cell)


def fill_notebook(work_notebook, script_blocks, gallery_conf):
    """Writes the Jupyter notebook cells

    If available, uses pypandoc to convert rst to markdown.

    Parameters
    ----------
    script_blocks : list
        Each list element should be a tuple of (label, content, lineno).
    """
    heading_level_counter = count(start=1)
    heading_levels = defaultdict(lambda: next(heading_level_counter))
    for blabel, bcontent, lineno in script_blocks:
        if blabel == 'code':
            add_code_cell(work_notebook, bcontent)
        else:
            if gallery_conf["pypandoc"] is False:
                markdown = rst2md(bcontent + '\n', heading_levels)
            else:
                import pypandoc
                # pandoc automatically addds \n to the end
                markdown = pypandoc.convert_text(
                    bcontent, to='md', format='rst', **gallery_conf["pypandoc"]
                )
            add_markdown_cell(work_notebook, markdown)


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
