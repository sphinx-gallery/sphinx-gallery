===================================
Getting Started with Sphinx-Gallery
===================================

.. _create_simple_gallery:

Creating a basic Gallery
========================

This section describes how to set up a basic gallery for your examples
using ``sphinx-gallery``. You'll do the following.

* Automatically generate sphinx rST for your examples, along with Jupyter
  notebooks of each that users can download.
* Create a gallery with thumbnails for each of these examples
  (such as `the one that scikit-learn
  <http://scikit-learn.org/stable/auto_examples/index.html>`_ uses)

.. _set_up_your_project:

Overview your project files and folders
---------------------------------------

This section describes the general files and structure needed for Sphinx-Gallery
to build your examples.

Let's say your Python project looks like this::

    .
    ├── doc
    │   ├── conf.py
    │   ├── index.rst
    │   └── Makefile
    ├── my_python_module
    │   ├── __init__.py
    │   └── mod.py
    └── examples
      	├── plot_example.py
      	├── example.py
      	└── README.txt

Your Python module is in ``my_python_module``, examples for how to use it are
in ``examples`` and the ``doc`` folder holds the base documentation
structure you get from executing ``sphinx-quickstart``.

Sphinx-Gallery expects examples to have a specific structure, which we'll
cover next.

Structure the examples folder
-----------------------------

In order for Sphinx-Gallery to build a gallery from your ``examples`` folder,
this folder must have the following things:

* **The Gallery Header** (``README.txt``). A file called ``README.txt`` that
  contains rST that will be used as a header for the gallery generated from
  this folder. It must have at least a title. For example::

    This is my gallery
    ==================

    Below is a gallery of examples

* **Example Python Scripts**: A collection of Python scripts that will be
  processed when you build your HTML documentation.  For information on how
  to structure these Python scripts with embedded rST, see
  :ref:`python_script_syntax`. By default files prefixed with ``plot``
  will be executed and their outputs captured to incorporate them in the
  HTML version of the script. Files without that prefix will be only parsed
  and presented in a rich literate programming fashion, without any output.
  To change the default pattern for execution and capture see
  :ref:`build_pattern`.

.. note::

   You can have sub-folders in your ``examples`` directory. These will be
   included as sub-sections of your gallery. They **must** contain their own
   ``README.txt`` file as well.

Configure and use sphinx-gallery
--------------------------------

After Sphinx-Gallery is installed, we must enable and configure it to build
with Sphinx.

First, enable Sphinx-Gallery in the Sphinx ``conf.py`` file with::

    extensions = [
        ...
        'sphinx_gallery.gen_gallery',
        ]

This loads Sphinx-Gallery as one of your extensions, the ellipsis
``...`` represents your other loaded extensions.

Next, create your configuration dictionary for Sphinx-Gallery. Here we will
simply tell Sphinx-Gallery which folder contains our example Python scripts.
For more advanced configuration, see the :ref:`configuration` page.

The following configuration declares the location of the examples directory
relative to ``conf.py`` (``../examples``) as well as the location of the
directory to be generated when your gallery is built (``auto_examples``).::

    sphinx_gallery_conf = {
         # path to your examples scripts
         'examples_dirs': '../examples',
         # path where to save gallery generated examples
         'gallery_dirs': 'auto_examples',
    }

After building your documentation, ``gallery_dirs`` will contain rST files
for your gallery, as well as for each example Python script.

Add your gallery to the documentation
-------------------------------------

When you build your documentation, sphinx-gallery will automatically populate
the folder specified in ``gallery_dirs`` above with Sphinx-ready rST.
It will create an ``index.rst`` file in the root of each gallery folder that
contains the rST for that gallery (in this example, it is ``gallery_dirs/index.rst``).
You can add it to your Sphinx navbar, or embed it with an ``.. include::`` statement.

Build the documentation
-----------------------

In your Sphinx documentation directory, (e.g., ``myproject/doc``) execute:

.. code-block:: bash

    $ make html

This will start the build of your complete documentation including the examples
gallery. Once a build is completed, all your examples outputs are cached.
In the future, only examples that have changed will be re-built.

You should now have a gallery built from your example scripts! For more
advanced usage and configuration, check out the :ref:`advanced_usage` page or
the :ref:`configuration` reference.
