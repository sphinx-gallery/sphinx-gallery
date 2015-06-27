# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import division, print_function, absolute_import
import os
from . import glr_path_static
from .gen_rst import generate_dir_rst
from .docs_resolv import embed_code_links
from . import Path


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
    build_image_dir = build_dir.pjoin('_images')
    if build_image_dir.exists:
        filelist = build_image_dir.listdir()
        for filename in filelist:
            if filename.startswith('sphx_glr') and filename.endswith('png'):
                os.remove(build_image_dir.pjoin(filename))


def generate_gallery_rst(app):
    """Generate the Main examples gallery reStructuredText

    Start the sphinx-gallery configuration and recursively scan the examples
    directories in order to populate the examples gallery
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

    clean_gallery_out(Path(app.builder.outdir))

    examples_dir = Path(os.path.relpath(gallery_conf['examples_dir'],
                                        app.builder.srcdir))
    if not examples_dir.exists:
        print("No examples directory found at", examples_dir)
        return

    gallery_dir = Path(os.path.relpath(gallery_conf['gallery_dir'],
                                       app.builder.srcdir))
    mod_examples_dir = Path(os.path.relpath(gallery_conf['mod_example_dir'],
                                            app.builder.srcdir))

    for workdir in [gallery_dir, mod_examples_dir]:
        workdir.makedirs()

    # Here we don't use an os.walk, but we recurse only twice: flat is
    # better than nested.
    seen_backrefs = set()
    gallery_index = generate_dir_rst(examples_dir, gallery_dir, gallery_conf,
                                     seen_backrefs)
    for directory in sorted(os.listdir(examples_dir)):
        if os.path.isdir(os.path.join(examples_dir, directory)):
            src_dir = examples_dir.pjoin(directory)
            target_dir = gallery_dir.pjoin(directory)
            gallery_index += generate_dir_rst(src_dir, target_dir, gallery_conf,
                                              seen_backrefs)

    # we create a gallery_index with all examples
    gallery_file = gallery_dir.pjoin('index'+app.config.source_suffix)
    with open(gallery_file, 'w') as fhindex:
            fhindex.write(gallery_conf['gallery_header'])
            fhindex.write(gallery_index)
            fhindex.flush()

gallery_conf = {
    'examples_dir'   : '../examples',
    'gallery_dir'    : 'auto_examples',
    'mod_example_dir': 'modules/generated',
    'doc_module'     : (),
    'reference_url'  : {},
}

def setup(app):
    """Setup sphinx-gallery sphinx extension"""
    app.add_config_value('plot_gallery', True, 'html')
    app.add_config_value('sphinxgallery_conf', gallery_conf, 'html')
    app.add_stylesheet('gallery.css')

    app.connect('builder-inited', generate_gallery_rst)

    app.connect('build-finished', embed_code_links)


def setup_module():
    # HACK: Stop nosetests running setup() above
    pass
