#!/bin/bash
# This script is meant to be called by the "after_success" step defined in
# .travis.yml. See https://docs.travis-ci.com/ for more details.

# License: 3-clause BSD

if [[ "$PYTHON_VERSION" != "nightly" ]]; then
    pip install codecov
    codecov
fi
