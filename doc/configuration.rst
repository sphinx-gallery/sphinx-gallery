.. _configuration:

=============
Configuration
=============

Configuration and customization of sphinx-gallery is done primarily with a
dictionary specified in your ``conf.py`` file. A list of the possible
keys are listed :ref:`below <list_of_options>` and explained in
greater detail in subsequent sections.

.. _list_of_options:

List of config options
======================

Most sphinx-gallery configuration options are set in the Sphinx ``conf.py``
file:

- ``examples_dirs`` and ``gallery_dirs`` (:ref:`multiple_galleries_config`)
- ``filename_pattern`` and ``ignore_pattern`` (:ref:`build_pattern`)
- ``subsection_order`` (:ref:`sub_gallery_order`)
- ``within_subsection_order`` (:ref:`within_gallery_order`)
- ``reference_url`` (:ref:`link_to_documentation`)
- ``backreferences_dir`` and ``doc_module`` (:ref:`references_to_examples`)
- ``default_thumb_file`` (:ref:`custom_default_thumb`)
- ``thumbnail_size`` (:ref:`setting_thumbnail_size`)
- ``line_numbers`` (:ref:`adding_line_numbers`)
- ``download_all_examples`` (:ref:`disable_all_scripts_download`)
- ``plot_gallery`` (:ref:`without_execution`)
- ``image_scrapers`` (and the deprecated ``find_mayavi_figures``)
  (:ref:`image_scrapers`)
- ``reset_modules`` (:ref:`reset_modules`)
- ``abort_on_example_error`` (:ref:`abort_on_first`)
- ``expected_failing_examples`` (:ref:`dont_fail_exit`)
- ``min_reported_time`` (:ref:`min_reported_time`)
- ``show_memory`` (:ref:`show_memory`)
- ``binder`` (:ref:`binder_links`)
- ``first_notebook_cell`` (:ref:`first_notebook_cell`)
- ``junit`` (:ref:`junit_xml`)

Some options can also be set or overridden on a file-by-file basis:

- ``# sphinx_gallery_line_numbers`` (:ref:`adding_line_numbers`)
- ``# sphinx_gallery_thumbnail_number`` (:ref:`choosing_thumbnail`)

Some options can be set during the build execution step, e.g. using a Makefile:

- ``make html-noplot`` (:ref:`without_execution`)
- ``make html_abort_on_example_error`` (:ref:`abort_on_first`)

And some things can be tweaked directly in CSS:

- ``.sphx-glr-thumbcontainer`` (:ref:`setting_thumbnail_size`)


.. _multiple_galleries_config:

Manage multiple galleries
=========================

Sphinx-Gallery only supports up to sub-folder level in its gallery directories.
This might be a limitation for you. Or you might want to have separate
galleries for different purposes, an examples gallery and a tutorials gallery.
For this you use in your Sphinx ``conf.py`` file a list of directories in
the sphinx configuration dictionary::

    sphinx_gallery_conf = {
        ...
        'examples_dirs': ['../examples', '../tutorials'],
        'gallery_dirs': ['auto_examples', 'tutorials'],
    }

Keep in mind that both lists have to be of the same length.

.. note:: If your examples take a long time to run, consider looking at the
          :ref:`execution times <sphx_glr_auto_examples_sg_execution_times>`
          file that is generated for each gallery dir.

.. _build_pattern:

Parsing and executing examples via matching patterns
====================================================

By default, Sphinx-Gallery will **parse and add** all files with a ``.py``
extension to the gallery, but only **execute** files beginning with ``plot_``.
These behaviors are controlled by the ``ignore_pattern`` and ``filename_pattern``
entries, which have the default values::

    sphinx_gallery_conf = {
        ...
        'filename_pattern': '/plot_',
        'ignore_pattern': r'__init__\.py',
    }

To omit some files from the gallery entirely (i.e., not execute, parse, or
add them), you can change the ``ignore_pattern`` option.
To choose which of the parsed and added Python scripts are actualy
executed, you can modify ``filename_pattern``. For example::

    sphinx_gallery_conf = {
        ...
        'filename_pattern': '/plot_compute_',
    }

