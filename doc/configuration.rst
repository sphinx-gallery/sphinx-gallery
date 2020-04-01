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
- ``backreferences_dir``, ``doc_module``, and ``inspect_global_variables`` (:ref:`references_to_examples`)
- ``default_thumb_file`` (:ref:`custom_default_thumb`)
- ``thumbnail_size`` (:ref:`setting_thumbnail_size`)
- ``line_numbers`` (:ref:`adding_line_numbers`)
- ``remove_config_comments`` (:ref:`removing_config_comments`)
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
- ``first_notebook_cell`` and ``last_notebook_cell`` (:ref:`own_notebook_cell`)
- ``junit`` (:ref:`junit_xml`)
- ``log_level`` (:ref:`log_level`)
- ``capture_repr`` and ``ignore_repr_types`` (:ref:`capture_repr`)

Some options can also be set or overridden on a file-by-file basis:

- ``# sphinx_gallery_line_numbers`` (:ref:`adding_line_numbers`)
- ``# sphinx_gallery_thumbnail_number`` (:ref:`choosing_thumbnail`)
- ``# sphinx_gallery_thumbnail_path`` (:ref:`providing_thumbnail`)

See also :ref:`removing_config_comments` to hide these comments from the
rendered examples.

Some options can be set during the build execution step, e.g. using a Makefile:

- ``make html-noplot`` (:ref:`without_execution`)
- ``make html_abort_on_example_error`` (:ref:`abort_on_first`)

And some things can be tweaked directly in CSS:

- ``.sphx-glr-thumbcontainer`` (:ref:`setting_thumbnail_size`)

You can also use the package ``warnings`` in the ``conf.py`` file to prevent
warnings from being captured and included in your built documentation. For
example, to remove the specific Matplotlib agg warning, you can add::

    import warnings

    warnings.filterwarnings("ignore", category=UserWarning,
                            message='Matplotlib is currently using agg, which is a'
                                    ' non-GUI backend, so cannot show the figure.')

to your ``conf.py`` file.

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
          file that is generated for each gallery dir (as long as any examples
          were actually executed in that directory during the build).

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

.. note::
    Sphinx-gallery only re-runs examples that have changed (according to their
    md5 hash). You can delete the associated MD5 files (e.g.,
    ``./auto_examples/plot_awesome_example.py.md5``) to force a rebuild if
    you have not changed the example itself between subsequent ``sphinx``
    calls.

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

