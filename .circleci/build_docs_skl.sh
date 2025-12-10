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

# Install scikit-learn from Scientific Python nightly wheels
python -m pip install --upgrade --pre threadpoolctl
python -m pip install --pre --only-binary ":all:" --default-timeout=60 \
	--index-url "https://pypi.anaconda.org/scientific-python-nightly-wheels/simple" \
	"scikit-learn>=1.7.dev0"

# Install scikit-learn doc dependencies
pip install sphinx numpydoc matplotlib Pillow pandas \
            polars scikit-image packaging seaborn sphinx-prompt \
            sphinxext-opengraph sphinx-copybutton plotly pooch \
            pydata-sphinx-theme sphinxcontrib-sass sphinx-design \
            sphinx-remove-toctrees

(set +x; __sep__)

.circleci/sg_dev_check.sh

(set +x; __sep__)

# Checkout scikit-learn main branch, to build docs from repo
git clone git@github.com:scikit-learn/scikit-learn.git
cd scikit-learn/doc
export EXAMPLES_PATTERN="plot_grid_search_text_feature_extraction|plot_display_object_visualization"
make html
