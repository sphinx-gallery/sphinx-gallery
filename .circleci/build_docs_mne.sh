#!/bin/bash -eo pipefail

# Build near-minimal version of MNE-Python docs

set -x
git clone git@github.com:/mne-tools/mne-python.git
pip install -ve mne-python[docs] mne-qt-browser "PySide6!=6.10.0" pyvistaqt

SG_LOC=$(python -c "import sphinx_gallery, pathlib; print(pathlib.Path(sphinx_gallery.__file__).parent)")
test SG_LOC == $(pwd)/sphinx_gallery

cd mne-python/doc
export MNE_BROWSER_BACKEND=qt
export PATTERN=10_array_objs
export MNE_BROWSER_PRECOMPUTE=false
sudo apt install optipng

make html-pattern
