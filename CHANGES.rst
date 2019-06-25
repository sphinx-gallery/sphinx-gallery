Change Log
==========

v0.4.0
------

Developer changes
'''''''''''''''''
- Added a private API contract for external scrapers to have string-based
  support, see:

    https://github.com/sphinx-gallery/sphinx-gallery/pull/494

- Standard error is now caught and displayed alongside standard output.
- Some sphinx markup is now removed from image thumbnail tooltips.

Incompatible changes
''''''''''''''''''''
- v0.4.0 will be the last release to support Python <= 3.4.
- Moving forward, we will support only the latest two stable Sphinx releases
  at the time of each sphinx-gallery release.

**Implemented enhancements:**

-  ENH: Remove some Sphinx markup from text `#511 <https://github.com/sphinx-gallery/sphinx-gallery/pull/511>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: Allow README.rst ext `#510 <https://github.com/sphinx-gallery/sphinx-gallery/pull/510>`__ (`larsoner <https://github.com/larsoner>`__)
-  binder requirements with Dockerfile? `#476 <https://github.com/sphinx-gallery/sphinx-gallery/issues/476>`__
-  ENH: Update docs `#509 <https://github.com/sphinx-gallery/sphinx-gallery/pull/509>`__ (`larsoner <https://github.com/larsoner>`__)
-  Add documentation note on RTD-Binder incompatibility `#505 <https://github.com/sphinx-gallery/sphinx-gallery/pull/505>`__ (`StanczakDominik <https://github.com/StanczakDominik>`__)
-  Add PlasmaPy to list of sphinx-gallery users `#504 <https://github.com/sphinx-gallery/sphinx-gallery/pull/504>`__ (`StanczakDominik <https://github.com/StanczakDominik>`__)
-  ENH: Expose example globals `#502 <https://github.com/sphinx-gallery/sphinx-gallery/pull/502>`__ (`larsoner <https://github.com/larsoner>`__)
-  DOC: Update docs `#501 <https://github.com/sphinx-gallery/sphinx-gallery/pull/501>`__ (`larsoner <https://github.com/larsoner>`__)
-  add link to view sourcecode in docs `#499 <https://github.com/sphinx-gallery/sphinx-gallery/pull/499>`__ (`sappelhoff <https://github.com/sappelhoff>`__)
-  MRG, ENH: Catch and write warnings `#495 <https://github.com/sphinx-gallery/sphinx-gallery/pull/495>`__ (`larsoner <https://github.com/larsoner>`__)
-  MRG, ENH: Add private API for external scrapers `#494 <https://github.com/sphinx-gallery/sphinx-gallery/pull/494>`__ (`larsoner <https://github.com/larsoner>`__)
-  Add list of external image scrapers `#492 <https://github.com/sphinx-gallery/sphinx-gallery/pull/492>`__ (`banesullivan <https://github.com/banesullivan>`__)
-  Add more examples of projects using sphinx-gallery `#489 <https://github.com/sphinx-gallery/sphinx-gallery/pull/489>`__ (`banesullivan <https://github.com/banesullivan>`__)
-  Add option to remove sphinx_gallery config comments `#487 <https://github.com/sphinx-gallery/sphinx-gallery/pull/487>`__ (`timhoffm <https://github.com/timhoffm>`__)
-  FIX: allow Dockerfile `#477 <https://github.com/sphinx-gallery/sphinx-gallery/pull/477>`__ (`jasmainak <https://github.com/jasmainak>`__)
-  MRG: Add SVG support `#471 <https://github.com/sphinx-gallery/sphinx-gallery/pull/471>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Simplify CircleCI build `#462 <https://github.com/sphinx-gallery/sphinx-gallery/pull/462>`__ (`larsoner <https://github.com/larsoner>`__)
-  Release v0.3.0 `#456 <https://github.com/sphinx-gallery/sphinx-gallery/pull/456>`__ (`choldgraf <https://github.com/choldgraf>`__)
-  adding contributing guide for releases `#455 <https://github.com/sphinx-gallery/sphinx-gallery/pull/455>`__ (`choldgraf <https://github.com/choldgraf>`__)

**Fixed bugs:**

-  fix wrong keyword in docs for “binder” `#500 <https://github.com/sphinx-gallery/sphinx-gallery/pull/500>`__ (`sappelhoff <https://github.com/sappelhoff>`__)
-  Fix ‘Out:’ label position in html output block `#484 <https://github.com/sphinx-gallery/sphinx-gallery/pull/484>`__ (`timhoffm <https://github.com/timhoffm>`__)
-  Mention pytest-coverage dependency `#482 <https://github.com/sphinx-gallery/sphinx-gallery/pull/482>`__ (`timhoffm <https://github.com/timhoffm>`__)
-  Fix ReST block after docstring `#480 <https://github.com/sphinx-gallery/sphinx-gallery/pull/480>`__ (`timhoffm <https://github.com/timhoffm>`__)
-  MAINT: Tolerate Windows mtime `#478 <https://github.com/sphinx-gallery/sphinx-gallery/pull/478>`__ (`larsoner <https://github.com/larsoner>`__)
-  FIX: Output from code execution is not stripped `#475 <https://github.com/sphinx-gallery/sphinx-gallery/pull/475>`__ (`padix-key <https://github.com/padix-key>`__)
-  FIX: Link `#470 <https://github.com/sphinx-gallery/sphinx-gallery/pull/470>`__ (`larsoner <https://github.com/larsoner>`__)
-  FIX: Minor fixes for memory profiling `#468 <https://github.com/sphinx-gallery/sphinx-gallery/pull/468>`__ (`larsoner <https://github.com/larsoner>`__)
-  Add output figure numbering breaking change in release notes. `#466 <https://github.com/sphinx-gallery/sphinx-gallery/pull/466>`__ (`lesteve <https://github.com/lesteve>`__)
-  Remove links to read the docs `#461 <https://github.com/sphinx-gallery/sphinx-gallery/pull/461>`__ (`GaelVaroquaux <https://github.com/GaelVaroquaux>`__)
-  [MRG+1] Add requirements.txt to manifest `#458 <https://github.com/sphinx-gallery/sphinx-gallery/pull/458>`__ (`ksunden <https://github.com/ksunden>`__)

**Closed issues:**

-  Allow .rst extension for README files `#508 <https://github.com/sphinx-gallery/sphinx-gallery/issues/508>`__
-  Generation of unchanged examples `#506 <https://github.com/sphinx-gallery/sphinx-gallery/issues/506>`__
-  Binder integration and Read the docs `#503 <https://github.com/sphinx-gallery/sphinx-gallery/issues/503>`__
-  Extending figure_rst to support html figures? `#498 <https://github.com/sphinx-gallery/sphinx-gallery/issues/498>`__
-  ENH: remove API crossrefs from hover text `#497 <https://github.com/sphinx-gallery/sphinx-gallery/issues/497>`__
-  BUG: warnings/stderr not captured `#491 <https://github.com/sphinx-gallery/sphinx-gallery/issues/491>`__
-  Should ``image\_scrapers`` be renamed (to ``output\_scrapers`` for example)? `#485 <https://github.com/sphinx-gallery/sphinx-gallery/issues/485>`__
-  Strip in-file sphinx_gallery directives from code `#481 <https://github.com/sphinx-gallery/sphinx-gallery/issues/481>`__
-  Generating gallery sometimes freezes `#479 <https://github.com/sphinx-gallery/sphinx-gallery/issues/479>`__
-  Adding a ReST block immediately after the module docstring breaks the generated .rst file `#473 <https://github.com/sphinx-gallery/sphinx-gallery/issues/473>`__
-  how to make custom image scraper `#469 <https://github.com/sphinx-gallery/sphinx-gallery/issues/469>`__
-  pythonhosted.org seems to be still up and running `#465 <https://github.com/sphinx-gallery/sphinx-gallery/issues/465>`__
-  Small regression in 0.3.1 with output figure numbering `#464 <https://github.com/sphinx-gallery/sphinx-gallery/issues/464>`__
-  Change output format of images `#463 <https://github.com/sphinx-gallery/sphinx-gallery/issues/463>`__
-  Version 0.3.0 release is broken on pypi `#459 <https://github.com/sphinx-gallery/sphinx-gallery/issues/459>`__
-  sphinx-gallery doesn’t play nice with sphinx’s ability to detect new files… `#449 <https://github.com/sphinx-gallery/sphinx-gallery/issues/449>`__
-  Remove the readthedocs version of sphinx gallery docs `#444 <https://github.com/sphinx-gallery/sphinx-gallery/issues/444>`__
-  Support for Plotly `#441 <https://github.com/sphinx-gallery/sphinx-gallery/issues/441>`__
-  Release v0.3.0 `#406 <https://github.com/sphinx-gallery/sphinx-gallery/issues/406>`__
-  Unnecessary regeneration of example pages `#395 <https://github.com/sphinx-gallery/sphinx-gallery/issues/395>`__
-  Unnecessary regeneration of API docs `#394 <https://github.com/sphinx-gallery/sphinx-gallery/issues/394>`__

v0.3.1
------

Bugfix release: add missing file that prevented "pip installing" the
package.

**Fixed bugs:**

- Version 0.3.0 release is broken on pypi
  `#459 <https://github.com/sphinx-gallery/sphinx-gallery/issues/459>`__

v0.3.0
------

Incompatible changes
''''''''''''''''''''

* the output figure numbering is always 1, 2, ..., ``number_of_figures``
  whereas in 0.2.0 it would follow the matplotlib figure numbers. If you
  include explicitly some figures generated by sphinx-gallery with the ``..
  figure`` directive in your ``.rst`` documentation you may need to adjust
  their paths if your example uses non-default matplotlib figure numbers (e.g.
  if you use ``plt.figure(0)``). See `#464
  <https://github.com/sphinx-gallery/sphinx-gallery/issues/464>` for more
  details.

Developer changes
'''''''''''''''''

