#!/bin/bash
# This script is meant to be called by the "Run test_script.sh" step defined in
# azure-pipelines.yml.
#
# License: 3-clause BSD

set -e

if [ "$DISTRIB" != "minimal" ] && [ "$PYTHON_VERSION" != "nightly" ]; then
    conda info --envs
    source activate base
fi

pytest sphinx_gallery -vv  --tb=short

if [ "$DISTRIB" != "minimal" ] && [ "$PYTHON_VERSION" != "nightly" ]; then
    cd doc
    make SPHINXOPTS= html-noplot
    make SPHINXOPTS=${SPHINXOPTS} html -j 2
    cd ..
    flake8 sphinx_gallery
    check-manifest
fi
