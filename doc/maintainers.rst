How to make a release
=====================

* Update the change log

Use `github_changelog_generator
<https://github.com/skywinder/github-changelog-generator#installation>`_ to
gather all merged pull requests and closed issues during the development
cycle. We do this because our failing discipline of writing in the
CHANGES.rst all relevant changes, this helps our memory.

.. code-block:: bash

   github_changelog_generator sphinx-gallery/sphinx-gallery

Read the changes in the generated CHANGELOG.md and propagate the relevant to
CHANGES.rst

* Update version

Update the version in ``sphinx_gallery/__init__.py``.

* Build the docs cleanly

Make sure to clean all and have a clean build. Double-check visually that
everything looks right.

* Push to your own master branch and check CI is happy
* Draft release
copy and edit to github markdown all changes from CHANGELOG.md.

* Build a source distribution

.. code-block:: bash

   python setup.py sdist

* Test upload to PyPI

.. code-block:: bash

   twine upload --repository test dist/sphinx-gallery-<version>.tar.gz

* Upload to PyPI


.. code-block:: bash

   twine upload dist/sphinx-gallery-<version>.tar.gz