* Dropped support for Sphinx <= 1.4.
* Refactor for independent rst file construction. Function
  ``sphinx_gallery.gen_rst.generate_file_rst`` does not anymore compose the
  rst file while it is executing each block of the source code. Currently
  executing the example script ``execute_script`` is an independent
  function and returns structured in a list the rst representation of the
  output of each source block. ``generate_file_rst`` calls for execution of
  the script when needed, then from the rst output it composes an rst
  document which includes the prose, code & output of the example which is
  the directly saved to file including the annotations of binder badges,
  download buttons and timing statistics.
* Binder link config changes. The configuration value for the BinderHub has
  been changed from ``url`` to ``binderhub_url`` in order to make it more
  explicit. The old configuration key (``url``) will be deprecated in
  version v0.4.0)
* Support for generating JUnit XML summary files via the ``'junit'``
  configuration value, which can be useful for building on CI services such as
  CircleCI. See the related `CircleCI doc <https://circleci.com/docs/2.0/collect-test-data/#metadata-collection-in-custom-test-steps>`__
  and `blog post <https://circleci.com/blog/how-to-output-junit-tests-through-circleci-2-0-for-expanded-insights/>`__.

**Fixed bugs:**

-  First gallery plot uses .matplotlibrc rather than the matplotlib
   defaults
   `#316 <https://github.com/sphinx-gallery/sphinx-gallery/issues/316>`__