will build all examples starting with ``plot_compute_``. The key
``filename_pattern`` (and ``ignore_pattern``) accepts `regular expressions`_
which will be matched with the full path of the example. This is the reason
the leading ``'/'`` is required. Users are advised to use ``re.escape(os.sep)``
instead of ``'/'`` if they want to be agnostic to the operating system.

The ``filename_pattern`` option is also useful if you want to build only a
subset of the examples. For example, you may
want to build only one example so that you can link it in the documentation. In that case,
you would do::

    sphinx_gallery_conf = {
        ...
        'filename_pattern': r'plot_awesome_example\.py',
    }

Here, one should escape the dot ``r'\.'`` as otherwise python `regular expressions`_ matches any character. Nevertheless, as
one is targeting a specific file, it would match the dot in the filename even without this escape character.

Similarly, to build only examples in a specific directory, you can do::

    sphinx_gallery_conf = {
        ...
        'filename_pattern': '/directory/plot_',
    }

Alternatively, you can skip executing some examples. For example, to skip building examples
starting with ``plot_long_examples_``, you would do::

    sphinx_gallery_conf = {
        ...
        'filename_pattern': '/plot_(?!long_examples)',
    }

As the patterns are parsed as `regular expressions`_, users are advised to consult the
`regular expressions`_ module for more details.

.. note::
    Remember that Sphinx allows overriding ``conf.py`` values from the command
    line, so you can for example build a single example directly via something like:

    .. code-block:: console

        $ sphinx-build -D sphinx_gallery_conf.filename_pattern=plot_specific_example\.py ...

.. _sub_gallery_order:

Sorting gallery subsections
===========================

Gallery subsections are sorted by default alphabetically by their folder
name, and as such you can always organize them by changing your folder
names. An alternative option is to use a sortkey to organize those
subsections. We provide an explicit order sortkey where you have to define
the order of all subfolders in your galleries::

    from sphinx_gallery.sorting import ExplicitOrder
    sphinx_gallery_conf = {
        ...
        'examples_dirs': ['../examples','../tutorials'],
        'subsection_order': ExplicitOrder(['../examples/sin_func',
                                           '../examples/no_output',
                                           '../tutorials/seaborn']),
    }

Here we build 2 main galleries `examples` and `tutorials`, each of them
with subsections. To specify their order explicitly in the gallery we
import :class:`sphinx_gallery.sorting.ExplicitOrder` and initialize it with
the list of all subfolders with their paths relative to `conf.py` in the
order you prefer them to appear. Keep in mind that we use a single sort key
for all the galleries that are built, thus we include the prefix of each
gallery in the corresponding subsection folders. One does not define a
sortkey per gallery. You can use Linux paths, and if your documentation is
built in a Windows system, paths will be transformed to work accordingly,
the converse does not hold.

If you so desire you can implement your own sorting key. It will be
provided the relative paths to `conf.py` of each sub gallery folder.


.. _within_gallery_order:

Sorting gallery examples
========================

Within a given gallery (sub)section, the example files are ordered by
using the standard :func:`sorted` function with the ``key`` argument by default
set to
:class:`NumberOfCodeLinesSortKey(src_dir) <sphinx_gallery.sorting.NumberOfCodeLinesSortKey>`,
which sorts the files based on the number of code lines::

    from sphinx_gallery.sorting import NumberOfCodeLinesSortKey
    sphinx_gallery_conf = {
        ...
        'within_subsection_order': NumberOfCodeLinesSortKey,
    }

In addition, multiple convenience classes are provided for use with
``within_subsection_order``:

- :class:`sphinx_gallery.sorting.NumberOfCodeLinesSortKey` (default) to sort by
  the number of code lines.
- :class:`sphinx_gallery.sorting.FileSizeSortKey` to sort by file size.
- :class:`sphinx_gallery.sorting.FileNameSortKey` to sort by file name.
- :class:`sphinx_gallery.sorting.ExampleTitleSortKey` to sort by example title.


.. _link_to_documentation:

Add intersphinx links to your examples
======================================

Sphinx-Gallery enables you to add hyperlinks in your example scripts so that
you can link the used functions to their matching online documentation. As such
code snippets within the gallery appear like this

