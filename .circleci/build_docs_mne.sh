#!/bin/bash

# Build near-minimal version of MNE-Python docs

set -exo pipefail
git clone git@github.com:/mne-tools/mne-python.git
pushd mne-python
git checkout -b credit origin/credit  # TODO: REMOVE BEFORE MERGE, NEEDS https://github.com/mne-tools/mne-python/pull/13477!
pip install -ve . --group doc mne-qt-browser "PySide6!=6.10.0"
popd

mne sys_info -d

./.circleci/sg_dev_check.sh

export MNE_BROWSER_BACKEND=qt
export MNE_BROWSER_PRECOMPUTE=false
export PATTERN=10_array_objs
make -C mne-python/doc html-pattern
