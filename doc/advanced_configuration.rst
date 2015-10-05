======================
Advanced Configuration
======================

Here are the personal configurations that you can modify within Sphinx-Gallery.


Changing default directories
============================

Within your Sphinx ``conf.py`` file you need to add a configuration dictionary:

.. code-block:: python

    sphinx_gallery_conf = {
        'examples_dirs' : '../examples',              # path to your examples scripts
        'gallery_dirs'  : 'auto_examples'}            # path where to save gallery generated examples


Directory paths are relative to your ``conf.py`` location.

Having Multiple galleries
-------------------------

Sphinx-Gallery only supports up to subfolder level in its gallery directories.
This might be a limitation for you. Or you might want to have separate
galleries for different purposes, an examples gallery and a tutorials gallery.
For this you use in your Sphinx ``conf.py`` file a list of directories in
the sphinx configuration dictionary:

.. code-block:: python

    sphinx_gallery_conf = {
        'examples_dirs'   : ['../examples', '../tutorials'],
        'gallery_dirs'    : ['auto_examples', 'tutorials'],
    }

Keep in mind that both lists have to be of the same length.


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
in our example :ref:`sphx_glr_auto_examples_plot_gallery_version.py`.

To make this work in your documentation you need to include to the configuration
dictionary within your Sphinx ``conf.py`` file :

.. code-block:: python

    sphinx_gallery_conf = {
        'reference_url':  {
                 # The module you locally document uses a None
                'sphinx_gallery': None,

                # External python modules use their documentation websites
                'matplotlib': 'http://matplotlib.org',
                'numpy': 'http://docs.scipy.org/doc/numpy-1.9.1'}
        }



Establishing local references to examples
=========================================

Sphinx-Gallery also enables you, when documenting your modules, to
reference into the examples that use that particular class or
function. For example if we are documenting the numpy.linspace
function its possible to embedd a small gallery of examples using it
like this:

.. include:: modules/generated/numpy.linspace.examples
.. raw:: html

        <div style='clear:both'></div>



For such behavior to be available you have to extend in your
Sphinx-Gallery configuration directory with:

.. code-block:: python

    sphinx_gallery_conf = {
        # path to store the module using example template
        'mod_example_dir'     : 'modules/generated',

        # Your documented modules. You can use a string or a list of strings
        'doc_module'          : ('sphinx_gallery', 'numpy')}

The path you specify in ``mod_example_dir`` will get populated with
ReStructuredText files describing the examples thumbnails with links
to them but only for the specific module.


Then within your sphinx documentation files you
include these lines to include these links::

    .. include:: modules/generated/numpy.linspace.examples
    .. raw:: html

        <div style='clear:both'></div>

Auto documenting your API with links to examples
------------------------------------------------

The previous feature can be automated for all your modules combining
it with the standard sphinx extension `autosummary
<http://sphinx-doc.org/ext/autosummary.html>`. First enable it in your
``conf.py`` extensions list.

.. code-block:: python

    import sphinxgallery
    extensions = [
        ...
	'sphinx.ext.autodoc',
        ]

Then append to your template files for classes and functions::

    .. include:: {{module}}.{{objname}}.examples
    .. raw:: html

	<div class='clear:both'></div>


Using a custom default thumbnail image
======================================

In case you want to use your own image for the thumbnail of examples that do
not generate any plot, you can specify it by editing your Sphinx ``conf.py``
file. You need to add to the configuration dictionary a key called
`default_thumb_file`. For example:

.. code-block:: python

    sphinx_gallery_conf = {
        'default_thumb_file'     : 'path/to/thumb/file.png'}}
