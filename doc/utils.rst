========================
Sphinx-Gallery Utilities
========================

Convert Python scripts into Jupyter Notebooks
=============================================

Sphinx Gallery exposes its python source to Jupyter notebook converter
as a executable script too. To use this utility just call the script
and give the Python source file as argument::

  $ sphx_glr_python_to_jupyter.py python_script.py


Embedding Sphinx-Gallery inside your documentation script extensions
====================================================================

If you want to embed Sphinx-Gallery in your project instead of putting
it as a dependency you can call our embedding script inside your
Sphinx extensions folder::

  $ copy_sphinxgallery.sh

This will download directly from PyPI our latest released code and
save it to the current folder. This is a stripped version of the
Sphinx-Gallery module to incorporate in your project. You should also
add it to your version control system.
