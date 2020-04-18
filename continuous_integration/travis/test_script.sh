#!/bin/bash
# This script is meant to be called by the "script" step defined in
# .travis.yml. See http://docs.travis-ci.com/ for more details.
#
# License: 3-clause BSD

set -e

pytest sphinx_gallery -vv  --tb=short
check-manifest -v --ignore doc*,examples*,tutorials*,mayavi_examples*,sphinx_gallery/tests*,.circleci*,continuous_integration*,appveyor.yml,RELEASES.md,dev-requirements.txt,sphinx_gallery/_static/broken_stamp.svg
cd doc
if [ "$DISTRIB" != "minimal" ] && [ "$PYTHON_VERSION" != "nightly" ]; then
    make SPHINXOPTS= html-noplot
    make SPHINXOPTS=${SPHINXOPTS} html -j 2
    flake8 sphinx_gallery
fi
