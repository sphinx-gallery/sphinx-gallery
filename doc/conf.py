# -*- coding: utf-8 -*-
#
# Sphinx-Gallery documentation build configuration file, created by
# sphinx-quickstart on Mon Nov 17 16:01:26 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import codecs
from datetime import date
import warnings

import sphinx_gallery
from sphinx_gallery.sorting import FileNameSortKey
import sphinx_rtd_theme

logger = sphinx_gallery.sphinx_compatibility.getLogger('sphinx-gallery')

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx_gallery.gen_gallery',
    'sphinx.ext.graphviz',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# generate autosummary even if no references
autosummary_generate = True

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Sphinx-Gallery'
copyright = u'2014-%s, Sphinx-gallery developers' % date.today().year

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = sphinx_gallery.__version__
# The full version, including alpha/beta/rc tags.
release = sphinx_gallery.__version__ + '-git'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# See warnings about bad links
nitpicky = True
nitpick_ignore = [('', "Pygments lexer name 'ipython' is not known")]

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
highlight_language = 'python3'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# The theme is set by the make target
html_theme = os.environ.get('SPHX_GLR_THEME', 'rtd')

# on_rtd is whether we are on readthedocs.org, this line of code grabbed
# from docs.readthedocs.org
if html_theme == 'rtd':
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


