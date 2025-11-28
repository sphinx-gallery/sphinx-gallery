#!/bin/bash

# Build near-minimal version of scikit-learn docs

if [[ "$COLUMNS" == "" ]]; then COLUMNS=80; fi
function __sep__ () {
    echo
    printf %"$COLUMNS"s | tr " " "-"
    echo -e "\n"
}

set -exo pipefail

(set +x; __sep__)

git clone git@github.com:scikit-learn/scikit-learn.git
cd scikit-learn
conda create -n sklearn-dev -c conda-forge \
  python numpy scipy cython meson-python ninja \
  pytest pytest-cov ruff==0.11.2 mypy numpydoc \
  joblib threadpoolctl
pip install -e .

(set +x; __sep__)

../.circleci/sg_dev_check.sh

(set +x; __sep__)

cd doc
make html -D sphinx_gallery_conf.filename_pattern=plot_grid_search_text_feature_extraction\|plot_display_object_visualization -D sphinx_gallery_conf.run_stale_examples=True
