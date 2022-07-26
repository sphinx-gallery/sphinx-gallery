:orphan:

==========================
Maintaining Sphinx Gallery
==========================

This document contains tips for maintenance.

.. contents::
   :local:
   :depth: 2

How to make a release
=====================

.. highlight:: console

Check credentials and prerequisites
-----------------------------------

Sphinx Gallery is `hosted on the pypi repository <https://pypi.org/project/sphinx-gallery/>`_.
To create a new release of Sphinx Gallery, you need to do these things:
You should double-check a few things to make sure that you can create
a new release for Sphinx Gallery.

1. Ensure that you **registered an account** on `the PyPI index <https://pypi.org/account/register/>`_.
2. Ensure you have **push access** to the
   `Sphinx Gallery pypi repository <https://pypi.org/project/sphinx-gallery/>`_.
   Ask one of the Sphinx Gallery core developers if you do not.
3. Install the `GitHub Changelog Generator <https://github.com/github-changelog-generator/github-changelog-generator#installation>`_.
   This is a small tool written in Ruby to generate a markdown list of recent changes.
4. Install `the twine package <https://twine.readthedocs.io/en/latest/>`_. This is
   a package that helps you
   bundle and push new Python package distributions to pip.


Prepare for release
-------------------
1. Update ``CHANGES.rst``

    1. Use `github_changelog_generator
       <https://github.com/skywinder/github-changelog-generator#installation>`_ to
       gather all merged pull requests and closed issues during the development
       cycle. You will likely need to `generate a Github token <https://github.com/settings/tokens/new?description=GitHub%20Changelog%20Generator%20token>`_
       as Github only allows 50 unauthenticated requests per hour. In the
       command below ``<version>`` is the current (not development) version of
       the package, e.g., ``0.6.0``. We do this because our failing discipline
       of writing in the CHANGES.rst all relevant changes, this helps our
       memory. It is a good idea to add appropriate labels (e.g., 'BUG') to
       issues and pull requests so they are categorized correctly in the
       CHANGES.rst generated. ::

          github_changelog_generator -u sphinx-gallery -p sphinx-gallery --since-tag=v<version> --token <your-40-digit-token>

    2. Edit CHANGELOG.md to look reasonable (it will be used later). It's a
       good idea to add labels to issues and pull requests so
       `github_changelog_generator` can correctly categorize them in in the
       CHANGES.rst file generated.

    3. Propagate the relevant changes to `CHANGES.rst <https://github.com/sphinx-gallery/sphinx-gallery/blob/master/CHANGES.rst>`_.
       You can easily convert it RST with pandoc::

          pandoc CHANGELOG.md --wrap=none -o CHANGELOG.rst

2. Build the docs cleanly

     Make sure to clean all and have a clean build. Double-check visually that
     everything looks right.

3. Double check CIs

     Make sure CIs are green on the master branch.

4. Update version

     Update the version in ``sphinx_gallery/__init__.py``, which should end in
     ``.dev0``. You should remove ``.dev0``, and the numbers that remain will
     become the version for this release.

5. Open a Pull Request that contains the two changes we've made above

     The **version bump** and **the CHANGELOG update** should be in the PR.
     Get somebody else to make sure all looks well, and merge this pull request.

Finalize the release
--------------------

1. Create the new release on PyPI

   * Build a source distribution and an ``any`` wheel::

        git clean -xdf
        python setup.py sdist bdist_wheel

   * Check the release::

        twine check dist/sphinx-gallery-<version>.*

     ``<version>`` should be the release version, e.g., ``0.7.0``, and it
     should check both the source distribution and the wheel.

   * Upload to PyPI::

        twine upload dist/*

     Again, ``<version>`` should be the release version, e.g., ``0.7.0``.

   * Confirm that the new version of Sphinx Gallery
     `is posted to pypi <https://pypi.org/project/sphinx-gallery/>`_.

2. Create a new release on GitHub

   * Go to the `Draft a new release <https://github.com/sphinx-gallery/sphinx-gallery/releases/new>`_ page.
   * The **tag version** is whatever the version is in ``__init__.py`` prepended with ``v``. E.g., ``v0.7.0``.
   * The **release title** is ``Release <tag-version>``.
   * The **description** should contain the markdown changelog
     you generated above (in the ``CHANGELOG.md`` file).
   * Click **Publish release** when you are done.

3. Now that the releases are complete, we need to switch the "master" branch back into a developer
   mode. Bump the `Sphinx Gallery version number <https://github.com/sphinx-gallery/sphinx-gallery/blob/master/sphinx_gallery/__init__.py>`_
   to the next minor (or major) release and append ``.dev0`` to the end, and make a PR for this change.

4. Celebrate! You've just released a new version of Sphinx Gallery!
