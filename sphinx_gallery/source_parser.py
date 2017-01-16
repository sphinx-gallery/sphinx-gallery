"""Parser for source files."""
import os
from . import py_source_parser
from . import lua_source_parser


supported_languages = {
    'python': ['.py'],
    'lua': ['.lua'],
    'C++': ['.cpp', '.cxx', '.hpp'],
    'C': ['.c', '.h'],
    'javascript': ['.js']
}

supported_extensions = tuple((x for lang, lang_extensions in
                              supported_languages.items()
                              for x in lang_extensions))


def get_lang(filename):
    """Get language of the file from filename."""
    filename, file_extension = os.path.splitext(filename)
    for lang, lang_extensions in supported_languages.items():
        if file_extension in lang_extensions:
            return lang

    raise ValueError('Unsupported language for file {}'.format(filename))


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
