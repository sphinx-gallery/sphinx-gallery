"""Parser for source files."""
from . import py_source_parser
from . import lua_source_parser


def get_docstring_and_rest(filename, lang='python'):
    if lang == 'python':
        return py_source_parser.get_docstring_and_rest(filename)
    elif lang == 'lua':
        return lua_source_parser.get_docstring_and_rest(filename)
    else:
        raise ValueError('Unsupported language {}'.format(lang))


def split_code_and_text_blocks(filename, lang='python'):
    if lang == 'python':
        return py_source_parser.split_code_and_text_blocks(filename)
    elif lang == 'lua':
        return lua_source_parser.split_code_and_text_blocks(filename)
    else:
        raise ValueError('Unsupported language {}'.format(lang))
