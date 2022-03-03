===================================
Getting Started with Sphinx-Gallery
===================================

.. _create_simple_gallery:

Creating a basic Gallery
========================

This section describes how to set up a basic gallery for your examples
using the Sphinx extension Sphinx-Gallery, which will do the following:

* Automatically generate `Sphinx rST
  <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
  out of your ``.py`` example files. The
  rendering of the resulting rST will provide the users with ``.ipynb``
  (Jupyter notebook) and ``.py`` files of each example, which users can
  download.
* Create a gallery with thumbnails for each of these examples
  (such as `the one that scikit-learn
  <http://scikit-learn.org/stable/auto_examples/index.html>`_ uses).

A `template repository <https://github.com/sphinx-gallery/sample-project>`_,
with sample example galleries and basic configurations is also available to
help you get started.

.. note::
   Working `sphinx 
   builders <https://www.sphinx-doc.org/en/master/man/sphinx-build.html#options>`_ 
   for sphinx_gallery include `html` and `latex`. Support for other builders
   is not guaranteed (e.g., `dirhtml` is known to be broken and will cause
   broken image links.).


.. _set_up_your_project:

Overview your project files and folders
---------------------------------------

This section describes the general files and structure needed for Sphinx-Gallery
to build your examples.

Let's say your Python project has the following structure:

.. code-block:: none

    .
    ├── doc
    │   ├── conf.py
    │   ├── index.rst
    |   ├── make.bat
    │   └── Makefile
    ├── my_python_module
    │   ├── __init__.py
    │   └── mod.py
    └── examples
      	├── plot_example.py
      	├── example.py
      	└── README.txt (or .rst)

* ``doc`` is the Sphinx 'source directory'. It contains the Sphinx base
  configuration files. Default versions of these base files can obtained from
  executing ``sphinx-quickstart`` (more details at `Sphinx-quickstart
  <http://www.sphinx-doc.org/en/master/usage/quickstart.html>`_). Sphinx
  ``.rst`` source files are generally also placed here (none included in
  our example directory structure above) but these are
  unassociated with Sphinx-Gallery functions.

* ``my_python_module`` contains the ``.py`` files of your Python module. This
  directory is not required and Sphinx-Gallery can be used for a variety of
  purposes outside of documenting examples for a package, for example
  creating a website for a Python tutorial.

* ``examples`` contains the files used by Sphinx-Gallery to build the gallery.

Sphinx-Gallery expects the ``examples`` directory to have a specific structure,
which we'll cover next.

Structure the examples folder
-----------------------------

In order for Sphinx-Gallery to build a gallery from your ``examples`` folder,
this folder must have the following things:

* **The gallery header**: A file named ``README.txt`` or ``README.rst`` that
  contains rST to be used as a header for the gallery welcome page, which will
  also include thumbnails generated from this folder. It must have at least a
  title. For example::

    This is my gallery
    ==================

    Below is a gallery of examples

* **Example Python scripts**: A collection of Python scripts that will be
  processed when you build your HTML documentation. For information on how
  to structure these Python scripts with embedded rST, see
  :ref:`python_script_syntax`.

    * By default **only** files prefixed with ``plot_`` will be executed and
      their outputs captured to incorporate them in the HTML
      output of the script. Files without that prefix will be only parsed and
      presented in a rich literate programming fashion, without any output. To
      change the default file pattern for execution and capture see
      :ref:`build_pattern`.
    * The output that is captured while executing the ``.py`` files and
      subsequently incorporated into the built documentation can be finely
      tuned. See :ref:`capture_repr`.
    * You can have sub-directories in your ``examples`` directory. These will be
      included as sub-sections of your gallery. They **must** contain their own
      ``README.txt`` or ``README.rst`` file as well.

.. warning::

   The variable name ``___`` (3 underscores) should never be used in your
   example Python scripts as it is used as an internal Sphinx-Gallery variable.

.. _configure_and_use_sphinx_gallery:

Configure and use Sphinx-Gallery
--------------------------------

After Sphinx-Gallery is installed, we must enable and configure it to build
with Sphinx.

First, enable Sphinx-Gallery in the Sphinx ``doc/conf.py`` file with::

    extensions = [
        ...
        'sphinx_gallery.gen_gallery',
        ]

This loads Sphinx-Gallery as one of your extensions, the ellipsis
``...`` represents your other loaded extensions.

Next, create your configuration dictionary for Sphinx-Gallery. Here we will
simply set the minimal required configurations. We must set the location of
the 'examples' directory (containing the gallery header file and our example
Python scripts) and the
directory to place the output files generated. The path to both of these
directories should be relative to the ``doc/conf.py`` file.

The following configuration declares the location of the 'examples' directory
(``'example_dirs'``) to be ``../examples`` and the 'output' directory
(``'gallery_dirs'``) to be ``auto_examples``::

    sphinx_gallery_conf = {
         'examples_dirs': '../examples',   # path to your example scripts
         'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
    }

After building your documentation, ``gallery_dirs`` will contain the following
files and directories:

* ``index.rst`` - the master document of the gallery containing the gallery
  header, table of contents tree and thumbnails for each example. It will serve
  as the welcome page for that gallery.
* ``sg_execution_times.rst`` - execution time of all example ``.py`` files,
  summarised in table format (`original pull request on GitHub
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/348>`_).
* ``images`` - directory containing images produced during execution of the
  example ``.py`` files (more details in :ref:`image_scrapers`) and thumbnail
  images for the gallery.
* A directory for each sub-directory in ``'example_dirs'``. Within each
  directory will be the above and below listed files for that 'sub-gallery'.

Additionally for **each** ``.py`` file, a file with the following suffix is
generated:

* ``.rst`` - the rendered rST version of the ``.py`` file, ready for Sphinx
  to build.
* ``.ipynb`` - to enable the user to download a Jupyter notebook version of the
  example.
* ``.py`` - to enable the user to download a ``.py`` version of the example.
* ``.py.md5`` - a md5 hash of the ``.py`` file, used to determine if changes
  have been made to the file and thus if new output files need to be generated.
* ``_codeobj.pickle`` - used to identify function names and to which module
  they belong (more details in
  :ref:`sphx_glr_auto_examples_plot_6_function_identifier.py`)

Additionally, two compressed ``.zip`` files containing all the ``.ipynb`` and
``.py`` files are generated.

For more advanced configuration, see the :ref:`configuration` page.

Add your gallery to the documentation
-------------------------------------

The ``index.rst`` file generated for your gallery can be added to the table of
contents tree in the main Sphinx ``doc/index.rst`` file  or embedded in a
Sphinx source ``.rst`` file with an ``.. include::`` statement.

Build the documentation
-----------------------

In your Sphinx source directory, (e.g., ``myproject/doc``) execute:

.. code-block:: bash

    $ make html

This will start the build of your complete documentation. Both
the Sphinx-Gallery output files described above and
the Sphinx built HTML documentation will
be generated. Once a build is completed, all the outputs from your examples
will be cached.
In the future, only examples that have changed will be re-built.

You should now have a gallery built from your example scripts! For more
advanced usage and configuration, check out the :ref:`advanced_usage` page or
the :ref:`configuration` reference.

.. note::
  Sphinx-Gallery may work for non-HTML Sphinx `builders
  <https://www.sphinx-doc.org/en/master/man/sphinx-build.html>`_ but support
  for this is mostly untested and results may vary.
