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

1. Update ``CHANGES.rst`` and version in a PR
---------------------------------------------

1. Use `github_changelog_generator
   <https://github.com/github-changelog-generator/github-changelog-generator#installation>`_ to
   gather all merged pull requests and closed issues during the development
   cycle. You will likely need to `generate a Github token <https://github.com/settings/tokens/new?description=GitHub%20Changelog%20Generator%20token>`_
   as Github only allows 50 unauthenticated requests per hour. In the
   command below ``<version>`` is the current (not development) version of
   the package, e.g., ``0.6.0``. The changelog can generated with the following::

      github_changelog_generator --since-tag=v<version> --token <your-40-digit-token>

   To avoid the need to pass ``--token``, you can use ``export CHANGELOG_GITHUB_TOKEN=<your-40-digit-token>`` instead.

2. Iteratively update PR labels on GitHub and regenerate ``CHANGELOG.md`` so
   that PRs are categorized correctly. The labels we currently use are:

   ``bug``
      For fixed bugs.
   ``enhancement``
      For enhancements.
   ``api``
      For API changes (deprecations and removals).
   ``maintenance``
      For general project maintenance (e.g., CIs).
   ``documentation``
      For documentation improvements.
   
   Once all PRs land in one of these categories, manually edit CHANGELOG.md to
   look reasonable if necessary.

3. Propagate the relevant changes to `CHANGES.rst <https://github.com/sphinx-gallery/sphinx-gallery/blob/master/CHANGES.rst>`_.
   You can easily convert it RST with pandoc::

      pandoc CHANGELOG.md --wrap=none -o CHANGELOG.rst

   Then copy just the sections to ``CHANGES.rst``. **Keep ``CHANGELOG.md`` for
   later.**

4. Update the version in ``sphinx_gallery/__init__.py``, which should end in
   ``.dev0``. You should replace ``.dev0`` with ``0`` to obtain a semantic
   version (e.g., ``0.12.dev0`` to ``0.12.0``).

5. Open a PR with the above **changelog** and **version** changes (along with
   any updates to this ``maintainers.rst`` document!).

6. Make sure CIs are green.

7. Check that the built documentation looks correct.

8. Get somebody else to make sure all looks well, and merge this pull request.

2.  Finalize the release
------------------------

1. Make sure CIs are green following the "Release" PR.
2. Create a new release on GitHub

   * Go to the `Draft a new release <https://github.com/sphinx-gallery/sphinx-gallery/releases/new>`_ page.
   * The **tag version** is whatever the version is in ``__init__.py`` prepended with ``v``. E.g., ``v0.7.0``.
   * The **release title** is ``Release <tag-version>``.
   * The **description** should contain the markdown changelog
     you generated above (in the ``CHANGELOG.md`` file).
   * Click **Publish release** when you are done.
   * Confirm that the new version of Sphinx Gallery
     `is posted to PyPI <https://pypi.org/project/sphinx-gallery/#history>`_.

3. Now that the releases are complete, we need to switch the `master`` branch
   back into a developer mode. Bump the `Sphinx Gallery version number <https://github.com/sphinx-gallery/sphinx-gallery/blob/master/sphinx_gallery/__init__.py>`_
   to the next minor (or major) release and append ``.dev0`` to the end, and make a PR for this change.

4. Celebrate! You've just released a new version of Sphinx Gallery!
