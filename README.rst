=================================
Getting Started to Sphinx-Gallery
=================================

.. image:: https://travis-ci.org/sphinx-gallery/sphinx-gallery.svg?branch=master
    :target: https://travis-ci.org/sphinx-gallery/sphinx-gallery

.. image:: https://readthedocs.org/projects/sphinx-gallery/badge/?version=latest
    :target: https://readthedocs.org/projects/sphinx-gallery/?badge=latest
    :alt: Documentation Status


Sphinx extension for automatic generation of an example gallery.
It is extracted from the scikit-learn project and aims to be an
independent general purpose extension.

Getting the package
===================

You can do a direct install via pip by using::

    $ pip install sphinx-gallery


Install as developer
--------------------

You can get the latest development source from our Github repository.
You need  ``setuptools`` installed in your system to install.

You will also need have installed:

* Sphinx
* matplotlib
* pillow

To install::

    $ git clone https://github.com/sphinx-gallery/sphinx-gallery
    $ cd sphinx-gallery
    $ python setup.py develop


Setting up your project
=======================

After installing you need to include in your Sphinx ``conf.py`` file:


.. code-block:: python

    import sphinx_gallery
    extensions = [
        ...
        'sphinx_gallery.gen_gallery',
        ]


you need to have a folder called ``examples`` in your main repository directory.
This folder needs

* A ``README.txt`` file with rst syntax to present your gallery
* ``plot_examples.py`` files. Python scripts that have to be executed
  and output a plot that will be presented in your gallery
* ``examples.py`` files. Python scripts that will not be executed but will be presented
  in the gallery

Your python scripts in the examples folder need to have a main comment. Written
in rst syntax to be used in the generated file in the example gallery.

You can have subfolders in your ``examples`` directory, those will be recursively
scanned by the gallery extension and presented in the gallery. Subfolder have to
respect the same structure of the main ``examples`` folder.

If these instructions are not clear enough, this package uses itself, to generated
its own example gallery. So check the directory structure and the contents of the
files. That is all, our module shall take care of the rest.

Building the documentation locally
----------------------------------

In your sphinx documentation directory, usually ``doc`` execute::

    $ make html

This will start the build of your complete documentation including the examples
gallery. Once documentation is build, our extension will have generated a ``auto_examples``
directory and populated it with rst files containing the gallery and each example.
Sphinx gives this files its regular processing and you can enjoy your
generated gallery unde the same path. That means you will find the gallery in the path::

    _build/html/auto_examples/index.html

that you can open under your favourite browser.

Extending your Makefile
-----------------------
Once your gallery is working you might need remove completely all generated files by
sphinx-gallery to have a clean build, or you might want to build the gallery without
running the examples files. For this you need to extend your ``Makefile`` with::

    clean:
            rm -rf $(BUILDDIR)/*
            rm -rf auto_examples/
            rm -rf modules/generated/*

    html-noplot:
            $(SPHINXBUILD) -D plot_gallery=0 -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
            @echo
            @echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

Remember that for in ``Makefile`` whitespace is significant and the indentation are tabs
and not spaces
