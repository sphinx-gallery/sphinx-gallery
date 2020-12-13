Change Log
==========

v0.8.2
------

Enables HTML animations to be rendered on readthedocs.

**Implemented enhancements:**

-  DOC Expand on sphinx_gallery_thumbnail_path `#764 <https://github.com/sphinx-gallery/sphinx-gallery/pull/764>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  ENH: Add run_stale_examples config var `#759 <https://github.com/sphinx-gallery/sphinx-gallery/pull/759>`__ (`larsoner <https://github.com/larsoner>`__)
-  Option to disable note in example header `#757 <https://github.com/sphinx-gallery/sphinx-gallery/issues/757>`__
-  Add show_signature option `#756 <https://github.com/sphinx-gallery/sphinx-gallery/pull/756>`__ (`jschueller <https://github.com/jschueller>`__)
-  ENH: Style HTML output like jupyter `#752 <https://github.com/sphinx-gallery/sphinx-gallery/pull/752>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: Add RST comments, read-only `#750 <https://github.com/sphinx-gallery/sphinx-gallery/pull/750>`__ (`larsoner <https://github.com/larsoner>`__)
-  Relate warnings and errors on generated rst file back to source Python file / prevent accidental writing of generated files `#725 <https://github.com/sphinx-gallery/sphinx-gallery/issues/725>`__

**Fixed bugs:**

-  Example gallery is down `#753 <https://github.com/sphinx-gallery/sphinx-gallery/issues/753>`__
-  DOC Amend run_stale_examples command in configuration.rst `#763 <https://github.com/sphinx-gallery/sphinx-gallery/pull/763>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC update link in projects_list `#754 <https://github.com/sphinx-gallery/sphinx-gallery/pull/754>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Enable animations HTML to be rendered on readthedocs `#748 <https://github.com/sphinx-gallery/sphinx-gallery/pull/748>`__ (`sdhiscocks <https://github.com/sdhiscocks>`__)

**Closed issues:**

-  MNT: Stop using ci-helpers in appveyor.yml `#766 <https://github.com/sphinx-gallery/sphinx-gallery/issues/766>`__

**Merged pull requests:**

-  FIX: Restore whitespace `#768 <https://github.com/sphinx-gallery/sphinx-gallery/pull/768>`__ (`larsoner <https://github.com/larsoner>`__)
-  CI: Remove AppVeyor, work on Azure `#767 <https://github.com/sphinx-gallery/sphinx-gallery/pull/767>`__ (`larsoner <https://github.com/larsoner>`__)
-  DOC Standardise capitalisation of Sphinx-Gallery `#762 <https://github.com/sphinx-gallery/sphinx-gallery/pull/762>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

v0.8.1
------

Fix Binder logo image file for Windows paths.

**Fixed bugs:**

-  sphinx_gallery/tests/test_full.py::test_binder_logo_exists fails (path is clearly wrong) `#746 <https://github.com/sphinx-gallery/sphinx-gallery/issues/746>`__
-  BUG Windows relative path error with \_static Binder logo `#744 <https://github.com/sphinx-gallery/sphinx-gallery/issues/744>`__
-  BUG Copy Binder logo to avoid Window drive rel path error `#745 <https://github.com/sphinx-gallery/sphinx-gallery/pull/745>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

**Merged pull requests:**

-  DOC Add link to cross referencing example `#743 <https://github.com/sphinx-gallery/sphinx-gallery/pull/743>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

v0.8.0
------

The default for configuration `thumbnail_size` will change from `(400, 280)`
(2.5x maximum size specified by CSS) to `(320, 224)` (2x maximum size specified
by CSS) in version 0.9.0.

**Implemented enhancements:**

-  Pass command line arguments to examples `#731 <https://github.com/sphinx-gallery/sphinx-gallery/issues/731>`__
-  Limited rst to md support in notebooks `#219 <https://github.com/sphinx-gallery/sphinx-gallery/issues/219>`__
-  Enable ffmpeg for animations for newer matplotlib `#733 <https://github.com/sphinx-gallery/sphinx-gallery/pull/733>`__ (`dopplershift <https://github.com/dopplershift>`__)
-  Implement option to pass command line args to example scripts `#732 <https://github.com/sphinx-gallery/sphinx-gallery/pull/732>`__ (`mschmidt87 <https://github.com/mschmidt87>`__)
-  ENH: Dont allow input `#729 <https://github.com/sphinx-gallery/sphinx-gallery/pull/729>`__ (`larsoner <https://github.com/larsoner>`__)
-  Add support for image links and data URIs for notebooks `#724 <https://github.com/sphinx-gallery/sphinx-gallery/pull/724>`__ (`sdhiscocks <https://github.com/sdhiscocks>`__)
-  Support headings in RST to MD `#723 <https://github.com/sphinx-gallery/sphinx-gallery/pull/723>`__ (`sdhiscocks <https://github.com/sdhiscocks>`__)
-  ENH Support pypandoc to convert rst to md for ipynb `#705 <https://github.com/sphinx-gallery/sphinx-gallery/pull/705>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  ENH: Use broader def of Animation `#693 <https://github.com/sphinx-gallery/sphinx-gallery/pull/693>`__ (`larsoner <https://github.com/larsoner>`__)

