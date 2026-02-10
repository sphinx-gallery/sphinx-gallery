Changelog
=========

v0.20.0
-------

Support for Sphinx 5 dropped in this release. Requirement is now Sphinx >= 6.

v0.19.0
-------

**Implemented enhancements:**

-  Add block-level ``sphinx_gallery_capture_repr_block`` setting `#1398 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1398>`__ (`tpvasconcelos <https://github.com/tpvasconcelos>`__)

**Fixed bugs:**

-  Fix minigallery duplicates and add tests and update documenation `#1435 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1435>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Fix: Fix minigallery duplicates `#1430 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1430>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Fix incorrect paths for JupyterLite Notebook interface URLs, unpin ``jupyterlite-sphinx``, and update JupyterLite integration docs `#1417 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1417>`__ (`agriyakhetarpal <https://github.com/agriyakhetarpal>`__)
-  BUG: make \_anim_rst windows compatible `#1399 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1399>`__ (`story645 <https://github.com/story645>`__)
-  Fix custom sort `#1391 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1391>`__ (`drammock <https://github.com/drammock>`__)

**Documentation**

-  DOC Fixes to minigallery doc in ``configuration\.rst`` `#1437 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1437>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Improve doc on linking code blocks `#1419 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1419>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Doc: mention color css property to hide links `#1412 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1412>`__ (`jschueller <https://github.com/jschueller>`__)
-  DOC Improve custom sort key docs `#1401 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1401>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

**Project maintenance**

-  [pre-commit.ci] pre-commit autoupdate `#1434 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1434>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1431 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1431>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1428 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1428>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  Fix label checker workflow `#1426 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1426>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1423 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1423>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1422 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1422>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1418 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1418>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1416 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1416>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1415 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1415>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1413 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1413>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1408 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1408>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1407 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1407>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  Bump codecov/codecov-action from 4 to 5 in the actions group `#1406 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1406>`__ (`dependabot[bot] <https://github.com/apps/dependabot>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1405 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1405>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  MNT Add test for ``minigallery_sort_order`` `#1402 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1402>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1400 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1400>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1395 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1395>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1393 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1393>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1390 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1390>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)

v0.18.0
-------

**Implemented enhancements:**

-  Allow to disable writing computation times `#1385 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1385>`__ (`bmwiedemann <https://github.com/bmwiedemann>`__)
-  [ENH] Add option to render multiple images from same cell as single-img `#1384 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1384>`__ (`tsbinns <https://github.com/tsbinns>`__)

**Fixed bugs:**

-  Fix ``indexst`` variable does not exist when own index gallery is first `#1383 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1383>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

**Project maintenance**

-  [pre-commit.ci] pre-commit autoupdate `#1387 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1387>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  Bump mamba-org/setup-micromamba from 1 to 2 in the actions group `#1386 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1386>`__ (`dependabot[bot] <https://github.com/apps/dependabot>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1380 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1380>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1379 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1379>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1378 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1378>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1377 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1377>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1376 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1376>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1375 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1375>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1373 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1373>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1372 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1372>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)

v0.17.1
-------

**Fixed bugs:**

-  FIX: Fix stability of stored compiled regex `#1369 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1369>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: Improve \_sanitize_rst `#1366 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1366>`__ (`timhoffm <https://github.com/timhoffm>`__)
-  Obey prefer_full_module setting when finding backreferences `#1364 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1364>`__ (`QuLogic <https://github.com/QuLogic>`__)
-  Fix linking to class attributes with prefer_full_module `#1363 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1363>`__ (`QuLogic <https://github.com/QuLogic>`__)
-  Improve minigallery directive path input resolution `#1360 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1360>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  FIX Allow str path minigallery entries when backreferences off `#1355 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1355>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  FIX generate zipfiles when index passed by user `#1353 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1353>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

**Documentation**

-  DOC Improve doc about joblib warnings `#1367 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1367>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC add note on filtering joblib warnings `#1362 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1362>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Minor update to minigallery directive doc `#1358 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1358>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

**Project maintenance**

-  [pre-commit.ci] pre-commit autoupdate `#1368 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1368>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  MNT Change mark and fixture names for adding files `#1365 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1365>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MNT Add warning when ‘examples_dirs’ and ‘gallery_dirs’ unequal lengths `#1361 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1361>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1357 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1357>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  Update pyvista in doc CI `#1352 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1352>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1351 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1351>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  MNT Bump version `#1350 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1350>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

v0.17.0
-------

Support for Python 3.8 and Sphinx 4 dropped in this release.
Requirement is now Python >= 3.9 and Sphinx >= 5.

**Implemented enhancements:**

-  Introduction tooltip corresponds to the first paragraph `#1344 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1344>`__ (`fgmacedo <https://github.com/fgmacedo>`__)
-  FIX Jupyterlite in CircleCI artifact `#1336 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1336>`__ (`lesteve <https://github.com/lesteve>`__)
-  MNT: Rename README.rst to GALLERY_HEADER.rst `#1321 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1321>`__ (`timhoffm <https://github.com/timhoffm>`__)
-  [ENH] Add custom thumbnails for failing examples `#1313 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1313>`__ (`tsbinns <https://github.com/tsbinns>`__)
-  ENH integrate download/launcher links into ``pydata-sphinx-theme`` secondary sidebar `#1312 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1312>`__ (`Charlie-XIAO <https://github.com/Charlie-XIAO>`__)
-  add option for zip downloads `#1299 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1299>`__ (`jamiecook <https://github.com/jamiecook>`__)
-  Allow setting animation format from gallery config `#1243 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1243>`__ (`QuLogic <https://github.com/QuLogic>`__)

**Fixed bugs:**

-  Fix handling of multi-module intersphinx registries `#1320 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1320>`__ (`QuLogic <https://github.com/QuLogic>`__)
-  BUG: Fix bug with traceback with SyntaxError `#1301 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1301>`__ (`larsoner <https://github.com/larsoner>`__)

**Documentation**

-  DOC Add napari to users `#1346 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1346>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Fix nested_sections `#1339 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1339>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Improve ``nested_sections`` `#1326 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1326>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC: Remove definition lists from contribution guide `#1318 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1318>`__ (`QuLogic <https://github.com/QuLogic>`__)
-  MNT: fixed documentation links in the readme `#1310 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1310>`__ (`story645 <https://github.com/story645>`__)

**Project maintenance**

