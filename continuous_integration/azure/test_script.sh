#!/bin/bash
# This script is meant to be called by the "Run test_script.sh" step defined in
# azure-pipelines.yml.
#
# License: 3-clause BSD

set -eo pipefail

if [ "$DISTRIB" == "ubuntu" ]; then
    python3 -m pytest sphinx_gallery -v --tb=short
else
    pytest sphinx_gallery -v --tb=short
fi

if [ "$DISTRIB" != "minimal" ] && [ "$DISTRIB" != "nightly" ]; then
    which gcc
    gcc --version
    make -C doc SPHINXOPTS= html-noplot
    make -C doc SPHINXOPTS=${SPHINXOPTS} html -j 2
fi
