# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Backreferences Generator
========================

Parses example file code in order to keep track of used functions
"""
from __future__ import print_function, unicode_literals

import ast
import codecs
import collections
from html import escape
import os
import re
import warnings

from . import sphinx_compatibility
from .scrapers import _find_image_ext
from .utils import _replace_md5


class NameFinder(ast.NodeVisitor):
    """Finds the longest form of variable names and their imports in code.

    Only retains names from imported modules.
    """

    def __init__(self, global_variables=None):
        super(NameFinder, self).__init__()
        self.imported_names = {}
        self.global_variables = global_variables or {}
        self.accessed_names = set()

    def visit_Import(self, node, prefix=''):
        for alias in node.names:
            local_name = alias.asname or alias.name
            self.imported_names[local_name] = prefix + alias.name

    def visit_ImportFrom(self, node):
        self.visit_Import(node, node.module + '.')

    def visit_Name(self, node):
        self.accessed_names.add(node.id)

    def visit_Attribute(self, node):
        attrs = []
        while isinstance(node, ast.Attribute):
            attrs.append(node.attr)
            node = node.value

        if isinstance(node, ast.Name):
            # This is a.b, not e.g. a().b
            attrs.append(node.id)
            self.accessed_names.add('.'.join(reversed(attrs)))
        else:
            # need to get a in a().b
            self.visit(node)

    def get_mapping(self):
        for name in self.accessed_names:
            local_name = name.split('.', 1)[0]
            remainder = name[len(local_name):]
            class_attr = False
            if local_name in self.imported_names:
                # Join import path to relative path
                full_name = self.imported_names[local_name] + remainder
                yield name, full_name, class_attr
            elif local_name in self.global_variables:
                obj = self.global_variables[local_name]
                if remainder and remainder[0] == '.':  # maybe meth or attr
                    method = [remainder[1:]]
                    class_attr = True
                else:
                    method = []
                # Recurse through all levels of bases
                classes = [obj.__class__]
                offset = 0
                while offset < len(classes):
                    for base in classes[offset].__bases__:
                        if base not in classes:
                            classes.append(base)
                    offset += 1
                for cc in classes:
                    module = cc.__module__.split('.')
                    class_name = cc.__name__
                    # a.b.C.meth could be documented as a.C.meth,
                    # so go down the list
                    for depth in range(len(module), 0, -1):
                        full_name = '.'.join(
                            module[:depth] + [class_name] + method)
                        yield name, full_name, class_attr


def _from_import(a, b):
    imp_line = 'from %s import %s' % (a, b)
    scope = dict()
    with warnings.catch_warnings(record=True):  # swallow warnings
        warnings.simplefilter('ignore')
        exec(imp_line, scope, scope)
    return scope


def _get_short_module_name(module_name, obj_name):
    """Get the shortest possible module name."""
    if '.' in obj_name:
        obj_name, attr = obj_name.split('.')
    else:
        attr = None
    scope = {}
    try:
        # Find out what the real object is supposed to be.
        scope = _from_import(module_name, obj_name)
    except Exception:  # wrong object
        return None
    else:
        real_obj = scope[obj_name]
        if attr is not None and not hasattr(real_obj, attr):  # wrong class
            return None  # wrong object

    parts = module_name.split('.')
    short_name = module_name
    for i in range(len(parts) - 1, 0, -1):
        short_name = '.'.join(parts[:i])
        scope = {}
        try:
            scope = _from_import(short_name, obj_name)
            # Ensure shortened object is the same as what we expect.
            assert real_obj is scope[obj_name]
        except Exception:  # libraries can throw all sorts of exceptions...
            # get the last working module name
            short_name = '.'.join(parts[:(i + 1)])
            break
    return short_name


_regex = re.compile(r':(?:'
                    r'func(?:tion)?|'
                    r'meth(?:od)?|'
                    r'attr(?:ibute)?|'
                    r'obj(?:ect)?|'
                    r'class):`(\S*)`'
                    )


def identify_names(script_blocks, global_variables=None, node=''):
    """Build a codeobj summary by identifying and resolving used names."""
    if node == '':  # mostly convenience for testing functions
        c = '\n'.join(txt for kind, txt, _ in script_blocks if kind == 'code')
        node = ast.parse(c)
    # Get matches from the code (AST)
    finder = NameFinder(global_variables)
    if node is not None:
        finder.visit(node)
    names = list(finder.get_mapping())
    # Get matches from docstring inspection
    text = '\n'.join(txt for kind, txt, _ in script_blocks if kind == 'text')
    names.extend((x, x, False) for x in re.findall(_regex, text))
    example_code_obj = collections.OrderedDict()  # order is important
    fill_guess = dict()
    for name, full_name, class_like in names:
        if name in example_code_obj:
            continue  # if someone puts it in the docstring and code
        # name is as written in file (e.g. np.asarray)
        # full_name includes resolved import path (e.g. numpy.asarray)
        splitted = full_name.rsplit('.', 1 + class_like)
        if len(splitted) == 1:
            splitted = ('builtins', splitted[0])
        elif len(splitted) == 3:  # class-like
            assert class_like
            splitted = (splitted[0], '.'.join(splitted[1:]))
        else:
            assert not class_like

        module, attribute = splitted
        # get shortened module name
        module_short = _get_short_module_name(module, attribute)
        cobj = {'name': attribute, 'module': module,
                'module_short': module_short}
        if module_short is not None:
            example_code_obj[name] = cobj
        elif name not in fill_guess:
            cobj['module_short'] = module
            fill_guess[name] = cobj
    for key, value in fill_guess.items():
        if key not in example_code_obj:
            example_code_obj[key] = value
    return example_code_obj


THUMBNAIL_TEMPLATE = """
.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="{snippet}">