-  [pre-commit.ci] pre-commit autoupdate `#1348 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1348>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  MNT: Fix ``gallery_conf`` changes do not need to be returned `#1347 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1347>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1345 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1345>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1342 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1342>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1338 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1338>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  MNT: Sort imports and add to pre commit `#1337 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1337>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MNT: Refactor ``generate_file_rst`` `#1335 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1335>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MNT: Refactor ``_fill_gallery_conf_defaults`` `#1334 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1334>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MNT Use ``os.sep`` everywhere `#1333 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1333>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MNT: Refactor ``generate_dir_rst`` and ``generate_gallery_rst`` `#1332 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1332>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MNT: Add ipython to dev dependencies `#1329 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1329>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1328 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1328>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  Fix make file clean in tinybuild `#1327 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1327>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Bump the actions group with 5 updates `#1325 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1325>`__ (`dependabot[bot] <https://github.com/apps/dependabot>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1324 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1324>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1319 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1319>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  Include dev dependencies in pyproject.toml and update docs on requirements `#1317 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1317>`__ (`AlexSzatmary <https://github.com/AlexSzatmary>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1314 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1314>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1311 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1311>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1307 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1307>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  MAINT Add ``sphinxcontrib-video`` to dev requirements `#1305 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1305>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1304 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1304>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  MNT: Turn the block tuple into a namedtuple `#1303 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1303>`__ (`timhoffm <https://github.com/timhoffm>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1300 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1300>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  lint: define codespell in ``pyproject.toml`` `#1298 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1298>`__ (`Borda <https://github.com/Borda>`__)
-  MAINT Bump version 0.17 `#1297 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1297>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

v0.16.0
-------
Sphinx 7.3.0 and above changed caching and serialization checks. Now instead of passing
instantiated classes like ``ResetArgv()``, classes like ``FileNameSortKey``, or
callables like ``notebook_modification_function`` in  ``sphinx_gallery_conf``,
you should pass fully qualified name strings to classes or callables. If you change
to using name strings, you can simply use a function as the use of classes to ensure
a stable ``__repr__`` would be redundant.

See :ref:`importing_callables` for details.

**Implemented enhancements:**

-  ENH: Allow plain list as subsection_order and support a wildcard `#1295 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1295>`__ (`timhoffm <https://github.com/timhoffm>`__)
-  [ENH] Minigallery can take arbitrary files/glob patterns as input `#1226 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1226>`__ (`story645 <https://github.com/story645>`__)

**Fixed bugs:**

-  BUG: Fix serialization with Sphinx 7.3 `#1289 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1289>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: minigallery_sort_order on full path `#1253 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1253>`__ (`story645 <https://github.com/story645>`__)
-  BUG: ``UnicodeDecodeError`` in recommender `#1244 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1244>`__ (`Charlie-XIAO <https://github.com/Charlie-XIAO>`__)

**Documentation**

-  DOC Update FFMpeg note in conf animation docs `#1292 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1292>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  readme: adding quickstart section `#1291 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1291>`__ (`Borda <https://github.com/Borda>`__)
-  readme: add link to docs `#1288 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1288>`__ (`Borda <https://github.com/Borda>`__)
-  DOC Clarify sub level example gallery `#1281 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1281>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Mention ``image_srcset`` config in scraper section in ``advanced.rst`` `#1280 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1280>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  BUG: Fix errors in example usage of ignore_repr_types and reset_argv `#1275 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1275>`__ (`speth <https://github.com/speth>`__)
-  DOC Use ‘nested_sections’ ``True`` for docs `#1263 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1263>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  fix: Missing full stop in download message `#1255 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1255>`__ (`AlejandroFernandezLuces <https://github.com/AlejandroFernandezLuces>`__)
-  Add HyperSpy and kikuchipy to ‘who uses’ `#1247 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1247>`__ (`jlaehne <https://github.com/jlaehne>`__)
-  DOC: Fix formatting in contribute.rst `#1237 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1237>`__ (`StefRe <https://github.com/StefRe>`__)

**Project maintenance**