.. raw:: html

    <div class="highlight-python"><div class="highlight"><pre>
    <span class="n">y</span> <span class="o">=</span> <a href="https://docs.scipy.org/doc/numpy/reference/generated/numpy.sin.html#numpy.sin"><span class="n">np</span><span class="o">.</span><span class="n">sin</span></a><span class="p">(</span><span class="n">x</span><span class="p">)</span>
    </pre></div>
    </div>

Have a look at this in full action
in our example :ref:`sphx_glr_auto_examples_plot_gallery_version.py`.

To make this work in your documentation you need to include to the configuration
dictionary within your Sphinx ``conf.py`` file::

    sphinx_gallery_conf = {
        ...
        'reference_url': {
             # The module you locally document uses None
            'sphinx_gallery': None,
        }
    }

To link to external modules, if you use the Sphinx extension
:mod:`sphinx.ext.intersphinx`, no additional changes are necessary,
as the ``intersphinx`` inventory will automatically be used.
If you do not use ``intersphinx``, then you should add entries that
point to the directory containing ``searchindex.js``, such as
``'matplotlib': 'https://matplotlib.org'``.

.. _references_to_examples:

Add mini-galleries for API documentation
========================================

When documenting a given function/class, Sphinx-Gallery enables you to link to
any examples that either:

1. Use the function/instantiate the class in the code.
2. Refer to that function/class using sphinx markup ``:func:``/``:class:``
   in a documentation block.

The former is useful for auto-documenting functions that are used and classes
that are explicitly instantiated. The latter is useful for classes that are
typically implicitly returned rather than explicitly instantiated (e.g.,
:class:`matplotlib.axes.Axes` which is most often instantiated only indirectly
within function calls).

For example, we can embed a small gallery of all examples that use or
refer to :obj:`numpy.exp`, which looks like this:

.. include:: gen_modules/backreferences/numpy.exp.examples
.. raw:: html

        <div style='clear:both'></div>

For such behavior to be available, you have to activate it in
your Sphinx-Gallery configuration ``conf.py`` file with::

    sphinx_gallery_conf = {
        ...
        # directory where function granular galleries are stored
        'backreferences_dir'  : 'gen_modules/backreferences',

        # Modules for which function level galleries are created.  In
        # this case sphinx_gallery and numpy in a tuple of strings.
        'doc_module'          : ('sphinx_gallery', 'numpy')}

The path you specify in ``backreferences_dir`` (here we choose
``gen_modules/backreferences``) will be populated with
ReStructuredText files. Each will contain a reduced version of the
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

Auto-documenting your API with links to examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The previous feature can be automated for all your modules combining
it with the standard sphinx extensions `autodoc
<http://sphinx-doc.org/ext/autodoc.html>`_ and `autosummary
<http://sphinx-doc.org/ext/autosummary.html>`_. First enable them in your
``conf.py`` extensions list::

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
extensions, please read about them. In this example we'll explain how
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
    :emphasize-lines: 12-22, 32-42
    :linenos:


.. _custom_default_thumb:

Using a custom default thumbnail
================================

In case you want to use your own image for the thumbnail of examples that do
not generate any plot, you can specify it by editing your Sphinx ``conf.py``
file. You need to add to the configuration dictionary a key called
`default_thumb_file`. For example::

    sphinx_gallery_conf = {
        ...
        'default_thumb_file': 'path/to/thumb/file.png',
    }


.. _adding_line_numbers:

Adding line numbers to examples
===============================

Line numbers can be displayed in listings by adding the global ``line_numbers``
setting::

    sphinx_gallery_conf = {
        ...
        'line_numbers': True,
    }

or by adding a comment to the example script, which overrides any global
setting::

    # sphinx_gallery_line_numbers = True

Note that for Sphinx < 1.3, the line numbers will not be consistent with the
original file.


.. _first_notebook_cell:

Add your own first notebook cell
================================

Sphinx-Gallery adds an extra cell to the beginning of every generated notebook.
This is often for adding code that is required to run properly in the notebook,
but not in a ``.py`` file. By default, this text is

.. code-block:: ipython

   %matplotlib inline

You can choose whatever text you like by modifying the ``first_notebook_cell``
configuration parameter. For example, the gallery of this documentation
displays a comment along-side each the code shown above.

.. code-block:: ipython

  # This cell is added by sphinx-gallery
  # It can be customized to whatever you like
  %matplotlib inline

