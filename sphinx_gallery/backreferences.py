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

from . import sphinx_compatibility
from .scrapers import _find_image_ext
from .utils import _replace_md5
from .py_source_parser import parse_source_file, split_code_and_text_blocks


class NameFinder(ast.NodeVisitor):
    """Finds the longest form of variable names and their imports in code.

    Only retains names from imported modules.
    """

    def __init__(self):
        super(NameFinder, self).__init__()
        self.imported_names = {}
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
            if local_name in self.imported_names:
                # Join import path to relative path
                full_name = self.imported_names[local_name] + remainder
                yield name, full_name


def _get_short_module_name(module_name, obj_name):
    """Get the shortest possible module name."""
    scope = {}
    try:
        # Find out what the real object is supposed to be.
        exec('from %s import %s' % (module_name, obj_name), scope, scope)
        real_obj = scope[obj_name]
    except Exception:
        return module_name

    parts = module_name.split('.')
    short_name = module_name
    for i in range(len(parts) - 1, 0, -1):
        short_name = '.'.join(parts[:i])
        scope = {}
        try:
            exec('from %s import %s' % (short_name, obj_name), scope, scope)
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


def _identify_names(script_blocks):
    """Build a codeobj summary by identifying and resolving used names."""
    finder = NameFinder()
    names = list()
    for script_block in script_blocks:
        kind, txt, _ = script_block
        # Get matches from the code (AST)
        if kind == 'code':
            node = ast.parse(txt)
            finder.visit(node)
        # Get matches from docstring inspection
        else:
            assert script_block[0] == 'text'
            names.extend((x, x) for x in re.findall(_regex, script_block[1]))
    names.extend(list(finder.get_mapping()))

    example_code_obj = collections.OrderedDict()
    for name, full_name in names:
        if name in example_code_obj:
            continue  # if someone puts it in the docstring and code
        # name is as written in file (e.g. np.asarray)
        # full_name includes resolved import path (e.g. numpy.asarray)
        splitted = full_name.rsplit('.', 1)
        if len(splitted) == 1:
            # module without attribute. This is not useful for
            # backreferences
            continue

        module, attribute = splitted
        # get shortened module name
        module_short = _get_short_module_name(module, attribute)
        cobj = {'name': attribute, 'module': module,
                'module_short': module_short}
        example_code_obj[name] = cobj
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
