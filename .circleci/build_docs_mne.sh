#!/bin/bash

# Build near-minimal version of MNE-Python docs

if [[ "$COLUMNS" == "" ]]; then COLUMNS=80; fi

function __sep__ () {
    echo
    printf %"$COLUMNS"s | tr " " "-"
    echo -e "\n"
}

set -exo pipefail

__sep__

git clone git@github.com:/mne-tools/mne-python.git
pushd mne-python
git checkout -b credit origin/credit  # TODO: REMOVE BEFORE MERGE, NEEDS https://github.com/mne-tools/mne-python/pull/13477!
pip install -e . --group doc mne-qt-browser "PySide6!=6.10.0"
popd

__sep__

mne sys_info -d

__sep__

./.circleci/sg_dev_check.sh

__sep__

export MNE_BROWSER_BACKEND=qt
export MNE_BROWSER_PRECOMPUTE=false
export PATTERN=10_array_objs
make -C mne-python/doc html-pattern
