======================
Advanced Configuration
======================

Here are the personal configurations that you can modify within Sphinx-Gallery.

.. _multiple_galleries_config:

Manage Multiple galleries
=========================

Sphinx-Gallery only supports up to sub-folder level in its gallery directories.
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

.. _build_pattern:

Building examples matching a pattern
====================================

By default, Sphinx-Gallery execute only examples beginning with ``plot``. However,
if this naming convention does not suit your project, you can modify this pattern
in your Sphinx ``conf.py``. For example:

.. code-block:: python

    sphinx_gallery_conf = {
        'filename_pattern'  : '/plot_compute_'
    }

will build all examples starting with ``plot_compute_``. The key ``filename_pattern`` accepts
`regular expressions`_ which will be matched with the full path of the example. This is the reason
the leading ``'/'`` is required. Users are advised to use ``os.sep`` instead of ``'/'`` if
they want to be agnostic to the operating system.

This option is also useful if you want to build only a subset of the examples. For example, you may
want to build only one example so that you can link it in the documentation. In that case,
you would do:

.. code-block:: python

    sphinx_gallery_conf = {
        'filename_pattern' : 'plot_awesome_example.py'
    }

Here, one should escape the dot ``'\.'`` as otherwise python `regular expressions`_ matches any character. Nevertheless, as
one is targeting a specific file, it is most certainly going to match the dot in the filename.

Similarly, to build only examples in a specific directory, you can do:

.. code-block:: python

    sphinx_gallery_conf = {
        'filename_pattern' : '/directory/plot_'
    }

Alternatively, you can skip some examples. For example, to skip building examples
starting with ``plot_long_examples_``, you would do:

.. code-block:: python

    sphinx_gallery_conf = {
        'filename_pattern' : '/plot_(?!long_examples)'
    }

As the patterns are parsed as `regular expressions`_, users are advised to consult the
`regular expressions`_ module for more details.

.. _link_to_documentation:

Linking to documentation
========================

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


.. _references_to_examples:

References to examples (backreferences)
=======================================

Sphinx-Gallery enables you, when documenting your modules, to
reference to the examples that use a particular function. For example
if we are documenting the :data:`numpy.exp` function its possible to embed
a small gallery of examples that is specific to this function and
looks like this:

.. include:: gen_modules/backreferences/numpy.exp.examples
.. raw:: html

        <div style='clear:both'></div>



For such behavior to be available, you have to activate it in your
Sphinx-Gallery configuration ``conf.py`` file with:

.. code-block:: python

    sphinx_gallery_conf = {
        # directory where function granular galleries are stored
        'backreferences_dir'  : 'gen_modules/backreferences',

        # Modules for which function level galleries are created.  In
        # this case sphinx_gallery and numpy in a tuple of strings.
        'doc_module'          : ('sphinx_gallery', 'numpy')}

The path you specify in ``backreferences_dir``, here we choose
``gen_modules/backreferences`` will get populated with
ReStructuredText files, each of which contains a reduced version of the
gallery specific to every function used across all the examples
galleries and belonging to the modules listed in ``doc_module``. Keep
in mind that the path set in ``backreferences_dir`` is **relative** to the
``conf.py`` file.

Then within your sphinx documentation ``.rst`` files you write these
lines to include this reduced version of the Gallery, which has
examples in use of a specific function, in this case ``numpy.exp``::

    .. include:: gen_modules/backreferences/numpy.exp.examples
    .. raw:: html

        <div style='clear:both'></div>

The ``include`` directive takes a path **relative** to the ``rst``
file it is called from. In the case of this documentation file (which
is in the same directory as ``conf.py``) we directly use the path
declared in ``backreferences_dir`` followed by the function whose
examples we want to show and the file has the ``.examples`` extension.

Auto documenting your API with links to examples
------------------------------------------------

The previous feature can be automated for all your modules combining
it with the standard sphinx extensions `autodoc
<http://sphinx-doc.org/ext/autodoc.html>`_ and `autosummary
<http://sphinx-doc.org/ext/autosummary.html>`_. First enable them in your
``conf.py`` extensions list.

.. code-block:: python

    import sphinx_gallery
    extensions = [
        ...
        'sphinx.ext.autodoc',
        'sphinx.ext.autosummary',
        'sphinx_gallery.gen_gallery',
        ]

    # generate autosummary even if no references
    autosummary_generate = True

`autodoc <http://sphinx-doc.org/ext/autodoc.html>`_ and `autosummary
<http://sphinx-doc.org/ext/autosummary.html>`_ are very powerful
extensions please read about them. In this example we'll explain how
the :ref:`sphx_glr_api_reference` is automatically generated. The
documentation is done at the module level. We first start with the
``reference.rst`` file

.. literalinclude:: reference.rst
    :language: rst

