# Contributing to `sphinx-gallery`

The Sphinx Gallery team is distributed across the globe in a variety of locations,
if you'd like to help contribute to sphinx-gallery, see the sections below for
some pointers.

## Making a new release

Sphinx Gallery is [hosted on the pypi repository](https://pypi.org/project/sphinx-gallery/).
To create a new release of Sphinx Gallery, you need to do these things:

1. Ensure that you have push access to the [Sphinx Gallery pypi repository](https://pypi.org/project/sphinx-gallery/)
2. Install [the twine package](https://twine.readthedocs.io/en/latest/). This is a package that helps you
   bundle and push new Python package distributions to pip.
3. Ensure that new additions, bugs, etc for this release are updated in
   [the CHANGELOG](https://github.com/sphinx-gallery/sphinx-gallery/blob/master/CHANGES.rst)
 release of Sphinx Gallery has
4. Ensure that all issues in the
   [milestone for the new version](https://github.com/sphinx-gallery/sphinx-gallery/milestones?direction=asc&sort=due_date) have been completed.
5. Ensure that the [Sphinx Gallery version number](https://github.com/sphinx-gallery/sphinx-gallery/blob/master/sphinx_gallery/__init__.py)
   is correct, and remove the `dev0` part of the version number.
6. Create a new distribution for Sphinx Gallery by
   [following the twine release instructions](https://twine.readthedocs.io/en/latest/#using-twine)
7. Confirm that the new version of Sphinx Gallery [is posted to pypi](https://pypi.org/project/sphinx-gallery/)
8. Bump the [Sphinx Gallery version number](https://github.com/sphinx-gallery/sphinx-gallery/blob/master/sphinx_gallery/__init__.py) to
   the next minor (or major) release and append `dev0` to the end.
9. Celebrate! You've just released a new version of Sphinx Gallery!