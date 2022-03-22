# -*- coding: utf-8 -*-
r"""
Parser for python source files
==============================
"""
# Created Sun Nov 27 14:03:07 2016
# Author: Óscar Nájera

from __future__ import division, absolute_import, print_function

import codecs
import ast
from io import BytesIO
import re
import tokenize
from textwrap import dedent

from sphinx.errors import ExtensionError
from .sphinx_compatibility import getLogger

logger = getLogger('sphinx-gallery')

SYNTAX_ERROR_DOCSTRING = """
SyntaxError
===========

Example script with invalid Python syntax
"""

# The pattern for in-file config comments is designed to not greedily match
# newlines at the start and end, except for one newline at the end. This
# ensures that the matched pattern can be removed from the code without
# changing the block structure; i.e. empty newlines are preserved, e.g. in
#
#     a = 1
#
#     # sphinx_gallery_thumbnail_number = 2
#
#     b = 2
INFILE_CONFIG_PATTERN = re.compile(
    r"^[\ \t]*#\s*sphinx_gallery_([A-Za-z0-9_]+)(\s*=\s*(.+))?[\ \t]*\n?",
    re.MULTILINE)


def parse_source_file(filename):
    """Parse source file into AST node.

    Parameters
    ----------
    filename : str
        File path

    Returns
    -------
    node : AST node
    content : utf-8 encoded string
    """
    with codecs.open(filename, 'r', 'utf-8') as fid:
        content = fid.read()
    # change from Windows format to UNIX for uniformity
    content = content.replace('\r\n', '\n')

    try:
        node = ast.parse(content)
        return node, content
    except SyntaxError:
        return None, content


def _get_docstring_and_rest(filename):
    """Separate ``filename`` content between docstring and the rest.

    Strongly inspired from ast.get_docstring.

    Returns
    -------
    docstring : str
        docstring of ``filename``
    rest : str
        ``filename`` content without the docstring
    lineno : int
        The line number.
    node : ast Node
        The node.
    """
    node, content = parse_source_file(filename)

    if node is None:
        return SYNTAX_ERROR_DOCSTRING, content, 1, node

    if not isinstance(node, ast.Module):
        raise ExtensionError("This function only supports modules. "
                             "You provided {0}"
                             .format(node.__class__.__name__))
    if not (node.body and isinstance(node.body[0], ast.Expr) and
            isinstance(node.body[0].value, ast.Str)):
        raise ExtensionError(
            'Could not find docstring in file "{0}". '
            'A docstring is required by sphinx-gallery '
            'unless the file is ignored by "ignore_pattern"'
            .format(filename))

    # Python 3.7+ way
    docstring = ast.get_docstring(node)
    assert docstring is not None  # should be guaranteed above
    # This is just for backward compat
    if len(node.body[0].value.s) and node.body[0].value.s[0] == '\n':
        # just for strict backward compat here
        docstring = '\n' + docstring
    ts = tokenize.tokenize(BytesIO(content.encode()).readline)
    # find the first string according to the tokenizer and get its end row
    for tk in ts:
        if tk.exact_type == 3:
            lineno, _ = tk.end
            break
    else:
        lineno = 0

    # This get the content of the file after the docstring last line
    # Note: 'maxsplit' argument is not a keyword argument in python2
    rest = '\n'.join(content.split('\n')[lineno:])
    lineno += 1
    return docstring, rest, lineno, node


def extract_file_config(content):
    """
    Pull out the file-specific config specified in the docstring.
    Note that this can be used for a single block too.
    When a directive is present several times in `content` only the last
    occurence will be present in the output config dict.
    """
    file_conf = {}
    for match in re.finditer(INFILE_CONFIG_PATTERN, content):
        name = match.group(1)
        value = match.group(3)
        if value is None:  # a flag rather than a config setting
            continue
        try:
            value = ast.literal_eval(value)
        except (SyntaxError, ValueError):
            logger.warning(
                'Sphinx-gallery option %s was passed invalid value %s',
                name, value)
        else:
            file_conf[name] = value
    return file_conf


class Block:
    """Contents of a parsed block"""
    __slots__ = ("contents", "lineno", "config")

    def __init__(self, contents, lineno, config=None):
        self.contents = contents
        self.lineno = lineno
        self.config = config if config is not None else {}

    def __repr__(self):
        return "%s(lineno=%s, config=%r, contents=%r)" % (
            type(self).__name__,
            self.lineno,
            self.config,
            self.contents[:100],
        )

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        else:
            return (
                self.contents == other.contents
                and self.lineno == other.lineno
                and self.config == other.config
            )

    def remove_config_comments(self):
        """Return a copy of this block with config comments removed."""
        new_contents = remove_config_comments(self.contents)
        blk_copy = type(self)(contents=new_contents, lineno=self.lineno, config=self.config)
        return blk_copy


class CodeBlock(Block):
    pass


class TextBlock(Block):
    pass


def split_code_and_text_blocks(source_file, return_node=False):
    """Return list with source file separated into code and text blocks.

    Parameters
    ----------
    source_file : str
        Path to the source file.
    return_node : bool
        If True, return the ast node.

    Returns
    -------
    file_conf : dict
        File-specific settings given in source file comments as:
        ``# sphinx_gallery_<name> = <value>``
    blocks : list[Block]
        List where each element is a CodeBlock or TextBlock.
    node : ast Node
        The parsed node.
    """
    docstring, rest_of_content, lineno, node = _get_docstring_and_rest(
        source_file)
    blocks = [TextBlock(contents=docstring, lineno=1)]

    # TODO This is maybe useless: now that the block-related ones are read below
    #   we could probably replace it with a union of all block configs
    file_conf = extract_file_config(rest_of_content)

    pattern = re.compile(
        r'(?P<header_line>^#{20,}.*|^# ?%%.*)\s(?P<text_content>(?:^#.*\s?)*)',
        flags=re.M)
    sub_pat = re.compile('^#', flags=re.M)

    pos_so_far = 0
    for match in re.finditer(pattern, rest_of_content):
        code_block_content = rest_of_content[pos_so_far:match.start()]
        if code_block_content.strip():
            cfg = extract_file_config(code_block_content)
            block = CodeBlock(contents=code_block_content, lineno=lineno, config=cfg)
            blocks.append(block)
        lineno += code_block_content.count('\n')

        lineno += 1  # Ignored header line of hashes.
        text_content = match.group('text_content')
        text_block_content = dedent(re.sub(sub_pat, '', text_content)).lstrip()
        if text_block_content.strip():
            block = TextBlock(contents=text_block_content, lineno=lineno, config={})
            blocks.append(block)
        lineno += text_content.count('\n')

        pos_so_far = match.end()

    remaining_content = rest_of_content[pos_so_far:]
    if remaining_content.strip():
        cfg = extract_file_config(remaining_content)
        block = CodeBlock(contents=remaining_content, lineno=lineno, config=cfg)
        blocks.append(block)

    out = (file_conf, blocks)
    if return_node:
        out += (node,)
    return out


def remove_config_comments(code_block):
    """
    Return the content of *code_block* with in-file config comments removed.

    Comment lines of the pattern '# sphinx_gallery_[option] = [val]' are
    removed, but surrounding empty lines are preserved.

    Parameters
    ----------
    code_block : str
        A code segment.
    """
    parsed_code, _ = re.subn(INFILE_CONFIG_PATTERN, '', code_block)
    return parsed_code