-  [pre-commit.ci] pre-commit autoupdate `#1294 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1294>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  Fix typo in ``test_fileno`` `#1287 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1287>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1284 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1284>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1279 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1279>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  Remove leftover config checking of ``image_srcset`` `#1278 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1278>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1277 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1277>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1273 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1273>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1272 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1272>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  More informative title for ‘check label’ CI workflow `#1271 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1271>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  pyproject: cleaning pytest config `#1269 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1269>`__ (`Borda <https://github.com/Borda>`__)
-  allow call script as pkg entry `#1268 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1268>`__ (`Borda <https://github.com/Borda>`__)
-  refactor: migrate to ``pyproject.toml`` `#1267 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1267>`__ (`Borda <https://github.com/Borda>`__)
-  lint: enable ``sphinx-lint`` for Sphinx extension `#1266 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1266>`__ (`Borda <https://github.com/Borda>`__)
-  ci: associate ``install.sh`` with used job `#1265 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1265>`__ (`Borda <https://github.com/Borda>`__)
-  lint: switch from Black to Ruff’s “Black” `#1264 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1264>`__ (`Borda <https://github.com/Borda>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1260 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1260>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1257 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1257>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1256 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1256>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1252 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1252>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1251 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1251>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1249 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1249>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1248 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1248>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1246 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1246>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1245 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1245>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  Fix AST deprecation warnings `#1242 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1242>`__ (`QuLogic <https://github.com/QuLogic>`__)
-  Simplify Matplotlib scraper `#1241 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1241>`__ (`QuLogic <https://github.com/QuLogic>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1239 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1239>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  MAINT: Fix deployment `#1236 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1236>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT Bump version and update ``maintainers.rst`` `#1234 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1234>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

v0.15.0
-------

Support for Python 3.7 dropped in this release. Requirement is now Python >=3.8.
Pillow added as a dependency.

**Implemented enhancements:**

-  ENH: Improve logging visibility of errors and filenames `#1225 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1225>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: Improve API usage graph `#1203 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1203>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: Always write sg_execution_times and make DataTable `#1198 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1198>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: Write all computation times `#1197 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1197>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: Support source files in any language `#1192 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1192>`__ (`speth <https://github.com/speth>`__)
-  FEA Add examples recommender system `#1125 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1125>`__ (`ArturoAmorQ <https://github.com/ArturoAmorQ>`__)

**Fixed bugs:**

-  FIX Copy JupyterLite contents early so it runs before jupyterlite_sphinx build-finished `#1213 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1213>`__ (`lesteve <https://github.com/lesteve>`__)
-  BUG: Fix bug with orphan sg_api_usage `#1207 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1207>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT Fix check for mismatched “ignore” blocks `#1193 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1193>`__ (`speth <https://github.com/speth>`__)
-  Avoid importing new modules in backrefs `#1177 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1177>`__ (`aganders3 <https://github.com/aganders3>`__)

**Documentation**

-  DOC Put configuration list under headings `#1230 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1230>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC: contributing guide `#1223 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1223>`__ (`story645 <https://github.com/story645>`__)
-  DOC Note support for python 3.7 dropped in release notes `#1199 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1199>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

**Project maintenance**

-  [pre-commit.ci] pre-commit autoupdate `#1231 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1231>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  MAINT Add ``extras_require`` in ``setup.py`` `#1229 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1229>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1227 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1227>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1224 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1224>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1219 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1219>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  MAINT: pydata-sphinx-theme `#1218 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1218>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Improve CircleCI time `#1216 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1216>`__ (`larsoner <https://github.com/larsoner>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1215 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1215>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  MAINT: Move to GHA `#1214 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1214>`__ (`larsoner <https://github.com/larsoner>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1206 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1206>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1201 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1201>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1196 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1196>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1194 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1194>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1191 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1191>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1189 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1189>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1187 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1187>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  MAINT: Bump ver `#1185 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1185>`__ (`larsoner <https://github.com/larsoner>`__)

v0.14.0
-------

**Implemented enhancements:**

-  MAINT Update backreferences docs and add tests `#1154 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1154>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Remove extra spaces in reported running time `#1147 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1147>`__ (`stefanv <https://github.com/stefanv>`__)

**Fixed bugs:**

-  MAINT: Fix for Sphinx 7.2 `#1176 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1176>`__ (`larsoner <https://github.com/larsoner>`__)
-  updated mpl gui warning catcher to new error message `#1160 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1160>`__ (`story645 <https://github.com/story645>`__)
-  Ensure consistent encoding for md5sum generation `#1159 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1159>`__ (`sdhiscocks <https://github.com/sdhiscocks>`__)
-  Maint: Fix ``app.builder.outdir`` as Sphinx now using pathlib `#1155 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1155>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Make \_LoggingTee compatible with TextIO `#1151 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1151>`__ (`o-laurent <https://github.com/o-laurent>`__)
-  MAINT: Replace build_sphinx with sphinx-build `#1139 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1139>`__ (`oscargus <https://github.com/oscargus>`__)
-  Set table.dataframe width to auto in CSS file close #1128 `#1137 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1137>`__ (`photoniker <https://github.com/photoniker>`__)

**Documentation**

-  DOC Fix typo in ``_get_docstring_and_rest`` docstring `#1182 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1182>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Fix Jupyterlite config example in ``configuration.rst`` `#1181 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1181>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Update basics gallery name `#1153 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1153>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC: Add link to sphinxcontrib-svg2pdfconverter `#1145 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1145>`__ (`oscargus <https://github.com/oscargus>`__)
-  MNT: Add a few badges `#1143 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1143>`__ (`oscargus <https://github.com/oscargus>`__)
-  MAINT: Fix Zenodo reference `#1140 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1140>`__ (`oscargus <https://github.com/oscargus>`__)
-  Add OpenTURNS to “who uses” list `#1133 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1133>`__ (`jschueller <https://github.com/jschueller>`__)
-  Correctly hide download buttons `#1131 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1131>`__ (`timhoffm <https://github.com/timhoffm>`__)

**Project maintenance**

-  MAINT: Force PRs to be labeled properly `#1183 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1183>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT Add to ``test_identify_names`` so class property tested `#1180 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1180>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MAINT Lint - fix ast node type in docstrings `#1179 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1179>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MAINT Move ``figure_rst`` path testing to own unit test `#1173 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1173>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MAINT Remove unused parametrize in ``test_figure_rst_srcset`` `#1172 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1172>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MAINT Parametrize notebook first/last cell test `#1171 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1171>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MAINT Lint api usage `#1170 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1170>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MAINT Fix lint, clean and expand docstrings `#1169 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1169>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [pre-commit.ci] pre-commit autoupdate `#1167 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1167>`__ (`pre-commit-ci[bot] <https://github.com/apps/pre-commit-ci>`__)
-  MAINT: yamllint `#1166 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1166>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: Use pre-commit `#1165 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1165>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: black . `#1164 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1164>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Make outdated check better `#1161 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1161>`__ (`larsoner <https://github.com/larsoner>`__)
-  Use pathlib for url ``_embed_code_links`` `#1157 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1157>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MAINT: Speed up conda solving `#1156 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1156>`__ (`larsoner <https://github.com/larsoner>`__)
-  MNT: Change % formatting to f-strings `#1135 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1135>`__ (`StefRe <https://github.com/StefRe>`__)
-  MAINT: Update deps and intersphinx links `#1132 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1132>`__ (`larsoner <https://github.com/larsoner>`__)

v0.13.0
-------

**Implemented enhancements:**

-  ENH: Create backreferences for default roles `#1122 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1122>`__ (`StefRe <https://github.com/StefRe>`__)
-  ENH raise error in check_jupyterlite_conf with unknown key `#1119 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1119>`__ (`lesteve <https://github.com/lesteve>`__)
-  ENH Add functionality to modify Jupyterlite notebooks based on their content `#1113 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1113>`__ (`lesteve <https://github.com/lesteve>`__)
-  ENH: Add support for WebP `#1111 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1111>`__ (`StefRe <https://github.com/StefRe>`__)

**Fixed bugs:**

-  ENH Clean-up code by early initialization of sphinx_gallery_conf `#1120 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1120>`__ (`lesteve <https://github.com/lesteve>`__)
-  FIX JupyterLite button links `#1115 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1115>`__ (`lesteve <https://github.com/lesteve>`__)
-  Fix thumbnail text formatting `#1108 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1108>`__ (`StefRe <https://github.com/StefRe>`__)
-  Fix JupyterLite URL with nested gallery folders `#1105 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1105>`__ (`lesteve <https://github.com/lesteve>`__)
-  Avoid potentially changing the matplotlib backend when scraping `#1102 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1102>`__ (`ayshih <https://github.com/ayshih>`__)
-  Remove default ‘%matplotlib inline’ line `#1099 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1099>`__ (`ArturoAmorQ <https://github.com/ArturoAmorQ>`__)
-  FIX: Only ANSI sanitize non-HTML output `#1097 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1097>`__ (`sdhiscocks <https://github.com/sdhiscocks>`__)
-  BUG: Fix bug with show_api_usage `#1095 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1095>`__ (`larsoner <https://github.com/larsoner>`__)
-  FIX: Add blank line at end of table of contents block `#1094 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1094>`__ (`sdhiscocks <https://github.com/sdhiscocks>`__)

**API changes**

-  API: Remove deprecated mayavi support `#1090 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1090>`__ (`larsoner <https://github.com/larsoner>`__)

**Documentation**

-  Add reference to qtgallery (Qt scraper) `#1126 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1126>`__ (`aganders3 <https://github.com/aganders3>`__)
-  DOC: Unify abbreviations of reStructuredText `#1118 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1118>`__ (`StefRe <https://github.com/StefRe>`__)
-  Add PyGMT to list “Who uses Sphinx-Gallery” `#1114 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1114>`__ (`yvonnefroehlich <https://github.com/yvonnefroehlich>`__)
-  DOC Update JupyterLite doc after JupyterLite 0.1.0b19 release `#1106 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1106>`__ (`lesteve <https://github.com/lesteve>`__)
-  Fix project list `#1101 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1101>`__ (`StefRe <https://github.com/StefRe>`__)
-  DOC: Document changes `#1098 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1098>`__ (`larsoner <https://github.com/larsoner>`__)
-  DOC: Document point release changes `#1096 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1096>`__ (`larsoner <https://github.com/larsoner>`__)

**Project maintenance**

-  MAINT: Use non-aliased status_iterator `#1124 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1124>`__ (`larsoner <https://github.com/larsoner>`__)
-  CLN Clean up naming of early config validation `#1123 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1123>`__ (`lesteve <https://github.com/lesteve>`__)
-  MNT: Remove Python 2 leftovers `#1116 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1116>`__ (`StefRe <https://github.com/StefRe>`__)
-  MNT: Sync minimum sphinx version with README.rst `#1110 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1110>`__ (`StefRe <https://github.com/StefRe>`__)
-  CI Install jupyterlite-pyodide-kernel in CI `#1107 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1107>`__ (`lesteve <https://github.com/lesteve>`__)
-  Add test for setting a non-agg Matplotlib backend `#1104 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1104>`__ (`ayshih <https://github.com/ayshih>`__)
-  MAINT: Bump version to dev `#1089 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1089>`__ (`larsoner <https://github.com/larsoner>`__)

v0.12.2
-------

**Fixed bugs:**

-  FIX: Only ANSI sanitize non-HTML output `#1097 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1097>`__ (`sdhiscocks <https://github.com/sdhiscocks>`__)

v0.12.1
-------

**Fixed bugs:**

-  BUG: Fix bug with show_api_usage `#1095 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1095>`__ (`larsoner <https://github.com/larsoner>`__)
-  FIX: Add blank line at end of table of contents block `#1094 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1094>`__ (`sdhiscocks <https://github.com/sdhiscocks>`__)

v0.12.0
-------
Support for Sphinx < 4 dropped in this release. Requirement is Sphinx >= 4.

**Implemented enhancements:**

-  ENH: allow rst files to pass through `#1071 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1071>`__ (`jklymak <https://github.com/jklymak>`__)
-  Update advanced usage examples `#1045 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1045>`__ (`HealthyPear <https://github.com/HealthyPear>`__)
-  Use descriptive link text for example page header `#1040 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1040>`__ (`betatim <https://github.com/betatim>`__)
-  Expose ``sphinx_gallery_conf`` in ``python_to_jupyter_cli`` `#1027 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1027>`__ (`OverLordGoldDragon <https://github.com/OverLordGoldDragon>`__)
-  DOC: fix ‘Who uses Sphinx-Gallery’ list `#1015 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1015>`__ (`StefRe <https://github.com/StefRe>`__)
-  [MAINT, MRG] A few small leftovers from API usage `#997 <https://github.com/sphinx-gallery/sphinx-gallery/pull/997>`__ (`alexrockhill <https://github.com/alexrockhill>`__)
-  [ENH, MRG] Make orphan of unused API entries `#983 <https://github.com/sphinx-gallery/sphinx-gallery/pull/983>`__ (`alexrockhill <https://github.com/alexrockhill>`__)
-  Jupyterlite integration `#977 <https://github.com/sphinx-gallery/sphinx-gallery/pull/977>`__ (`amueller <https://github.com/amueller>`__)

**Fixed bugs:**

-  MNT: fix subfolder README detection `#1086 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1086>`__ (`jklymak <https://github.com/jklymak>`__)
-  API: Deprecate mayavi scraper `#1083 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1083>`__ (`larsoner <https://github.com/larsoner>`__)
-  FIX: indentation fix `#1077 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1077>`__ (`jklymak <https://github.com/jklymak>`__)
-  Adds ``plot_gallery`` as a string by default `#1062 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1062>`__ (`melissawm <https://github.com/melissawm>`__)
-  Fix broken links when using dirhtml builder `#1060 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1060>`__ (`mgoulao <https://github.com/mgoulao>`__)
-  BUG: Remove ignore blocks when remove_config_comments=True `#1059 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1059>`__ (`guberti <https://github.com/guberti>`__)
-  Fixed a bug where backslashes in paths could show up in reST files `#1047 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1047>`__ (`ayshih <https://github.com/ayshih>`__)
-  Allow 2 decimal places in srcset `#1039 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1039>`__ (`OverLordGoldDragon <https://github.com/OverLordGoldDragon>`__)
-  Fix “``subsection_index_toctree`` referenced before assignment” `#1035 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1035>`__ (`OverLordGoldDragon <https://github.com/OverLordGoldDragon>`__)
-  [BUG, MRG] fix issue with api usage dict `#1033 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1033>`__ (`alexrockhill <https://github.com/alexrockhill>`__)
-  MAINT: Remove lingering ref `#1022 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1022>`__ (`larsoner <https://github.com/larsoner>`__)
-  MNT: Fix erroneous commit c6ed4e `#1021 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1021>`__ (`StefRe <https://github.com/StefRe>`__)
-  MNT: make “clean” behave the same on Windows as on Linux `#1020 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1020>`__ (`StefRe <https://github.com/StefRe>`__)
-  DOC Fix typo in scraper doc `#1018 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1018>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Fix outdated import `#1016 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1016>`__ (`OverLordGoldDragon <https://github.com/OverLordGoldDragon>`__)
-  FIX: role names `#1012 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1012>`__ (`StefRe <https://github.com/StefRe>`__)
-  Bugfix thumbnail text formatting `#1005 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1005>`__ (`alexisthual <https://github.com/alexisthual>`__)
-  [MAINT, MRG] Add unused option for API usage, set as default `#1001 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1001>`__ (`alexrockhill <https://github.com/alexrockhill>`__)
-  FIX: No orphan `#1000 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1000>`__ (`larsoner <https://github.com/larsoner>`__)
-  BUG: Short circuit when disabled `#999 <https://github.com/sphinx-gallery/sphinx-gallery/pull/999>`__ (`larsoner <https://github.com/larsoner>`__)

**Documentation**

-  DOC: Add note for html-noplot to suppress config warning. `#1084 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1084>`__ (`rossbar <https://github.com/rossbar>`__)
-  Reorder paragraphs in the minigallery documentation `#1048 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1048>`__ (`ayshih <https://github.com/ayshih>`__)
-  DOC: Switch to pydata-sphinx-theme `#1013 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1013>`__ (`larsoner <https://github.com/larsoner>`__)
-  Fix sphinx link typo in CHANGES `#996 <https://github.com/sphinx-gallery/sphinx-gallery/pull/996>`__ (`alexisthual <https://github.com/alexisthual>`__)

**Project maintenance**

-  MAINT: Fix CIs `#1074 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1074>`__ (`larsoner <https://github.com/larsoner>`__)
-  TST: gallery inventory/re-structure tinybuild `#1072 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1072>`__ (`jklymak <https://github.com/jklymak>`__)
-  MAINT: Rotate CircleCI key `#1064 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1064>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Update CIs `#1061 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1061>`__ (`larsoner <https://github.com/larsoner>`__)
-  BUG: Fix full check `#1053 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1053>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Work around IPython lexer bug `#1052 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1052>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Fix CIs `#1046 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1046>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Check CI status `#1028 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1028>`__ (`larsoner <https://github.com/larsoner>`__)
-  MNT: Fix required sphinx version `#1019 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1019>`__ (`StefRe <https://github.com/StefRe>`__)
-  BUG: Update for matplotlib `#1010 <https://github.com/sphinx-gallery/sphinx-gallery/pull/1010>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Bump to dev `#995 <https://github.com/sphinx-gallery/sphinx-gallery/pull/995>`__ (`larsoner <https://github.com/larsoner>`__)


v0.11.1
-------

Support for Sphinx < 3 dropped in this release. Requirement is Sphinx >= 3.

**Fixed bugs:**

-  BUG: Fix single column example `#993 <https://github.com/sphinx-gallery/sphinx-gallery/pull/993>`__ (`larsoner <https://github.com/larsoner>`__)

**Implemented enhancements:**

- Use Mock more in tests `#986 <https://github.com/sphinx-gallery/sphinx-gallery/pull/986>`__ (`QuLogic <https://github.com/QuLogic>`__)
- Remove old sphinx compatibility code `#985 <https://github.com/sphinx-gallery/sphinx-gallery/pull/985>`__ (`QuLogic <https://github.com/QuLogic>`__)


v0.11.0
-------

In this version, the "Out:" prefix applied to code outputs is now created from
CSS pseudo-elements instead of additional real text. For more details, see
`#896 <https://github.com/sphinx-gallery/sphinx-gallery/pull/896>`__.

**Implemented enhancements:**

Nesting gallery sections (i.e. gallery subfolders) was implemented in `#904 <https://github.com/sphinx-gallery/sphinx-gallery/pull/904>`__. This feature can be disabled (see config option ``nested_sections`` in the documentation) if the previous behaviour is prefered (`alexisthual <https://github.com/alexisthual>`__)

Tooltips now overlay gallery items `commit 36166cd <https://github.com/sphinx-gallery/sphinx-gallery/pull/944/commits/36166cd2fc2b43ecbd585654cfe8745f3a1b3f64>`__. Custom CSS might need to be adapted (`alexisthual <https://github.com/alexisthual>`__).

-  Problem in section and example title level in subgalleries `#935 <https://github.com/sphinx-gallery/sphinx-gallery/issues/935>`__
-  Add ability to write nested ``index.rst`` `#855 <https://github.com/sphinx-gallery/sphinx-gallery/issues/855>`__
-  Optional usage of ``module`` instead of ``module_short`` when doing backreferencing `#950 <https://github.com/sphinx-gallery/sphinx-gallery/pull/950>`__ (`ExtremOPS <https://github.com/ExtremOPS>`__)
-  ENH: Better dark mode support `#948 <https://github.com/sphinx-gallery/sphinx-gallery/pull/948>`__ (`larsoner <https://github.com/larsoner>`__)
-  Store API reference examples thumbnails in common div `#946 <https://github.com/sphinx-gallery/sphinx-gallery/pull/946>`__ (`alexisthual <https://github.com/alexisthual>`__)
-  Add flag to ignore code blocks in Python source parser `#941 <https://github.com/sphinx-gallery/sphinx-gallery/pull/941>`__ (`guberti <https://github.com/guberti>`__)
-  Improve Jupyter notebook converter’s handling of code blocks `#940 <https://github.com/sphinx-gallery/sphinx-gallery/pull/940>`__ (`guberti <https://github.com/guberti>`__)
-  [MRG] Changelog regarding nested sections `#926 <https://github.com/sphinx-gallery/sphinx-gallery/pull/926>`__ (`alexisthual <https://github.com/alexisthual>`__)
-  Possibility to exclude implicit backreferences `#908 <https://github.com/sphinx-gallery/sphinx-gallery/pull/908>`__ (`StefRe <https://github.com/StefRe>`__)
-  [MRG] Handle nested structures `#904 <https://github.com/sphinx-gallery/sphinx-gallery/pull/904>`__ (`alexisthual <https://github.com/alexisthual>`__)
-  Use pseudo-elements for ‘Out:’ prefixing `#896 <https://github.com/sphinx-gallery/sphinx-gallery/pull/896>`__ (`QuLogic <https://github.com/QuLogic>`__)
-  FIX: Fix for latest pytest `#894 <https://github.com/sphinx-gallery/sphinx-gallery/pull/894>`__ (`larsoner <https://github.com/larsoner>`__)
-  Config capture_repr on file-by-file basis `#891 <https://github.com/sphinx-gallery/sphinx-gallery/pull/891>`__ (`StefRe <https://github.com/StefRe>`__)

**Fixed bugs:**

We now display gallery items using CSS grid instead of  ``float`` property `#906 <https://github.com/sphinx-gallery/sphinx-gallery/pull/906>`__, see `migration guide <https://github.com/sphinx-gallery/sphinx-gallery/pull/906#issuecomment-1019542067>`__ to adapt custom CSS for thumbnails (`alexisthual <https://github.com/alexisthual>`__)

-  BUG: Hotfix for docopts_url `#980 <https://github.com/sphinx-gallery/sphinx-gallery/pull/980>`__ (`larsoner <https://github.com/larsoner>`__)
-  BUG: Fix bug with clicking examples `#973 <https://github.com/sphinx-gallery/sphinx-gallery/pull/973>`__ (`larsoner <https://github.com/larsoner>`__)
-  Remove test examples for seaborn warning `#971 <https://github.com/sphinx-gallery/sphinx-gallery/pull/971>`__ (`lesteve <https://github.com/lesteve>`__)
-  Fix typo `#970 <https://github.com/sphinx-gallery/sphinx-gallery/pull/970>`__ (`tkoyama010 <https://github.com/tkoyama010>`__)
-  Avoid matplotlib warnings in seaborn reset_module `#969 <https://github.com/sphinx-gallery/sphinx-gallery/pull/969>`__ (`lesteve <https://github.com/lesteve>`__)
-  Fix Tensorflow/Abseil compatibility `#961 <https://github.com/sphinx-gallery/sphinx-gallery/pull/961>`__ (`guberti <https://github.com/guberti>`__)
-  syntax error fix in sphinx_gallery.downloads `#951 <https://github.com/sphinx-gallery/sphinx-gallery/pull/951>`__ (`photoniker <https://github.com/photoniker>`__)
-  Merge toctrees containing subcategories indices and examples without … `#944 <https://github.com/sphinx-gallery/sphinx-gallery/pull/944>`__ (`alexisthual <https://github.com/alexisthual>`__)
-  Fix rendering of embedded URIs in Python notebooks `#943 <https://github.com/sphinx-gallery/sphinx-gallery/pull/943>`__ (`guberti <https://github.com/guberti>`__)
-  FIX: Fix for dep `#938 <https://github.com/sphinx-gallery/sphinx-gallery/pull/938>`__ (`larsoner <https://github.com/larsoner>`__)
-  Fix typos `#934 <https://github.com/sphinx-gallery/sphinx-gallery/pull/934>`__ (`kianmeng <https://github.com/kianmeng>`__)
-  MAINT: Fix CIs `#932 <https://github.com/sphinx-gallery/sphinx-gallery/pull/932>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Use -nWT –keep-going on Azure `#924 <https://github.com/sphinx-gallery/sphinx-gallery/pull/924>`__ (`larsoner <https://github.com/larsoner>`__)
-  Ensures right builder conifg `#922 <https://github.com/sphinx-gallery/sphinx-gallery/pull/922>`__ (`ExtremOPS <https://github.com/ExtremOPS>`__)
-  MAINT: Fix CIs `#920 <https://github.com/sphinx-gallery/sphinx-gallery/pull/920>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Clean up namespace `#917 <https://github.com/sphinx-gallery/sphinx-gallery/pull/917>`__ (`larsoner <https://github.com/larsoner>`__)
-  FIX: Azure `#915 <https://github.com/sphinx-gallery/sphinx-gallery/pull/915>`__ (`larsoner <https://github.com/larsoner>`__)
-  [WIP] Bugfix missing parent div for mini gallery `#914 <https://github.com/sphinx-gallery/sphinx-gallery/pull/914>`__ (`alexisthual <https://github.com/alexisthual>`__)
-  Honor show_signature `#909 <https://github.com/sphinx-gallery/sphinx-gallery/pull/909>`__ (`jschueller <https://github.com/jschueller>`__)
-  Css grid for thumbnails `#906 <https://github.com/sphinx-gallery/sphinx-gallery/pull/906>`__ (`alexisthual <https://github.com/alexisthual>`__)
-  Fix matplotlib intersphinx url `#902 <https://github.com/sphinx-gallery/sphinx-gallery/pull/902>`__ (`StefRe <https://github.com/StefRe>`__)
-  FIX: Pin pyvista `#901 <https://github.com/sphinx-gallery/sphinx-gallery/pull/901>`__ (`larsoner <https://github.com/larsoner>`__)
-  Fix matplotlib resetter \_reset_matplotlib `#890 <https://github.com/sphinx-gallery/sphinx-gallery/pull/890>`__ (`StefRe <https://github.com/StefRe>`__)
-  Fix “Out” layout for pydata-sphinx-theme `#886 <https://github.com/sphinx-gallery/sphinx-gallery/pull/886>`__ (`timhoffm <https://github.com/timhoffm>`__)

**Documentation updates**

-  added RADIS in Who uses Sphinx-gallery ? `#979 <https://github.com/sphinx-gallery/sphinx-gallery/pull/979>`__ (`erwanp <https://github.com/erwanp>`__)
-  add Tonic to list of sphinx-gallery users `#972 <https://github.com/sphinx-gallery/sphinx-gallery/pull/972>`__ (`biphasic <https://github.com/biphasic>`__)
-  Add Apache TVM to user projects list `#942 <https://github.com/sphinx-gallery/sphinx-gallery/pull/942>`__ (`guberti <https://github.com/guberti>`__)
-  DOC: fix rst link syntax in changelog `#925 <https://github.com/sphinx-gallery/sphinx-gallery/pull/925>`__ (`GaelVaroquaux <https://github.com/GaelVaroquaux>`__)
-  add GitHub URL for PyPi `#923 <https://github.com/sphinx-gallery/sphinx-gallery/pull/923>`__ (`andriyor <https://github.com/andriyor>`__)
-  Add Biotite to list of user projects `#919 <https://github.com/sphinx-gallery/sphinx-gallery/pull/919>`__ (`padix-key <https://github.com/padix-key>`__)
-  MAINT: Remove LooseVersion `#916 <https://github.com/sphinx-gallery/sphinx-gallery/pull/916>`__ (`larsoner <https://github.com/larsoner>`__)
-  DOC Fix example “Identifying function names in a script” `#903 <https://github.com/sphinx-gallery/sphinx-gallery/pull/903>`__ (`StefRe <https://github.com/StefRe>`__)
-  DOC Update docs for Adding mini-galleries for API documentation `#899 <https://github.com/sphinx-gallery/sphinx-gallery/pull/899>`__ (`StefRe <https://github.com/StefRe>`__)
-  Add PyVista examples! `#888 <https://github.com/sphinx-gallery/sphinx-gallery/pull/888>`__ (`banesullivan <https://github.com/banesullivan>`__)
-  Fix a few links in project lists `#883 <https://github.com/sphinx-gallery/sphinx-gallery/pull/883>`__ (`ixjlyons <https://github.com/ixjlyons>`__)


v0.10.1
-------

Support for Python 3.6 dropped in this release. Requirement is Python >=3.7.

**Implemented enhancements:**

-  Feature Request: ``reset_modules`` to be applied after each or all examples `#866 <https://github.com/sphinx-gallery/sphinx-gallery/issues/866>`__
-  Enable ``reset_modules`` to run either before or after examples, or both `#870 <https://github.com/sphinx-gallery/sphinx-gallery/pull/870>`__ (`MatthewFlamm <https://github.com/MatthewFlamm>`__)

**Fixed bugs:**

-  embed_code_links throwing <exception: list indices must be integers or slices, not str> `#879 <https://github.com/sphinx-gallery/sphinx-gallery/issues/879>`__
-  ``0.10.0`` breaks ``sphinx_gallery.load_style`` `#878 <https://github.com/sphinx-gallery/sphinx-gallery/issues/878>`__
-  Add imagesg directive in load style `#880 <https://github.com/sphinx-gallery/sphinx-gallery/pull/880>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Use bools for ‘plot_gallery’ in sphinx_gallery_conf `#863 <https://github.com/sphinx-gallery/sphinx-gallery/pull/863>`__ (`timhoffm <https://github.com/timhoffm>`__)

**Merged pull requests:**

-  DOC Add reference to sphinx-codeautolink `#874 <https://github.com/sphinx-gallery/sphinx-gallery/pull/874>`__ (`felix-hilden <https://github.com/felix-hilden>`__)
-  Add Neuraxle to “Who uses Sphinx-Gallery” `#873 <https://github.com/sphinx-gallery/sphinx-gallery/pull/873>`__ (`guillaume-chevalier <https://github.com/guillaume-chevalier>`__)
-  DOC Fix typo in dummy images doc `#871 <https://github.com/sphinx-gallery/sphinx-gallery/pull/871>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  CI: Fix CircleCI `#865 <https://github.com/sphinx-gallery/sphinx-gallery/pull/865>`__ (`larsoner <https://github.com/larsoner>`__)

v0.10.0
-------

In this version, the default Sphinx-Gallery `.css` files have been
updated so their names are all prepended with 'sg\_'.
For more details see `#845 <https://github.com/sphinx-gallery/sphinx-gallery/pull/845#issuecomment-913130302>`_.

**Implemented enhancements:**

-  Generalising image_scrapers facility for non-images `#833 <https://github.com/sphinx-gallery/sphinx-gallery/issues/833>`__
-  Add a mode that fails only for rst warnings and does not run examples `#751 <https://github.com/sphinx-gallery/sphinx-gallery/issues/751>`__
-  Add a “template”, to make it easy to get started `#555 <https://github.com/sphinx-gallery/sphinx-gallery/issues/555>`__
-  ENH Add config that generates dummy images to prevent missing image warnings `#828 <https://github.com/sphinx-gallery/sphinx-gallery/pull/828>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  ENH: add hidpi option to matplotlib_scraper and directive `#808 <https://github.com/sphinx-gallery/sphinx-gallery/pull/808>`__ (`jklymak <https://github.com/jklymak>`__)

**Fixed bugs:**

-  BUG URL quote branch names and filepaths in Binder URLs `#844 <https://github.com/sphinx-gallery/sphinx-gallery/pull/844>`__ (`sdhiscocks <https://github.com/sdhiscocks>`__)
-  Sanitize ANSI characters from generated reST: Remove `ANSI characters <https://en.wikipedia.org/wiki/ANSI_escape_code>`_ from HTML output `#838 <https://github.com/sphinx-gallery/sphinx-gallery/pull/838>`__ (`agramfort <https://github.com/agramfort>`__)
-  Bug Pin markupsafe version in Python nightly `#831 <https://github.com/sphinx-gallery/sphinx-gallery/pull/831>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  BUG Fix test_minigallery_directive failing on Windows `#830 <https://github.com/sphinx-gallery/sphinx-gallery/pull/830>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  BUG Fix LaTeX Error: File \`tgtermes.sty’ not found in CI `#829 <https://github.com/sphinx-gallery/sphinx-gallery/pull/829>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

**Merged pull requests:**

-  DOC Update reset_modules documentation `#861 <https://github.com/sphinx-gallery/sphinx-gallery/pull/861>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Remove trailing whitespace `#859 <https://github.com/sphinx-gallery/sphinx-gallery/pull/859>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Add info on enabling animation support to example `#858 <https://github.com/sphinx-gallery/sphinx-gallery/pull/858>`__ (`dstansby <https://github.com/dstansby>`__)
-  Update css file names, fix documentation `#857 <https://github.com/sphinx-gallery/sphinx-gallery/pull/857>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MAINT: Fix mayavi build hang circleci `#850 <https://github.com/sphinx-gallery/sphinx-gallery/pull/850>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  MAINT: Fix mayavi build hang azure CI `#848 <https://github.com/sphinx-gallery/sphinx-gallery/pull/848>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Refactor execute_code_block in gen_rst.py `#842 <https://github.com/sphinx-gallery/sphinx-gallery/pull/842>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  [Maint] Remove travis `#840 <https://github.com/sphinx-gallery/sphinx-gallery/pull/840>`__ (`agramfort <https://github.com/agramfort>`__)
-  DOC Add gif to supported image extensions `#836 <https://github.com/sphinx-gallery/sphinx-gallery/pull/836>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Clarifications and fixes to image_scrapers doc `#834 <https://github.com/sphinx-gallery/sphinx-gallery/pull/834>`__ (`jnothman <https://github.com/jnothman>`__)
-  DOC Update projects list in readme.rst `#826 <https://github.com/sphinx-gallery/sphinx-gallery/pull/826>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Fix zenodo badge link `#825 <https://github.com/sphinx-gallery/sphinx-gallery/pull/825>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Add TorchIO to users list `#824 <https://github.com/sphinx-gallery/sphinx-gallery/pull/824>`__ (`fepegar <https://github.com/fepegar>`__)

v0.9.0
------

Support for Python 3.5 dropped in this release. Requirement is Python >=3.6.

**Implemented enhancements:**

-  Add a mode which “skips” an example if it fails `#789 <https://github.com/sphinx-gallery/sphinx-gallery/issues/789>`__
-  Can sphinx_gallery_thumbnail_number support negative indexes? `#785 <https://github.com/sphinx-gallery/sphinx-gallery/issues/785>`__
-  Configure thumbnail style `#780 <https://github.com/sphinx-gallery/sphinx-gallery/issues/780>`__
-  ENH: Check for invalid sphinx_gallery_conf keys `#774 <https://github.com/sphinx-gallery/sphinx-gallery/issues/774>`__
-  DOC Document how to hide download link note `#760 <https://github.com/sphinx-gallery/sphinx-gallery/issues/760>`__
-  DOC use intersphinx references in projects_list.rst `#755 <https://github.com/sphinx-gallery/sphinx-gallery/issues/755>`__
-  Delay output capturing to a further code block `#363 <https://github.com/sphinx-gallery/sphinx-gallery/issues/363>`__
-  ENH: Only add minigallery if there’s something to show `#813 <https://github.com/sphinx-gallery/sphinx-gallery/pull/813>`__ (`NicolasHug <https://github.com/NicolasHug>`__)
-  Optional flag to defer figure scraping to the next code block `#801 <https://github.com/sphinx-gallery/sphinx-gallery/pull/801>`__ (`ayshih <https://github.com/ayshih>`__)
-  ENH: PyQt5 `#794 <https://github.com/sphinx-gallery/sphinx-gallery/pull/794>`__ (`larsoner <https://github.com/larsoner>`__)
-  Add a configuration to warn on error not fail `#792 <https://github.com/sphinx-gallery/sphinx-gallery/pull/792>`__ (`Cadair <https://github.com/Cadair>`__)
-  Let sphinx_gallery_thumbnail_number support negative indexes `#786 <https://github.com/sphinx-gallery/sphinx-gallery/pull/786>`__ (`seisman <https://github.com/seisman>`__)
-  Make any borders introduced when rescaling images to thumbnails transparent `#781 <https://github.com/sphinx-gallery/sphinx-gallery/pull/781>`__ (`rossbar <https://github.com/rossbar>`__)
-  MAINT: Move travis CI jobs to Azure `#779 <https://github.com/sphinx-gallery/sphinx-gallery/pull/779>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  ENH, DEP: Check for invalid keys, remove ancient key `#775 <https://github.com/sphinx-gallery/sphinx-gallery/pull/775>`__ (`larsoner <https://github.com/larsoner>`__)

**Fixed bugs:**

-  Custom CSS for space above title target conflicts with pydata-sphinx-theme `#815 <https://github.com/sphinx-gallery/sphinx-gallery/issues/815>`__
-  Minigalleries are generated even for objects without examples `#812 <https://github.com/sphinx-gallery/sphinx-gallery/issues/812>`__
-  Python nightly failing due to Jinja2 import from collections.abc `#790 <https://github.com/sphinx-gallery/sphinx-gallery/issues/790>`__
-  test_rebuild and test_error_messages failing on travis `#777 <https://github.com/sphinx-gallery/sphinx-gallery/issues/777>`__
-  Animation not show on Read the Docs `#772 <https://github.com/sphinx-gallery/sphinx-gallery/issues/772>`__
-  BUG: Empty code block output `#765 <https://github.com/sphinx-gallery/sphinx-gallery/issues/765>`__
-  BUG: Fix CSS selector `#816 <https://github.com/sphinx-gallery/sphinx-gallery/pull/816>`__ (`larsoner <https://github.com/larsoner>`__)
-  MAINT: Fix test for links `#811 <https://github.com/sphinx-gallery/sphinx-gallery/pull/811>`__ (`larsoner <https://github.com/larsoner>`__)
-  Fix SVG default thumbnail support `#810 <https://github.com/sphinx-gallery/sphinx-gallery/pull/810>`__ (`jacobolofsson <https://github.com/jacobolofsson>`__)
-  Clarify clean docs for custom gallery_dirs `#798 <https://github.com/sphinx-gallery/sphinx-gallery/pull/798>`__ (`timhoffm <https://github.com/timhoffm>`__)
-  MAINT Specify Jinja2 version in azure Python nightly `#793 <https://github.com/sphinx-gallery/sphinx-gallery/pull/793>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  BUG Remove if final block empty `#791 <https://github.com/sphinx-gallery/sphinx-gallery/pull/791>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Replace Travis CI badge with Azure Badge in README `#783 <https://github.com/sphinx-gallery/sphinx-gallery/pull/783>`__ (`sdhiscocks <https://github.com/sdhiscocks>`__)
-  Point to up-to-date re documentation `#778 <https://github.com/sphinx-gallery/sphinx-gallery/pull/778>`__ (`dstansby <https://github.com/dstansby>`__)

**Merged pull requests:**

-  DOC Add section on altering CSS `#820 <https://github.com/sphinx-gallery/sphinx-gallery/pull/820>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Use intersphinx references in projects_list.rst `#819 <https://github.com/sphinx-gallery/sphinx-gallery/pull/819>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Update CI badge `#818 <https://github.com/sphinx-gallery/sphinx-gallery/pull/818>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Include SOURCEDIR in Makefile `#814 <https://github.com/sphinx-gallery/sphinx-gallery/pull/814>`__ (`NicolasHug <https://github.com/NicolasHug>`__)
-  DOC: add 2 projects using sphinx gallery `#807 <https://github.com/sphinx-gallery/sphinx-gallery/pull/807>`__ (`mfeurer <https://github.com/mfeurer>`__)
-  DOC: clarify advanced doc wrt referencing examples `#806 <https://github.com/sphinx-gallery/sphinx-gallery/pull/806>`__ (`mfeurer <https://github.com/mfeurer>`__)
-  MAINT: Add link `#800 <https://github.com/sphinx-gallery/sphinx-gallery/pull/800>`__ (`larsoner <https://github.com/larsoner>`__)
-  Add Optuna to “Who uses Optuna” `#796 <https://github.com/sphinx-gallery/sphinx-gallery/pull/796>`__ (`crcrpar <https://github.com/crcrpar>`__)
-  DOC Add segment on CSS styling `#788 <https://github.com/sphinx-gallery/sphinx-gallery/pull/788>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC minor doc typo fixes `#787 <https://github.com/sphinx-gallery/sphinx-gallery/pull/787>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC Update CI links in index.rst `#784 <https://github.com/sphinx-gallery/sphinx-gallery/pull/784>`__ (`lucyleeow <https://github.com/lucyleeow>`__)

v0.8.2
------

Enables HTML animations to be rendered on readthedocs.

**Implemented enhancements:**

-  DOC Expand on sphinx_gallery_thumbnail_path `#764 <https://github.com/sphinx-gallery/sphinx-gallery/pull/764>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  ENH: Add run_stale_examples config var `#759 <https://github.com/sphinx-gallery/sphinx-gallery/pull/759>`__ (`larsoner <https://github.com/larsoner>`__)
-  Option to disable note in example header `#757 <https://github.com/sphinx-gallery/sphinx-gallery/issues/757>`__
-  Add show_signature option `#756 <https://github.com/sphinx-gallery/sphinx-gallery/pull/756>`__ (`jschueller <https://github.com/jschueller>`__)
-  ENH: Style HTML output like jupyter `#752 <https://github.com/sphinx-gallery/sphinx-gallery/pull/752>`__ (`larsoner <https://github.com/larsoner>`__)
-  ENH: Add reST comments, read-only `#750 <https://github.com/sphinx-gallery/sphinx-gallery/pull/750>`__ (`larsoner <https://github.com/larsoner>`__)
-  Relate warnings and errors on generated rst file back to source Python file / prevent accidental writing of generated files `#725 <https://github.com/sphinx-gallery/sphinx-gallery/issues/725>`__

**Fixed bugs:**

-  Example gallery is down `#753 <https://github.com/sphinx-gallery/sphinx-gallery/issues/753>`__
-  DOC Amend run_stale_examples command in configuration.rst `#763 <https://github.com/sphinx-gallery/sphinx-gallery/pull/763>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  DOC update link in projects_list `#754 <https://github.com/sphinx-gallery/sphinx-gallery/pull/754>`__ (`lucyleeow <https://github.com/lucyleeow>`__)
-  Enable animations HTML to be rendered on readthedocs `#748 <https://github.com/sphinx-gallery/sphinx-gallery/pull/748>`__ (`sdhiscocks <https://github.com/sdhiscocks>`__)

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
-  Support headings in reST to MD `#723 <https://github.com/sphinx-gallery/sphinx-gallery/pull/723>`__ (`sdhiscocks <https://github.com/sdhiscocks>`__)
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
-  Fix reST block after docstring `#480 <https://github.com/sphinx-gallery/sphinx-gallery/pull/480>`__ (`timhoffm <https://github.com/timhoffm>`__)
-  MAINT: Tolerate Windows mtime `#478 <https://github.com/sphinx-gallery/sphinx-gallery/pull/478>`__ (`larsoner <https://github.com/larsoner>`__)
-  FIX: Output from code execution is not stripped `#475 <https://github.com/sphinx-gallery/sphinx-gallery/pull/475>`__ (`padix-key <https://github.com/padix-key>`__)
-  FIX: Link `#470 <https://github.com/sphinx-gallery/sphinx-gallery/pull/470>`__ (`larsoner <https://github.com/larsoner>`__)
-  FIX: Minor fixes for memory profiling `#468 <https://github.com/sphinx-gallery/sphinx-gallery/pull/468>`__ (`larsoner <https://github.com/larsoner>`__)
-  Add output figure numbering breaking change in release notes. `#466 <https://github.com/sphinx-gallery/sphinx-gallery/pull/466>`__ (`lesteve <https://github.com/lesteve>`__)
-  Remove links to read the docs `#461 <https://github.com/sphinx-gallery/sphinx-gallery/pull/461>`__ (`GaelVaroquaux <https://github.com/GaelVaroquaux>`__)
-  [MRG+1] Add requirements.txt to manifest `#458 <https://github.com/sphinx-gallery/sphinx-gallery/pull/458>`__ (`ksunden <https://github.com/ksunden>`__)


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
* Sphinx-Gallery now raises an exception if the matplotlib backend can
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
