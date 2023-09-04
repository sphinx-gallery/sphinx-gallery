import ast
import re

from sphinx.errors import ExtensionError
from sphinx.util.logging import getLogger

logger = getLogger("sphinx-gallery")

class BlockParser:
    """
    Base class for a parser that breaks a source file into blocks of code and
    markup text. The default implementation handles extraction of
    ``sphinx_gallery_*`` directives for languages that use line-style comments
    with a single comment marker.

    Derived classes must implement the `split_code_and_text_blocks` method.

    Parameters
    ----------
    line_comment_delimiter : str | None
        String that starts a comment line
    """

    def __init__(self, line_comment_delimiter=None):

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
        if line_comment_delimiter is not None:
            flag_start = rf"^[\ \t]*{line_comment_delimiter}\s*"

            self.infile_config_pattern = re.compile(
                flag_start + r"sphinx_gallery_([A-Za-z0-9_]+)(\s*=\s*(.+))?[\ \t]*\n?",
                re.MULTILINE
            )

            self.start_ignore_flag = flag_start + "sphinx_gallery_start_ignore"
            self.end_ignore_flag = flag_start + "sphinx_gallery_end_ignore"
            self.ignore_block_pattern = re.compile(
                rf"{self.start_ignore_flag}(?:[\s\S]*?){self.end_ignore_flag}\n?",
                re.MULTILINE
            )

    def split_code_and_text_blocks(self, source_file, return_node=False):
        """Return list with source file separated into code and text blocks.

        Parameters
        ----------
        source_file : str
            Path to the source file.
        return_node : bool
            If True, return the ast node (if possible)

        Returns
        -------
        file_conf : dict
            File-specific settings given in source file comments as:
            ``# sphinx_gallery_<name> = <value>``
        blocks : list
            (label, content, line_number)
            List where each element is a tuple with the label ('text' or 'code'),
            the corresponding content string of block and the leading line number.
        node : ast.Module | None
            The parsed ast node, or None if not requested or not possible
        """
        raise NotImplementedError("BlockParser.split_code_and_text_blocks")

    def extract_file_config(self, content):
        """Pull out the file-specific config specified in the docstring."""
        file_conf = {}
        for match in re.finditer(self.infile_config_pattern, content):
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

    def remove_ignore_blocks(self, code_block):
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
        num_start_flags = len(re.findall(self.start_ignore_flag, code_block))
        num_end_flags = len(re.findall(self.end_ignore_flag, code_block))

        if num_start_flags != num_end_flags:
            raise ExtensionError(
                'All "sphinx_gallery_start_ignore" flags must have a matching '
                '"sphinx_gallery_end_ignore" flag!'
            )
        return re.subn(self.ignore_block_pattern, "", code_block)[0]

    def remove_config_comments(self, code_block):
        """
        Return the content of *code_block* with in-file config comments removed.

        Comment lines of the pattern ``// sphinx_gallery_[option] = [val]`` are
        removed, but surrounding empty lines are preserved.

        Parameters
        ----------
        code_block : str
            A code segment.
        """
        parsed_code, _ = re.subn(self.infile_config_pattern, "", code_block)
        return parsed_code
