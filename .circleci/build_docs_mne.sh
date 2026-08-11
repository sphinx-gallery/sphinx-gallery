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
uv pip install -e . --group doc mne-qt-browser "PySide6!=6.10.0"

(set +x; __sep__)

mne sys_info -d

(set +x; __sep__)

../.circleci/sg_dev_check.sh

(set +x; __sep__)

export MNE_BROWSER_BACKEND=qt
export MNE_BROWSER_PRECOMPUTE=false
export PATTERN=10_array_objs
# TEMPORARY: prefix every line with elapsed time so we can see which build
# phase this job actually spends its ~14 min in. Revert once we know.
make -C doc html-pattern 2>&1 | python -u -c "
import sys, time
t0 = time.time()
for line in sys.stdin:
    sys.stdout.write(f'[{time.time() - t0:8.1f}s] {line}')
"
