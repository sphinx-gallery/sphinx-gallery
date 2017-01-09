# -*- coding: utf-8 -*-
r"""
Parser for Lua source files
==============================
"""
# Created Mon Jan 9 1:13:07 2017
# Author: Sasank Chilamkurthy

from __future__ import division, absolute_import, print_function
import re
from textwrap import dedent

SYNTAX_ERROR_DOCSTRING = """
SyntaxError
===========

Example script with invalid Python syntax
"""

LUA_BLOCK_COMMENT_REGEX = r"--\[\[(?P<docstring>(?:.|[\r\n])*?)(?:\]\]|--\]\]?)"


def get_docstring_and_rest(filename):
    """Separate `filename` content between docstring and the rest.

    Strongly inspired from ast.get_docstring.

    Returns
    -------
    docstring: str
        docstring of `filename`
    rest: str
        `filename` content without the docstring
    """
    # can't use codecs.open(filename, 'r', 'utf-8') here b/c ast doesn't
    # seem to work with unicode strings in Python2.7
    # "SyntaxError: encoding declaration in Unicode string"
    with open(filename, 'rb') as fid:
        content = fid.read()
    # change from Windows format to UNIX for uniformity
    content = content.replace(b'\r\n', b'\n')
    content = content.decode('utf-8').strip()
    match = re.search(LUA_BLOCK_COMMENT_REGEX, content)
    if match is not None:
        match_start_pos, match_end_pos = match.span()
        if match_start_pos > 1:
            raise ValueError(('Block comment must be first thing in the '
                              'file {}').format(filename))

        docstring = match.group('docstring')
        rest = content[match_end_pos:]
        return docstring.strip(), rest.strip()
    else:
        raise ValueError(('Could not find docstring in file "{0}". '
                          'A docstring is required by sphinx-gallery')
                         .format(filename))


def split_code_and_text_blocks(source_file):
    """Return list with source file separated into code and text blocks.

    Returns
    -------
    blocks : list of (label, content)
        List where each element is a tuple with the label ('text' or 'code'),
        and content string of block.
    """
    docstring, rest_of_content = get_docstring_and_rest(source_file)
    blocks = [('text', docstring), ('code', rest_of_content)]

    return blocks