.. warning:: If you create your own class for ``'subsection_order'``, ensure
             that the ``__str__`` of your class is stable across runs.
             Sphinx determines if the build environment has changed
             (and thus if *all* documents should be rewritten)
             by examining the config values using
             ``md5(str(obj).encode()).hexdigest()`` in
             ``sphinx/builders/html.py``. Default class instances
             in Python have their memory address in their ``__repr__`` which
             will in general change for each build. For ``ExplicitOrder``
             for example, this is fixed via::

                 def __repr__(self):
                     return '<%s: %s>' % (self.__class__.__name__, self.ordered_list)

             Thus the files are only all rebuilt if the specified ordered list
             is changed.

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
in our example :ref:`sphx_glr_auto_examples_plot_0_sin.py`.

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

        <div class="sphx-glr-clear"></div>

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
galleries and belonging to the modules listed in ``doc_module``.
``backreferences_dir` should be a string or ``pathlib.Path`` object that is
**relative** to the ``conf.py`` file, or ``None``. It is ``None`` by default.

Then within your sphinx documentation ``.rst`` files you write these
lines to include this reduced version of the Gallery, which has
examples in use of a specific function, in this case ``numpy.exp``::

    .. include:: gen_modules/backreferences/numpy.exp.examples
    .. raw:: html

        <div class="sphx-glr-clear"></div>

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

Toggling global variable inspection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, Sphinx-gallery will inspect global variables (and code objects)
at the end of each code block to try to find classes of variables and
method calls. It also tries to find methods called on classes.
For example, this code::

    lst = [1, 2]
    fig, ax = plt.subplots()
    ax.plot(lst)

should end up with the following links (assuming intersphinx is set up
properly):

- :class:`lst <python:list>`
- :func:`plt.subplots <matplotlib.pyplot.subplots>`
- :class:`fig  <matplotlib.figure.Figure>`
- :class:`ax <matplotlib.axes.Axes>`
- :meth:`ax.plot <matplotlib.axes.Axes.plot>`

However, this feature might not work properly in all instances.
Moreover, if variable names get reused in the same script to refer to
different classes, it will break.

To disable this global variable introspection, you can use the configuration
key::

    sphinx_gallery_conf = {
        ...
        'inspect_global_variables'  : False,
    }

Stylizing code links using CSS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each link in the code blocks will be decorated with two or three CSS classes.

1. ``sphx-glr-backref-module-*``
        CSS class named after the module where the object is documented.
        ``*`` represents the module, e.g.,
        ``sphx-glr-backref-module-matplotlib-figure``.
2. ``sphx-glr-backref-type-*``
        CSS class named after the type of the object, where ``*`` represents
        the object type. This is a sanitized intersphinx type, e.g., a
        ``py:class`` will have the CSS class ``sphx-glr-backref-type-py-class``.
3. ``sphx-glr-backref-instance``
        The third 'optional' class that is added only if the object is an
        instance of a class (rather than, e.g., a class itself, method, or
        function). By default, Sphinx-Gallery adds the following CSS in
        ``gallery.css``:

        .. code-block:: css

            a.sphx-glr-backref-instance {
                text-decoration: none;
            }

        This is done to reduce the visual impact of instance linking
        in example code. This means that for the following code::

            x = Figure()

        ``x``, an instance of a class, will have the
        ``sphx-glr-backref-instance`` CSS class, and will not be decorated.
        ``Figure`` however, is a class, so will not have the
        ``sphx-glr-backref-instance`` CSS class, and will thus be decorated the
        standard way for links in the given parent styles.

These three CSS classes are meant to give fine-grained control over how
different links are decorated. For example, using CSS selectors you could
choose to avoid highlighting any ``sphx-glr-backref-*`` links except for ones
that you whitelist (e.g., those from your own module). For example, the
following css prevents any module except for matplotlib from being decorated:

.. code-block:: css

    a[class^="sphx-glr-backref-module-"] {
        text-decoration: none;
    }
    a[class^="sphx-glr-backref-module-matplotlib"] {
        text-decoration: underline;
    }

There are likely elements other than ``text-decoration`` that might be worth
setting, as well.

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

.. _removing_config_comments:

Removing config comments
========================

Some configurations can be done on a file-by-file basis by adding a special
comment with the pattern :samp:`# sphinx_gallery_{config} = {value}` to the
example source files. By default, the source files are parsed as is and thus
the comment will appear in the example.

To remove the comment from the rendered example set the option::

    sphinx_gallery_conf = {
        ...
        'remove_config_comments': True,
    }

.. _own_notebook_cell:

Add your own first and last notebook cell
=========================================

Sphinx-Gallery allows you to add your own first and/or last cell to *every*
generated notebook. Adding a first cell can be useful for including code that
is required to run properly in the notebook, but not in a ``.py`` file. By
default, the following first cell is added to each notebook::

.. code-block:: ipython

   %matplotlib inline

Adding a last cell can be useful for performing a desired action such as
reporting on the user's evironment. By default no last cell is added.

You can choose whatever text you like by modifying the ``first_notebook_cell``
and ``last_notebook_cell`` configuration parameters. For example, the gallery
of this documentation adds the following first cell::

.. code-block:: ipython

  # This cell is added by sphinx-gallery
  # It can be customized to whatever you like
  %matplotlib inline

Which is achieved by the following configuration::

    sphinx_gallery_conf = {
        ...
        'first_notebook_cell': ("# This cell is added by sphinx-gallery\n"
                                "# It can be customized to whatever you like\n"
                                "%matplotlib inline")
    }

A last cell may be added similarly by setting the ``last_notebook_cell``
parameter::

    sphinx_gallery_conf = {
        ...
        'first_notebook_cell': ("# This cell is added by sphinx-gallery\n"
                                "# It can be customized to whatever you like\n"
                                "%matplotlib inline"),
        'last_notebook_cell': "# This is the last cell",
    }

If the value of ``first_notebook_cell`` or ``last_notebook_cell`` is set to
``None``, then no extra first or last cell will be added to the notebook.


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


.. _log_level:

Setting log level
=================