**Closed issues:**

-  SG not respecting highlight_lang in conf.py
   `#452 <https://github.com/sphinx-gallery/sphinx-gallery/issues/452>`__
-  sphinx-gallery doesn’t play nice with sphinx’s ability to detect new
   files…
   `#449 <https://github.com/sphinx-gallery/sphinx-gallery/issues/449>`__
-  gallery generation broken on cpython master
   `#442 <https://github.com/sphinx-gallery/sphinx-gallery/issues/442>`__
-  Improve binder button instructions
   `#438 <https://github.com/sphinx-gallery/sphinx-gallery/issues/438>`__
-  Won’t display stdout
   `#435 <https://github.com/sphinx-gallery/sphinx-gallery/issues/435>`__
-  realtive paths in github.io
   `#434 <https://github.com/sphinx-gallery/sphinx-gallery/issues/434>`__
-  ‘make html’ does not attempt to run examples
   `#425 <https://github.com/sphinx-gallery/sphinx-gallery/issues/425>`__
-  Sprint tomorrow @ euroscipy?
   `#412 <https://github.com/sphinx-gallery/sphinx-gallery/issues/412>`__
-  Release v0.3.0
   `#409 <https://github.com/sphinx-gallery/sphinx-gallery/issues/409>`__
-  Supported Python and Sphinx versions
   `#404 <https://github.com/sphinx-gallery/sphinx-gallery/issues/404>`__
-  How to get the ``.css`` files to copy over on building the docs?
   `#399 <https://github.com/sphinx-gallery/sphinx-gallery/issues/399>`__
-  feature request: only rebuild individual examples
   `#397 <https://github.com/sphinx-gallery/sphinx-gallery/issues/397>`__
-  Unnecessary regeneration of example pages
   `#395 <https://github.com/sphinx-gallery/sphinx-gallery/issues/395>`__