The important directives are ``currentmodule`` where we specify which
module we are documenting, for our purpose is ``sphinx_gallery``. The
``autosummary`` directive is responsible for generating the ``rst``
files documenting each module.  ``autosummary`` takes the option
*toctree* which is where the ``rst`` files are saved and *template*
which is the file that describes how the module ``rst`` documentation
file is to be constructed, finally we write the modules we wish to
document, in this case all modules of Sphinx-Gallery.

The template file ``module.rst`` for the ``autosummary`` directive has
to be saved in the path ``_templates/module.rst``. We present our
configuration in the following block. The most relevant part is the
loop defined between lines **12-22** that parses all the functions of
the module. There we have included the snippet introduced in the
previous section. Keep in mind that the include directive is
**relative** to the file location, and module documentation files are
saved in the directory we specified in the *toctree* option of the
``autosummary`` directive used before in the ``reference.rst`` file.
The files we are including are from the ``backreferences_dir``
configuration option setup for Sphinx-Gallery.

.. literalinclude:: _templates/module.rst
    :language: rst
    :lines: 3-
    :emphasize-lines: 12-22
    :linenos:


Using a custom default thumbnail image
======================================

In case you want to use your own image for the thumbnail of examples that do
not generate any plot, you can specify it by editing your Sphinx ``conf.py``
file. You need to add to the configuration dictionary a key called
`default_thumb_file`. For example:

.. code-block:: python

    sphinx_gallery_conf = {
        'default_thumb_file'     : 'path/to/thumb/file.png'}}


Choosing the thumbnail image from multiple figures
==================================================

For examples that generate multiple figures, the default behavior will use
the first figure created in each as the thumbnail image displayed in the
gallery. To change the thumbnail image to a figure generated later in
an example script, add a comment to the example script to specify the
number of the figure you would like to use as the thumbnail. For example,
to use the 2nd figure created as the thumbnail:

.. code-block:: python

    # sphinx_gallery_thumbnail_number = 2

The default behavior is ``sphinx_gallery_thumbnail_number = 1``. See
:ref:`sphx_glr_auto_examples_plot_choose_thumbnail.py` for an example
of this functionality.

Build the Gallery without executing the examples
================================================

Sphinx-Gallery can parse all your examples and build the gallery
without executing any of the scripts. This is just for speed
visualization processes of the gallery and the size it takes your
website to display, or any use you can imagine for it. To achieve this you
need to pass the no plot option in the build process by modifying
your ``Makefile`` with::

    html-noplot:
        $(SPHINXBUILD) -D plot_gallery=0 -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
        @echo
        @echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

Remember that for ``Makefile`` white space is significant and the indentation are tabs
and not spaces.

Alternatively, you can add the ``plot_gallery`` option to the
``sphinx_gallery_conf`` dictionary inside your ``conf.py``
configuration file to have it as a default. The highest precedence is
always given to the `-D` flag of the ``sphinx-build`` command.


Dealing with failing Gallery example scripts
============================================

As your project evolves some of your example scripts might stop
executing properly. Sphinx-Gallery assist you in the discovery process
of those bugged examples. The default behavior is to replace the
thumbnail of those examples in the gallery with the broken
thumbnail. That allows you to find with a quick glance of the gallery
which examples failed. Broken examples remain accessible in the html
view of the gallery and the traceback message is written for the
failing code block. Refer to example
:ref:`sphx_glr_auto_examples_plot_raise.py` to view the default
behavior.

The build is also failed exiting with code 1 and giving you a summary
of the failed examples with their respective traceback. This way you
are aware of failing examples right after the build and can find them
easily.

There are some additional options at your hand to deal with broken examples.

Abort build on first fail
^^^^^^^^^^^^^^^^^^^^^^^^^

Sphinx-Gallery provides the early fail option. In
this mode the gallery build process breaks as soon as an exception
occurs in the execution of the examples scripts. To activate this
behavior you need to pass a flag at the build process. It can be done
by including in your ``Makefile``::

    html_abort_on_example_error:
	$(SPHINXBUILD) -D abort_on_example_error=1 -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

Remember that for ``Makefile`` white space is significant and the indentation are tabs
and not spaces.

Alternatively, you can add the ``abort_on_example_error`` option to
the ``sphinx_gallery_conf`` dictionary inside your ``conf.py``
configuration file to have it as a default. The highest precedence is
always given to the `-D` flag of the ``sphinx-build`` command.


Don't fail the build on exit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It might be the case that you want to keep the gallery even with
failed examples. Thus you can configure Sphinx-Gallery to allow
certain examples to fail and still exit with a 0 exit code. For this
you need to list all the examples you want to allow to fail during
build. Change your `conf.py` accordingly:


.. code-block:: python

    sphinx_gallery_conf = {
        ...
        'expected_failing_examples': ['../examples/plot_raise.py']
    }

Here you list the examples you allow to fail during the build process,
keep in mind to specify the full relative path from your `conf.py` to
the example script.


.. _regular expressions: https://docs.python.org/2/library/re.html
