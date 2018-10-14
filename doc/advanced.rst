.. _advanced_usage:

==============
Advanced usage
==============

This page contains more advanced topics in case you want to understand how
to use Sphinx-Gallery more deeply.

Extend your Makefile for Sphinx-Gallery
=======================================

This section describes some common extensions to the documentation Makefile
that are useful for Sphinx-Gallery.

Cleaning the gallery files
--------------------------

Once your gallery is working you might need completely remove all generated files by
Sphinx-Gallery to have a clean build. For this we recommend adding the following
to your Sphinx ``Makefile``:

.. code-block:: bash

    clean:
            rm -rf $(BUILDDIR)/*
            rm -rf auto_examples/

Build the gallery without running any examples
----------------------------------------------

If you wish to build your gallery without running examples first (e.g., if an
example takes a long time to run), add the following to your ``Makefile``.

.. code-block:: bash

    html-noplot:
            $(SPHINXBUILD) -D plot_gallery=0 -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
            @echo
            @echo "Build finished. The HTML pages are in $(BUILDDIR)/html."


Use Sphinx-Gallery with Jupyter Notebooks
=========================================

If you'd like to store your examples in Jupyter Notebook format, Sphinx-Gallery
provides a helper function to convert ``.ipynb`` format into Python files formatted
for Sphinx-Gallery. Here's how to use it:

1. Put your Jupyter Notebooks in a folder in your documentation
2. In your ``conf.py`` file, use the ``convert_ipynb_to_gallery`` function to
   generate Sphinx-Gallery python. For example, this code snippet uses ``glob`` to
   convert Jupyter Notebooks in the same folder:

   .. code-block:: python
      from glob import glob
      from sphinx_gallery.notebooks import convert_ipynb_to_gallery

      # Collect a list of all ipynb files
      ipynb_files = glob('path/to/my/notebooks/*.ipynb')

      # Loop through each file and convert to Sphinx-Gallery Python
      for nb_file in ipynb_files:
          convert_ipynb_to_gallery(nb_file)

Now, Sphinx-Gallery will process these Python files for your gallery. We recommend
adding these files to your ``.gitignore`` file in order to avoid duplicating
content across your files.


Know your Gallery files
=======================

The Gallery has been built, now you and all of your project's users
can already start enjoying it. All the temporary files needed to
generate the gallery(rst files, images, chache objects, etc) are
stored where you configured in ``gallery_dirs``. The final files that go
into the HTML version of your documentation have a particular
namespace, to avoid colisions with your own files and images.

Our namespace convention is to prefix everything with ``sphx_glr`` and
change path separators with underscores. This is valid for
cross-references labels, and images.

So for example if we want to reference the example
:ref:`sphx_glr_auto_examples_plot_gallery_version.py`, we just call
its reference
``:ref:`sphx_glr_auto_examples_plot_gallery_version.py```. The image
it generated has the name ``sphx_glr_plot_gallery_version_thumb.png``
and its thumbnail is ``sphx_glr_plot_gallery_version_thumb.png``
