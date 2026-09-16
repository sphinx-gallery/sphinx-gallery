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

1. Update ``CHANGES.rst`` in a PR
---------------------------------

1. Use `github_changelog_generator
   <https://github.com/github-changelog-generator/github-changelog-generator#installation>`_ to
   gather all merged pull requests and closed issues during the development
   cycle. You will likely need to `generate a Github token <https://github.com/settings/tokens/new?description=GitHub%20Changelog%20Generator%20token>`_
   as Github only allows 50 unauthenticated requests per hour. In the
   command below ``<version>`` is the current (not development) version of
   the package, e.g., ``0.6.0``. The changelog can generated with the following::

      github_changelog_generator --since-tag=v<version> --token <your-40-digit-token>

   To avoid the need to pass ``--token``, you can use ``export CHANGELOG_GITHUB_TOKEN=<your-40-digit-token>`` instead.

2. Update `PR labels on GitHub <https://github.com/sphinx-gallery/sphinx-gallery/pulls?q=is%3Apr+is%3Aclosed>`__
   if necessary and regenerate ``CHANGELOG.md`` so that PRs are categorized correctly. The labels we currently use are:

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

   Once all PRs land in one of these categories using the changelog generator,
   manually edit CHANGELOG.md to look reasonable if necessary.

3. Propagate the relevant changes to `CHANGES.rst <https://github.com/sphinx-gallery/sphinx-gallery/blob/master/CHANGES.rst>`_.
   You can easily convert it reST with pandoc::

      pandoc CHANGELOG.md --wrap=none -o CHANGELOG.rst

   Then copy just the sections to ``CHANGES.rst``. **Keep ``CHANGELOG.md`` for
   later.**

4. Open a PR with the above **changelog** changes (along with any updates to this
   ``maintainers.rst`` document!). There is no version to bump: the version comes
   from the git tag via ``setuptools-scm``, and ``sphinx_gallery.__version__``
   reads it back with ``importlib.metadata``.

5. Make sure CIs are green.

6. Check that the built documentation looks correct.

7. Get somebody else to make sure all looks well, and merge this pull request.

2. Finalize the release
-----------------------

1. Make sure CIs are green following the "Release" PR.
2. Create a new release on GitHub

   * Go to the `Draft a new release <https://github.com/sphinx-gallery/sphinx-gallery/releases/new>`_ page.
   * The **tag version** is the semantic version being released, prepended with ``v``. E.g., ``v0.7.0``.
     This tag is what sets the released version, so make sure it is right.
   * The **release title** is ``Release <tag-version>``.
   * The **description** should contain the markdown changelog
     you generated above (in the ``CHANGELOG.md`` file) and include a "Full changelog"
     link at the top, e.g.;
     ``[Full Changelog](https://github.com/sphinx-gallery/sphinx-gallery/compare/v0.13.0...v0.14.0)``
   * Click **Publish release** when you are done.
   * Confirm that the new version of Sphinx Gallery
     `is posted to PyPI <https://pypi.org/project/sphinx-gallery/#history>`_.

3. Celebrate! You've just released a new version of Sphinx Gallery! ``master`` goes
   back into developer mode on its own: the next commit after the tag builds as
   ``<next-minor>.0.dev<N>``.

3. Post-release tasks
---------------------

1. Check for any deprecations (e.g., ``git grep eprecat``) and complete them, usually by
   removing code or some behavior in a PR.
2. Check and update **minimum supported (old)** Python and Sphinx versions (older than
   2 years) plus check for any **new** ones, and update if necessary in a PR:

   - ``pyproject.toml`` (old)
   - ``.github/workflows/tests.yml`` (old and new)
   - ``README.rst::Installation`` (old)
