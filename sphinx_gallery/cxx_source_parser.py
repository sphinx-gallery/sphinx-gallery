import codecs
import re

from sphinx.util.logging import getLogger
from .block_parser import BlockParser

logger = getLogger("sphinx-gallery")

class CxxParser(BlockParser):
    """
    Parser for source files that use C++ style comments. That is, lines starting with
    ``//`` and blocks starting with ``/*`` and ending with ``*/``.

    ``sphinx_gallery`` flags are supported for line comments starting with ``//``.
    """
    def __init__(self):
        super().__init__("//")

    def split_code_and_text_blocks(self, source_file, return_node=False):
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
        file_conf = self.extract_file_config(content)
        node = None

        return file_conf, blocks, node