**Fixed bugs:**

-  \_repr_html\_ not shown on RTD `#736 <https://github.com/sphinx-gallery/sphinx-gallery/issues/736>`__
-  Binder icon is hardcoded, which causes a loading failure with on some browsers `#735 <https://github.com/sphinx-gallery/sphinx-gallery/issues/735>`__
-  How to scrape for images without executing example scripts `#728 <https://github.com/sphinx-gallery/sphinx-gallery/issues/728>`__
-  sphinx-gallery/0.7.0: TypeError: ‘str’ object is not callable when building its documentation `#727 <https://github.com/sphinx-gallery/sphinx-gallery/issues/727>`__
-  Thumbnail oversampling `#717 <https://github.com/sphinx-gallery/sphinx-gallery/issues/717>`__
-  Working with pre-built galleries `#704 <https://github.com/sphinx-gallery/sphinx-gallery/issues/704>`__
-  Calling “plt.show()” raises an ugly warning `#694 <https://github.com/sphinx-gallery/sphinx-gallery/issues/694>`__
-  Searching in docs v0.6.2 stable does not work `#689 <https://github.com/sphinx-gallery/sphinx-gallery/issues/689>`__
-  Fix logger message pypandoc `#741 <https://github.com/sphinx-gallery/sphinx-gallery/pull/741>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Use local binder logo svg `#738 <https://github.com/sphinx-gallery/sphinx-gallery/pull/738>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  BUG: Fix handling of scraper error `#737 <https://github.com/sphinx-gallery/sphinx-gallery/pull/737>`__ (`larsoner <https://github.com/larsoner>`__)
-  Improve documentation of example for custom image scraper `#730 <https://github.com/sphinx-gallery/sphinx-gallery/pull/730>`__ (`mschmidt87 <https://github.com/mschmidt87>`__)
-  Make md5 hash independent of platform line endings `#722 <https://github.com/sphinx-gallery/sphinx-gallery/pull/722>`__ (`sdhiscocks <https://github.com/sdhiscocks>`__)
-  MAINT: Deal with mayavi `#720 <https://github.com/sphinx-gallery/sphinx-gallery/pull/720>`__ (`larsoner <https://github.com/larsoner>`__)
-  DOC Clarify thumbnail_size and note change in default `#719 <https://github.com/sphinx-gallery/sphinx-gallery/pull/719>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  BUG: Always do linking `#714 <https://github.com/sphinx-gallery/sphinx-gallery/pull/714>`__ (`larsoner <https://github.com/larsoner>`__)
-  DOC: Correctly document option `#711 <https://github.com/sphinx-gallery/sphinx-gallery/pull/711>`__ (`larsoner <https://github.com/larsoner>`__)
-  BUG Check ‘capture_repr’ and ‘ignore_repr_types’ `#709 <https://github.com/sphinx-gallery/sphinx-gallery/pull/709>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Update Sphinx url `#708 <https://github.com/sphinx-gallery/sphinx-gallery/pull/708>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  BUG: Use relative paths for zip downloads `#706 <https://github.com/sphinx-gallery/sphinx-gallery/pull/706>`__ (`pmeier <https://github.com/pmeier>`__)
-  FIX: Build on nightly using master `#703 <https://github.com/sphinx-gallery/sphinx-gallery/pull/703>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Fix CircleCI `#701 <https://github.com/sphinx-gallery/sphinx-gallery/pull/701>`__ (`larsoner <https://github.com/larsoner>`__)
-  Enable html to be rendered on readthedocs `#700 <https://github.com/sphinx-gallery/sphinx-gallery/pull/700>`__ (`sdhiscocks <https://github.com/sdhiscocks>`__)
-  Remove matplotlib agg warning `#696 <https://github.com/sphinx-gallery/sphinx-gallery/pull/696>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

**Closed issues:**

-  Reference :ref:``sphx\_glr\_auto\_examples`` goes to SciKit-Learn examples `#734 <https://github.com/sphinx-gallery/sphinx-gallery/issues/734>`__
-  Q: how to have a couple of images with ``bbox\_inches='tight'``. `#726 <https://github.com/sphinx-gallery/sphinx-gallery/issues/726>`__
-  filename_pattern still doesn’t work all that great for working on one tutorial `#721 <https://github.com/sphinx-gallery/sphinx-gallery/issues/721>`__
-  Gallery example using plotly `#715 <https://github.com/sphinx-gallery/sphinx-gallery/issues/715>`__
-  DOC Builder types clarification `#697 <https://github.com/sphinx-gallery/sphinx-gallery/issues/697>`__

