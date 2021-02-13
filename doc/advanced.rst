.. _advanced_usage:

==============
Advanced usage
==============

This page contains more advanced topics in case you want to understand how
to use Sphinx-Gallery more deeply.

.. contents:: **Contents**
    :local:
    :depth: 2

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
generate the gallery (rst files, images, cache objects, etc) are
stored where you configured in ``gallery_dirs``. The final files that go
into the HTML version of your documentation have a particular
namespace, to avoid collisions with your own files and images.

Our namespace convention is to prefix everything with ``sphx_glr`` and
change path separators with underscores. This is valid for
cross-references labels, and images.

So for example if we want to reference the example
:ref:`sphx_glr_auto_examples_plot_0_sin.py`, we just call
its reference
``:ref:`sphx_glr_auto_examples_plot_0_sin.py```. The image
it generated has the name ``sphx_glr_plot_0_sin_001.png``
and its thumbnail is ``sphx_glr_plot_0_sin_thumb.png``

You can also include part of a gallery script elsewhere in your documentation
using the :rst:dir:`literalinclude` directive, in order to limit code duplication:


.. code-block:: rst

   .. literalinclude:: ../examples/plot_0_sin.py
      :language: python
      :start-after: # License: BSD 3 clause
      :end-before: # To avoid matplotlib

The above directive inserts the following block:

.. literalinclude:: ../examples/plot_0_sin.py
    :language: python
    :start-after: # License: BSD 3 clause
    :end-before: # To avoid matplotlib

.. warning::

   Using literalinclude is fragile and can break easily when examples are
   changed (all the more when line numbers are used instead of ``start-after``
   and  ``end-before``). Use with caution: linking directly to examples is
   a more robust alternative.

.. _warning_errors:

Understanding warning and error outputs
=======================================

Any warnings or errors that occur when executing code blocks in the gallery
Python files will be printed in pink during building of the documentation. The
``.py`` file path and the line number that the error occurred in will also be
printed. For example, the example
:ref:`sphx_glr_auto_examples_no_output_plot_raise.py` will raise the following
error::

    File "<full_path>/examples/no_output/plot_raise.py", line 27, in <module>
        iae
    NameError: name 'iae' is not defined

Problems in the text (rST) blocks of the gallery Python files will result
in warnings or errors when Sphinx is converting the generated ``.rst`` files
to HTML. These will be printed by Sphinx in pink, after code block errors,
during building of the documentation. In this case, the ``.rst`` file path and
``.rst`` file line number will be printed. To fix the problem, you will need
to amend the original ``.py`` file, **not** the generated ``.rst`` file.
To figure out where the problem is, you will need to match the content of the
``.rst`` file at the line number printed to the original ``.py`` file.

Example ``.rst`` warning::

    <full_path>/auto_examples/plot_example.rst:19: WARNING: Explicit markup ends without a blank line; unexpected unindent.

The warning above occurred due to line 19 in ``plot_example.rst``. The
original ``plot_example.py`` file will need to be amended to fix it.
Sphinx-Gallery only (re)builds new, modified or failed examples, so
re-running the documentation build should rebuild just the modified example,
allowing for quick iteration.

.. _custom_scraper:

Write a custom image scraper
============================

.. warning:: The API for custom scrapers is currently experimental.

By default, Sphinx-Gallery supports image scrapers for Matplotlib
(:func:`~sphinx_gallery.scrapers.matplotlib_scraper`) and Mayavi
(:func:`~sphinx_gallery.scrapers.mayavi_scraper`). If you wish to capture
output from other python packages, first determine if the object you wish to
capture has a ``_repr_html_`` method. If so, you can use the configuration
``capture_repr`` (:ref:`capture_repr`) to control the display of the object,
without the need to write a custom scraper. This configuration allows capture
of the raw html output, in a process similar to other html-based displays such
as `jupyter <https://jupyter.org/>`_. If the first option does not work,
this section describes how to write a custom scraper.

Image scrapers are functions (or callable class instances) that do two things:

1. Collect a list of images created in the latest execution of code.
2. Write these images to disk in PNG, JPEG, or SVG format (with .png, .jpg, or
   .svg extensions, respectively)
