======================
Advanced Configuration
======================

Here are the personal configurations that you can modify within Sphinx-Gallery.
What is writen from here on are the default values.

Changing default directories
============================

Within your Sphinx ``conf.py`` file you need to add a configuration dictionary:

.. code-block:: python

    sphinxgallery_conf = {
        'root_dir'          : '../examples',              # path to your examples scripts
        'examples_gallery'  : 'auto_examples'}            # path where to save gallery generated examples


Directory paths are relative to your ``conf.py`` location.

Linking to external documentations
==================================

If you want to hyperlink commands in your example scripts you can. Again within
your Sphinx ``conf.py`` file you need to add a configuration dictionary:

.. code-block:: python

    sphinxgallery_conf = {
        'doc_module'        : 'sphinxgallery',      # Your module
        'resolver_urls'     : {                     # External python modules documentation websites
            'matplotlib': 'http://matplotlib.org',
            'numpy': 'http://docs.scipy.org/doc/numpy-1.9.1',
            'scipy': 'http://docs.scipy.org/doc/scipy-0.15.1/reference'}
        }

Establishing local calls to examples
====================================

Maybe when you are documenting your modules you would like to reference
to examples that use that particular module. In that case within
your Sphinx ``conf.py`` file you need to add a configuration dictionary:

.. code-block:: python

    sphinxgallery_conf = {
        'mod_generated'     : 'modules/generated', # path where to store your example linker
        'doc_module'        : 'numpy'}             # Your module (In this example we use numpy)

Then within your sphinx documentation files you include this lines::

    .. include:: modules/generated/numpy.linspace.examples
    .. raw:: html

        <div style='clear:both'></div>

where you have include an ``*.example`` file that is stored in your ``mod_generated``
directory you put in the configuration. And then the file you call has all the path
of your module. In this case ``numpy.linspace``. That will be rendered as

.. include:: modules/generated/numpy.linspace.examples
.. raw:: html

        <div style='clear:both'></div>
