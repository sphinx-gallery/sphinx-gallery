.. include:: ../README.rst


Know your Gallery files
=======================

The Gallery has been built, now you and all of your project's users
can already start enjoying it. All the temporary files needed to
generate the gallery(rst files, images, chache objects, etc) are
stored where you configured in ``gallery_dirs``. The final files that go
into the HTML version of your documentation have a particular
namespace, to avoid colisions with your own files and images.

Our namespace convention is to prefix everything with ``sphx_glr`` and
change path separators with underscores. This is valid for
cross-references labels, and images.

So for example if we want to reference the example
:ref:`sphx_glr_auto_examples_plot_gallery_version.py`, we just call
its reference
``:ref:`sphx_glr_auto_examples_plot_gallery_version.py```. The image
it generated has the name ``sphx_glr_plot_gallery_version_thumb.png``
and its thumbnail is ``sphx_glr_plot_gallery_version_thumb.png``

Disable joint download of all gallery scripts
---------------------------------------------

By default Sphinx-Gallery prepares zip files of all python scripts and
all Jupyter notebooks for each gallery section and makes them
available for download at the end of each section. To disable this
behavior add to the configuration dictionary in your ``conf.py`` file

.. code-block:: python

    sphinx_gallery_conf = {
	'download_section_examples'  : False}
