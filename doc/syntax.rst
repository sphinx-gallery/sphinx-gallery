.. _python_script_syntax:

=======================================================
How to structure your Python scripts for Sphinx-Gallery
=======================================================

This page describes the structure and syntax that can be used in Python scripts
to generate rendered HTML gallery pages.

A simple example
================

Sphinx-Gallery expects each Python file to have two things:

1. **A docstring**, written in rST, that defines the
   header for the example. It must begin by defining an rST title. For example::

    """
    This is my example script
    =========================

    This example doesn't do much, it just makes a simple plot
    """
2. **Python code**. This can be any valid Python code that you wish. Any
   Matplotlib or Mayavi images that are generated will be saved to disk, and
   the rST generated will display these images with the built examples.

For a quick reference have a look at the example
:ref:`sphx_glr_auto_examples_plot_gallery_version.py`

.. _embedding_rst:

Embed rST in your example Python files
======================================

Additionally, you may embed rST syntax within your Python scripts. This will
be rendered in-line with the Python code and its outputs, similar to how
Jupyter Notebooks are structured (in fact, Sphinx-Gallery also **creates** a
Jupyter Notebook for each example that is built).

You can embed rST in your Python examples by including a line of ``#`` symbols
that spans >= 20 columns. We recommend using 79 columns, like
this::

  ###############################################################################

Any commented lines (that begin with ``#`` and a space so they are
PEP8-compliant) that immediately follow will be rendered as rST in the built
gallery examples. For example::

  # This is commented python
  myvariable = 2
  print("my variable is {}".format(myvariable))

  ###############################################################################
  # This is a section header
  # ------------------------
  #
  # In the built documentation, it will be rendered as rST.

  # These lines won't be rendered as rST because there is a gap after the last
  # commented rST block. Instead, they'll resolve as regular Python comments.
  print('my variable plus 2 is {}'.format(myvariable + 2))

Here are the contents of an example Python file from the snippets above.::

  """
  This is my example script
  =========================

  This example doesn't do much, it just makes a simple plot
  """

  ###############################################################################
  # This is a section header
  # ------------------------
  #
  # .. note:: This is the first section!

  # This line won't be rendered as rST because there's a space after the last block.
  myvariable = 2
  print("my variable is {}".format(myvariable))

  ###############################################################################
  # This is another section header
  # ------------------------------
  #
  # In the built documentation, it will be rendered as rST after the code above!

  print('my variable plus 2 is {}'.format(myvariable + 2))

For a clear example refer to the rendered example
:ref:`sphx_glr_tutorials_plot_notebook.py` and compare it to the generated
:download:`original python script <tutorials/plot_notebook.py>`