**Merged pull requests:**

-  DOC add section on interpreting error/warnings `#740 <https://github.com/sphinx-gallery/sphinx-gallery/pull/740>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Add citation details to readme `#739 <https://github.com/sphinx-gallery/sphinx-gallery/pull/739>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Plotly example for the gallery `#718 <https://github.com/sphinx-gallery/sphinx-gallery/pull/718>`__ (`emmanuelle <https://github.com/emmanuelle>`__)
-  DOC Specify matplotlib in animation example `#716 <https://github.com/sphinx-gallery/sphinx-gallery/pull/716>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MAINT: Bump pytest versions in Travis runs `#712 <https://github.com/sphinx-gallery/sphinx-gallery/pull/712>`__ (`larsoner <https://github.com/larsoner>`__)
-  DOC Update warning section in configuration.rst `#702 <https://github.com/sphinx-gallery/sphinx-gallery/pull/702>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC remove mention of other builder types `#698 <https://github.com/sphinx-gallery/sphinx-gallery/pull/698>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Bumpversion `#692 <https://github.com/sphinx-gallery/sphinx-gallery/pull/692>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

v0.7.0
------

Developer changes
'''''''''''''''''

- Use Sphinx errors rather than built-in errors.

**Implemented enhancements:**

-  ENH: Use Sphinx errors `#690 <https://github.com/sphinx-gallery/sphinx-gallery/pull/690>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: Add support for FuncAnimation `#687 <https://github.com/sphinx-gallery/sphinx-gallery/pull/687>`__ (`larsoner <https://github.com/larsoner>`__)
-  Sphinx directive to insert mini-galleries `#685 <https://github.com/sphinx-gallery/sphinx-gallery/pull/685>`__ (`ayshih <https://github.com/ayshih>`__)
-  Provide a Sphinx directive to insert a mini-gallery `#683 <https://github.com/sphinx-gallery/sphinx-gallery/issues/683>`__
-  ENH Add cross ref label to template module.rst `#680 <https://github.com/sphinx-gallery/sphinx-gallery/pull/680>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  ENH: Add show_memory extension API `#677 <https://github.com/sphinx-gallery/sphinx-gallery/pull/677>`__ (`larsoner <https://github.com/larsoner>`__)
-  Support for GPU memory logging `#671 <https://github.com/sphinx-gallery/sphinx-gallery/issues/671>`__
-  ENH Add alt attribute for thumbnails `#668 <https://github.com/sphinx-gallery/sphinx-gallery/pull/668>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  ENH More informative ‘alt’ attribute for thumbnails in index `#664 <https://github.com/sphinx-gallery/sphinx-gallery/issues/664>`__
-  ENH More informative ‘alt’ attribute for images `#663 <https://github.com/sphinx-gallery/sphinx-gallery/pull/663>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  ENH: Use optipng when requested `#656 <https://github.com/sphinx-gallery/sphinx-gallery/pull/656>`__ (`larsoner <https://github.com/larsoner>`__)
-  thumbnails cause heavy gallery pages and long loading time `#655 <https://github.com/sphinx-gallery/sphinx-gallery/issues/655>`__
-  MAINT: Better error messages `#600 <https://github.com/sphinx-gallery/sphinx-gallery/issues/600>`__
-  More informative “alt” attribute for image tags `#538 <https://github.com/sphinx-gallery/sphinx-gallery/issues/538>`__
-  ENH: easy linking to “examples using my_function” `#496 <https://github.com/sphinx-gallery/sphinx-gallery/issues/496>`__
-  sub-galleries should be generated with a separate “gallery rst” file `#413 <https://github.com/sphinx-gallery/sphinx-gallery/issues/413>`__
-  matplotlib animations support `#150 <https://github.com/sphinx-gallery/sphinx-gallery/issues/150>`__

**Fixed bugs:**

-  Add backref label for classes in module.rst `#688 <https://github.com/sphinx-gallery/sphinx-gallery/pull/688>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Fixed backreference inspection to account for tilde use `#684 <https://github.com/sphinx-gallery/sphinx-gallery/pull/684>`__ (`ayshih <https://github.com/ayshih>`__)
-  Fix regex for numpy RandomState in test_full `#682 <https://github.com/sphinx-gallery/sphinx-gallery/pull/682>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  fix tests regex to search for numpy data in html `#681 <https://github.com/sphinx-gallery/sphinx-gallery/issues/681>`__
-  FIX: Fix sys.stdout patching `#678 <https://github.com/sphinx-gallery/sphinx-gallery/pull/678>`__ (`larsoner <https://github.com/larsoner>`__)
-  check-manifest causing master to fail `#675 <https://github.com/sphinx-gallery/sphinx-gallery/issues/675>`__
-  Output of logger is not captured if the logger is created in a different cell `#672 <https://github.com/sphinx-gallery/sphinx-gallery/issues/672>`__
-  FIX: Remove newlines from title `#669 <https://github.com/sphinx-gallery/sphinx-gallery/pull/669>`__ (`larsoner <https://github.com/larsoner>`__)
-  BUG Tinybuild autosummary links fail with Sphinx dev `#659 <https://github.com/sphinx-gallery/sphinx-gallery/issues/659>`__

**Documentation:**

-  DOC Update label to raw string in plot_0_sin.py `#674 <https://github.com/sphinx-gallery/sphinx-gallery/pull/674>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Update Sphinx url to https `#673 <https://github.com/sphinx-gallery/sphinx-gallery/pull/673>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Clarify syntax.rst `#670 <https://github.com/sphinx-gallery/sphinx-gallery/pull/670>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Note config comment removal in code only `#667 <https://github.com/sphinx-gallery/sphinx-gallery/pull/667>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Update links in syntax.rst `#666 <https://github.com/sphinx-gallery/sphinx-gallery/pull/666>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Fix typos, clarify `#662 <https://github.com/sphinx-gallery/sphinx-gallery/pull/662>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Update html-noplot `#658 <https://github.com/sphinx-gallery/sphinx-gallery/pull/658>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC: Fix PNGScraper example `#653 <https://github.com/sphinx-gallery/sphinx-gallery/pull/653>`__ (`denkii <https://github.com/denkii>`__)
-  DOC: Fix typos in documentation files. `#652 <https://github.com/sphinx-gallery/sphinx-gallery/pull/652>`__ (`TomDonoghue <https://github.com/TomDonoghue>`__)
-  Inconsistency with applying & removing sphinx gallery configs `#665 <https://github.com/sphinx-gallery/sphinx-gallery/issues/665>`__
-  ``make html-noplot`` instructions outdated `#606 <https://github.com/sphinx-gallery/sphinx-gallery/issues/606>`__

**Closed issues:**

-  intersphinx links need backreferences_dir `#467 <https://github.com/sphinx-gallery/sphinx-gallery/issues/467>`__

**Merged pull requests:**

-  Fix lint in gen_gallery.py `#686 <https://github.com/sphinx-gallery/sphinx-gallery/pull/686>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Better alt thumbnail test for punctuation in title `#679 <https://github.com/sphinx-gallery/sphinx-gallery/pull/679>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Update manifest for changes to check-manifest `#676 <https://github.com/sphinx-gallery/sphinx-gallery/pull/676>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MAINT: Update CircleCI `#657 <https://github.com/sphinx-gallery/sphinx-gallery/pull/657>`__ (`larsoner <https://github.com/larsoner>`__)
-  Bump version to 0.7.0.dev0 `#651 <https://github.com/sphinx-gallery/sphinx-gallery/pull/651>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

v0.6.2
------

- Patch release due to missing CSS files in v0.6.1. Manifest check added to CI.

**Implemented enhancements:**

-  How do I best cite sphinx-gallery? `#639 <https://github.com/sphinx-gallery/sphinx-gallery/issues/639>`__
-  MRG, ENH: Add Zenodo badge `#641 <https://github.com/sphinx-gallery/sphinx-gallery/pull/641>`__ (`larsoner <https://github.com/larsoner>`__)

**Fixed bugs:**

-  BUG Wrong pandas intersphinx URL `#646 <https://github.com/sphinx-gallery/sphinx-gallery/issues/646>`__
-  css not included in wheels? `#644 <https://github.com/sphinx-gallery/sphinx-gallery/issues/644>`__
-  BUG: Fix CSS includes and add manifest check in CI `#648 <https://github.com/sphinx-gallery/sphinx-gallery/pull/648>`__ (`larsoner <https://github.com/larsoner>`__)
-  Update pandas intersphinx url `#647 <https://github.com/sphinx-gallery/sphinx-gallery/pull/647>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

**Merged pull requests:**

-  Update maintainers url in RELEASES.md `#649 <https://github.com/sphinx-gallery/sphinx-gallery/pull/649>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Amend maintainers `#643 <https://github.com/sphinx-gallery/sphinx-gallery/pull/643>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Change version back to 0.7.0.dev0 `#642 <https://github.com/sphinx-gallery/sphinx-gallery/pull/642>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

v0.6.1
------

Developer changes
'''''''''''''''''

