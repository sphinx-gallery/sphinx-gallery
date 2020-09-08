import os.path as op
import numpy as np
from sphinx_gallery.scrapers import matplotlib_scraper
from sphinx_gallery.sorting import FileNameSortKey


class matplotlib_format_scraper(object):

    def __repr__(self):
        return self.__class__.__name__

    def __call__(self, block, block_vars, gallery_conf):
        kwargs = dict()
        if op.basename(block_vars['target_file']) == 'plot_svg.py' and \
                gallery_conf['builder_name'] != 'latex':
            kwargs['format'] = 'svg'
        return matplotlib_scraper(block, block_vars, gallery_conf, **kwargs)


class ResetArgv:
    def __repr__(self):
        return "ResetArgv"

    def __call__(self, sphinx_gallery_conf, script_vars):
        if 'plot_command_line_args.py' in script_vars['src_file']:
            return ['plot']
        else:
            return []


class MockScrapeProblem:

    def __init__(self):
        from matplotlib.figure import Figure
        self._orig_mpl = Figure.savefig

    def __repr__(self):
        return "MockScrapeProblem"

    def __call__(self, gallery_conf, fname):
        from matplotlib.figure import Figure
        if 'scraper_broken' in fname:
            Figure.savefig = lambda *args, **kwargs: np.min([])
        else:
            Figure.savefig = self._orig_mpl


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_gallery.gen_gallery',
]
templates_path = ['_templates']
autosummary_generate = True
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'joblib': ('https://joblib.readthedocs.io/en/latest', None),
}
sphinx_gallery_conf = {
    'doc_module': ('sphinx_gallery',),
    'reference_url': {
        'sphinx_gallery': None,
        'scipy': 'http://docs.scipy.org/doc/scipy/wrong_url',  # bad one
    },
    'binder': {'org': 'sphinx-gallery',
               'repo': 'sphinx-gallery.github.io',
               'branch': 'master',
               'binderhub_url': 'https://mybinder.org',
               'dependencies': './binder/requirements.txt',
               'notebooks_dir': 'notebooks',
               'use_jupyter_lab': True,
               },
    'examples_dirs': ['examples/'],
    'reset_argv': ResetArgv(),
    'reset_modules': (MockScrapeProblem(), 'matplotlib'),
    'gallery_dirs': ['auto_examples'],
    'backreferences_dir': 'gen_modules/backreferences',
    'within_section_order': FileNameSortKey,
    'image_scrapers': (matplotlib_format_scraper(),),
    'expected_failing_examples': [
        'examples/future/plot_future_imports_broken.py',
        'examples/plot_scraper_broken.py',
    ],
    'show_memory': True,
    'compress_images': ('images', 'thumbnails'),
    'junit': op.join('sphinx-gallery', 'junit-results.xml'),
    'matplotlib_animations': True,
    'pypandoc': True,
}
nitpicky = True
highlight_language = 'python3'
html_static_path = ['_static_nonstandard']
