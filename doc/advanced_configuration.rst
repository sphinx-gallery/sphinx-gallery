======================
Advanced Configuration
======================

Here are the personal configurations that you can modify within Sphinx-Gallery.


Changing default directories
============================

Within your Sphinx ``conf.py`` file you need to add a configuration dictionary:

.. code-block:: python

    sphinxgallery_conf = {
        'examples_dir' : '../examples',              # path to your examples scripts
        'gallery_dir'  : 'auto_examples'}            # path where to save gallery generated examples


Directory paths are relative to your ``conf.py`` location.

Having Multiple galleries
-------------------------

Sphinx-Gallery only supports up to subfolder level in its gallery directories.
This might be a limitation for you. Or you might want to have separate
galleries for different purposes, an examples gallery and a tutorials gallery.
For this you use in your Sphinx ``conf.py`` file a list of directories in
the sphinx configuration dictionary:

.. code-block:: python

    sphinxgallery_conf = {
        'examples_dir'   : ['../examples', '../tutorials'],
        'gallery_dir'    : ['auto_examples', 'tutorials'],
    }

Keep in mind that both list have to be of the same length.


Linking to external documentations
==================================

Sphinx-Gallery enables you to add hyperlinks in your example scripts so that
you can link the used functions to their matching online documentation. As such
code snippets within the gallery appear like this

.. raw:: html

    <div class="highlight-python"><div class="highlight"><pre>
    <span class="n">y</span> <span class="o">=</span> <a href="http://docs.scipy.org/doc/numpy-1.9.1/reference/generated/numpy.sin.html#numpy.sin"><span class="n">np</span><span class="o">.</span><span class="n">sin</span></a><span class="p">(</span><span class="n">x</span><span class="p">)</span>
    </pre></div>
    </div>

Have a look at this in full action
in our example :ref:`example_auto_examples_plot_gallery_version.py`.

To make this work in your documentation you need to include to the configuration
dictionary within your Sphinx ``conf.py`` file :

.. code-block:: python

    sphinxgallery_conf = {
        'reference_url':  {
                 # The module you locally document uses a None
                'sphinxgallery': None,

                # External python modules use their documentation websites
                'matplotlib': 'http://matplotlib.org',
                'numpy': 'http://docs.scipy.org/doc/numpy-1.9.1'}
        }



Establishing local references to examples
=========================================

Linking commands in your examples to their documentation is not enough.
Sphinx-Gallery also enables you, when documenting your modules, to reference
into examples that use that particular module.

In that case within your Sphinx ``conf.py`` file you need to add to their
configuration dictionary:

.. code-block:: python

    sphinxgallery_conf = {
        # path where to store your example linker templates
        'mod_example_dir'     : 'modules/generated',

        # Your documented modules. You can use a string or a list of strings
        'doc_module'          : ('sphinxgallery', 'numpy')}

The path you specified will get populated with the links to examples using your
module and their methods. Then within your sphinx documentation files you
include these lines to include these links::

    .. include:: modules/generated/numpy.linspace.examples
    .. raw:: html

        <div style='clear:both'></div>

The file you are including is referenced with its relative path to your defined
directory and includes all the module specific location. In this case
``numpy.linspace``.

That will be rendered as

.. include:: modules/generated/numpy.linspace.examples
.. raw:: html

        <div style='clear:both'></div>


