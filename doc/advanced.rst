.. _advanced_usage:

==============
Advanced usage
==============

This page contains more advanced topics in case you want to understand how
to use Sphinx-Gallery more deeply.

Extend your Makefile for Sphinx-Gallery
=======================================

This section describes some common extensions to the documentation Makefile
that are useful for Sphinx-Gallery.

Cleaning the gallery files
--------------------------

Once your gallery is working you might need completely remove all generated files by
Sphinx-Gallery to have a clean build. For this we recommend adding the following
to your Sphinx ``Makefile``:

.. code-block:: bash

    clean:
            rm -rf $(BUILDDIR)/*
            rm -rf auto_examples/

Build the gallery without running any examples
----------------------------------------------

If you wish to build your gallery without running examples first (e.g., if an
example takes a long time to run), add the following to your ``Makefile``.

.. code-block:: bash

    html-noplot:
            $(SPHINXBUILD) -D plot_gallery=0 -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
            @echo
            @echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

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

.. _custom_scraper:

Writing a custom image scraper
==============================

.. warning:: The API for custom scrapers is currently experimental.

By default, Sphinx-gallery supports image scrapers for Matplotlib
(:func:`sphinx_gallery.scrapers.matplotlib_scraper`) and Mayavi
(:func:`sphinx_gallery.scrapers.mayavi_scraper`). You can also write a custom
scraper for other python packages. This section describes how to do so.

Image scrapers are functions (or callable class instances) that do two things:

1. Collect a list of images created in the latest execution of code.
2. Write these images to disk
3. Return rST that embeds these figures in the built documentation.

The function should take the following inputs (in this order): ``block``,
``block_vars``, and ``gallery_conf``. It should return a string containing the
rST for embedding this figure in the documentation.
See the :func:`sphinx_gallery.scrapers.matplotlib_scraper` for
a description of the inputs/outputs.

This function will be called once for each code block of your examples.

Example one - a Matplotlib and Mayavi-style scraper
---------------------------------------------------

For example, we will show sample code for a scraper for a hypothetical package.
It uses an approach similar to what :func:`sphinx_gallery.scrapers.matplotlib_scraper`
and :func:`sphinx_gallery.scrapers.mayavi_scraper` do under the hood, which
use the helper function :func:`sphinx_gallery.scrapers.figure_rst` to
create the standardized rST. If your package will be used to write an image file
to disk (e.g., PNG or JPEG), we recommend you use a similar approach.

.. code-block:: python

   def my_module_scraper(block, block_vars, gallery_conf)
       import mymodule
       # We use a list to collect references to image names
       image_names = list()
       # The `image_path_iterator` is created by Sphinx-gallery, it will yield
       # a path to a file name that adheres to Sphinx-gallery naming convention.
       image_path_iterator = block_vars['image_path_iterator']

       # Define a list of our already-created figure objects.
       list_of_my_figures = mymodule.get_figures()

       # Iterate through figure objects, save to disk, and keep track of paths.
       for fig, image_path in zip(list_of_my_figures, image_path_iterator):
           fig.save_png(image_path)
           image_names.append(image_path)

       # Close all references to figures so they aren't used later.
       mymodule.close('all')

       # Use the `figure_rst` helper function to generate the rST for this
       # code block's figures. Alternatively you can define your own rST.
       return figure_rst(image_names, gallery_conf['src_dir'])

This code would be defined either in your ``conf.py`` file, or as a module that
you import into your ``conf.py`` file. The configuration needed to use this
scraper would look like::

    sphinx_gallery_conf = {
        ...
        'image_scrapers': ('matplotlib', my_module_scraper),
    }

Example two - detecting image files on disk
-------------------------------------------

Here's another example that assumes that images have *already been written to
disk*. In this case we won't *generate* any image files, we'll only generate
the rST needed to embed them in the documentation.

We'll use a callable class in this case, and assume it is defined within your
package in a module called ``scraper``. Here is the scraper code:

.. code-block:: python

   from glob import glob
   import shutil
   import os
   from sphinx_gallery.gen_rst import figure_rst

   class PNGScraper(object):
       def __init__(self):
           self.seen = set()

       def __call__(self, block, block_vars, gallery_conf):
           # Find all PNG files in the directory of this example.
           path_current_example = os.path.dirname(block_vars['src_file'])
           pngs = sorted(glob(os.path.join(os.getcwd(), '*.png'))

           # Iterate through PNGs, copy them to the sphinx-gallery output directory
           image_names = list()
           image_path_iterator = block_vars['image_path_iterator']
           for png in pngs:
               if png not in seen:
                   seen |= set(png)
                   this_image_path = image_path_iterator.next()
                   image_names.append(this_image_path)
                   shutil.move(png, this_image_path)
           # Use the `figure_rst` helper function to generate rST for image files
           return figure_rst(image_names, gallery_conf['src_dir'])


Then, in our ``conf.py`` file, we include the following code:

.. code-block:: python

   from mymodule import PNGScraper
   my_scraper_instance = PNGScraper()

   sphinx_gallery_conf = {
       ...
       'image_scrapers': ('matplotlib', my_scraper_instance),
   }

Contributing scrapers back to Sphinx-gallery
--------------------------------------------

If you've developed a custom scraper for Sphinx-gallery that would be useful
to the broader community, we encourage you to contribute it to the list of
natively-supported scrapers located in
`the scrapers module <https://github.com/sphinx-gallery/sphinx-gallery/blob/master/sphinx_gallery/scrapers.py>`_.
We welcome PRs!

.. _custom_reset:

Defining resetting behavior for custom visualization libraries
--------------------------------------------------------------

Sphinx-gallery natively supports resetting ``matplotlib`` and ``seaborn``.
However, if you'd like to support resetting for other libraries (or would like
to modify the resetting behavior for a natively-supported library), you can
add a custom function to the resetting tuple defined in ``conf.py``.

The function takes two variables: a dictionary called ``gallery_conf`` (which is
your Sphinx-gallery configuration) and a string called ``fname`` (which is the
file name of the currently-executed Python script). These generally don't need
to be used in order to perform whatever resetting behavior you want, but must
be included in the function definition for compatibility reasons.

For example, to reset matplotlib to always use the ``ggplot`` style, you could do:


.. code-block:: python

   def reset_mpl(gallery_conf, fname):
       from matplotlib import style
       style.use('ggplot')

Any custom functions can be defined (or imported) in ``conf.py`` and given to
the ``reset_modules`` configuration key. For the function defined above:

.. code-block:: python

   sphinx_gallery_conf = {
       ...
       'reset_modules': (reset_mpl, 'seaborn'),
   }

.. note:: Using resetters such as ``reset_mpl`` that deviate from the
          standard behavior that users will experience when manually running
          examples themselves is discouraged due to the inconsistency
          that results between the rendered examples and local outputs.