- Added Zenodo integration. This release is for Zenodo to pick it up.

**Implemented enhancements:**

-  Allow pathlib.Path to backreferences_dir option `#635 <https://github.com/sphinx-gallery/sphinx-gallery/issues/635>`__
-  ENH Allow backrefences_dir to be pathlib object `#638 <https://github.com/sphinx-gallery/sphinx-gallery/pull/638>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

**Fixed bugs:**

-  TypeError when creating links from gallery to documentation `#634 <https://github.com/sphinx-gallery/sphinx-gallery/issues/634>`__
-  BUG Checks if filenames have space `#636 <https://github.com/sphinx-gallery/sphinx-gallery/pull/636>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Fix missing space in error message. `#632 <https://github.com/sphinx-gallery/sphinx-gallery/pull/632>`__ (`anntzer <https://github.com/anntzer>`__)
-  BUG: Spaces in example filenames break image linking `#440 <https://github.com/sphinx-gallery/sphinx-gallery/issues/440>`__

**Closed issues:**

-  New release? `#627 <https://github.com/sphinx-gallery/sphinx-gallery/issues/627>`__

**Merged pull requests:**

-  DOC minor update to release guide `#633 <https://github.com/sphinx-gallery/sphinx-gallery/pull/633>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Bump release version `#631 <https://github.com/sphinx-gallery/sphinx-gallery/pull/631>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