3. Return rST that embeds these figures in the built documentation.

The function should take the following inputs (in this order):

1. ``block`` - a Sphinx-Gallery ``.py`` file is separated into consecutive
   lines of 'code' and rST 'text', called 'blocks'. For each
   block, a tuple containing the (label, content, line_number)
   (e.g. ``('code', 'print("Hello world")', 5)``) of the block is created.

   * 'label' is a string that can either be ``'text'`` or ``'code'``. In this
     context, it should only be ``'code'`` as this function is only called for
     code blocks.
   * 'content' is a string containing the actual content of the code block.
   * 'line_number' is an integer, indicating the line number that the block
     starts at.

2. ``block_vars`` - dictionary of configuration and runtime variables. Of
   interest for image scrapers is the element ``'image_path_iterator'`` which
   is an iterable object which returns an absolute path to an image file name
   adhering to Sphinx-Gallery naming convention. The path directs to the
   ``gallery_dirs/images`` directory (:ref:`configure_and_use_sphinx_gallery`)
   and the image file name is ``'sphx_glr_'`` followed by the name of the
   source ``.py`` file then a number, which starts at 1 and increases by 1 at
   each iteration. The default file format is ``.'png'``. For example:
   ``'home/user/Documents/module/auto_examples/images/sphx_glr_plot_mymodule_001.png'``

3. ``gallery_conf`` - dictionary containing the configuration of Sphinx-Gallery,
   set under ``sphinx_gallery_conf`` in ``doc/conf.py`` (:ref:`configuration`).

It should return a string containing the rST for embedding this figure in the
documentation. See :func:`~sphinx_gallery.scrapers.matplotlib_scraper` for an
example of a scraper function (click on 'source' below the function name to see
the source code). The :func:`~sphinx_gallery.scrapers.matplotlib_scraper` uses
the helper function :func:`sphinx_gallery.scrapers.figure_rst` to help generate
rST (see below).

This function will be called once for each code block of your examples.
Sphinx-Gallery will take care of scaling images for the gallery
index page thumbnails. PNG images are scaled using Pillow, and
SVG images are copied.

.. warning:: SVG images do not work with ``latex`` build modes, thus will not
             work while building a PDF version of your documentation.

Example 1: a Matplotlib and Mayavi-style scraper
------------------------------------------------

For example, we will show sample code for a scraper for a hypothetical package.
It uses an approach similar to what :func:`sphinx_gallery.scrapers.matplotlib_scraper`
and :func:`sphinx_gallery.scrapers.mayavi_scraper` do under the hood, which
use the helper function :func:`sphinx_gallery.scrapers.figure_rst` to
create the standardized rST. If your package will be used to write an image file
to disk (e.g., PNG or JPEG), we recommend you use a similar approach. ::

   def my_module_scraper(block, block_vars, gallery_conf)
       import mymodule
       # We use a list to collect references to image names
       image_names = list()
       # The `image_path_iterator` is created by Sphinx-Gallery, it will yield
       # a path to a file name that adheres to Sphinx-Gallery naming convention.
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

Example 2: detecting image files on disk
----------------------------------------

Here's another example that assumes that images have *already been written to
disk*. In this case we won't *generate* any image files, we'll only generate
the rST needed to embed them in the documentation. Note that the example scripts
will still need to be executed to scrape the files, but the images
don't need to be produced during the execution.

We'll use a callable class in this case, and assume it is defined within your
package in a module called ``scraper``. Here is the scraper code::

   from glob import glob
   import shutil
   import os
   from sphinx_gallery.gen_rst import figure_rst

   class PNGScraper(object):
       def __init__(self):
           self.seen = set()

       def __repr__(self):
           return 'PNGScraper'

       def __call__(self, block, block_vars, gallery_conf):
           # Find all PNG files in the directory of this example.
           path_current_example = os.path.dirname(block_vars['src_file'])
           pngs = sorted(glob(os.path.join(path_current_example, '*.png')))

           # Iterate through PNGs, copy them to the sphinx-gallery output directory
           image_names = list()
           image_path_iterator = block_vars['image_path_iterator']
           for png in pngs:
               if png not in self.seen:
                   self.seen |= set(png)
                   this_image_path = image_path_iterator.next()
                   image_names.append(this_image_path)
                   shutil.move(png, this_image_path)
           # Use the `figure_rst` helper function to generate rST for image files
           return figure_rst(image_names, gallery_conf['src_dir'])


