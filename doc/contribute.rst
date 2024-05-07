.. _contribute-guide:

==========
Contribute
==========

We appreciate your help in improving this document and our library!

Please `open an issue <https://github.com/sphinx-gallery/sphinx-gallery/issues>`_
if this document is unclear or missing a step.

.. _development-workflow:

Development Workflow
====================

If you are interested in contributing code or documentation, we strongly recommend
 that you install a development version of sphinx-gallery in a development environment.
 If you are unfamiliar with the git/github workflow, please see Github's guide to
 `contributing to projects
 <https://docs.github.com/en/get-started/quickstart/contributing-to-projects#creating-a-branch-to-work-on>`_.

This guide assumes familiarity with the Github workflow and focuses on aspects
 specific to contributing to Sphinx-Gallery.

.. _checkout-source:

Get Latest Source
-----------------

You can get the latest development source from our `Github repository
<https://github.com/sphinx-gallery/sphinx-gallery>`_.

.. code-block:: console

    git clone https://github.com/<your github user name>/sphinx-gallery

.. _virtual-environment:

Create a Dedicated Environment
------------------------------

We strongly recommend that you create a virtual environment for developing
 Sphinx Gallery to isolate it from other Python installations on your system.

Create a new virtual environment:

.. code-block:: console

    python -m venv <file folder location>

Activate the virtual environment using one of the following:

.. code-block:: console

    source <file folder location>/bin/activate  # Linux/macOS
    <file folder location>\Scripts\activate.bat  # Windows cmd.exe
    <file folder location>\Scripts\Activate.ps1

.. _install-dependencies:

Install Dependencies
--------------------

Most of the Sphinx Gallery dependencies are listed in :file:`requirements.txt`
 and :file:`dev-requirements.txt` and can be installed from those files:

.. code-block:: console

    python -m pip install -r dev-requirements.txt

Sphinx Gallery requires that `setuptools <https://setuptools.pypa.io/en/latest/setuptools.html>`_
 is installed. It is usually packaged with python, but if necessary can be installed
 using ``pip``:

.. code-block:: console

    python -m pip install setuptools


.. _editable-install:

Install for Development
-----------------------

Editable installs means that the environment Python will always use the most
 recently changed version of your code. To install Sphinx Gallery in editable mode,
 ensure you are in the sphinx-gallery directory

.. code-block:: console

    cd sphinx-gallery

Then install using the editable flag:

.. code-block:: console

    python -m pip install -e .

.. _verify-install:

Verify install
--------------

Check that you are all set by running the tests:

.. code-block:: console

    python -m pytest sphinx_gallery


And by building the docs:

.. code-block:: console

    cd doc
    make html

.. _pre-commit-hooks:

Install pre-commit hooks
------------------------

pre-commit hooks check for things like spelling and formatting in contributed
 code and documentation. To set up pre-commit hooks:

.. code-block:: console

    python -m pip install pre-commit
    pre-commit install


.. _code-contributions:

Guidelines
==========

.. _code-contrib-testing:

Testing
-------

All code contributions should be tested. We use the `pytest <https://docs.pytest.org/>`_
 testing framework and ``tinybuild`` to build test pages.
 Tests can be found in :file:`sphinx_gallery/tests`.

.. _testing-tinybuild:

tinybuild
^^^^^^^^^

``tinybuild`` is designed as the minimal full sphinx doc build that you can run with
 ``make html`` from :file:`tinybuild/doc` to get a traditional build experience.

``tinybuild`` gets run in :file:`tests/test_full.py` to build a test page using the
 ``.rst`` document files in :file:`tests/doc/tinybuild`. The tests examine the ``html``
 output to verify the behavior of the directives in the ``.rst`` files.

