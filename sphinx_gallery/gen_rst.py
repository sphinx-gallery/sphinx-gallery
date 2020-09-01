# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
RST file generator
==================

Generate the rst files for the examples by iterating over the python
example files.

Files that generate images should start with 'plot'.
"""
# Don't use unicode_literals here (be explicit with u"..." instead) otherwise
# tricky errors come up with exec(code_blocks, ...) calls
from __future__ import division, print_function, absolute_import
from time import time
import copy
import contextlib
import ast
import codecs
from functools import partial
import gc
import pickle
import importlib
from io import StringIO
import os
import re
from textwrap import indent
import warnings
from shutil import copyfile
import subprocess
import sys
import traceback
import codeop

from sphinx.errors import ExtensionError

from .scrapers import (save_figures, ImagePathIterator, clean_modules,
                       _find_image_ext)
from .utils import (replace_py_ipynb, scale_image, get_md5sum, _replace_md5,
                    optipng)
from . import glr_path_static
from . import sphinx_compatibility
from .backreferences import (_write_backreferences, _thumbnail_div,
                             identify_names)
from .downloads import CODE_DOWNLOAD
from .py_source_parser import (split_code_and_text_blocks,
                               remove_config_comments)

from .notebook import jupyter_notebook, save_notebook
from .binder import check_binder_conf, gen_binder_rst

logger = sphinx_compatibility.getLogger('sphinx-gallery')


###############################################################################


class _LoggingTee(object):
    """A tee object to redirect streams to the logger."""

    def __init__(self, src_filename):
        self.logger = logger
        self.src_filename = src_filename
        self.logger_buffer = ''
        self.set_std_and_reset_position()

    def set_std_and_reset_position(self):
        if not isinstance(sys.stdout, _LoggingTee):
            self.origs = (sys.stdout, sys.stderr)
        sys.stdout = sys.stderr = self
        self.first_write = True
        self.output = StringIO()
        return self

    def restore_std(self):
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout, sys.stderr = self.origs

    def write(self, data):
        self.output.write(data)

        if self.first_write:
            self.logger.verbose('Output from %s', self.src_filename,
                                color='brown')
            self.first_write = False

        data = self.logger_buffer + data
        lines = data.splitlines()
        if data and data[-1] not in '\r\n':
            # Wait to write last line if it's incomplete. It will write next
            # time or when the LoggingTee is flushed.
            self.logger_buffer = lines[-1]
            lines = lines[:-1]
        else:
            self.logger_buffer = ''

        for line in lines:
            self.logger.verbose('%s', line)

    def flush(self):
        self.output.flush()
        if self.logger_buffer:
            self.logger.verbose('%s', self.logger_buffer)
            self.logger_buffer = ''

    # When called from a local terminal seaborn needs it in Python3
    def isatty(self):
        return self.output.isatty()

    # When called in gen_rst, conveniently use context managing
    def __enter__(self):
        return self

    def __exit__(self, type_, value, tb):
        self.restore_std()


###############################################################################
# The following strings are used when we have several pictures: we use
# an html div tag that our CSS uses to turn the lists into horizontal
# lists.
HLIST_HEADER = """
.. rst-class:: sphx-glr-horizontal

"""

HLIST_IMAGE_TEMPLATE = """
    *

      .. image:: /%s
            :class: sphx-glr-multi-img
"""

SINGLE_IMAGE = """
.. image:: /%s
    :class: sphx-glr-single-img
"""

# This one could contain unicode
CODE_OUTPUT = u""".. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

{0}\n"""

TIMING_CONTENT = """
.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ({0: .0f} minutes {1: .3f} seconds)

"""

SPHX_GLR_SIG = """\n
.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
"""

# Header used to include raw html
html_header = """.. raw:: html