def setup(app):
    """Sphinx setup function."""
    app.add_css_file('theme_override.css')
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')
    app.connect('autodoc-process-docstring', write_api_entries)
    app.connect('doctree-resolved', write_api_entry_usage)

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Sphinx-Gallerydoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'Sphinx-Gallery.tex', u'Sphinx-Gallery Documentation',
     u'Óscar Nájera', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'sphinx-gallery', u'Sphinx-Gallery Documentation',
     [u'Óscar Nájera'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'Sphinx-Gallery', u'Sphinx-Gallery Documentation',
     u'Óscar Nájera', 'Sphinx-Gallery', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(sys.version_info), None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'matplotlib': ('https://matplotlib.org/stable', None),
    'mayavi': ('http://docs.enthought.com/mayavi/mayavi', None),
    'pyvista': ('https://docs.pyvista.org/', None),
    'sklearn': ('https://scikit-learn.org/stable', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
}

examples_dirs = ['../examples', '../tutorials']
gallery_dirs = ['auto_examples', 'tutorials']


image_scrapers = ('matplotlib',)
try:
    # Run the mayavi examples and find the mayavi figures if mayavi is
    # installed
    from mayavi import mlab
except Exception:  # can raise all sorts of errors
    image_scrapers = ('matplotlib',)
else:
    image_scrapers += ('mayavi',)
    examples_dirs.append('../mayavi_examples')
    gallery_dirs.append('auto_mayavi_examples')
    # Do not pop up any mayavi windows while running the
    # examples. These are very annoying since they steal the focus.
    mlab.options.offscreen = True

try:
    # Run the PyVista examples and find the PyVista figures if PyVista is
    # installed
    import pyvista
except Exception:  # can raise all sorts of errors
    pass
else:
    image_scrapers += ('pyvista',)
    examples_dirs.append('../pyvista_examples')
    gallery_dirs.append('auto_pyvista_examples')
    pyvista.OFF_SCREEN = True
    # Preferred plotting style for documentation
    pyvista.set_plot_theme('document')
    pyvista.global_theme.window_size = [1024, 768]
    pyvista.global_theme.font.size = 22
    pyvista.global_theme.font.label_size = 22
    pyvista.global_theme.font.title_size = 22
    pyvista.global_theme.return_cpos = False
    # necessary when building the sphinx gallery
    pyvista.BUILDING_GALLERY = True
    pyvista.set_jupyter_backend(None)

# Set plotly renderer to capture _repr_html_ for sphinx-gallery
try:
    import plotly.io.renderers
except ImportError:
    pass
else:
    plotly.io.renderers.default = 'sphinx_gallery'

min_reported_time = 0
if 'SOURCE_DATE_EPOCH' in os.environ:
    min_reported_time = sys.maxint if sys.version_info[0] == 2 else sys.maxsize

sphinx_gallery_conf = {
    'backreferences_dir': 'gen_modules/backreferences',
    'doc_module': ('sphinx_gallery', 'numpy'),
    'reference_url': {
        'sphinx_gallery': None,
    },
    'examples_dirs': examples_dirs,
    'gallery_dirs': gallery_dirs,
    'image_scrapers': image_scrapers,
    'compress_images': ('images', 'thumbnails'),
    # specify the order of examples to be according to filename
    'within_subsection_order': FileNameSortKey,
    'expected_failing_examples': ['../examples/no_output/plot_raise.py',
                                  '../examples/no_output/plot_syntaxerror.py'],
    'min_reported_time': min_reported_time,
    'binder': {'org': 'sphinx-gallery',
               'repo': 'sphinx-gallery.github.io',
               'branch': 'master',
               'binderhub_url': 'https://mybinder.org',
               'dependencies': './binder/requirements.txt',
               'notebooks_dir': 'notebooks',
               'use_jupyter_lab': True,
               },
    'show_memory': True,
    'promote_jupyter_magic': False,
    'junit': os.path.join('sphinx-gallery', 'junit-results.xml'),
    # capture raw HTML or, if not present, __repr__ of last expression in
    # each code block
    'capture_repr': ('_repr_html_', '__repr__'),
    'matplotlib_animations': True,
    'image_srcset': ["2x"],
    'nested_sections': False,
}

# Remove matplotlib agg warnings from generated doc when using plt.show
warnings.filterwarnings("ignore", category=UserWarning,
                        message='Matplotlib is currently using agg, which is a'
                                ' non-GUI backend, so cannot show the figure.')

html_context = {
    'current_version': 'dev' if 'dev' in version else 'stable',
    'versions': (
        ('dev', 'https://sphinx-gallery.github.io/dev'),
        ('stable', 'https://sphinx-gallery.github.io/stable'),
    )
}

def write_api_entries(app, what, name, obj, options, lines):
    """Write unused API entries and API usage in gallery."""
    if 'api_entries' not in app.config.sphinx_gallery_conf:
        app.config.sphinx_gallery_conf['api_entries'] = dict()
    if what not in app.config.sphinx_gallery_conf['api_entries']:
        app.config.sphinx_gallery_conf['api_entries'][what] = set()
    app.config.sphinx_gallery_conf['api_entries'][what].add(name)


def write_api_entry_usage(app, doctree, docname):
    gallery_conf = app.config.sphinx_gallery_conf
    for gallery_dir in gallery_conf['gallery_dirs']:
        target_dir = os.path.join(app.builder.srcdir, gallery_dir)
        _write_api_entry_usage(gallery_conf, target_dir)


SPHX_GLR_ORPHAN = """
:orphan:

.. _{0}:

"""


def _write_api_entry_usage(gallery_conf, target_dir):
    import pdb; pdb.set_trace()
    if gallery_conf['backreferences_dir'] is None:
        return

    backreferences_dir = os.path.join(gallery_conf['src_dir'],
                                      gallery_conf['backreferences_dir'])
    try:
        import graphviz
        has_graphviz = True
    except ImportError:
        logger.info('`graphviz` required for graphical visualization')
        has_graphviz = False

    example_files = set.union(
        *[gallery_conf['api_entries'][obj_type]
          for obj_type in ('class', 'method', 'function')])

    total_count = len(example_files)

    if total_count == 0:
        return

    def get_entry_type(entry):
        if entry in gallery_conf['api_entries']['class']:
            return 'class'
        elif entry in gallery_conf['api_entries']['method']:
            return 'meth'
        else:
            assert entry in gallery_conf['api_entries']['function']
            return 'func'

    target_dir_clean = os.path.relpath(
        target_dir, gallery_conf['src_dir']).replace(os.path.sep, '_')
    new_ref = 'sphx_glr_%s_sg_api_usage' % target_dir_clean
    replace_count = len('sphx_glr_' + os.path.basename(target_dir) + '_')
    with codecs.open(os.path.join(target_dir, 'sg_api_usage.rst'), 'w',
                     encoding='utf-8') as fid:
        fid.write(SPHX_GLR_ORPHAN.format(new_ref))
        unused_api_entries = list()
        used_api_entries = dict()
        for entry in example_files:
            # check if backreferences empty
            example_fname = os.path.join(
                backreferences_dir, f'{entry}.examples.new')
            if not os.path.isfile(example_fname):  # use without new
                example_fname = os.path.splitext(example_fname)[0]
            assert os.path.isfile(example_fname)
            if os.path.getsize(example_fname) == 0:
                unused_api_entries.append(entry)
            else:
                used_api_entries[entry] = list()
                with open(example_fname, 'r', encoding='utf-8') as fid2:
                    for line in fid2:
                        if line.startswith('  :ref:'):
                            example_name = line.split('`')[1]
                            used_api_entries[entry].append(example_name)

        title = 'Unused API Entries'
        fid.write(title + '\n' + '^' * len(title) + '\n\n')
        for entry in sorted(unused_api_entries):
            fid.write(f'- :{get_entry_type(entry)}:`{entry}`\n')
        fid.write('\n\n')

        unused_dot_fname = os.path.join(target_dir, 'sg_api_unused.dot')
        if has_graphviz and unused_api_entries:
            fid.write('.. graphviz:: ./sg_api_unused.dot\n'
                      '    :alt: API unused entries graph\n'
                      '    :layout: neato\n\n')

        used_count = len(used_api_entries)
        used_percentage = used_count / total_count
        fid.write('\nAPI entries used: '
                  f'{round(used_percentage * 100, 2)}% '
                  f'({used_count}/{total_count})\n\n')

        title = 'Used API Entries'
        fid.write(title + '\n' + '^' * len(title) + '\n\n')
        for entry in sorted(used_api_entries):
            fid.write(f'- :{get_entry_type(entry)}:`{entry}`\n\n')
            for ref in used_api_entries[entry]:
                fid.write(f'  - :ref:`{ref}`\n')
            fid.write('\n\n')

        used_dot_fname = os.path.join(target_dir, '{}_sg_api_used.dot')
        if has_graphviz and used_api_entries:
            used_modules = set([os.path.splitext(entry)[0]
                                for entry in used_api_entries])
            for module in sorted(used_modules):
                fid.write(f'{module}\n' + '^' * len(module) + '\n'
                          f'.. graphviz:: ./{module}_sg_api_used.dot\n'
                          f'    :alt: {module} usage graph\n'
                          '    :layout: neato\n\n')

        def make_graph(fname, entries):
            dg = graphviz.Digraph(filename=fname,
                                  node_attr={'color': 'lightblue2',
                                             'style': 'filled',
                                             'fontsize': '40'})

            if isinstance(entries, list):
                connections = set()
                lut = dict()
                structs = [entry.split('.') for entry in entries]
                for struct in sorted(structs, key=len):
                    for level in range(len(struct) - 2):
                        if (struct[level], struct[level + 1]) in connections:
                            continue
                        connections.add((struct[level], struct[level + 1]))
                        node_from = lut[struct[level]] if \
                            struct[level] in lut else struct[level]
                        dg.attr('node', color='lightblue2')
                        dg.node(node_from)
                        node_to = struct[level + 1]
                        # count, don't show leaves
                        if len(struct) - 3 == level:
                            leaf_count = 0
                            for struct2 in structs:
                                # find structures of the same length as struct
                                if len(struct2) != level + 3:
                                    continue
                                # find structures with two entries before
                                # the leaf that are the same as struct
                                if all([struct2[level2] == struct[level2]
                                        for level2 in range(level + 2)]):
                                    leaf_count += 1
                            node_to += f'\n({leaf_count})'
                            lut[struct[level + 1]] = node_to
                            if leaf_count > 10:
                                color = 'red'
                            elif leaf_count > 5:
                                color = 'orange'
                            else:
                                color = 'yellow'
                            dg.attr('node', color=color)
                        else:
                            dg.attr('node', color='lightblue2')
                        dg.node(node_to)
                        dg.edge(node_from, node_to)
                # add modules with all API entries
                dg.attr('node', color='lightblue2')
                for module in gallery_conf['api_entries']['module']:
                    struct = module.split('.')
                    for i in range(len(struct) - 1):
                        if struct[i + 1] not in lut:
                            dg.edge(struct[i], struct[i + 1])
            else:
                assert isinstance(entries, dict)
                for entry, refs in entries.items():
                    dg.attr('node', color='lightblue2')
                    dg.node(entry)
                    dg.attr('node', color='yellow')
                    for ref in refs:
                        dg.node(ref[replace_count:])
                        dg.edge(entry, ref[replace_count:])

            dg.attr(overlap='scale')
            dg.save(fname)

        # design graph
        if has_graphviz and unused_api_entries:
            make_graph(unused_dot_fname, unused_api_entries)

        if has_graphviz and used_api_entries:
            for module in used_modules:
                logger.info(f'Making API usage graph for {module}')
                entries = {entry: ref for entry, ref in
                           used_api_entries.items()
                           if os.path.splitext(entry)[0] == module}
                make_graph(used_dot_fname.format(module), entries)