-  Unnecessary regeneration of API docs
   `#394 <https://github.com/sphinx-gallery/sphinx-gallery/issues/394>`__
-  matplotlib inline vs notebook
   `#388 <https://github.com/sphinx-gallery/sphinx-gallery/issues/388>`__
-  Can this work for files other than .py ?
   `#378 <https://github.com/sphinx-gallery/sphinx-gallery/issues/378>`__
-  v0.1.14 release plan
   `#344 <https://github.com/sphinx-gallery/sphinx-gallery/issues/344>`__
-  SG misses classes that aren’t imported
   `#205 <https://github.com/sphinx-gallery/sphinx-gallery/issues/205>`__
-  Add a page showing the time taken by the examples
   `#203 <https://github.com/sphinx-gallery/sphinx-gallery/issues/203>`__
-  Lack of ``install\_requires``
   `#192 <https://github.com/sphinx-gallery/sphinx-gallery/issues/192>`__

**Merged pull requests:**

-  [MRG+1]: Output JUnit XML file
   `#454 <https://github.com/sphinx-gallery/sphinx-gallery/pull/454>`__
   (`larsoner <https://github.com/larsoner>`__)
-  MRG: Use highlight_language
   `#453 <https://github.com/sphinx-gallery/sphinx-gallery/pull/453>`__
   (`larsoner <https://github.com/larsoner>`__)
-  BUG: Fix execution time writing
   `#451 <https://github.com/sphinx-gallery/sphinx-gallery/pull/451>`__
   (`larsoner <https://github.com/larsoner>`__)
-  MRG: Adjust lineno for 3.8
   `#450 <https://github.com/sphinx-gallery/sphinx-gallery/pull/450>`__
   (`larsoner <https://github.com/larsoner>`__)