.. only:: html

 .. figure:: /{thumbnail}

     :ref:`sphx_glr_{ref_name}`

.. raw:: html

    </div>
"""

BACKREF_THUMBNAIL_TEMPLATE = THUMBNAIL_TEMPLATE + """
.. only:: not html

 * :ref:`sphx_glr_{ref_name}`
"""


def _thumbnail_div(target_dir, src_dir, fname, snippet, is_backref=False,
                   check=True):
    """Generate RST to place a thumbnail in a gallery."""
    thumb, _ = _find_image_ext(
        os.path.join(target_dir, 'images', 'thumb',
                     'sphx_glr_%s_thumb.png' % fname[:-3]))
    if check and not os.path.isfile(thumb):
        # This means we have done something wrong in creating our thumbnail!
        raise RuntimeError('Could not find internal sphinx-gallery thumbnail '
                           'file:\n%s' % (thumb,))
    thumb = os.path.relpath(thumb, src_dir)
    full_dir = os.path.relpath(target_dir, src_dir)

    # Inside rst files forward slash defines paths
    thumb = thumb.replace(os.sep, "/")

    ref_name = os.path.join(full_dir, fname).replace(os.path.sep, '_')

    template = BACKREF_THUMBNAIL_TEMPLATE if is_backref else THUMBNAIL_TEMPLATE
    return template.format(snippet=escape(snippet),
                           thumbnail=thumb, ref_name=ref_name)


def _write_backreferences(backrefs, seen_backrefs, gallery_conf,
                          target_dir, fname, snippet):
    """Write backreference file including a thumbnail list of examples."""
    if gallery_conf['backreferences_dir'] is None:
        return

    for backref in backrefs:
        include_path = os.path.join(gallery_conf['src_dir'],
                                    gallery_conf['backreferences_dir'],
                                    '%s.examples.new' % backref)
        seen = backref in seen_backrefs
        with codecs.open(include_path, 'a' if seen else 'w',
                         encoding='utf-8') as ex_file:
            if not seen:
                heading = 'Examples using ``%s``' % backref
                ex_file.write('\n\n' + heading + '\n')
                ex_file.write('^' * len(heading) + '\n')
            ex_file.write(_thumbnail_div(target_dir, gallery_conf['src_dir'],
                                         fname, snippet, is_backref=True))
            seen_backrefs.add(backref)


def _finalize_backreferences(seen_backrefs, gallery_conf):
    """Replace backref files only if necessary."""
    logger = sphinx_compatibility.getLogger('sphinx-gallery')
    if gallery_conf['backreferences_dir'] is None:
        return

    for backref in seen_backrefs:
        path = os.path.join(gallery_conf['src_dir'],
                            gallery_conf['backreferences_dir'],
                            '%s.examples.new' % backref)
        if os.path.isfile(path):
            _replace_md5(path)
        else:
            level = gallery_conf['log_level'].get('backreference_missing',
                                                  'warning')
            func = getattr(logger, level)
            func('Could not find backreferences file: %s' % (path,))
            func('The backreferences are likely to be erroneous '
                 'due to file system case insensitivity.')
