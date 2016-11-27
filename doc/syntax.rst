=====================
Sphinx-Gallery Syntax
=====================

For your examples to work you have to make them valid python code.


Simple examples
===============

This is the base of a python script of module. The structure follows
a leading docstring that must follow reStructuredText syntax and a header.
Then the executable code of your script.

For a quick reference have a look at the example
:ref:`sphx_glr_auto_examples_plot_gallery_version.py`

In this 2 block structure, the website is rendered ordered with
the docstring, then output images and output code. Finally the
generating code script.


.. _notebook_examples_syntax:

Notebook Styled examples syntax
===============================

It is also possible to have more complicated examples, for which you
want to embed more documenting strings within your code and separating
it by blocks. This is also possible, you follow standard python coding
syntax but new documenting strings that will be rendered as reStructuredText
have to be leaded by a line of hashes.

For a clear example refer to the rendered example
:ref:`sphx_glr_tutorials_plot_notebook.py` and compare it to the generating
:download:`original python script <tutorials/plot_notebook.py>`

In this multiblock structure, the website is rendered ordered by the
leading docstring. Then executable python code is presented and after
its output in images and test, following  the intuitive notebook structure.