-  MRG: Only rebuild necessary parts
   `#448 <https://github.com/sphinx-gallery/sphinx-gallery/pull/448>`__
   (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Drop 3.4, add mayavi to one
   `#447 <https://github.com/sphinx-gallery/sphinx-gallery/pull/447>`__
   (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Modernize requirements
   `#445 <https://github.com/sphinx-gallery/sphinx-gallery/pull/445>`__
   (`larsoner <https://github.com/larsoner>`__)
-  Activating travis on pre-release of python
   `#443 <https://github.com/sphinx-gallery/sphinx-gallery/pull/443>`__
   (`NelleV <https://github.com/NelleV>`__)
-  [MRG] updating binder instructions
   `#439 <https://github.com/sphinx-gallery/sphinx-gallery/pull/439>`__
   (`choldgraf <https://github.com/choldgraf>`__)
-  FIX: Fix for latest sphinx-dev
   `#437 <https://github.com/sphinx-gallery/sphinx-gallery/pull/437>`__
   (`larsoner <https://github.com/larsoner>`__)
-  adding notes for filename
   `#436 <https://github.com/sphinx-gallery/sphinx-gallery/pull/436>`__
   (`choldgraf <https://github.com/choldgraf>`__)
-  FIX: correct sorting docstring for the FileNameSortKey class
   `#433 <https://github.com/sphinx-gallery/sphinx-gallery/pull/433>`__
   (`mrakitin <https://github.com/mrakitin>`__)
-  MRG: Fix for latest pytest
   `#432 <https://github.com/sphinx-gallery/sphinx-gallery/pull/432>`__
   (`larsoner <https://github.com/larsoner>`__)
-  FIX: Bump version
   `#431 <https://github.com/sphinx-gallery/sphinx-gallery/pull/431>`__
   (`larsoner <https://github.com/larsoner>`__)
-  MRG: Fix for newer sphinx
   `#430 <https://github.com/sphinx-gallery/sphinx-gallery/pull/430>`__
   (`larsoner <https://github.com/larsoner>`__)
-  DOC: Missing perenthisis in PNGScraper
   `#428 <https://github.com/sphinx-gallery/sphinx-gallery/pull/428>`__
   (`ksunden <https://github.com/ksunden>`__)
-  Fix #425
   `#426 <https://github.com/sphinx-gallery/sphinx-gallery/pull/426>`__
   (`Titan-C <https://github.com/Titan-C>`__)
-  Scraper documentation and an image file path scraper
   `#417 <https://github.com/sphinx-gallery/sphinx-gallery/pull/417>`__
   (`choldgraf <https://github.com/choldgraf>`__)
-  MRG: Remove outdated cron job
   `#416 <https://github.com/sphinx-gallery/sphinx-gallery/pull/416>`__
   (`larsoner <https://github.com/larsoner>`__)
-  ENH: Profile memory
   `#415 <https://github.com/sphinx-gallery/sphinx-gallery/pull/415>`__
   (`larsoner <https://github.com/larsoner>`__)
-  fix typo
   `#414 <https://github.com/sphinx-gallery/sphinx-gallery/pull/414>`__
   (`zasdfgbnm <https://github.com/zasdfgbnm>`__)
-  FIX: Travis
   `#410 <https://github.com/sphinx-gallery/sphinx-gallery/pull/410>`__
   (`larsoner <https://github.com/larsoner>`__)
-  documentation index page and getting_started updates
   `#403 <https://github.com/sphinx-gallery/sphinx-gallery/pull/403>`__
   (`choldgraf <https://github.com/choldgraf>`__)
-  adding ability to customize first cell of notebooks
   `#401 <https://github.com/sphinx-gallery/sphinx-gallery/pull/401>`__
   (`choldgraf <https://github.com/choldgraf>`__)
-  spelling fix
   `#398 <https://github.com/sphinx-gallery/sphinx-gallery/pull/398>`__
   (`amueller <https://github.com/amueller>`__)
-  [MRG] Fix Circle v2
   `#393 <https://github.com/sphinx-gallery/sphinx-gallery/pull/393>`__
   (`lesteve <https://github.com/lesteve>`__)
-  MRG: Move to CircleCI V2
   `#392 <https://github.com/sphinx-gallery/sphinx-gallery/pull/392>`__
   (`larsoner <https://github.com/larsoner>`__)
-  MRG: Fix for 1.8.0 dev
   `#391 <https://github.com/sphinx-gallery/sphinx-gallery/pull/391>`__
   (`larsoner <https://github.com/larsoner>`__)
-  Drop “Total running time” when generating the documentation
   `#390 <https://github.com/sphinx-gallery/sphinx-gallery/pull/390>`__
   (`lamby <https://github.com/lamby>`__)
-  Add dedicated class for timing related block
   `#359 <https://github.com/sphinx-gallery/sphinx-gallery/pull/359>`__
   (`ThomasG77 <https://github.com/ThomasG77>`__)
-  MRG: Add timing information
   `#348 <https://github.com/sphinx-gallery/sphinx-gallery/pull/348>`__
   (`larsoner <https://github.com/larsoner>`__)
-  MRG: Add refs from docstring to backrefs
   `#347 <https://github.com/sphinx-gallery/sphinx-gallery/pull/347>`__
   (`larsoner <https://github.com/larsoner>`__)
-  API: Refactor image scraping
   `#313 <https://github.com/sphinx-gallery/sphinx-gallery/pull/313>`__
   (`larsoner <https://github.com/larsoner>`__)
-  [MRG] FIX import local modules in examples
   `#305 <https://github.com/sphinx-gallery/sphinx-gallery/pull/305>`__
   (`NelleV <https://github.com/NelleV>`__)
-  [MRG] Separate rst notebook generation from execution of the script
   `#239 <https://github.com/sphinx-gallery/sphinx-gallery/pull/239>`__
   (`Titan-C <https://github.com/Titan-C>`__)

v0.2.0
------

New features
''''''''''''

* Added experimental support to auto-generate Binder links for examples via
  ``binder`` config. Note that this API may change in the future. `#244
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/244>`_ and `#371
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/371>`_.
* Added ``ignore_pattern`` configurable to allow not adding some python files
  into the gallery. See `#346
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/346>`_ for more
  details.
* Support for custom default thumbnails in 'RGBA' space `#375 <https://github.com/sphinx-gallery/sphinx-gallery/pull/375>`_
* Allow title only -\> use title as first paragraph `#345 <https://github.com/sphinx-gallery/sphinx-gallery/pull/345>`_

Bug Fixes
'''''''''

* Fix name string_replace trips on projects with ".py" in path. See `#322
  <https://github.com/sphinx-gallery/sphinx-gallery/issues/322>`_ and `#331
  <https://github.com/sphinx-gallery/sphinx-gallery/issues/331>`_ for more details.
* Fix __future__ imports across cells. See `#308
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/308>`_ for more details.
* Fix encoding related issues when locale is not UTF-8. See `#311
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/311>`_ for more
  details.
* In verbose mode, example output is printed to the console during execution of
  the example, rather than only at the end. See `#301
  <https://github.com/sphinx-gallery/sphinx-gallery/issues/301>`_ for a use
  case where it matters.
* Fix SphinxDocLinkResolver error with sphinx 1.7. See `#352
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/352>`_ for more
  details.
* Fix unexpected interaction between ``file_pattern`` and
  ``expected_failing_examples``. See `#379
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/379>`_ and `#335
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/335>`_
* FIX: Use unstyled pygments for output `#384 <https://github.com/sphinx-gallery/sphinx-gallery/pull/384>`_
* Fix: Gallery name for paths ending with '/' `#372 <https://github.com/sphinx-gallery/sphinx-gallery/pull/372>`_
* Fix title detection logic. `#356 <https://github.com/sphinx-gallery/sphinx-gallery/pull/356>`_
* FIX: Use ``docutils_namespace`` to avoid warning in sphinx 1.8dev `#387 <https://github.com/sphinx-gallery/sphinx-gallery/pull/387>`_

Incompatible Changes
''''''''''''''''''''

* Removed optipng feature that was triggered when the ``SKLEARN_DOC_OPTIPNG``
  variable was set. See `#349
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/349>`_ for more
  details.
* ``Backreferences_dir`` is now mandatory `#307 <https://github.com/sphinx-gallery/sphinx-gallery/pull/307>`_

Developer changes
'''''''''''''''''

* Dropped support for Sphinx <= 1.4.
* Add SphinxAppWrapper class in ``test_gen_gallery.py`` `#386 <https://github.com/sphinx-gallery/sphinx-gallery/pull/386>`_
* Notes on how to do a release `#360 <https://github.com/sphinx-gallery/sphinx-gallery/pull/360>`_
* Add codecov support `#328 <https://github.com/sphinx-gallery/sphinx-gallery/pull/328>`_

v0.1.13
-------

New features
''''''''''''

* Added ``min_reported_time`` configurable.  For examples that run faster than
  that threshold (in seconds), the execution time is not reported.
* Add thumbnail_size option `#283 <https://github.com/sphinx-gallery/sphinx-gallery/pull/283>`_
* Use intersphinx for all function reference resolution `#296 <https://github.com/sphinx-gallery/sphinx-gallery/pull/296>`_
* Sphinx only directive for downloads `#298 <https://github.com/sphinx-gallery/sphinx-gallery/pull/298>`_
* Allow sorting subsection files `#281 <https://github.com/sphinx-gallery/sphinx-gallery/pull/281>`_
* We recommend using a string for ``plot_gallery`` rather than Python booleans, e.g. ``'True'`` instead
  of ``True``, as it avoids a warning about unicode when controlling this value via the command line
  switches of ``sphinx-build``

Bug Fixes
'''''''''

* Crasher in doc_resolv, in js_index.loads `#287 <https://github.com/sphinx-gallery/sphinx-gallery/issues/287>`_
* Fix gzip/BytesIO error `#293 <https://github.com/sphinx-gallery/sphinx-gallery/pull/293>`_
* Deactivate virtualenv provided by Travis `#294 <https://github.com/sphinx-gallery/sphinx-gallery/pull/294>`_

Developer changes
'''''''''''''''''

* Push the docs from Circle CI into github `#268 <https://github.com/sphinx-gallery/sphinx-gallery/pull/268>`_
* Report version to sphinx. `#292 <https://github.com/sphinx-gallery/sphinx-gallery/pull/292>`_
* Minor changes to log format. `#285 <https://github.com/sphinx-gallery/sphinx-gallery/pull/285>`_ and `#291 <https://github.com/sphinx-gallery/sphinx-gallery/pull/291>`_

v0.1.12
-------

New features
''''''''''''

* Implement a explicit order sortkey to specify the subsection's order
  within a gallery. Refer to discussion in
  `#37 <https://github.com/sphinx-gallery/sphinx-gallery/issues/37>`_,
  `#233 <https://github.com/sphinx-gallery/sphinx-gallery/pull/233>`_ and
  `#234 <https://github.com/sphinx-gallery/sphinx-gallery/pull/234>`_
* Cleanup console output during build
  `#250 <https://github.com/sphinx-gallery/sphinx-gallery/pull/250>`_
* New  configuration Test
  `#225 <https://github.com/sphinx-gallery/sphinx-gallery/pull/225>`_

Bug Fixes
'''''''''

* Reset ``sys.argv`` before running each example. See
  `#252 <https://github.com/sphinx-gallery/sphinx-gallery/pull/252>`_
  for more details.
* Correctly re-raise errors in doc resolver. See
  `#264 <https://github.com/sphinx-gallery/sphinx-gallery/pull/264>`_.
* Allow and use https links where possible
  `#258 <https://github.com/sphinx-gallery/sphinx-gallery/pull/258>`_.
* Escape tooltips for any HTML special characters.
  `#249 <https://github.com/sphinx-gallery/sphinx-gallery/pull/249>`_

Documentation
'''''''''''''''

* Update link to numpy to point to latest
  `#271 <https://github.com/sphinx-gallery/sphinx-gallery/pull/271>`_
* Added documentation dependencies.
  `#267 <https://github.com/sphinx-gallery/sphinx-gallery/pull/267>`_

v0.1.11
-------

Documentation
'''''''''''''''

* Frequently Asked Questions added to Documentation. Why `__file__` is
  not defined?

Bug Fixed
'''''''''

* Changed attribute name of Sphinx `app` object in `#242
  <https://github.com/sphinx-gallery/sphinx-gallery/issues/242>`_

v0.1.10
-------

Bug Fixed
'''''''''

* Fix image path handling bug introduced in #218

v0.1.9
------

Incompatible Changes
''''''''''''''''''''

* Sphinx Gallery's example back-references are deactivated by
  default. Now it is users responsibility to turn them on and set the
  directory where to store the files. See discussion in `#126
  <https://github.com/sphinx-gallery/sphinx-gallery/issues/126>`_ and
  pull request `#151
  <https://github.com/sphinx-gallery/sphinx-gallery/issues/151>`_.

Bug Fixed
'''''''''

* Fix download zip files path in windows builds. See `#218 <https://github.com/sphinx-gallery/sphinx-gallery/pull/218>`_
* Fix embedded missing link. See `#214 <https://github.com/sphinx-gallery/sphinx-gallery/pull/214>`_

Developer changes
'''''''''''''''''

* Move testing to py.test
* Include link to github repository in documentation

v0.1.8
------

New features
''''''''''''

* Drop styling in codelinks tooltip. Replaced for title attribute which is managed by the browser.
* Gallery output is shorter when embedding links
* Circle CI testing

Bug Fixes
'''''''''

* Sphinx-Gallery build even if examples have Syntax errors. See `#177 <https://github.com/sphinx-gallery/sphinx-gallery/pull/177>`_
* Sphinx-Gallery can now build by directly calling sphinx-build from
  any path, no explicit need to run the Makefile from the sources
  directory. See `#190 <https://github.com/sphinx-gallery/sphinx-gallery/pull/190>`_
  for more details.

v0.1.7
------

Bug Fixes
'''''''''

* Released Sphinx 1.5 has new naming convention for auto generated
  files and breaks Sphinx-Gallery documentation scanner. Fixed in
  `#178 <https://github.com/sphinx-gallery/sphinx-gallery/pull/178>`_,
  work for linking to documentation generated with Sphinx<1.5 and for
  new docs post 1.5
* Code links tooltip are now left aligned with code

New features
''''''''''''

* Development support of Sphinx-Gallery on Windows `#179
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/179>`_ & `#182
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/182>`_

v0.1.6
----------

New features
''''''''''''

* Executable script to convert Python scripts into Jupyter Notebooks `#148 <https://github.com/sphinx-gallery/sphinx-gallery/pull/148>`_


Bug Fixes
'''''''''
* Sphinx-Gallery now raises an exception if the matplotlib bakend can
  not be set to ``'agg'``. This can happen for example if
  matplotlib.pyplot is imported in conf.py. See `#157
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/157>`_ for
  more details.
* Fix ``backreferences.identify_names`` when module is used without
  attribute `#173
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/173>`_. Closes
  `#172 <https://github.com/sphinx-gallery/sphinx-gallery/issues/172>`_
  and `#149
  <https://github.com/sphinx-gallery/sphinx-gallery/issues/149>`_
* Raise FileNotFoundError when README.txt is not present in the main
  directory of the examples gallery(`#164
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/164>`_). Also
  include extra empty lines after reading README.txt to obtain the
  correct rendering of the html file.(`#165
  <https://github.com/sphinx-gallery/sphinx-gallery/pull/165>`_)
* Ship a License file in PyPI release

v0.1.5
------

New features
''''''''''''
* CSS. Now a tooltip is displayed on the source code blocks to make
  the doc-resolv functionality more discorverable. Function calls in
  the source code blocks are hyperlinks to their online documentation.
* Download buttons have a nicer look across all themes offered by
  Sphinx

Developer changes
'''''''''''''''''
* Support on the fly theme change for local builds of the
  Sphinx-Gallery docs. Passing to the make target the variable `theme`
  builds the docs with the new theme. All sphinx themes are available
  plus read the docs online theme under the value `rtd` as shown in this
  usage example.

  .. code-block:: console

    $ make html theme=rtd

* Test Sphinx Gallery support on Ubuntu 14 packages, drop Ubuntu 12
  support. Drop support for Python 2.6 in the conda environment


v0.1.4
------

New features
''''''''''''
* Enhanced CSS for download buttons
* Download buttons at the end of the gallery to download all python
  scripts or Jupyter notebooks together in a zip file. New config
  variable `download_all_examples` to toggle this effect. Activated by
  default
* Downloadable zip file with all examples as Python scripts and
  notebooks for each gallery
* Improved conversion of rst directives to markdown for the Jupyter
  notebook text blocks

Bug Fixes
'''''''''
* When seaborn is imported in a example the plot style preferences are
  transferred to plots executed afterwards. The CI is set up such that
  users can follow how to get the compatible versions of
  mayavi-pandas-seaborn and nomkl in a conda environment to have all
  the features available.
* Fix math conversion from example rst to Jupyter notebook text for
  inline math and multi-line equations

v0.1.3
------

New features
''''''''''''
* Summary of failing examples with traceback at the end of the sphinx
  build. By default the build exits with a 1 exit code if an example
  has failed. A list of examples that are expected to fail can be
  defined in `conf.py` and exit the build with 0
  exit code. Alternatively it is possible to exit the build as soon as
  one example has failed.
* Print aggregated and sorted list of computation times of all examples
  in the console during the build.
* For examples that create multiple figures, set the thumbnail image.
* The ``plot_gallery`` and ``abort_on_example_error`` options can now
  be specified in ``sphinx_gallery_conf``. The build option (``-D``
  flag passed to ``sphinx-build``) takes precedence over the
  ``sphinx_gallery_conf`` option.

Bug Fixes
'''''''''

* Failing examples are retried on every build


v0.1.2
------

Bug Fixes
'''''''''

* Examples that use ``if __name__ == '__main__'`` guards are now run
* Added vertical space between code output and code source in non
  notebook examples

v0.1.1
------

Bug Fixes
'''''''''

* Restore the html-noplot functionality
* Gallery CSS now implicitly enforces thumbnails width

v0.1.0
------

Highlights
''''''''''

Example scripts are now available for download as IPython Notebooks
`#75 <https://github.com/sphinx-gallery/sphinx-gallery/pull/75>`_

New features
''''''''''''

* Configurable filename pattern to select which example scripts are
  executed while building the Gallery
* Examples script update check are now by md5sum check and not date
* Broken Examples now display a Broken thumbnail in the gallery view,
  inside the rendered example traceback is printed. User can also set
  build process to abort as soon as an example fails.
* Sorting examples by script size
* Improve examples style

v0.0.11
-------

Highlights
''''''''''

This release incorporates the Notebook styled examples for the gallery
with PR `#36
<https://github.com/sphinx-gallery/sphinx-gallery/pull/36>`_

Incompatible Changes
''''''''''''''''''''

Sphinx-Gallery renames its python module name to sphinx\_gallery this
follows the discussion raised in `#47
<https://github.com/sphinx-gallery/sphinx-gallery/issues/47>`_ and
resolved with `#66
<https://github.com/sphinx-gallery/sphinx-gallery/pull/66>`_

The gallery configuration dictionary also changes its name to ``sphinx_gallery_conf``

From PR `#36
<https://github.com/sphinx-gallery/sphinx-gallery/pull/36>`_ it is
decided into a new namespace convention for images, thumbnails and
references. See `comment
<https://github.com/sphinx-gallery/sphinx-gallery/pull/36#issuecomment-121392815>`_


v0.0.10
-------

Highlights
''''''''''

This release allows to use the Back references. This features
incorporates fine grained examples galleries listing examples using a
particular function. `#26
<https://github.com/sphinx-gallery/sphinx-gallery/pull/26>`_

New features
''''''''''''

* Shell script to place a local copy of Sphinx-Gallery in your project
* Support Mayavi plots in the gallery
