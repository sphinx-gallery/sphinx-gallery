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
pwd

# Deactivate python venv activated in `setup_bash.sh`
deactivate

# Install miniforge
# Copied from: https://github.com/scikit-learn/scikit-learn/blob/94f18cefbdc145a9ae439112d7fc89d84467c647/build_tools/circle/build_doc.sh#L171-L176
MINIFORGE_URL="https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh"
curl -L --retry 10 $MINIFORGE_URL -o miniconda.sh
MINIFORGE_PATH=$HOME/miniforge3
bash ./miniconda.sh -b -p $MINIFORGE_PATH
source $MINIFORGE_PATH/etc/profile.d/conda.sh
conda activate

conda create -n sklearn-dev -c conda-forge \
  python numpy scipy joblib threadpoolctl
conda activate sklearn-dev

pip install .
# Install the dev version of SG
pip install ../sphinx-gallery
# Install skl doc dependencies
pip install sphinx numpydoc matplotlib Pillow pandas \
            polars scikit-image packaging seaborn sphinx-prompt \
            sphinxext-opengraph sphinx-copybutton plotly pooch \
            pydata-sphinx-theme sphinxcontrib-sass sphinx-design \
            sphinx-remove-toctrees

(set +x; __sep__)

../.circleci/sg_dev_check.sh

(set +x; __sep__)

cd doc
export EXAMPLES_PATTERN="plot_grid_search_text_feature_extraction|plot_display_object_visualizations"
make html
