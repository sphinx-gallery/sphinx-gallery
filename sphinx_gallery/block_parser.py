import ast
import codecs
import re
from pathlib import Path
import pygments.lexers
import pygments.token
import re
from textwrap import dedent

from sphinx.errors import ExtensionError
from sphinx.util.logging import getLogger

logger = getLogger("sphinx-gallery")

# Don't just use "x in pygments.token.Comment" because it also includes preprocessor
# statements
COMMENT_TYPES = (pygments.token.Comment.Single, pygments.token.Comment.Multiline,
                 pygments.token.Comment)

SPACES = re.compile(r"^[ \t]+$")

class BlockParser:
    """
    A parser that breaks a source file into blocks of code and markup text. Determines
    the source language and identifies comment blocks using pygments.

    Parameters
    ----------
    source_file : str
        A file name that has a suffix compatible with files that are subsequently parsed
    gallery_conf : dict
        Contains the configuration of Sphinx-Gallery.
    """

    def __init__(self, source_file, gallery_conf):
        source_file = Path(source_file)
        if name := gallery_conf["filetype_parsers"].get(source_file.suffix):
            self.lexer = pygments.lexers.find_lexer_class_by_name(name)()
        else:
            self.lexer = pygments.lexers.find_lexer_class_for_filename(source_file)()
        self.language = self.lexer.name

        # determine valid comment starting syntaxes
        comment_tests = {
            "#": "# comment",
            "//": "// comment",
            r"/\*": "/* comment */",
            "%": "% comment",
            "!": "! comment",
            "#=": "#= comment =#",
        }

        self.allowed_comments = {start for start, comment in comment_tests.items()
                                 if next(self.lexer.get_tokens(comment))[0] in COMMENT_TYPES}

        comment_start = "|".join(self.allowed_comments)
        self.start_special = re.compile(f"(?:{comment_start}) ?%% ?(.*)", re.DOTALL)
        self.continue_text = re.compile(f"(?:{comment_start}) ?(.*)", re.DOTALL)

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
        flag_start = rf"^[\ \t]*{comment_start}\s*"

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
            Ignored; returning an ast node is not supported

        Returns
        -------
        file_conf : dict
            File-specific settings given in source file comments as:
            ``# sphinx_gallery_<name> = <value>``
        blocks : list
            (label, content, line_number)
            List where each element is a tuple with the label ('text' or 'code'),
            the corresponding content string of block and the leading line number.
        node : None
            Returning an ast node is not supported.
        """

        with codecs.open(source_file, "r", "utf-8") as fid:
            content = fid.read()
        # change from Windows format to UNIX for uniformity
        content = content.replace("\r\n", "\n")
        return self._split_content(content)

    def _split_content(self, content):
        blocks = []
        def append_block(blocks, kind, block):
            block = "".join(block)
            if block and set(block) != {"\n"}:
                if not block.endswith("\n"):
                    block += "\n"
                if kind == "text":
                    block = cleanup_comment(block)
                line_no = blocks[-1][2] if blocks else 0
                line_no += block.count("\n")
                blocks.append((kind, block, line_no))

        def cleanup_comment(block):
            if ("/\\*" not in self.allowed_comments
                or not (b := block.rstrip()).endswith("*/")):

                # Normalize leading and trailing newlines: none to start, one at the end
                block = block.lstrip("\n")
                if block.endswith("\n\n"):
                    block = block.rstrip("\n") + "\n"

                return dedent(block)

            # Otherwise, remove decorations from C-style multiline comments
            lines = b[:-2].splitlines()  # delete the trailing "*/"
            lines = [line.rstrip(" \t") for line in lines]

            if len(lines) == 1:
                return lines[0]

            # Find the longest consistent prefix consisting of these characters
            prefix_chars = {"\t", " ", "*", "/"}
            N, longest = max((len(re.match(r"\s*[\*/]*\s*", line).group(0)), line)
                            for line in lines[1:])
            matched = 0
            for i in range(1, N+1):
                for line in lines[1:]:
                    if set(line[:i]) - prefix_chars:
                        break
                    elif len(line) < i:
                        if line != longest[:len(line)]:
                            break
                    elif line[:i] != longest[:i]:
                        break
                else:
                    matched = i
                if matched != i:
                    break

            # delete the prefix from lines after the first
            block = (lines[0].lstrip() + "\n"
                     + "\n".join((line[matched:] for line in lines[1:])))

            # Normalize leading and trailing newlines: none to start, one at the end
            block = block.lstrip("\n")
            if block.endswith("\n\n") or not block.endswith("\n"):
                block = block.rstrip("\n") + "\n"

            return block

        block = []
        mode = None
        start_of_text = self.continue_text  # Take first comment block without sentinel
        last_space = ""
        newline_count = 0
        for token, text in self.lexer.get_tokens(content):
            # Track consecutive newlines, which can indicate the end of a special
            # comment block
            if block and token in pygments.token.Whitespace:
                newline_count += text.count("\n")
            else:
                newline_count = text.count("\n")

            if token in pygments.token.Whitespace:
                # Defer categorizing start-of-line whitespace; it may belong to the
                # following block
                last_space = text[text.rindex("\n")+1:] if "\n" in text else text

                if mode == "text" and newline_count >= 2:
                    append_block(blocks, "text", block)
                    block = [last_space]
                    last_space = ""
                    mode = None
            elif token in COMMENT_TYPES and (m := start_of_text.match(text)):
                # Complete the preceding code block
                append_block(blocks, "code", block)

                # Start of first comment block or a special comment block.
                if (text := m.group(1)).strip():
                    block = [last_space, text]
                elif "\n" in text:
                    block = [text[text.rindex("\n")+1:]]
                else:
                    block = [last_space]
                last_space = ""
                mode = "text"
                # For subsequent blocks, require the special sentinel
                start_of_text = self.start_special
            elif mode == "text" and token in COMMENT_TYPES:
                # continuation of a special comment block
                block.append(last_space)
                last_space = ""
                if m := self.continue_text.match(text):
                    block.append(m.group(1))
            elif mode != "code":
                # start of a code block; complete the preceding text block
                append_block(blocks, "text", block)
                block = [last_space]
                last_space = ""
                block.append(text)
                mode = "code"
            else:
                # continuation of a code block
                block.extend((last_space, text))
                last_space = ""

        if mode is not None:
            append_block(blocks, mode, block)

        file_conf = self.extract_file_config(content)
        return file_conf, blocks, None

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

        An ignore block starts with ``?? sphinx_gallery_begin_ignore`` and ends with
        ``?? sphinx_gallery_end_ignore`` where ``??`` is the active language's line
        comment marker. These lines and anything in between them will be removed, but
        surrounding empty lines are preserved.

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

        Comment lines with the pattern ``sphinx_gallery_[option] = [val]`` after the
        line comment character are removed, but surrounding empty lines are preserved.

        Parameters
        ----------
        code_block : str
            A code segment.
        """
        parsed_code, _ = re.subn(self.infile_config_pattern, "", code_block)
        return parsed_code