Which is achieved by the following configuration::

  'first_notebook_cell': ("# This cell is added by sphinx-gallery\n"
                          "# It can be customized to whatever you like\n"
                          "%matplotlib inline")

If the value of ``first_notebook_cell`` is set to ``None``, then no extra first
cell will be added to the notebook.


.. _junit_xml:

Using JUnit XML files
=====================

Sphinx-Gallery can create a JUnit XML file of your example run times,
successes, and failures. To create a file named e.g. ``junit-result.xml``
in the ``/build`` output directory, set the configuration key (path is relative
to the HTML output directory)::

     sphinx_gallery_conf = {
         ...
         'junit': '../test-results/sphinx-gallery/junit.xml',
     }

By default, JUnit XML file generation is disabled (by setting ``'junit': ''``).
JUnit XML files are useful for example on CircleCI builds, where you can add
a line like this to get a summary of your example run times in the CircleCI GUI
(which will parse the file path
``doc/_build/test-results/sphinx-gallery/junit.xml`` and infer the tests
came from ``sphinx-gallery`` based on the nested subdirectory name):

.. code-block:: yaml

    - store_test_results:
        path: doc/_build/test-results
    - store_artifacts:
        path: doc/_build/test-results

For more information on CircleCI integration, peruse the related
`CircleCI doc <https://circleci.com/docs/2.0/collect-test-data/#metadata-collection-in-custom-test-steps>`__
and `blog post <https://circleci.com/blog/how-to-output-junit-tests-through-circleci-2-0-for-expanded-insights/>`__.

.. _disable_all_scripts_download:

Disabling download button of all scripts
========================================

By default Sphinx-Gallery collects all python scripts and all Jupyter
notebooks from each gallery into zip files which are made available for
download at the bottom of each gallery. To disable this behavior add to the
configuration dictionary in your ``conf.py`` file::

    sphinx_gallery_conf = {
        ...
        'download_all_examples': False,
    }


.. _choosing_thumbnail:

Choosing the thumbnail image
============================

For examples that generate multiple figures, the default behavior will use
the first figure created in each as the thumbnail image displayed in the
gallery. To change the thumbnail image to a figure generated later in
an example script, add a comment to the example script to specify the
number of the figure you would like to use as the thumbnail. For example,
to use the 2nd figure created as the thumbnail::

    # sphinx_gallery_thumbnail_number = 2

The default behavior is ``sphinx_gallery_thumbnail_number = 1``. See
:ref:`sphx_glr_auto_examples_plot_choose_thumbnail.py` for an example
of this functionality.

.. _binder_links:

Generate Binder links for gallery notebooks (experimental)
==========================================================

Sphinx-Gallery automatically generates Jupyter notebooks for any
examples built with the gallery. `Binder <https://mybinder.org>`_ makes it
possible to create interactive GitHub repositories that connect to cloud resources.

If you host your documentation on a GitHub repository, it is possible to
auto-generate a Binder link for each notebook. Clicking this link will
take users to a live version of the Jupyter notebook where they may
run the code interactively. For more information see the `Binder documentation
<https://docs.mybinder.org>`__.

.. warning::

   Binder is still beta technology, so there may be instability in the
   experience of users who click Binder links.

In order to enable Binder links with Sphinx-Gallery, you must specify
a few pieces of information in ``conf.py``. These are given as a nested
dictionary following the pattern below::

    sphinx_gallery_conf = {
      ...
      'binder': {
         # Required keys
         'org': '<github_org>',
         'repo': '<github_repo>',
         'ref': '<ref-for-documentation>',  # Can be any branch, tag, or commit hash. Use a branch that hosts your docs.
         'binderhub_url': '<binder_url>',  # Any URL of a binderhub deployment. Must be full URL (e.g. https://mybinder.org).
         'dependencies': '<list_of_paths_to_dependency_files>',
         # Optional keys
         'filepath_prefix': '<prefix>' # A prefix to prepend to any filepaths in Binder links.
         'notebooks_dir': '<notebooks-directory-name>' # Jupyter notebooks for Binder will be copied to this directory (relative to built documentation root).
         'use_jupyter_lab': <bool> # Whether Binder links should start Jupyter Lab instead of the Jupyter Notebook interface.
         }
    }

