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
    'examples_dirs': ['examples/'],
    'gallery_dirs': ['auto_examples'],
    'backreferences_dir': 'gen_modules/backreferences',
    'within_section_order': FileNameSortKey,
    'image_scrapers': (matplotlib_format_scraper(),),
    'expected_failing_examples': ['examples/future/plot_future_imports_broken.py'],  # noqa
    'show_memory': True,
    'compress_images': ('images', 'thumbnails'),
    'junit': op.join('sphinx-gallery', 'junit-results.xml'),
    'matplotlib_animations': True,
}
nitpicky = True
highlight_language = 'python3'
html_static_path = ['_static']