Sphinx-Gallery logs output at several stages. Warnings can be generated for
code that requires case sensitivity (e.g., ``plt.subplot`` and ``plt.Subplot``)
when building docs on a filesystem that does not support case sensitive
naming (e.g., Windows). In this case, by default a ``logger.warning`` is
emitted, which will lead to a build failure when buidling with ``-W``.
The log level can be set with::

    sphinx_gallery_conf = {
        ...
        'log_level': {'backreference_missing': 'warning'},
    }

The only valid key currently is ``backreference_missing``.
The valid values are ``'debug'``, ``'info'``, ``'warning'``, and ``'error'``.


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
:ref:`sphx_glr_auto_examples_plot_4_choose_thumbnail.py` for an example
of this functionality.


.. _providing_thumbnail:

Providing a figure for the thumbnail image
==========================================

An arbitrary image can be provided to serve as a thumbnail image. To provide a
figure for the thumbnail image, add a comment to the example script to specify
the path to the figure you would like to use as the thumbnail. For example, the
following defines that the figure ``demo.png`` in the folder ``_static/``
should be used to create the thumbnail::

    # sphinx_gallery_thumbnail_path = ``_static/demo.png``

Note that ``sphinx_gallery_thumbnail_number`` overrules
``sphinx_gallery_thumbnail_path``. See
:ref:`sphx_glr_auto_examples_plot_4b_provide_thumbnail.py` for an example of
this functionality.


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
         'branch': '<github_branch>',  # Can be any branch, tag, or commit hash. Use a branch that hosts your docs.
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
3. The rST output of each Sphinx-Gallery example will now have a ``launch binder`` button in it.
4. That button will point to a binder link with the following structure

   .. code-block:: html

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

.. note::

   It is not currently possible to host notebooks generated by
   Sphinx-Gallery with readthedocs.org, as RTD does not provide you
   with a GitHub repository you could link Binder to. If you'd like to
   use readthedocs with Sphinx-Gallery and Binder links, you should
   independently build your documentation and host it on a GitHub branch
   as well as building it with readthedocs.

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
your ``Makefile`` with:

.. code-block:: Makefile

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
Scrapers can be activated by appending scraper names to the
``'image_scrapers'`` tuple in your Sphinx-gallery configuration. For example,
to scrape both matplotlib and Mayavi images you can do::

      sphinx_gallery_conf = {
          ...
          'image_scrapers': ('matplotlib', 'mayavi'),
      }

The default value is ``'image_scrapers': ('matplotlib',)`` which only scrapes
Matplotlib images. Note that this includes any images produced by pacakges that
are based on Matplotlib, for example Seaborn or Yellowbrick.

The following scrapers are supported:

- matplotlib
    Sphinx-gallery maintains a scraper for
    :mod:`matplotlib <matplotlib.pyplot>` figures via the string
    ``'matplotlib'``.
- Mayavi
    Sphinx-gallery maintains a scraper for
    :mod:`Mayavi <mayavi.mlab>` figures via the string
    ``'mayavi'``.
- PyVista
    `PyVista <https://github.com/pyvista/pyvista>`__ maintains a scraper
    (for PyVista >= 0.20.3) enabled by the string ``'pyvista'``.
- PyGMT
    See `their website <https://www.pygmt.org/dev/>`__ for more information on
    how to integrate with Sphinx-Gallery.

It is possible to write custom scrapers for images generated by packages
outside of those listed above. This is accomplished
by writing your own Python function to define how to detect and retrieve
images produced by an arbitrary package. For instructions, see
:ref:`custom_scraper`. If you come up with an implementation that would be
useful for general use (e.g., a custom scraper for a plotting library)
feel free to add it to the list above (see discussion
`here <https://github.com/sphinx-gallery/sphinx-gallery/issues/441#issuecomment-493782430>`__)!

.. _reset_modules:

Resetting modules
=================

Often you wish to "reset" the behavior of your visualization packages in order
to ensure that any changes made to plotting behavior in one example do not
propagate to the other examples.

By default, before each example file executes, Sphinx-gallery will
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
executing properly. Sphinx-gallery will assist you in the discovery process
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
by including in your ``Makefile``:

.. code-block:: Makefile

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

.. note:: If an example is expected to fail, sphinx-gallery will error if
          the example runs without error.


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


.. _capture_repr:

Controlling what output is captured
===================================

.. note::

    Configure ``capture_repr`` to be an empty tuple (i.e.,``capture_repr: ()``)
    to return to the output capturing behaviour prior to release v0.5.0.

