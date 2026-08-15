========================
Sphinx-Gallery Utilities
========================

Convert Python scripts into Jupyter Notebooks
=============================================

Sphinx Gallery exposes its python source to Jupyter notebook converter
as a executable script too. To use this utility just call the script
and give the Python source file as argument:

.. code-block:: console

  $ sphinx_gallery_py2jupyter python_script.py


Embedding Sphinx-Gallery inside your documentation script extensions
====================================================================

If you want to embed Sphinx-Gallery in your project instead of putting
it as a dependency you can call our embedding script inside your
Sphinx extensions folder:

.. code-block:: console

    # Script to do a local install of sphinx-gallery
    rm -rf tmp sphinx_gallery

    easy_install -Zeab tmp sphinx-gallery

    cp -vru tmp/sphinx-gallery/sphinx_gallery/ .

    echo "Remember to add sphinx_gallery to your version control"
    echo "Use in case of git:"
    echo "$ git add sphinx_gallery"

This will download directly from PyPI our latest released code and
save it to the current folder. This is a stripped version of the
Sphinx-Gallery module to incorporate in your project. You should also
add it to your version control system.

Minigallery directive
======================

Sphinx-Gallery provides the ``minigallery`` directive so you can easily add a reduced
version of the gallery to your documentation.
See :ref:`minigalleries_to_examples` for details.
