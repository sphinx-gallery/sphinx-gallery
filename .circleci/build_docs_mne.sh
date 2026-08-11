#!/bin/bash

# Build near-minimal version of MNE-Python docs

if [[ "$COLUMNS" == "" ]]; then COLUMNS=80; fi

function __sep__ () {
    echo
    printf %"$COLUMNS"s | tr " " "-"
    echo -e "\n"
}

set -exo pipefail

(set +x; __sep__)

git clone git@github.com:/mne-tools/mne-python.git
cd mne-python
pip install -e . --group doc mne-qt-browser "PySide6!=6.10.0"

(set +x; __sep__)

mne sys_info -d

(set +x; __sep__)

../.circleci/sg_dev_check.sh

(set +x; __sep__)

export MNE_BROWSER_BACKEND=qt
export MNE_BROWSER_PRECOMPUTE=false
# MNE feeds this to sphinx_gallery_conf["parallel"], so it exercises our own
# parallel example execution; `make` already gets Sphinx's -j from their Makefile
export MNE_DOC_BUILD_N_JOBS=2
export PATTERN=10_array_objs
make -C doc html-pattern
