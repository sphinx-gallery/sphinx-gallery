:orphan:

==========================
Maintaining Sphinx Gallery
==========================

The Sphinx Gallery team is distributed across the globe in a variety of locations,
if you'd like to help contribute to sphinx-gallery, see the sections below for
some pointers.

How to make a release
=====================

Sphinx Gallery is `hosted on the pypi repository <https://pypi.org/project/sphinx-gallery/>`_.
To create a new release of Sphinx Gallery, you need to do these things:

Before you start
----------------

You should double-check a few things to make sure that you can create
a new release for Sphinx Gallery.

1. Ensure that you **registered an acccount** on `the PyPI index <https://pypi.org/account/register/>`_.
2. Ensure you have **push access** to the
   `Sphinx Gallery pypi repository <https://pypi.org/project/sphinx-gallery/>`_.
   Ask one of the Sphinx Gallery core developers if you do not.
3. Install the `GitHub Changelog Generator <https://github.com/github-changelog-generator/github-changelog-generator#installation>`_.
   This is a small tool written in Ruby to generate a markdown list of recent changes.
4. Install `the twine package <https://twine.readthedocs.io/en/latest/>`_. This is
   a package that helps you
   bundle and push new Python package distributions to pip.


Check that we are ready for a release
-------------------------------------
* Update the change log

  Use `github_changelog_generator
  <https://github.com/skywinder/github-changelog-generator#installation>`_ to
  gather all merged pull requests and closed issues during the development
  cycle. We do this because our failing discipline of writing in the
  CHANGES.rst all relevant changes, this helps our memory.

  .. code-block:: bash

     github_changelog_generator sphinx-gallery/sphinx-gallery --token <<your-github-api-token>>

  Read the changes in the generated CHANGELOG.md and propagate the relevant
  changes to
  `CHANGES.rst <https://github.com/sphinx-gallery/sphinx-gallery/blob/master/CHANGES.rst>`_.
  You can easily convert this document to ``.rst`` by using `Pandoc <https://pandoc.org/>`_.

* Build the docs cleanly

  Make sure to clean all and have a clean build. Double-check visually that
  everything looks right.

* Double check that continuous integration is passing on the master branch of
  Sphinx Gallery.

* Update version

  Update the version in ``sphinx_gallery/__init__.py``. It should end in
  ``dev0``. You should remove this text, and the remaining number will become
  the version for this release.

* Open a Pull Request that contains the two changes we've made above: **the version bump**
  and **the CHANGELOG update**. Get somebody else to make sure all looks well, and
  merge this pull request. Once that is done, move on to the final step!

Make the release
----------------

* Create the new release on PyPI

  * Build a source distribution

    .. code-block:: bash

       python setup.py sdist

  * Upload to PyPI

    .. code-block:: bash

       twine upload dist/sphinx-gallery-<version>.tar.gz

  * Confirm that the new version of Sphinx Gallery
    `is posted to pypi <https://pypi.org/project/sphinx-gallery/>`_.

* Create a new release on GitHub

  * Go to the `Draft a new release <https://github.com/sphinx-gallery/sphinx-gallery/releases/new>`_ page.
  * The **tag version** is whatever the version is in ``__init__.py`` prepended with ``v``. E.g., ``v0.3.0``.
  * The **release title** is ``Release: << tag-version >>``.
  * The **description** should contain the markdown changelog
    you generated above (in the ``CHANGELOG.md`` file). Make sure to update any links to point
    to the tag that will be created for this release (e.g., change ``HEAD`` to ``v0.3.0``).
  * Click **Publish release** when you are done.

* Now that the releases are complete, we need to switch the "master" branch back into a developer
  mode. Bump the `Sphinx Gallery version number <https://github.com/sphinx-gallery/sphinx-gallery/blob/master/sphinx_gallery/__init__.py>`_
  to the next minor (or major) release and append `dev0` to the end.

* Celebrate! You've just released a new version of Sphinx Gallery!