{0}\n    <br />\n    <br />"""


def codestr2rst(codestr, lang='python', lineno=None):
    """Return reStructuredText code block from code string"""
    if lineno is not None:
        # Sphinx only starts numbering from the first non-empty line.
        blank_lines = codestr.count('\n', 0, -len(codestr.lstrip()))
        lineno = '   :lineno-start: {0}\n'.format(lineno + blank_lines)
    else:
        lineno = ''
    code_directive = "\n.. code-block:: {0}\n{1}\n".format(lang, lineno)
    indented_block = indent(codestr, ' ' * 4)
    return code_directive + indented_block


def _regroup(x):
    x = x.groups()
    return x[0] + x[1].split('.')[-1] + x[2]


def _sanitize_rst(string):
    """Use regex to remove at least some sphinx directives."""
    # :class:`a.b.c <thing here>`, :ref:`abc <thing here>` --> thing here
    p, e = r'(\s|^):[^:\s]+:`', r'`(\W|$)'
    string = re.sub(p + r'\S+\s*<([^>`]+)>' + e, r'\1\2\3', string)
    # :class:`~a.b.c` --> c
    string = re.sub(p + r'~([^`]+)' + e, _regroup, string)
    # :class:`a.b.c` --> a.b.c
    string = re.sub(p + r'([^`]+)' + e, r'\1\2\3', string)

    # ``whatever thing`` --> whatever thing
    p = r'(\s|^)`'
    string = re.sub(p + r'`([^`]+)`' + e, r'\1\2\3', string)
    # `whatever thing` --> whatever thing
    string = re.sub(p + r'([^`]+)' + e, r'\1\2\3', string)
    return string


def extract_intro_and_title(filename, docstring):
    """Extract and clean the first paragraph of module-level docstring."""
    # lstrip is just in case docstring has a '\n\n' at the beginning
    paragraphs = docstring.lstrip().split('\n\n')
    # remove comments and other syntax like `.. _link:`
    paragraphs = [p for p in paragraphs
                  if not p.startswith('.. ') and len(p) > 0]
    if len(paragraphs) == 0:
        raise ExtensionError(
            "Example docstring should have a header for the example title. "
            "Please check the example file:\n {}\n".format(filename))
    # Title is the first paragraph with any ReSTructuredText title chars
    # removed, i.e. lines that consist of (3 or more of the same) 7-bit
    # non-ASCII chars.
    # This conditional is not perfect but should hopefully be good enough.
    title_paragraph = paragraphs[0]
    match = re.search(r'^(?!([\W _])\1{3,})(.+)', title_paragraph,
                      re.MULTILINE)

    if match is None:
        raise ExtensionError(
            'Could not find a title in first paragraph:\n{}'.format(
                title_paragraph))
    title = match.group(0).strip()
    # Use the title if no other paragraphs are provided
    intro_paragraph = title if len(paragraphs) < 2 else paragraphs[1]
    # Concatenate all lines of the first paragraph and truncate at 95 chars
    intro = re.sub('\n', ' ', intro_paragraph)
    intro = _sanitize_rst(intro)
    if len(intro) > 95:
        intro = intro[:95] + '...'
    return intro, title


def md5sum_is_current(src_file, mode='b'):
    """Checks whether src_file has the same md5 hash as the one on disk"""

    src_md5 = get_md5sum(src_file, mode)

    src_md5_file = src_file + '.md5'
    if os.path.exists(src_md5_file):
        with open(src_md5_file, 'r') as file_checksum:
            ref_md5 = file_checksum.read()

        return src_md5 == ref_md5

    return False


def save_thumbnail(image_path_template, src_file, file_conf, gallery_conf):
    """Generate and Save the thumbnail image

    Parameters
    ----------
    image_path_template : str
        holds the template where to save and how to name the image
    src_file : str
        path to source python file
    gallery_conf : dict
        Sphinx-Gallery configuration dictionary
    """

    thumb_dir = os.path.join(os.path.dirname(image_path_template), 'thumb')
    if not os.path.exists(thumb_dir):
        os.makedirs(thumb_dir)

    # read specification of the figure to display as thumbnail from main text
    thumbnail_number = file_conf.get('thumbnail_number', None)
    thumbnail_path = file_conf.get('thumbnail_path', None)
    # thumbnail_number has priority.
    if thumbnail_number is None and thumbnail_path is None:
        # If no number AND no path, set to default thumbnail_number
        thumbnail_number = 1
    if thumbnail_number is None:
        image_path = os.path.join(gallery_conf['src_dir'], thumbnail_path)
    else:
        if not isinstance(thumbnail_number, int):
            raise ExtensionError(
                'sphinx_gallery_thumbnail_number setting is not a number, '
                'got %r' % (thumbnail_number,))
        image_path = image_path_template.format(thumbnail_number)
    del thumbnail_number, thumbnail_path, image_path_template
    thumbnail_image_path, ext = _find_image_ext(image_path)

    base_image_name = os.path.splitext(os.path.basename(src_file))[0]
    thumb_file = os.path.join(thumb_dir,
                              'sphx_glr_%s_thumb.%s' % (base_image_name, ext))

    if src_file in gallery_conf['failing_examples']:
        img = os.path.join(glr_path_static(), 'broken_example.png')
    elif os.path.exists(thumbnail_image_path):
        img = thumbnail_image_path
    elif not os.path.exists(thumb_file):
        # create something to replace the thumbnail
        img = os.path.join(glr_path_static(), 'no_image.png')
        img = gallery_conf.get("default_thumb_file", img)
    else:
        return
    if ext in ('svg', 'gif'):
        copyfile(img, thumb_file)
    else:
        scale_image(img, thumb_file, *gallery_conf["thumbnail_size"])
        if 'thumbnails' in gallery_conf['compress_images']:
            optipng(thumb_file, gallery_conf['compress_images_args'])


def _get_readme(dir_, gallery_conf, raise_error=True):
    extensions = ['.txt'] + sorted(gallery_conf['app'].config['source_suffix'])
    for ext in extensions:
        for fname in ('README', 'readme'):
            fpth = os.path.join(dir_, fname + ext)
            if os.path.isfile(fpth):
                return fpth
    if raise_error:
        raise ExtensionError(
            "Example directory {0} does not have a README file with one "
            "of the expected file extensions {1}. Please write one to "
            "introduce your gallery.".format(dir_, extensions))
    return None


def generate_dir_rst(src_dir, target_dir, gallery_conf, seen_backrefs):
    """Generate the gallery reStructuredText for an example directory."""
    head_ref = os.path.relpath(target_dir, gallery_conf['src_dir'])
    fhindex = """\n\n.. _sphx_glr_{0}:\n\n""".format(
        head_ref.replace(os.path.sep, '_'))

    fname = _get_readme(src_dir, gallery_conf)
    with codecs.open(fname, 'r', encoding='utf-8') as fid:
        fhindex += fid.read()
    # Add empty lines to avoid bug in issue #165
    fhindex += "\n\n"

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    # get filenames
    listdir = [fname for fname in os.listdir(src_dir)
               if fname.endswith('.py')]
    # limit which to look at based on regex (similar to filename_pattern)
    listdir = [fname for fname in listdir
               if re.search(gallery_conf['ignore_pattern'],
                            os.path.normpath(os.path.join(src_dir, fname)))
               is None]
    # sort them
    sorted_listdir = sorted(
        listdir, key=gallery_conf['within_subsection_order'](src_dir))
    entries_text = []
    costs = []
    build_target_dir = os.path.relpath(target_dir, gallery_conf['src_dir'])
    iterator = sphinx_compatibility.status_iterator(
        sorted_listdir,
        'generating gallery for %s... ' % build_target_dir,
        length=len(sorted_listdir))
    for fname in iterator:
        intro, title, cost = generate_file_rst(
            fname, target_dir, src_dir, gallery_conf, seen_backrefs)
        src_file = os.path.normpath(os.path.join(src_dir, fname))
        costs.append((cost, src_file))
        this_entry = _thumbnail_div(target_dir, gallery_conf['src_dir'],
                                    fname, intro, title) + """