v0.6.0
------

Developer changes
'''''''''''''''''

- Reduced number of hard dependencies and added `dev-requirements.txt`.
- AppVeyor bumped from Python 3.6 to 3.7.
- Split CSS and create sub-extension that loads CSS.

**Implemented enhancements:**

-  ENH Add last cell config `#625 <https://github.com/sphinx-gallery/sphinx-gallery/pull/625>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  ENH: Add sub-classes for download links `#623 <https://github.com/sphinx-gallery/sphinx-gallery/pull/623>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: New file-based conf-parameter thumbnail_path `#609 <https://github.com/sphinx-gallery/sphinx-gallery/pull/609>`__ (`prisae <https://github.com/prisae>`__)
-  MRG, ENH: Provide sub-extension sphinx_gallery.load_style `#601 <https://github.com/sphinx-gallery/sphinx-gallery/pull/601>`__ (`mgeier <https://github.com/mgeier>`__)
-  [DOC] Minor amendments to CSS config part `#594 <https://github.com/sphinx-gallery/sphinx-gallery/pull/594>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [MRG] [ENH] Add css for pandas df `#590 <https://github.com/sphinx-gallery/sphinx-gallery/pull/590>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  ENH: Add CSS classes for backrefs `#581 <https://github.com/sphinx-gallery/sphinx-gallery/pull/581>`__ (`larsoner <https://github.com/larsoner>`__)
-  Add ability to ignore repr of specific types `#577 <https://github.com/sphinx-gallery/sphinx-gallery/pull/577>`__ (`banesullivan <https://github.com/banesullivan>`__)

**Fixed bugs:**

-  BUG: Longer timeout on macOS `#629 <https://github.com/sphinx-gallery/sphinx-gallery/pull/629>`__ (`larsoner <https://github.com/larsoner>`__)
-  BUG Fix test for new sphinx `#619 <https://github.com/sphinx-gallery/sphinx-gallery/pull/619>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MRG, FIX: Allow pickling `#604 <https://github.com/sphinx-gallery/sphinx-gallery/pull/604>`__ (`larsoner <https://github.com/larsoner>`__)
-  CSS: Restrict thumbnail height to 112 px `#595 <https://github.com/sphinx-gallery/sphinx-gallery/pull/595>`__ (`mgeier <https://github.com/mgeier>`__)
-  MRG, FIX: Link to RandomState properly `#593 <https://github.com/sphinx-gallery/sphinx-gallery/pull/593>`__ (`larsoner <https://github.com/larsoner>`__)
-  MRG, FIX: Fix backref styling `#591 <https://github.com/sphinx-gallery/sphinx-gallery/pull/591>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Update checks for PIL/JPEG `#586 <https://github.com/sphinx-gallery/sphinx-gallery/pull/586>`__ (`larsoner <https://github.com/larsoner>`__)
-  DOC: Fix code block language `#585 <https://github.com/sphinx-gallery/sphinx-gallery/pull/585>`__ (`larsoner <https://github.com/larsoner>`__)
-  [MRG] Fix backreferences for functions not directly imported `#584 <https://github.com/sphinx-gallery/sphinx-gallery/pull/584>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  BUG: Fix repr None `#578 <https://github.com/sphinx-gallery/sphinx-gallery/pull/578>`__ (`larsoner <https://github.com/larsoner>`__)
-  [MRG] Add ignore pattern to check dups `#574 <https://github.com/sphinx-gallery/sphinx-gallery/pull/574>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [MRG] Check backreferences_dir config `#571 <https://github.com/sphinx-gallery/sphinx-gallery/pull/571>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  URLError `#569 <https://github.com/sphinx-gallery/sphinx-gallery/pull/569>`__ (`EtienneCmb <https://github.com/EtienneCmb>`__)
-  MRG Remove last/first_notebook_cell redundancy `#626 <https://github.com/sphinx-gallery/sphinx-gallery/pull/626>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Remove duplicate doc_solver entry in the API reference structure `#589 <https://github.com/sphinx-gallery/sphinx-gallery/pull/589>`__ (`kanderso-nrel <https://github.com/kanderso-nrel>`__)

**Closed issues:**

-  Allow removal of “download jupyter notebook” link `#622 <https://github.com/sphinx-gallery/sphinx-gallery/issues/622>`__
-  thumbnails from loaded figures `#607 <https://github.com/sphinx-gallery/sphinx-gallery/issues/607>`__
-  last_notebook_cell `#605 <https://github.com/sphinx-gallery/sphinx-gallery/issues/605>`__
-  Building fails with pickling error `#602 <https://github.com/sphinx-gallery/sphinx-gallery/issues/602>`__
-  BUG: Bugs with backref links `#587 <https://github.com/sphinx-gallery/sphinx-gallery/issues/587>`__
-  BUG backreferences not working for functions if not imported directly `#583 <https://github.com/sphinx-gallery/sphinx-gallery/issues/583>`__
-  AttributeError: ‘URLError’ object has no attribute ‘url’ `#568 <https://github.com/sphinx-gallery/sphinx-gallery/issues/568>`__
-  BUG Check “backreferences_dir” is str or None `#567 <https://github.com/sphinx-gallery/sphinx-gallery/issues/567>`__
-  check_duplicated does not respect the ignore_pattern `#474 <https://github.com/sphinx-gallery/sphinx-gallery/issues/474>`__
-  Sphinx-Gallery Binder links: environment.yml does not get “installed” `#628 <https://github.com/sphinx-gallery/sphinx-gallery/issues/628>`__
-  Another place to replace “######” separators by “# %%” `#620 <https://github.com/sphinx-gallery/sphinx-gallery/issues/620>`__
-  How to prevent output to stderr from being captured. `#618 <https://github.com/sphinx-gallery/sphinx-gallery/issues/618>`__
-  Master failing with sphinx dev `#617 <https://github.com/sphinx-gallery/sphinx-gallery/issues/617>`__
-  Mention the support for \_repr_html\_ on custom scraper doc `#614 <https://github.com/sphinx-gallery/sphinx-gallery/issues/614>`__
-  Mention the multiple possible separators in the notebook-style example `#611 <https://github.com/sphinx-gallery/sphinx-gallery/issues/611>`__
-  Cell marker causes pycodestyle error `#608 <https://github.com/sphinx-gallery/sphinx-gallery/issues/608>`__
-  Reduce the amount of hard dependencies? `#597 <https://github.com/sphinx-gallery/sphinx-gallery/issues/597>`__
-  instances not getting correct CSS classes `#588 <https://github.com/sphinx-gallery/sphinx-gallery/issues/588>`__
-  greedy backreferences `#580 <https://github.com/sphinx-gallery/sphinx-gallery/issues/580>`__
-  Error when using two image scrappers together `#579 <https://github.com/sphinx-gallery/sphinx-gallery/issues/579>`__
-  Improve the junit xml `#576 <https://github.com/sphinx-gallery/sphinx-gallery/issues/576>`__
-  Remove the note linking to the download section at the beginning of the example from latex/pdf output `#572 <https://github.com/sphinx-gallery/sphinx-gallery/issues/572>`__
-  typing.TYPE_CHECKING is True at runtime in executed .py files `#570 <https://github.com/sphinx-gallery/sphinx-gallery/issues/570>`__
-  How best to handle data files? `#565 <https://github.com/sphinx-gallery/sphinx-gallery/issues/565>`__
-  ENH Add CSS for pandas dataframe `#544 <https://github.com/sphinx-gallery/sphinx-gallery/issues/544>`__

**Merged pull requests:**

-  DOC use # %% `#624 <https://github.com/sphinx-gallery/sphinx-gallery/pull/624>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC capture repr in scraper section `#616 <https://github.com/sphinx-gallery/sphinx-gallery/pull/616>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [MRG+1] DOC Improve doc of splitters and use in IDE `#615 <https://github.com/sphinx-gallery/sphinx-gallery/pull/615>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC mention template `#613 <https://github.com/sphinx-gallery/sphinx-gallery/pull/613>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  recommend consistent use of one block splitter `#610 <https://github.com/sphinx-gallery/sphinx-gallery/pull/610>`__ (`mikofski <https://github.com/mikofski>`__)
-  MRG, MAINT: Split CSS and add control `#599 <https://github.com/sphinx-gallery/sphinx-gallery/pull/599>`__ (`larsoner <https://github.com/larsoner>`__)
-  MRG, MAINT: Update deps `#598 <https://github.com/sphinx-gallery/sphinx-gallery/pull/598>`__ (`larsoner <https://github.com/larsoner>`__)
-  MRG, ENH: Link to methods and properties properly `#596 <https://github.com/sphinx-gallery/sphinx-gallery/pull/596>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Try to get nightly working `#592 <https://github.com/sphinx-gallery/sphinx-gallery/pull/592>`__ (`larsoner <https://github.com/larsoner>`__)
-  mention literalinclude in the doc `#582 <https://github.com/sphinx-gallery/sphinx-gallery/pull/582>`__ (`emmanuelle <https://github.com/emmanuelle>`__)
-  MAINT: Bump AppVeyor to 3.7 `#575 <https://github.com/sphinx-gallery/sphinx-gallery/pull/575>`__ (`larsoner <https://github.com/larsoner>`__)

v0.5.0
------

Developer changes
'''''''''''''''''

