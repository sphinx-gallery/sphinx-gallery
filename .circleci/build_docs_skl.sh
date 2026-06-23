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

# Install scikit-learn and doc dependencies
VERSION=$(pip index versions scikit-learn | cut -d "(" -f2 | cut -d ")" -f1 | cut -d "." -f1 -f2 | head -n 1)
echo "Installing scikit-learn version $VERSION"
pip install --only-binary=:all: \
            sphinx numpydoc matplotlib Pillow pandas \
            polars scikit-image packaging seaborn sphinx-prompt \
            sphinxext-opengraph sphinx-copybutton plotly pooch \
            pydata-sphinx-theme sphinxcontrib-sass sphinx-design \
            sphinx-remove-toctrees \
            "scikit-learn==${VERSION}"

(set +x; __sep__)

# Checkout scikit-learn main branch, to build docs from repo
git clone git@github.com:scikit-learn/scikit-learn.git --single-branch --depth 1 --branch ${VERSION}.X
cd scikit-learn/doc
export EXAMPLES_PATTERN="plot_grid_search_text_feature_extraction|plot_display_object_visualization"
make html
