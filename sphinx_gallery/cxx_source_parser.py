"""
Parser for source files that use C++ style comments. That is, lines starting with
``//`` and blocks starting with ``/*`` and ending with ``*/``.

``sphinx_gallery`` flags are supported for line comments starting with ``//``.
"""

import ast
import codecs
import re

from sphinx.errors import ExtensionError
from sphinx.util.logging import getLogger

logger = getLogger("sphinx-gallery")

# The pattern for in-file config comments is designed to not greedily match
# newlines at the start and end, except for one newline at the end. This
# ensures that the matched pattern can be removed from the code without
# changing the block structure; i.e. empty newlines are preserved, e.g. in
#
#     a = 1
#
#     // sphinx_gallery_thumbnail_number = 2
#
#     b = 2
FLAG_START = r"^[\ \t]*//\s*"
INFILE_CONFIG_PATTERN = re.compile(
    FLAG_START + r"sphinx_gallery_([A-Za-z0-9_]+)(\s*=\s*(.+))?[\ \t]*\n?", re.MULTILINE
)

START_IGNORE_FLAG = FLAG_START + "sphinx_gallery_start_ignore"
END_IGNORE_FLAG = FLAG_START + "sphinx_gallery_end_ignore"
IGNORE_BLOCK_PATTERN = re.compile(
    rf"{START_IGNORE_FLAG}(?:[\s\S]*?){END_IGNORE_FLAG}\n?", re.MULTILINE
)


def split_code_and_text_blocks(source_file, return_node=False):
    """Return list with source file separated into code and text blocks.

    Parameters
    ----------
    source_file : str
        Path to the source file.
    return_node : bool
        Ignored by non-Python parser.

    Returns
    -------
    file_conf : dict
        File-specific settings given in source file comments as:
        ``// sphinx_gallery_<name> = <value>``
    blocks : list
        (label, content, line_number)
        List where each element is a tuple with the label ('text' or 'code'),
        the corresponding content string of block and the leading line number.
    node : None
        Not used by this parser
    """
    with codecs.open(source_file, "r", "utf-8") as fid:
        content = fid.read()
    # change from Windows format to UNIX for uniformity
    content = content.replace("\r\n", "\n")

    lines = content.splitlines()

    text_blocks = []
    code_blocks = []

    text_start = None

    def start_c_block(line):
        if not text_blocks:
            # Capture the first comment block
            return re.match(r"\s*/\*(.*)$", line)
        else:
            # Capture subsequent comment blocks only if they contain the sentinel
            return re.match(r"\s*/\* {0,1}%%(.*)$", line)

    def end_c_block(line):
        return re.match(r"(.*)\*/", line)

    def start_cxx_block(line):
        if not text_blocks:
            return re.match(r"\s*//(.*)", line)
        else:
            return re.match(r"\s*// {0,1}%%(.*)", line)

    def end_cxx_block(line):
        return line.strip() and not re.match(r"\s*//", line)

    text_start = None
    code_start = None
    for i, line in enumerate(lines):
        if text_start is None:
            if m := start_c_block(line):
                if g := m.group(1):
                    lines[i] = g
                    text_start = i
                else:
                    text_start = i + 1
                end_matcher = end_c_block
            elif m := start_cxx_block(line):
                if m.group(1):
                    lines[i] = re.sub("(.*//) {0,1}%%(.*)", r"\1\2", line)
                    text_start = i
                else:
                    text_start = i + 1
                end_matcher = end_cxx_block
            if m and code_start is not None:
                code_blocks.append((code_start, i))
                code_start = None
        elif m := end_matcher(line):
            if m is True:
                text_blocks.append((text_start, i))
                code_start = i
            else:
                if g := m.group(1):
                    lines[i] = g
                text_blocks.append((text_start, i+1))
                code_start = i+1
            text_start = None

    if text_start is not None:
        text_blocks.append((text_start, i+1))
    elif code_start is not None:
        code_blocks.append((code_start, i+1))

    for start,end in text_blocks:
        block = lines[start:end]
        prefix_chars = {"\t", " ", "*", "/"}

        N, longest = max((len(re.match(r"\s*[\*/]*\s*", line).group(0)), line)
                         for line in block)
        matched = 0
        for i in range(1, N+1):
            for line in block:
                if set(line[:i]) - prefix_chars:
                    break
                if len(line) < i:
                    if line != longest[:len(line)]:
                        break
                elif line[:i] != longest[:i]:
                    break
            else:
                matched = i
            if matched != i:
                break

        for i in range(start, end):
            lines[i] = lines[i][matched:]

    blocks = []
    for start, end in text_blocks:
        blocks.append(('text', '\n'.join(lines[start:end]), start))

    for start, end in code_blocks:
        blocks.append(('code', '\n'.join(lines[start:end]), start))

    blocks.sort(key=lambda item: item[2])
    file_conf = extract_file_config(content)
    node = None

    return file_conf, blocks, node


def extract_file_config(content):
    """Pull out the file-specific config specified in the docstring."""
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
                "Sphinx-gallery option %s was passed invalid value %s", name, value
            )
        else:
            file_conf[name] = value
    return file_conf


def remove_ignore_blocks(code_block):
    """
    Return the content of *code_block* with ignored areas removed.

    An ignore block starts with ``// sphinx_gallery_begin_ignore`` and ends with
    ``// sphinx_gallery_end_ignore``. These lines and anything in between them
    will be removed, but surrounding empty lines are preserved.

    Parameters
    ----------
    code_block : str
        A code segment.
    """
    num_start_flags = len(re.findall(START_IGNORE_FLAG, code_block))
    num_end_flags = len(re.findall(END_IGNORE_FLAG, code_block))

    if num_start_flags != num_end_flags:
        raise ExtensionError(
            'All "sphinx_gallery_start_ignore" flags must have a matching '
            '"sphinx_gallery_end_ignore" flag!'
        )
    return re.subn(IGNORE_BLOCK_PATTERN, "", code_block)[0]


def remove_config_comments(code_block):
    """
    Return the content of *code_block* with in-file config comments removed.

    Comment lines of the pattern ``// sphinx_gallery_[option] = [val]`` are
    removed, but surrounding empty lines are preserved.

    Parameters
    ----------
    code_block : str
        A code segment.
    """
    parsed_code, _ = re.subn(INFILE_CONFIG_PATTERN, "", code_block)
    return parsed_code
