import os.path as op
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


def _raise(*args, **kwargs):
    import matplotlib.pyplot as plt
    plt.close('all')
    raise ValueError('zero-size array to reduction operation minimum which '
                     'has no identity')


class MockScrapeProblem:

    def __init__(self):
        from matplotlib.colors import colorConverter
        self._orig = colorConverter.to_rgba

    def __repr__(self):
        return "MockScrapeProblem"

    def __call__(self, gallery_conf, fname):
        from matplotlib.colors import colorConverter
        if 'scraper_broken' in fname:
            colorConverter.to_rgba = _raise
        else:
            colorConverter.to_rgba = self._orig


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
    'matplotlib': ('https://matplotlib.org/stable/', None),
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
    'within_subsection_order': FileNameSortKey,
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
    'image_srcset': ["2x"],
    'exclude_implicit_doc': ['figure_rst'],
}
nitpicky = True
highlight_language = 'python3'
html_static_path = ['_static_nonstandard']
