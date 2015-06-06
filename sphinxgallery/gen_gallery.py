# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import division, print_function, absolute_import
import os
from . import glr_path_static
from .gen_rst import generate_dir_rst
from .docs_resolv import embed_code_links


class Path(str):
    """Path object for manipulating directory and file paths."""

    def __init__(self, path):
        super(Path, self).__init__(path)

    @property
    def isdir(self):
        return os.path.isdir(self)

    @property
    def exists(self):
        """Return True if path exists"""
        return os.path.exists(self)

    def pjoin(self, *args):
        """Join paths. `p` prefix prevents confusion with string method."""
        return self.__class__(os.path.join(self, *args))

    def psplit(self):
        """Split paths. `p` prefix prevents confusion with string method."""
        return [self.__class__(p) for p in os.path.split(self)]

    def makedirs(self):
        if not self.exists:
            os.makedirs(self)

    def listdir(self):
        return os.listdir(self)

    def format(self, *args, **kwargs):
        return self.__class__(super(Path, self).format(*args, **kwargs))

    def __add__(self, other):
        return self.__class__(super(Path, self).__add__(other))

    def __iadd__(self, other):
        return self.__add__(other)


def clean_gallery_out(build_dir):
    # Sphinx hack: sphinx copies generated images to the build directory
    #  each time the docs are made.  If the desired image name already
    #  exists, it appends a digit to prevent overwrites.  The problem is,
    #  the directory is never cleared.  This means that each time you build
    #  the docs, the number of images in the directory grows.
    #
    # This question has been asked on the sphinx development list, but there
    #  was no response: http://osdir.com/ml/sphinx-dev/2011-02/msg00123.html
    #
    # The following is a hack that prevents this behavior by clearing the
    #  image build directory each time the docs are built.  If sphinx
    #  changes their layout between versions, this will not work (though
    #  it should probably not cause a crash).  Tested successfully
    #  on Sphinx 1.0.7
    build_image_dir = os.path.join(build_dir, '_images')
    if os.path.exists(build_image_dir):
        filelist = os.listdir(build_image_dir)
        for filename in filelist:
            if filename.startswith('sphx_glr') and filename.endswith('png'):
                os.remove(os.path.join(build_image_dir, filename))


def generate_gallery_rst(app):
    """Starts the gallery configuration and recursively scans the examples
    directory in order to populate the examples gallery
    """
    try:
        plot_gallery = eval(app.builder.config.plot_gallery)
    except TypeError:
        plot_gallery = bool(app.builder.config.plot_gallery)

    gallery_conf.update(app.config.sphinxgallery_conf)

    # this assures I can call the config in other places
    app.config.sphinxgallery_conf = gallery_conf
    app.config.html_static_path.append(glr_path_static())

    if not plot_gallery:
        return

    clean_gallery_out(app.builder.outdir)

    examples_dir = os.path.relpath(gallery_conf['examples_dir'],
                                   app.builder.srcdir)
    gallery_dir = os.path.relpath(gallery_conf['gallery_dir'],
                                  app.builder.srcdir)
    mod_examples_dir = os.path.relpath(gallery_conf['mod_example_dir'],
                                       app.builder.srcdir)

    for workdir in [examples_dir, gallery_dir, mod_examples_dir]:
        if not os.path.exists(workdir):
            os.makedirs(workdir)

    # we create an index.rst with all examples
    fhindex = open(os.path.join(gallery_dir, 'index.rst'), 'w')
    fhindex.write(""".. _examples-index:

Gallery of Examples
===================\n\n""")
    # Here we don't use an os.walk, but we recurse only twice: flat is
    # better than nested.
    seen_backrefs = set()
    fhindex.write(generate_dir_rst(examples_dir, gallery_dir, gallery_conf,
                                   plot_gallery, seen_backrefs))
    for directory in sorted(os.listdir(examples_dir)):
        if os.path.isdir(os.path.join(examples_dir, directory)):
            src_dir = os.path.join(examples_dir, directory)
            target_dir = os.path.join(gallery_dir, directory)
            fhindex.write(generate_dir_rst(src_dir, target_dir, gallery_conf,
                                           plot_gallery, seen_backrefs))
    fhindex.flush()


gallery_conf = {
    'examples_dir'   : '../examples',
    'gallery_dir'    : 'auto_examples',
    'mod_example_dir': 'modules/generated',
    'doc_module'     : (),
    'reference_url'  : {},
}

def setup(app):
    app.add_config_value('plot_gallery', True, 'html')
    app.add_config_value('sphinxgallery_conf', gallery_conf, 'html')
    app.add_stylesheet('gallery.css')


    app.connect('builder-inited', generate_gallery_rst)

    app.connect('build-finished', embed_code_links)



def setup_module():
    # HACK: Stop nosetests running setup() above
    pass
