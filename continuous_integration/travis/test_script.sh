#!/bin/bash
# This script is meant to be called by the "script" step defined in
# .travis.yml. See http://docs.travis-ci.com/ for more details.
#
# License: 3-clause BSD

set -e

pytest sphinx_gallery -vv  --tb=short
cd doc
if [ "$DISTRIB" != "minimal" ] && [ "$PYTHON_VERSION" != "nightly" ]; then
    make SPHINXOPTS= html-noplot
    make SPHINXOPTS=${SPHINXOPTS} html -j 2
    flake8 sphinx_gallery
fi
