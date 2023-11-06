"""Sphinx-Gallery documentation build configuration file."""

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
from datetime import date
import warnings

import sphinx_gallery
from sphinx_gallery.sorting import FileNameSortKey, FunctionSortKey
from sphinx_gallery.notebook import add_markdown_cell, add_code_cell

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx_gallery.gen_gallery",
    "sphinx.ext.graphviz",
    "jupyterlite_sphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# generate autosummary even if no references
autosummary_generate = True

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Sphinx-Gallery"
copyright = "2014-%s, Sphinx-gallery developers" % date.today().year

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = sphinx_gallery.__version__
# The full version, including alpha/beta/rc tags.
release = sphinx_gallery.__version__ + "-git"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# See warnings about bad links
nitpicky = True
nitpick_ignore = [("", "Pygments lexer name 'ipython' is not known")]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
highlight_language = "python3"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# The theme is set by the make target
html_theme = "pydata_sphinx_theme"


def setup(app):
    """Sphinx setup function."""
    app.add_css_file("theme_override.css")
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "navbar_center": ["navbar-nav"],
    "show_toc_level": 2,
    "show_nav_level": 2,
    "navbar_end": ["theme-switcher", "version-switcher", "navbar-icon-links"],
    "navigation_with_keys": False,
    "logo": {
        "text": "🖼️ Sphinx-Gallery",
    },
    "switcher": dict(
        json_url="https://sphinx-gallery.github.io/dev/_static/switcher.json",
        version_match="dev" if "dev" in version else "stable",
    ),
    "github_url": "https://github.com/sphinx-gallery/sphinx-gallery",
    "icon_links": [
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/sphinx-gallery",
            "icon": "fa-solid fa-box",
        },
    ],
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    "reference": [],
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "Sphinx-Gallerydoc"


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
    (
        "index",
        "Sphinx-Gallery.tex",
        "Sphinx-Gallery Documentation",
        "Óscar Nájera",
        "manual",
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ("index", "sphinx-gallery", "Sphinx-Gallery Documentation", ["Óscar Nájera"], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "Sphinx-Gallery",
        "Sphinx-Gallery Documentation",
        "Óscar Nájera",
        "Sphinx-Gallery",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": (f"https://docs.python.org/{sys.version_info.major}", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "pyvista": ("https://docs.pyvista.org/version/stable", None),
    "sklearn": ("https://scikit-learn.org/stable", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
}

examples_dirs = ["../examples", "../tutorials"]
gallery_dirs = ["auto_examples", "tutorials"]


image_scrapers = ("matplotlib",)
try:
    # Run the PyVista examples and find the PyVista figures if PyVista is
    # installed
    import pyvista
except Exception:  # can raise all sorts of errors
    pass
else:
    image_scrapers += ("pyvista",)
    examples_dirs.append("../pyvista_examples")
    gallery_dirs.append("auto_pyvista_examples")
    pyvista.OFF_SCREEN = True
    # Preferred plotting style for documentation
    pyvista.set_plot_theme("document")
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
    import plotly.io
except ImportError:
    pass
else:
    plotly.io.renderers.default = "sphinx_gallery"
    examples_dirs.append("../plotly_examples")
    gallery_dirs.append("auto_plotly_examples")

min_reported_time = 0
if "SOURCE_DATE_EPOCH" in os.environ:
    min_reported_time = sys.maxint if sys.version_info[0] == 2 else sys.maxsize


def notebook_modification_function(notebook_content, notebook_filename):
    """Implement JupyterLite-specific modifications of notebooks."""
    notebook_content_str = str(notebook_content)
    warning_template = "\n".join(
        [
            "<div class='alert alert-{message_class}'>",
            "",
            "# JupyterLite warning",
            "",
            "{message}",
            "</div>",
        ]
    )

    if "pyvista_examples" in notebook_filename:
        message_class = "danger"
        message = (
            "PyVista is not packaged in Pyodide, this notebook is not "
            "expected to work inside JupyterLite"
        )
    elif "import plotly" in notebook_content_str:
        message_class = "danger"
        message = (
            "This notebook is not expected to work inside JupyterLite for now."
            " There seems to be some issues with Plotly, see "
            "[this]('https://github.com/jupyterlite/jupyterlite/pull/950') "
            "for more details."
        )
    else:
        message_class = "warning"
        message = (
            "JupyterLite integration in sphinx-gallery is beta "
            "and it may break in unexpected ways"
        )

    markdown = warning_template.format(message_class=message_class, message=message)

    dummy_notebook_content = {"cells": []}
    add_markdown_cell(dummy_notebook_content, markdown)

    code_lines = []

    if "seaborn" in notebook_content_str:
        code_lines.append("%pip install seaborn")

    if code_lines:
        code_lines = ["# JupyterLite-specific code"] + code_lines
        code = "\n".join(code_lines)
        add_code_cell(dummy_notebook_content, code)

    notebook_content["cells"] = (
        dummy_notebook_content["cells"] + notebook_content["cells"]
    )


sphinx_gallery_conf = {
    "backreferences_dir": "gen_modules/backreferences",
    "doc_module": ("sphinx_gallery", "numpy"),
    "reference_url": {
        "sphinx_gallery": None,
    },
    "examples_dirs": examples_dirs,
    "gallery_dirs": gallery_dirs,
    "image_scrapers": image_scrapers,
    "compress_images": ("images", "thumbnails"),
    # specify the order of examples to be according to filename
    "within_subsection_order": FileNameSortKey,
    # put duplicate figure at end
    "minigallery_sort_order": FunctionSortKey(
        lambda x: (not x.startswith("plot_4b"), x)
    ),
    "expected_failing_examples": [
        "../examples/no_output/plot_raise.py",
        "../examples/no_output/plot_syntaxerror.py",
    ],
    "min_reported_time": min_reported_time,
    "binder": {
        "org": "sphinx-gallery",
        "repo": "sphinx-gallery.github.io",
        "branch": "master",
        "binderhub_url": "https://mybinder.org",
        "dependencies": "./binder/requirements.txt",
        "notebooks_dir": "notebooks",
        "use_jupyter_lab": True,
    },
    "jupyterlite": {"notebook_modification_function": notebook_modification_function},
    "show_memory": True,
    "promote_jupyter_magic": False,
    "junit": os.path.join("sphinx-gallery", "junit-results.xml"),
    # capture raw HTML or, if not present, __repr__ of last expression in
    # each code block
    "capture_repr": ("_repr_html_", "__repr__"),
    "matplotlib_animations": True,
    "image_srcset": ["2x"],
    "nested_sections": False,
    "show_api_usage": True,
}

# Remove matplotlib agg warnings from generated doc when using plt.show
warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    message="Matplotlib is currently using agg, which is a"
    " non-GUI backend, so cannot show the figure.",
)