The ``capture_repr`` configuration allows the user to control what output
is captured, while executing the example ``.py`` files, and subsequently
incorporated into the built documentation. Data directed to standard output
is always captured. The value of the last statement of *each* code block, *if*
it is an expression, can also be captured. This can be done by providing
the name of the 'representation' method to be captured in the ``capture_repr``
tuple, in order of preference. The representation methods currently supported
are:

* ``__repr__`` - returns the official string representation of an object. This
  is what is returned when your Python shell evaluates an expression.
* ``__str__`` - returns a string containing a nicely printable representation
  of an object. This is what is used when you ``print()`` an object or pass it
  to ``format()``.
* ``_repr_html_`` - returns a HTML version of the object. This method is only
  present in some objects, for example, pandas dataframes.

The default setting is::

    sphinx_gallery_conf = {
        ...
        'capture_repr': ('_repr_html_', '__repr__'),
    }

With the default setting Sphinx-Gallery would first attempt to capture the
``_repr_html_`` of the last statement of a code block, *if* it is an
expression. If this method does not exist for the expression, the second
'representation' method in the tuple, ``__repr__``, would be captured. If the
``__repr__`` also does not exist (unlikely for non-user defined objects),
nothing would be captured. Data directed to standard output is **always**
captured.

To capture only data directed to standard output, configure ``'capture_repr'``
to be an empty tuple: ``'capture_repr': ()``. This will imitate the behaviour
of Sphinx-Gallery prior to v0.5.0.

From another perspective, take for example the following code block::

    print('Hello world')
    a=2
    a   # this is an expression

``'Hello world'`` would be captured for every ``capture_repr`` setting as this
is directed to standard output. Further,

* if ``capture_repr`` is an empty tuple, nothing else would be
  captured.
* if ``capture_repr`` is ``('__repr__')``, ``2`` would also be captured.
* if ``capture_repr`` is ``('_repr_html_', '__repr__')`` (the default)
  Sphinx-Gallery would first attempt to capture ``_repr_html_``. Since this
  does not exist for ``a``, it will then attempt to capture ``__repr__``.
  The ``__repr__`` method does exist for ``a``, thus ``2`` would be also
  captured in this case.

**Matplotlib note**: if the ``'capture_repr'`` tuple includes ``'__repr__'``
and/or ``'__str__'``, code blocks which have a Matplotlib function call as the
last expression will generally produce a yellow output box in the built
documentation, as well as the figure. This is because matplotlib function calls
usually return something as well as creating/amending the plot in standard
output. For example, ``matplotlib.plot()`` returns a list of ``Line2D`` objects
representing the plotted data. This list has a ``__repr__`` and a ``__str__``
method which would thus be captured. You can prevent this by:

* assigning the (last) plotting function to a temporary variable. For example::

    import matplotlib.pyplot as plt

    _ = plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

* add ``plt.show()`` (which does not return anything) to the end of your
  code block. For example::

    import matplotlib.pyplot as plt

    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.show()

The unwanted string output will not occur if ``'capture_repr'`` is an empty
tuple or does not contain ``__repr__`` or ``__str__``.

.. _regular expressions: https://docs.python.org/2/library/re.html

Prevent capture of certain classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you wish to capture a representation of the last expression of each code
blocks **unless** the last expression is of a certain type, you can use
``'ignore_repr_types'``. ``'ignore_repr_types'`` is by default an empty raw
string (``r''``), meaning no types are ignored. To exclude specific type(s)
from being captured, ``'ignore_repr_types'`` can be set to a regular
expression matching the name(s) of the type(s) to be excluded.

For example, the configuration below would capture the ``__repr__`` of the
last expression of each code block unless the name of the ``type()`` of the last
expression includes the string 'matplotlib.text' *or* 'matplotlib.axes'.
This would prevent capturing of all subclasses of 'matplotlib.text', e.g.
expressions of type 'matplotlib.text.Annotation', 'matplotlib.text.OffsetFrom'
etc. Similarly subclasses of 'matplotlib.axes' (e.g. 'matplotlib.axes.Axes',
'matplotlib.axes.Axes.plot' etc.) will also not be captured.

.. code-block:: python

    sphinx_gallery_conf = {
        ...
        'capture_repr': ('__repr__'),
        'ignore_repr_types': r'matplotlib.text|matplotlib.axes',
    }