- Separated 'dev' documentation, which tracks master and 'stable' documentation,
  which follows releases.
- Added official jpeg support.

Incompatible changes
''''''''''''''''''''

- Dropped support for Sphinx < 1.8.3.
- Dropped support for Python < 3.5.
- Added ``capture_repr`` configuration with the default setting
  ``('_repr_html_', __repr__')``. This may result the capturing of unwanted output
  in existing projects. Set ``capture_repr: ()`` to return to behaviour prior
  to this release.

**Implemented enhancements:**

-  Explain the inputs of the image scrapers `#472 <https://github.com/sphinx-gallery/sphinx-gallery/issues/472>`__
-  Capture HTML output as in Jupyter `#396 <https://github.com/sphinx-gallery/sphinx-gallery/issues/396>`__
-  Feature request: Add an option for different cell separations `#370 <https://github.com/sphinx-gallery/sphinx-gallery/issues/370>`__
-  Mark sphinx extension as parallel-safe for writing `#561 <https://github.com/sphinx-gallery/sphinx-gallery/pull/561>`__ (`astrofrog <https://github.com/astrofrog>`__)
-  ENH: Support linking to builtin modules `#558 <https://github.com/sphinx-gallery/sphinx-gallery/pull/558>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: Add official JPG support and better tests `#557 <https://github.com/sphinx-gallery/sphinx-gallery/pull/557>`__ (`larsoner <https://github.com/larsoner>`__)
-  [MRG] ENH: Capture ’repr’s of last expression `#541 <https://github.com/sphinx-gallery/sphinx-gallery/pull/541>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  look for both ‘README’ and ‘readme’ `#535 <https://github.com/sphinx-gallery/sphinx-gallery/pull/535>`__ (`revesansparole <https://github.com/revesansparole>`__)
-  ENH: Speed up builds `#526 <https://github.com/sphinx-gallery/sphinx-gallery/pull/526>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: Add live object refs and methods `#525 <https://github.com/sphinx-gallery/sphinx-gallery/pull/525>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: Show memory usage, too `#523 <https://github.com/sphinx-gallery/sphinx-gallery/pull/523>`__ (`larsoner <https://github.com/larsoner>`__)
-  [MRG] EHN support #%% cell separators `#518 <https://github.com/sphinx-gallery/sphinx-gallery/pull/518>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MAINT: Remove support for old Python and Sphinx `#513 <https://github.com/sphinx-gallery/sphinx-gallery/pull/513>`__ (`larsoner <https://github.com/larsoner>`__)

**Fixed bugs:**

-  Documentation is ahead of current release `#559 <https://github.com/sphinx-gallery/sphinx-gallery/issues/559>`__
-  Fix JPEG thumbnail generation `#556 <https://github.com/sphinx-gallery/sphinx-gallery/pull/556>`__ (`rgov <https://github.com/rgov>`__)
-  [MRG] Fix terminal rst block last word `#548 <https://github.com/sphinx-gallery/sphinx-gallery/pull/548>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [MRG][FIX] Remove output box from print(__doc__) `#529 <https://github.com/sphinx-gallery/sphinx-gallery/pull/529>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  BUG: Fix kwargs modification in loop `#527 <https://github.com/sphinx-gallery/sphinx-gallery/pull/527>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Fix AppVeyor `#524 <https://github.com/sphinx-gallery/sphinx-gallery/pull/524>`__ (`larsoner <https://github.com/larsoner>`__)

**Closed issues:**

-  Making sphinx-gallery parallel_write_safe `#560 <https://github.com/sphinx-gallery/sphinx-gallery/issues/560>`__
-  Mayavi example cannot run in binder `#554 <https://github.com/sphinx-gallery/sphinx-gallery/issues/554>`__
-  Support pyqtgraph plots `#553 <https://github.com/sphinx-gallery/sphinx-gallery/issues/553>`__
-  Last word in rst used as code `#546 <https://github.com/sphinx-gallery/sphinx-gallery/issues/546>`__
-  ENH capture ’repr’s of last expression `#540 <https://github.com/sphinx-gallery/sphinx-gallery/issues/540>`__
-  Mention list of projects using sphinx-gallery in a documentation page `#536 <https://github.com/sphinx-gallery/sphinx-gallery/issues/536>`__
-  consider looking also for ‘readme.\*’ instead of only ‘README.\*’ `#534 <https://github.com/sphinx-gallery/sphinx-gallery/issues/534>`__
-  Small regression in 0.4.1: print(__doc__) creates empty output block `#528 <https://github.com/sphinx-gallery/sphinx-gallery/issues/528>`__
-  Show memory usage in build output `#522 <https://github.com/sphinx-gallery/sphinx-gallery/issues/522>`__
-  Linking to external examples `#519 <https://github.com/sphinx-gallery/sphinx-gallery/issues/519>`__
-  Intro text gets truncated on ‘-’ character `#517 <https://github.com/sphinx-gallery/sphinx-gallery/issues/517>`__
-  REL: New release `#507 <https://github.com/sphinx-gallery/sphinx-gallery/issues/507>`__
-  Matplotlib raises warning when ‘pyplot.show()’ is called `#488 <https://github.com/sphinx-gallery/sphinx-gallery/issues/488>`__
-  Only support the latest 2 or 3 Sphinx versions `#407 <https://github.com/sphinx-gallery/sphinx-gallery/issues/407>`__
-  Drop Python 2.X support `#405 <https://github.com/sphinx-gallery/sphinx-gallery/issues/405>`__
-  Inspiration from new gallery package for sphinx: sphinx-exhibit `#402 <https://github.com/sphinx-gallery/sphinx-gallery/issues/402>`__
-  DOC: each example should start by explaining why it’s there `#143 <https://github.com/sphinx-gallery/sphinx-gallery/issues/143>`__

**Merged pull requests:**

-  [MRG] DOC: Add warning filter note in doc `#564 <https://github.com/sphinx-gallery/sphinx-gallery/pull/564>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [MRG] DOC: Explain each example `#563 <https://github.com/sphinx-gallery/sphinx-gallery/pull/563>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  ENH: Add dev/stable distinction `#562 <https://github.com/sphinx-gallery/sphinx-gallery/pull/562>`__ (`larsoner <https://github.com/larsoner>`__)
-  DOC update example capture_repr `#552 <https://github.com/sphinx-gallery/sphinx-gallery/pull/552>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  BUG: Fix index check `#551 <https://github.com/sphinx-gallery/sphinx-gallery/pull/551>`__ (`larsoner <https://github.com/larsoner>`__)
-  FIX: Fix spurious failures `#550 <https://github.com/sphinx-gallery/sphinx-gallery/pull/550>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Update CIs `#549 <https://github.com/sphinx-gallery/sphinx-gallery/pull/549>`__ (`larsoner <https://github.com/larsoner>`__)
-  list of projects using sphinx-gallery `#547 <https://github.com/sphinx-gallery/sphinx-gallery/pull/547>`__ (`emmanuelle <https://github.com/emmanuelle>`__)
-  [MRG] DOC typos and clarifications `#545 <https://github.com/sphinx-gallery/sphinx-gallery/pull/545>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  add class to clear tag `#543 <https://github.com/sphinx-gallery/sphinx-gallery/pull/543>`__ (`dorafc <https://github.com/dorafc>`__)
-  MAINT: Fix for 3.8 `#542 <https://github.com/sphinx-gallery/sphinx-gallery/pull/542>`__ (`larsoner <https://github.com/larsoner>`__)
-  [MRG] DOC: Explain image scraper inputs `#539 <https://github.com/sphinx-gallery/sphinx-gallery/pull/539>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [MRG] Allow punctuation marks in title `#537 <https://github.com/sphinx-gallery/sphinx-gallery/pull/537>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Improve documentation `#533 <https://github.com/sphinx-gallery/sphinx-gallery/pull/533>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  ENH: Add direct link to artifact `#532 <https://github.com/sphinx-gallery/sphinx-gallery/pull/532>`__ (`larsoner <https://github.com/larsoner>`__)
-  [MRG] Remove matplotlib agg backend + plt.show warnings from doc `#521 <https://github.com/sphinx-gallery/sphinx-gallery/pull/521>`__ (`lesteve <https://github.com/lesteve>`__)
-  MAINT: Fixes for latest pytest `#516 <https://github.com/sphinx-gallery/sphinx-gallery/pull/516>`__ (`larsoner <https://github.com/larsoner>`__)
-  Add FURY to the sphinx-gallery users list `#515 <https://github.com/sphinx-gallery/sphinx-gallery/pull/515>`__ (`skoudoro <https://github.com/skoudoro>`__)

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
