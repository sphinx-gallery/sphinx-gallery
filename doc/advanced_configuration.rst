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


Linking to external documentations
==================================

Sphinx-Gallery enables you to hyperlink commands in your example scripts to the
matching location in their online documentation . Have a look at this in action
in our example :ref:`example_plot_gallery_version.py`.

To make this work in your documentation you need to include to the configuration
dictionary within your Sphinx ``conf.py`` file :

.. code-block:: python

    sphinxgallery_conf = {
        'reference_url':  {
                 # Modules you locally document use a None
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
