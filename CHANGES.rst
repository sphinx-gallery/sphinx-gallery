Change Log
==========

v0.1.2
------

Bug Fixes
.........

* Examples that use ``if __name__ == '__main__'`` guards are now run
* Added vertical space between code output and code source in non
  notebook examples

v0.1.1
------

Bug Fixes
'''''''''

* Restore the html-noplot functionality
* Gallery CSS now implictly enforces thumbnails width

v0.1.0
------

Highlights
''''''''''

Example scripts are now available for download as IPython Notebooks
`#75 <https://github.com/sphinx-gallery/sphinx-gallery/pull/75>`_

New features
------------

* Configurable filename pattern to select which example scripts are
  executed while building the Gallery
* Examples script update check are now by md5sum check and not date
* Broken Examples now display a Broken thumbnail in the gallery view,
  inside the rendered example traceback is printed. User can also set
  build process to abort as soon as an example fails.
* Sorting examples by script size
* Improve examples style

v0.0.11
-------

Highlights
''''''''''

This release incorporates the Notebook styled examples for the gallery
with PR `#36
<https://github.com/sphinx-gallery/sphinx-gallery/pull/36>`_

Incompatible Changes
''''''''''''''''''''

Sphinx-Gallery renames its python module name to sphinx\_gallery this
follows the discussion raised in `#47
<https://github.com/sphinx-gallery/sphinx-gallery/issues/47>`_ and
resolved with `#66
<https://github.com/sphinx-gallery/sphinx-gallery/pull/66>`_

The gallery configuration dictionary also changes its name to ``sphinx_gallery_conf``

From PR `#36
<https://github.com/sphinx-gallery/sphinx-gallery/pull/36>`_ it is
decided into a new namespace convention for images, thumbnails and
references. See `comment
<https://github.com/sphinx-gallery/sphinx-gallery/pull/36#issuecomment-121392815>`_


v0.0.10
-------

Highlights
''''''''''

This release allows to use the Back references. This features
incorporates fine grained examples galleries listing examples using a
particular function. `#26
<https://github.com/sphinx-gallery/sphinx-gallery/pull/26>`_

New features
''''''''''''

* Shell script to place a local copy of Sphinx-Gallery in your project
* Support Mayavi plots in the gallery