If a Sphinx-Gallery configuration for Binder is discovered, the following extra things will happen:

1. The dependency files specified in ``dependencies`` will be copied to a ``binder/`` folder in your built documentation.
2. The built Jupyter Notebooks from the documentation will be copied to a folder called ``<notebooks_dir/>`` at the root of
   your built documentation (they will follow the same folder hierarchy within the notebooks directory folder.
2. The rST output of each Sphinx-Gallery example will now have a ``launch binder`` button in it.
4. That button will point to a binder link with the following structure::

       <binderhub_url>/v2/gh/<org>/<repo>/<ref>?filepath=<filepath_prefix>/<notebooks_dir>/path/to/notebook.ipynb

Below is a more complete explanation of each field.

org (type: string)
  The GitHub organization where your documentation is stored.
repo (type: string)
  The GitHub repository where your documentation is stored.
ref (type: string)
  A reference to the version of your repository where your documentation exists.
  For example, if your built documentation is stored on a ``gh-pages`` branch, then this field
  should be set to ``gh-pages``.
binderhub_url (type: string)
  The full URL to a BinderHub deployment where you want your examples to run. One
  public BinderHub deployment is at ``https://mybinder.org``, though if you (and your users) have access to
  another, this can be configured with this field.
dependencies (type: list)
  A list of paths (relative to ``conf.py``) to dependency files that Binder uses to infer the environment needed
  to run your examples. For example, a ``requirements.txt`` file. These will be copied into a folder
  called ``binder/`` in your built documentation folder. For a list of all the possible dependency files
  you can use, see `the Binder configuration documentation <https://mybinder.readthedocs.io/en/latest/config_files.html#config-files>`_.
filepath_prefix (type: string | None, default: ``None``)
  A prefix to append to the filepath in the Binder links. You should use this if you will store your built
  documentation in a sub-folder of a repository, instead of in the root.
notebooks_dir (type: string, default: ``notebooks``)
  The name of a folder where the built Jupyter notebooks will be copied. This ensures that all the notebooks are
  in one place (though they retain their folder hierarchy) in case you'd like users to browse multiple notebook examples in one session.
use_jupyter_lab (type: bool, default: ``False``)
  Whether the default interface activated by the Binder link will be for
  Jupyter Lab or the classic Jupyter Notebook interface.

Each generated Jupyter Notebook will be copied to the folder
specified in ``notebooks_dir``. This will be a subfolder of the sphinx output
directory and included with your site build.
Binder links will point to these notebooks.

See the Sphinx-Gallery `Sphinx configuration file <https://github.com/sphinx-gallery/sphinx-gallery/blob/master/doc/conf.py>`_
for an example that uses the `public Binder server <http://mybinder.org>`_.

.. _without_execution:

Building without executing examples
===================================

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
``sphinx_gallery_conf`` dictionary inside your ``conf.py`` to have it as
a default::

    sphinx_gallery_conf = {
        ...
        'plot_gallery': 'False',
    }

The highest precedence is always given to the `-D` flag of the
``sphinx-build`` command.


.. _image_scrapers:

Image scrapers
==============

Image scrapers are plugins that allow Sphinx-gallery to detect images produced
during execution of your examples, and then embed them into documentation.
Scrapers can be activated by appending scraper names to the ``image_scrapers``
field of your Sphinx-gallery configuration (see below). There are currently
two native image scrapers in Sphinx-gallery (Matplotlib and Mayavi).

By default, Sphinx-gallery will only detect new :mod:`matplotlib.pyplot`
figures. This behavior is equivalent to the default of::

    sphinx_gallery_conf = {
        ...
        'image_scrapers': ('matplotlib',),
    }

Built-in support is also provided for finding :mod:`Mayavi <mayavi.mlab>`
figures. Enable this feature with the following configuration::

   sphinx_gallery_conf = {
       ...
       'image_scrapers': ('matplotlib', 'mayavi'),
   }

.. note:: The parameter ``find_mayavi_figures`` which can also be used to
          extract Mayavi figures is **deprecated** in version 0.2+,
          and will be removed in a future release.

Custom scrapers
^^^^^^^^^^^^^^^

It is possible to write custom scrapers for images generated by packages
outside of those supported natively in Sphinx-gallery. This is accomplished
by writing your own Python function to define how to detect and retrieve
images produced by an arbitrary package. **For instructions on how to accomplish
this, see :ref:`custom_scrapers`**.

If you've developed a custom scraper for Sphinx-gallery that would be useful
to the broader community, we encourage you to contribute it to the list of
natively-supported scrapers located in
`the scrapers module <https://github.com/sphinx-gallery/sphinx-gallery/blob/master/sphinx_gallery/scrapers.py>`_.
We welcome PRs!

.. _reset_modules:

Resetting modules
=================

Often you wish to "reset" the behavior of your visualization packages in order
to ensure that any changes made to plotting behavior in one example do not
propagate to the other examples.

By default, at the end of executing each example file, Sphinx-gallery will
reset ``matplotlib`` (by using :func:`matplotlib.pyplot.rcdefaults`) and ``seaborn``
(by trying to unload the module from ``sys.modules``). This is equivalent to the
following configuration::

    sphinx_gallery_conf = {
        ...
        'reset_modules': ('matplotlib', 'seaborn'),
    }

Currently, Sphinx-gallery natively supports resetting ``matplotlib`` and
``seaborn``. However, you can also add your own custom function to
this tuple in order to define resetting behavior for other visualization libraries.

To do so, follow the instructions in :ref:`custom_reset`.


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
:ref:`sphx_glr_auto_examples_no_output_plot_raise.py` to view the default
behavior.

The build is also failed exiting with code 1 and giving you a summary
of the failed examples with their respective traceback. This way you
are aware of failing examples right after the build and can find them
easily.

There are some additional options at your hand to deal with broken examples.

.. _abort_on_first:

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
configuration file to have it as a default::

    sphinx_gallery_conf = {
        ...
        'abort_on_example_error': True,
    }


The highest precedence is always given to the `-D` flag of
the ``sphinx-build`` command.

.. _dont_fail_exit:

Don't fail the build on exit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It might be the case that you want to keep the gallery even with
failed examples. Thus you can configure Sphinx-Gallery to allow
certain examples to fail and still exit with a 0 exit code. For this
you need to list all the examples you want to allow to fail during
build. Change your `conf.py` accordingly::

    sphinx_gallery_conf = {
        ...
        'expected_failing_examples': ['../examples/plot_raise.py']
    }

Here you list the examples you allow to fail during the build process,
keep in mind to specify the full relative path from your `conf.py` to
the example script.


.. _setting_thumbnail_size:

Setting gallery thumbnail size
==============================

By default Sphinx-gallery will generate thumbnails at size ``(400, 280)``,
and add pillarboxes or letterboxes as necessary to scale the image while
maintaining the original aspect ratio. This size can be controlled with the
``thumbnail_size`` entry as, e.g.::

    sphinx_gallery_conf = {
        ...
        'thumbnail_size': (250, 250),
    }

The gallery uses various CSS classes to display these thumbnails, which
default to maximum 160x160px. To change this, e.g. to display the images
at 250x250px, you can modify the default CSS with something like the following
in your own site's CSS file:

.. code-block:: css

    .sphx-glr-thumbcontainer {
        min-height: 320px !important;
        margin: 20px !important;
    }
    .sphx-glr-thumbcontainer .figure {
        width: 250px !important;
    }
    .sphx-glr-thumbcontainer img {
        max-height: 250px !important;
        width: 250px !important;
    }
    .sphx-glr-thumbcontainer a.internal {
        padding: 270px 10px 0 !important;
    }


.. _min_reported_time:

Minimal reported time
=====================

By default, Sphinx-gallery logs and embeds in the html output the time it took
to run each script.  If the majority of your examples runs quickly, you may not
need this information.

The ``min_reported_time`` parameter can be set to a number of seconds.  The
duration of scripts that ran faster than that amount will not be logged nor
embedded in the html output.

.. _regular expressions: https://docs.python.org/2/library/re.html


.. _show_memory:

Showing memory consumption
==========================

Sphinx-Gallery can use ``memory_profiler``, if installed, to report the peak
memory during the run of an example. After installing ``memory_profiler``,
you can do::

    sphinx_gallery_conf = {
        ...
        'show_memory': True,
    }