Then, in our ``conf.py`` file, we include the following code::

   from mymodule import PNGScraper

   sphinx_gallery_conf = {
       ...
       'image_scrapers': ('matplotlib', PNGScraper()),
   }

Example 3: matplotlib with SVG format
-------------------------------------
The :func:`sphinx_gallery.scrapers.matplotlib_scraper` supports ``**kwargs``
to pass to :meth:`matplotlib.figure.Figure.savefig`, one of which is the
``format`` argument. Currently Sphinx-Gallery supports PNG (default) and SVG
output formats. To use SVG, you can do::

    from sphinx_gallery.scrapers import matplotlib_scraper

    class matplotlib_svg_scraper(object):

        def __repr__(self):
            return self.__class__.__name__

        def __call__(self, *args, **kwargs):
            return matplotlib_scraper(*args, format='svg', **kwargs)

    sphinx_gallery_conf = {
        ...
        'image_scrapers': (matplotlib_svg_scraper(),),
        ...
    }

You can also use different formats on a per-image basis, but this requires
writing a customized scraper class or function.

Integrate custom scrapers with Sphinx-Gallery
---------------------------------------------

Sphinx-Gallery plans to internally maintain only two scrapers: matplotlib and
mayavi. If you have extended or fixed bugs with these scrapers, we welcome PRs
to improve them!

On the other hand, if you have developed a custom scraper for a different
plotting library that would be useful to the broader community, we encourage
you to get it working with Sphinx-Gallery and then maintain it externally
(probably in the package that it scrapes), and then integrate and advertise
it with Sphinx-Gallery. You can:

1. Contribute it to the list of externally supported scrapers located in
   :ref:`reset_modules`.
2. Optional: add a custom hook to your module root to simplify scraper use.
   Taking PyVista as an example, adding ``pyvista._get_sg_image_scraper()``
   that returns the ``callable`` scraper to be used by Sphinx-Gallery allows
   PyVista users to just use strings as they already can for
   ``'matplotlib'`` and ``'mayavi'``::

       sphinx_gallery_conf = {
           ...
           'image_scrapers': ('pyvista',)
       }

   Sphinx-Gallery will look for this custom function and call it to get the
   PyVista image scraper to use before running any examples.

.. _custom_reset:

Define resetting behavior (e.g., for custom libraries)
======================================================

Sphinx-Gallery natively supports resetting ``matplotlib`` and ``seaborn``.
However, if you'd like to support resetting for other libraries (or would like
to modify the resetting behavior for a natively-supported library), you can
add a custom function to the resetting tuple defined in ``conf.py``.

The function takes two variables: a dictionary called ``gallery_conf`` (which is
your Sphinx-Gallery configuration) and a string called ``fname`` (which is the
file name of the currently-executed Python script). These generally don't need
to be used in order to perform whatever resetting behavior you want, but must
be included in the function definition for compatibility reasons.

For example, to reset matplotlib to always use the ``ggplot`` style, you could do::

   def reset_mpl(gallery_conf, fname):
       from matplotlib import style
       style.use('ggplot')

Any custom functions can be defined (or imported) in ``conf.py`` and given to
the ``reset_modules`` configuration key. For the function defined above::

   sphinx_gallery_conf = {
       ...
       'reset_modules': (reset_mpl, 'seaborn'),
   }

.. note:: Using resetters such as ``reset_mpl`` that deviate from the
          standard behavior that users will experience when manually running
          examples themselves is discouraged due to the inconsistency
          that results between the rendered examples and local outputs.

Using (only) Sphinx-Gallery styles
==================================

If you just want to make use of sphinx-Gallery CSS files, instead of using
the ``sphinx_gallery.gen_gallery`` extension, you can use in ``conf.py``::

    extensions = ['sphinx_gallery.load_style']

This will only cause the ``gallery.css`` file to be added to your build.
