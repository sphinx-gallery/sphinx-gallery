#!/bin/bash
# This script is meant to be called by the "script" step defined in
# .travis.yml. See http://docs.travis-ci.com/ for more details.
#
# License: 3-clause BSD

set -e

python setup.py test
pytest sphinx_gallery
cd doc
make html-noplot
make html -j 2
