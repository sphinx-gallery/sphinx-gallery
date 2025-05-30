==============
Sphinx-Gallery
==============

.. image:: https://img.shields.io/pypi/v/sphinx-gallery
    :target: https://pypi.org/project/sphinx-gallery/
    :alt: PyPI

.. image:: https://img.shields.io/conda/vn/conda-forge/sphinx-gallery
    :target: https://anaconda.org/conda-forge/sphinx-gallery
    :alt: Conda-forge

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3741780.svg
    :target: https://doi.org/10.5281/zenodo.3741780
    :alt: Zenodo DOI

.. image:: https://dev.azure.com/sphinx-gallery/sphinx-gallery/_apis/build/status/sphinx-gallery.sphinx-gallery?branchName=master
    :target: https://dev.azure.com/sphinx-gallery/sphinx-gallery/_build/latest?definitionId=1&branchName=master
    :alt: Azure CI status

.. image:: https://circleci.com/gh/sphinx-gallery/sphinx-gallery.svg?style=shield
    :target: https://circleci.com/gh/sphinx-gallery/sphinx-gallery
    :alt: CircleCI status

.. image:: https://codecov.io/github/sphinx-gallery/sphinx-gallery/badge.svg?branch=master&service=github(
    :target: https://app.codecov.io/github/sphinx-gallery/sphinx-gallery
    :alt: Code coverage


.. tagline-begin-content

A `Sphinx <https://www.sphinx-doc.org/en/master/>`_ extension that builds an
HTML gallery of examples from any set of Python scripts.
Check out the `documentation`_ for introductions on how to use it and more...

.. tagline-end-content

.. image:: doc/_static/demo.png
   :width: 80%
   :alt: A demo of a gallery generated by Sphinx-Gallery

Quickstart
==========

Sphinx-Gallery can be used to generate an example gallery from ``.py`` files,
for a library,
as well as a stand-alone web page showcasing examples of a particular
Python package, module, or class.

Let's get started with a simple example or check out the
 `documentation`_ for introductions on how
 to use it and more...

Install via ``pip``
-------------------

.. installation-begin-content

You can do a direct install via ``pip`` by using:

.. code-block:: bash

    $ pip install sphinx-gallery

.. tip::
    Sphinx-Gallery also has support for scraping images from Matplotlib
    and Matplotlib-based packages such as Seaborn.
    We recommend installing system ``optipng`` binaries to reduce
    the file sizes of the generated PNG files.

.. installation-end-content

Add examples to your docs
-------------------------

Let's assume simple scenario, you have a Python package with a directory structure like this:

.. code-block::

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
        └── README.txt (or .rst)

Enable Sphinx-Gallery by adding the following to your ``doc/conf.py``:

.. code-block:: python

    extensions = [
        ...
        'sphinx_gallery.gen_gallery',
    ]

    # path to the examples scripts
    sphinx_gallery_conf = {
        'examples_dirs': '../examples',   # path to your example scripts
        'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
    }

Finally just compile your docs as usual.
Sphinx-Gallery will generate reST files, adding execution outputs, and save them in ``auto_examples/``.
Add a link to ``auto_examples/index.rst`` to include the gallery in your documentation.

Who uses Sphinx-Gallery
=======================

An incomplete list:

.. projects_list_start

* `Apache TVM <https://tvm.apache.org/docs/tutorial/index.html>`_
* `Astropy <https://docs.astropy.org/en/stable/generated/examples/index.html>`_
* `auto-sklearn <https://automl.github.io/auto-sklearn/master/examples/index.html>`_
* `Biotite <https://www.biotite-python.org/examples/gallery/index.html>`_
* `Cartopy <https://scitools.org.uk/cartopy/docs/latest/gallery/>`_
* `FURY <https://fury.gl/latest/auto_examples/index.html>`_
* `pyGIMLi <https://www.pygimli.org/_examples_auto/index.html>`_
* `HyperSpy <https://hyperspy.org/hyperspy-doc/current/>`_
* `kikuchipy <https://kikuchipy.org>`_
* `Matplotlib <https://matplotlib.org/stable/index.html>`_
* `MNE-Python <https://mne.tools/stable/auto_examples/index.html>`_
* `napari <https://napari.org/stable/gallery.html>`_
* `Nestle <http://kylebarbary.com/nestle/examples/index.html>`_
* `NetworkX <https://networkx.org/documentation/stable/auto_examples/index.html>`_
* `Neuraxle <https://www.neuraxle.org/stable/examples/index.html>`_
* `Nilearn <https://nilearn.github.io/stable/auto_examples/index.html>`_
* `OpenML <https://openml.github.io/openml-python/main/examples/index.html>`_
* `OpenTURNS <https://openturns.github.io/openturns/latest/examples/examples.html>`_
* `Optuna <https://optuna.readthedocs.io/en/stable/tutorial/index.html>`_
* `PlasmaPy <https://docs.plasmapy.org/en/latest/examples.html>`_
* `POT <https://pythonot.github.io/auto_examples/index.html>`_
* `PyGMT <https://www.pygmt.org/latest/gallery/index.html>`_
* `pyRiemann <https://pyriemann.readthedocs.io/en/latest/index.html>`_
* `PyStruct <https://pystruct.github.io/auto_examples/index.html>`_
* `PySurfer <https://pysurfer.github.io/>`_
* `PyTorch tutorials <https://pytorch.org/tutorials>`_
* `PyVista <https://docs.pyvista.org/examples/>`_
* `pyxem <https://pyxem.readthedocs.io>`_
* `RADIS <https://radis.readthedocs.io/en/latest/auto_examples/index.html>`_
* `scikit-image <https://scikit-image.org/docs/dev/auto_examples/>`_
* `scikit-learn <https://scikit-learn.org/stable/auto_examples/index.html>`_
* `SimPEG <https://docs.simpeg.xyz/content/examples/>`_
* `SKADA Scikit-adaptation <https://scikit-adaptation.github.io/auto_examples/index.html>`_
* `Sphinx-Gallery <https://sphinx-gallery.github.io/stable/auto_examples/index.html>`_
* `SunPy <https://docs.sunpy.org/en/stable/generated/gallery/index.html>`_
* `Tonic <https://tonic.readthedocs.io/en/latest/auto_examples/index.html>`_
* `TorchDR <https://torchdr.github.io/auto_examples/index.html>`_
* `TorchIO <https://torchio.readthedocs.io/auto_examples/index.html>`_

.. projects_list_end

Contributing
============

You can get the latest development source from our `Github repository
<https://github.com/sphinx-gallery/sphinx-gallery>`_. You need
``setuptools`` installed in your system to install Sphinx-Gallery. For example,
you can do:

.. code-block:: console

    $ git clone https://github.com/sphinx-gallery/sphinx-gallery
    $ cd sphinx-gallery
    $ conda install graphviz  # if using conda, you can get graphviz this way
    $ pip install -e .[dev]


Check that you are all set by running:

.. code-block:: console

    $ pytest sphinx_gallery

How to cite
===========

.. citation-begin-content

If you would like to cite Sphinx-Gallery you can do so using our `Zenodo
deposit <https://zenodo.org/record/3741780>`_.

.. _documentation: https://sphinx-gallery.github.io/

.. citation-end-content