.. toctree::
   :hidden:

   /%s\n""" % os.path.join(build_target_dir, fname[:-3]).replace(os.sep, '/')
        entries_text.append(this_entry)

    for entry_text in entries_text:
        fhindex += entry_text

    # clear at the end of the section
    fhindex += """.. raw:: html\n
    <div class="sphx-glr-clear"></div>\n\n"""

    return fhindex, costs


def handle_exception(exc_info, src_file, script_vars, gallery_conf):
    """Trim and format exception, maybe raise error, etc."""
    from .gen_gallery import _expected_failing_examples
    etype, exc, tb = exc_info
    stack = traceback.extract_tb(tb)
    # The full traceback will look something like:
    #
    #   File "/home/larsoner/python/sphinx-gallery/sphinx_gallery/gen_rst.py...
    #     mem_max, _ = gallery_conf['call_memory'](
    #   File "/home/larsoner/python/sphinx-gallery/sphinx_gallery/gen_galler...
    #     mem, out = memory_usage(func, max_usage=True, retval=True,
    #   File "/home/larsoner/.local/lib/python3.8/site-packages/memory_profi...
    #     returned = f(*args, **kw)
    #   File "/home/larsoner/python/sphinx-gallery/sphinx_gallery/gen_rst.py...
    #     exec(self.code, self.fake_main.__dict__)
    #   File "/home/larsoner/python/sphinx-gallery/sphinx_gallery/tests/tiny...
    #     raise RuntimeError('some error')
    # RuntimeError: some error
    #
    # But we should trim these to just the relevant trace at the user level,
    # so we inspect the traceback to find the start and stop points.
    start = 0
    stop = len(stack)
    root = os.path.dirname(__file__) + os.sep
    for ii, s in enumerate(stack, 1):
        # Trim our internal stack
        if s.filename.startswith(root + 'gen_gallery.py') and \
                s.name == 'call_memory':
            start = max(ii, start)
        elif s.filename.startswith(root + 'gen_rst.py'):
            # SyntaxError
            if s.name == 'execute_code_block' and ('compile(' in s.line or
                                                   'save_figures' in s.line):
                start = max(ii, start)
            # Any other error
            elif s.name == '__call__':
                start = max(ii, start)
            # Our internal input() check
            elif s.name == '_check_input' and ii == len(stack):
                stop = ii - 1
    stack = stack[start:stop]

    formatted_exception = 'Traceback (most recent call last):\n' + ''.join(
        traceback.format_list(stack) +
        traceback.format_exception_only(etype, exc))

    expected = src_file in _expected_failing_examples(gallery_conf)
    if expected:
        func, color = logger.info, 'blue',
    else:
        func, color = logger.warning, 'red'
    func('%s failed to execute correctly: %s', src_file,
         formatted_exception, color=color)

    except_rst = codestr2rst(formatted_exception, lang='pytb')

    # Breaks build on first example error
    if gallery_conf['abort_on_example_error']:
        raise
    # Stores failing file
    gallery_conf['failing_examples'][src_file] = formatted_exception
    script_vars['execute_script'] = False

    # Ensure it's marked as our style
    except_rst = ".. rst-class:: sphx-glr-script-out\n\n" + except_rst
    return except_rst


# Adapted from github.com/python/cpython/blob/3.7/Lib/warnings.py
def _showwarning(message, category, filename, lineno, file=None, line=None):
    if file is None:
        file = sys.stderr
        if file is None:
            # sys.stderr is None when run with pythonw.exe:
            # warnings get lost
            return
    text = warnings.formatwarning(message, category, filename, lineno, line)
    try:
        file.write(text)
    except OSError:
        # the file (probably stderr) is invalid - this warning gets lost.
        pass


@contextlib.contextmanager
def patch_warnings():
    """Patch warnings.showwarning to actually write out the warning."""
    # Sphinx or logging or someone is patching warnings, but we want to
    # capture them, so let's patch over their patch...
    orig_showwarning = warnings.showwarning
    try:
        warnings.showwarning = _showwarning
        yield
    finally:
        warnings.showwarning = orig_showwarning


class _exec_once(object):
    """Deal with memory_usage calling functions more than once (argh)."""

    def __init__(self, code, fake_main):
        self.code = code
        self.fake_main = fake_main
        self.run = False

    def __call__(self):
        if not self.run:
            self.run = True
            old_main = sys.modules.get('__main__', None)
            with patch_warnings():
                sys.modules['__main__'] = self.fake_main
                try:
                    exec(self.code, self.fake_main.__dict__)
                finally:
                    if old_main is not None:
                        sys.modules['__main__'] = old_main


def _get_memory_base(gallery_conf):
    """Get the base amount of memory used by running a Python process."""
    if not gallery_conf['plot_gallery']:
        return 0.
    # There might be a cleaner way to do this at some point
    from memory_profiler import memory_usage
    if sys.platform in ('win32', 'darwin'):
        sleep, timeout = (1, 2)
    else:
        sleep, timeout = (0.5, 1)
    proc = subprocess.Popen(
        [sys.executable, '-c',
            'import time, sys; time.sleep(%s); sys.exit(0)' % sleep],
        close_fds=True)
    memories = memory_usage(proc, interval=1e-3, timeout=timeout)
    kwargs = dict(timeout=timeout) if sys.version_info >= (3, 5) else {}
    proc.communicate(**kwargs)
    # On OSX sometimes the last entry can be None
    memories = [mem for mem in memories if mem is not None] + [0.]
    memory_base = max(memories)
    return memory_base


def execute_code_block(compiler, block, example_globals,
                       script_vars, gallery_conf):
    """Execute the code block of the example file."""
    if example_globals is None:  # testing shortcut
        example_globals = script_vars['fake_main'].__dict__
    blabel, bcontent, lineno = block
    # If example is not suitable to run, skip executing its blocks
    if not script_vars['execute_script'] or blabel == 'text':
        return ''

    cwd = os.getcwd()
    # Redirect output to stdout and

    src_file = script_vars['src_file']
    logging_tee = _check_reset_logging_tee(src_file)
    assert isinstance(logging_tee, _LoggingTee)

    # First cd in the original example dir, so that any file
    # created by the example get created in this directory

    os.chdir(os.path.dirname(src_file))

    sys_path = copy.deepcopy(sys.path)
    sys.path.append(os.getcwd())
    need_save_figures = True
    try:
        dont_inherit = 1
        if sys.version_info >= (3, 8):
            ast_Module = partial(ast.Module, type_ignores=[])
        else:
            ast_Module = ast.Module
        code_ast = ast_Module([bcontent])
        flags = ast.PyCF_ONLY_AST | compiler.flags
        code_ast = compile(bcontent, src_file, 'exec', flags, dont_inherit)
        ast.increment_lineno(code_ast, lineno - 1)
        # capture output if last line is expression
        is_last_expr = False
        if len(code_ast.body) and isinstance(code_ast.body[-1], ast.Expr):
            is_last_expr = True
            last_val = code_ast.body.pop().value
            # exec body minus last expression
            mem_body, _ = gallery_conf['call_memory'](
                _exec_once(
                    compiler(code_ast, src_file, 'exec'),
                    script_vars['fake_main']))
            # exec last expression, made into assignment
            body = [ast.Assign(
                targets=[ast.Name(id='___', ctx=ast.Store())], value=last_val)]
            last_val_ast = ast_Module(body=body)
            ast.fix_missing_locations(last_val_ast)
            mem_last, _ = gallery_conf['call_memory'](
                _exec_once(
                    compiler(last_val_ast, src_file, 'exec'),
                    script_vars['fake_main']))
            # capture the assigned variable
            ___ = example_globals['___']
            mem_max = max(mem_body, mem_last)
        else:
            mem_max, _ = gallery_conf['call_memory'](
                _exec_once(
                    compiler(code_ast, src_file, 'exec'),
                    script_vars['fake_main']))
        script_vars['memory_delta'].append(mem_max)
        # This should be inside the try block, e.g., in case of a savefig error
        logging_tee.restore_std()
        need_save_figures = False
        images_rst = save_figures(block, script_vars, gallery_conf)
    except Exception:
        logging_tee.restore_std()
        except_rst = handle_exception(sys.exc_info(), src_file, script_vars,
                                      gallery_conf)
        code_output = u"\n{0}\n\n\n\n".format(except_rst)
        # still call this even though we won't use the images so that
        # figures are closed
        if need_save_figures:
            save_figures(block, script_vars, gallery_conf)
    else:
        sys.path = sys_path
        os.chdir(cwd)

        last_repr = None
        repr_meth = None
        if is_last_expr:
            if gallery_conf['ignore_repr_types']:
                ignore_repr = re.search(
                    gallery_conf['ignore_repr_types'], str(type(___))
                )
            else:
                ignore_repr = False
            if gallery_conf['capture_repr'] != () and not ignore_repr:
                for meth in gallery_conf['capture_repr']:
                    try:
                        last_repr = getattr(___, meth)()
                        # for case when last statement is print()
                        if last_repr is None or last_repr == 'None':
                            repr_meth = None
                        else:
                            repr_meth = meth
                    except Exception:
                        pass
                    else:
                        if isinstance(last_repr, str):
                            break
        captured_std = logging_tee.output.getvalue().expandtabs()
        # normal string output
        if repr_meth in ['__repr__', '__str__'] and last_repr:
            captured_std = u"{0}\n{1}".format(captured_std, last_repr)
        if captured_std and not captured_std.isspace():
            captured_std = CODE_OUTPUT.format(indent(captured_std, u' ' * 4))
        else:
            captured_std = ''
        # give html output its own header
        if repr_meth == '_repr_html_':
            captured_html = html_header.format(indent(last_repr, u' ' * 4))
        else:
            captured_html = ''
        code_output = u"\n{0}\n\n{1}\n{2}\n\n".format(
            images_rst, captured_std, captured_html)

    finally:
        os.chdir(cwd)
        sys.path = sys_path
        logging_tee.restore_std()

    return code_output


def _check_reset_logging_tee(src_file):
    # Helper to deal with our tests not necessarily calling execute_script
    # but rather execute_code_block directly
    if isinstance(sys.stdout, _LoggingTee):
        logging_tee = sys.stdout
    else:
        logging_tee = _LoggingTee(src_file)
    logging_tee.set_std_and_reset_position()
    return logging_tee


def executable_script(src_file, gallery_conf):
    """Validate if script has to be run according to gallery configuration

    Parameters
    ----------
    src_file : str
        path to python script

    gallery_conf : dict
        Contains the configuration of Sphinx-Gallery

    Returns
    -------
    bool
        True if script has to be executed
    """

    filename_pattern = gallery_conf.get('filename_pattern')
    execute = re.search(filename_pattern, src_file) and gallery_conf[
        'plot_gallery']
    return execute


def _check_input(prompt=None):
    raise ExtensionError(
        'Cannot use input() builtin function in Sphinx-gallery examples')


def execute_script(script_blocks, script_vars, gallery_conf):
    """Execute and capture output from python script already in block structure

    Parameters
    ----------
    script_blocks : list
        (label, content, line_number)
        List where each element is a tuple with the label ('text' or 'code'),
        the corresponding content string of block and the leading line number
    script_vars : dict
        Configuration and run time variables
    gallery_conf : dict
        Contains the configuration of Sphinx-Gallery

    Returns
    -------
    output_blocks : list
        List of strings where each element is the restructured text
        representation of the output of each block
    time_elapsed : float
        Time elapsed during execution
    """
    # Examples may contain if __name__ == '__main__' guards
    # for in example scikit-learn if the example uses multiprocessing.
    # Here we create a new __main__ module, and temporarily change
    # sys.modules when running our example
    fake_main = importlib.util.module_from_spec(
        importlib.util.spec_from_loader('__main__', None))
    example_globals = fake_main.__dict__

    example_globals.update({
        # A lot of examples contains 'print(__doc__)' for example in
        # scikit-learn so that running the example prints some useful
        # information. Because the docstring has been separated from
        # the code blocks in sphinx-gallery, __doc__ is actually
        # __builtin__.__doc__ in the execution context and we do not
        # want to print it
        '__doc__': '',
        # Don't ever support __file__: Issues #166 #212
        # Don't let them use input()
        'input': _check_input,
    })
    script_vars['example_globals'] = example_globals

    argv_orig = sys.argv[:]
    if script_vars['execute_script']:
        # We want to run the example without arguments. See
        # https://github.com/sphinx-gallery/sphinx-gallery/pull/252
        # for more details.
        sys.argv[0] = script_vars['src_file']
        sys.argv[1:] = gallery_conf['reset_argv'](gallery_conf, script_vars)
        gc.collect()
        memory_start, _ = gallery_conf['call_memory'](lambda: None)
    else:
        memory_start = 0.

    t_start = time()
    compiler = codeop.Compile()
    # include at least one entry to avoid max() ever failing
    script_vars['memory_delta'] = [memory_start]
    script_vars['fake_main'] = fake_main
    output_blocks = list()
    with _LoggingTee(script_vars.get('src_file', '')) as logging_tee:
        for block in script_blocks:
            logging_tee.set_std_and_reset_position()
            output_blocks.append(execute_code_block(
                compiler, block, example_globals, script_vars, gallery_conf))
    time_elapsed = time() - t_start
    sys.argv = argv_orig
    script_vars['memory_delta'] = max(script_vars['memory_delta'])
    if script_vars['execute_script']:
        script_vars['memory_delta'] -= memory_start
        # Write md5 checksum if the example was meant to run (no-plot
        # shall not cache md5sum) and has built correctly
        with open(script_vars['target_file'] + '.md5', 'w') as file_checksum:
            file_checksum.write(get_md5sum(script_vars['target_file'], 't'))
        gallery_conf['passing_examples'].append(script_vars['src_file'])

    return output_blocks, time_elapsed


def generate_file_rst(fname, target_dir, src_dir, gallery_conf,
                      seen_backrefs=None):
    """Generate the rst file for a given example.

    Parameters
    ----------
    fname : str
        Filename of python script
    target_dir : str
        Absolute path to directory in documentation where examples are saved
    src_dir : str
        Absolute path to directory where source examples are stored
    gallery_conf : dict
        Contains the configuration of Sphinx-Gallery
    seen_backrefs : set
        The seen backreferences.

    Returns
    -------
    intro: str
        The introduction of the example
    cost : tuple
        A tuple containing the ``(time, memory)`` required to run the script.
    """
    seen_backrefs = set() if seen_backrefs is None else seen_backrefs
    src_file = os.path.normpath(os.path.join(src_dir, fname))
    target_file = os.path.join(target_dir, fname)
    _replace_md5(src_file, target_file, 'copy', mode='t')

    file_conf, script_blocks, node = split_code_and_text_blocks(
        src_file, return_node=True)
    intro, title = extract_intro_and_title(fname, script_blocks[0][1])
    gallery_conf['titles'][src_file] = title

    executable = executable_script(src_file, gallery_conf)

    if md5sum_is_current(target_file, mode='t'):
        if executable:
            gallery_conf['stale_examples'].append(target_file)
        return intro, title, (0, 0)

    image_dir = os.path.join(target_dir, 'images')
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    base_image_name = os.path.splitext(fname)[0]
    image_fname = 'sphx_glr_' + base_image_name + '_{0:03}.png'
    image_path_template = os.path.join(image_dir, image_fname)

    script_vars = {
        'execute_script': executable,
        'image_path_iterator': ImagePathIterator(image_path_template),
        'src_file': src_file,
        'target_file': target_file}

    if gallery_conf['remove_config_comments']:
        script_blocks = [
            (label, remove_config_comments(content), line_number)
            for label, content, line_number in script_blocks
        ]

    if executable:
        clean_modules(gallery_conf, fname)
    output_blocks, time_elapsed = execute_script(script_blocks,
                                                 script_vars,
                                                 gallery_conf)

    logger.debug("%s ran in : %.2g seconds\n", src_file, time_elapsed)

    example_rst = rst_blocks(script_blocks, output_blocks,
                             file_conf, gallery_conf)
    memory_used = gallery_conf['memory_base'] + script_vars['memory_delta']
    if not executable:
        time_elapsed = memory_used = 0.  # don't let the output change
    save_rst_example(example_rst, target_file, time_elapsed, memory_used,
                     gallery_conf, target_dir)

    save_thumbnail(image_path_template, src_file, file_conf, gallery_conf)

    example_nb = jupyter_notebook(script_blocks, gallery_conf, target_dir)
    ipy_fname = replace_py_ipynb(target_file) + '.new'
    save_notebook(example_nb, ipy_fname)
    _replace_md5(ipy_fname, mode='t')

    # Write names
    if gallery_conf['inspect_global_variables']:
        global_variables = script_vars['example_globals']
    else:
        global_variables = None
    example_code_obj = identify_names(script_blocks, global_variables, node)
    if example_code_obj:
        codeobj_fname = target_file[:-3] + '_codeobj.pickle.new'
        with open(codeobj_fname, 'wb') as fid:
            pickle.dump(example_code_obj, fid, pickle.HIGHEST_PROTOCOL)
        _replace_md5(codeobj_fname)
    backrefs = set('{module_short}.{name}'.format(**cobj)
                   for cobjs in example_code_obj.values()
                   for cobj in cobjs
                   if cobj['module'].startswith(gallery_conf['doc_module']))
    # Write backreferences
    _write_backreferences(backrefs, seen_backrefs, gallery_conf, target_dir,
                          fname, intro, title)

    return intro, title, (time_elapsed, memory_used)


def rst_blocks(script_blocks, output_blocks, file_conf, gallery_conf):
    """Generates the rst string containing the script prose, code and output

    Parameters
    ----------
    script_blocks : list
        (label, content, line_number)
        List where each element is a tuple with the label ('text' or 'code'),
        the corresponding content string of block and the leading line number
    output_blocks : list
        List of strings where each element is the restructured text
        representation of the output of each block
    file_conf : dict
        File-specific settings given in source file comments as:
        ``# sphinx_gallery_<name> = <value>``
    gallery_conf : dict
        Contains the configuration of Sphinx-Gallery

    Returns
    -------
    out : str
        rst notebook
    """

    # A simple example has two blocks: one for the
    # example introduction/explanation and one for the code
    is_example_notebook_like = len(script_blocks) > 2
    example_rst = u""  # there can be unicode content
    for (blabel, bcontent, lineno), code_output in \
            zip(script_blocks, output_blocks):
        if blabel == 'code':

            if not file_conf.get('line_numbers',
                                 gallery_conf.get('line_numbers', False)):
                lineno = None

            code_rst = codestr2rst(bcontent, lang=gallery_conf['lang'],
                                   lineno=lineno) + '\n'
            if is_example_notebook_like:
                example_rst += code_rst
                example_rst += code_output
            else:
                example_rst += code_output
                if 'sphx-glr-script-out' in code_output:
                    # Add some vertical space after output
                    example_rst += "\n\n|\n\n"
                example_rst += code_rst
        else:
            block_separator = '\n\n' if not bcontent.endswith('\n') else '\n'
            example_rst += bcontent + block_separator
    return example_rst


def save_rst_example(example_rst, example_file, time_elapsed,
                     memory_used, gallery_conf, target_dir):
    """Saves the rst notebook to example_file including header & footer

    Parameters
    ----------
    example_rst : str
        rst containing the executed file content
    example_file : str
        Filename with full path of python example file in documentation folder
    time_elapsed : float
        Time elapsed in seconds while executing file
    memory_used : float
        Additional memory used during the run.
    gallery_conf : dict
        Sphinx-Gallery configuration dictionary
    target_dir : str
        Absolute path to directory in documentation where examples are saved.
    """

    ref_fname = os.path.relpath(example_file, gallery_conf['src_dir'])
    ref_fname = ref_fname.replace(os.path.sep, "_")

    binder_conf = check_binder_conf(gallery_conf.get('binder'))

    binder_text = (" or to run this example in your browser via Binder"
                   if len(binder_conf) else "")
    example_rst = (".. only:: html\n\n"
                   "    .. note::\n"
                   "        :class: sphx-glr-download-link-note\n\n"
                   "        Click :ref:`here <sphx_glr_download_{0}>` "
                   "    to download the full example code{1}\n"
                   "    .. rst-class:: sphx-glr-example-title\n\n"
                   "    .. _sphx_glr_{0}:\n\n"
                   ).format(ref_fname, binder_text) + example_rst

    if time_elapsed >= gallery_conf["min_reported_time"]:
        time_m, time_s = divmod(time_elapsed, 60)
        example_rst += TIMING_CONTENT.format(time_m, time_s)
    if gallery_conf['show_memory']:
        example_rst += ("**Estimated memory usage:** {0: .0f} MB\n\n"
                        .format(memory_used))

    # Generate a binder URL if specified
    binder_badge_rst = ''
    if len(binder_conf) > 0:
        binder_badge_rst += gen_binder_rst(example_file, binder_conf,
                                           gallery_conf, target_dir)

    fname = os.path.basename(example_file)
    example_rst += CODE_DOWNLOAD.format(fname,
                                        replace_py_ipynb(fname),
                                        binder_badge_rst,
                                        ref_fname)
    example_rst += SPHX_GLR_SIG

    write_file_new = re.sub(r'\.py$', '.rst.new', example_file)
    with codecs.open(write_file_new, 'w', encoding="utf-8") as f:
        f.write(example_rst)
    # in case it wasn't in our pattern, only replace the file if it's
    # still stale.
    _replace_md5(write_file_new, mode='t')
