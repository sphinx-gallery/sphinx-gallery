#!/bin/bash
# This script is meant to be called by the "install" step defined in
# .travis.yml. See http://docs.travis-ci.com/ for more details.
# The behavior of the script is controlled by environment variabled defined
# in the .travis.yml in the top level folder of the project.
#
# License: 3-clause BSD

set -e

if [ "$DISTRIB" == "conda" ]; then
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    chmod +x miniconda.sh
    ./miniconda.sh -b
    export PATH=$HOME/miniconda3/bin:$PATH
    conda update -y conda

    # Force conda to think about other dependencies that can break
    conda create -yn testenv "python=$PYTHON_VERSION pip numpy scipy setuptools matplotlib pillow pytest pytest-cov coverage seaborn flake8 $CONDA_PKGS"
    source activate testenv
    # Optional packages
    if [ "$PYTHON_VERSION" != "3.5" ]; then
        pip install memory_profiler vtk mayavi ipython
    fi
    if [ "$SPHINX_VERSION" != "dev" ]; then
        pip install "sphinx${SPHINX_VERSION}"
    else
        pip install "https://api.github.com/repos/sphinx-doc/sphinx/zipball/master"
    fi
    pip install -q sphinx_rtd_theme
    python setup.py install
elif [ "$PYTHON_VERSION" == "nightly" ]; then
    # Python nightly requires to use the virtual env provided by travis.
    pip install . numpy sphinx pytest-cov
elif [ "$DISTRIB" == "minimal" ]; then
    pip install . pytest pytest-cov
elif [ "$DISTRIB" == "ubuntu" ]; then
    pip install -r requirements.txt | cat
    # test show_memory=True without memory_profiler by not installing it (not in req)
    pip install seaborn sphinx==1.8.3 pytest pytest-cov sphinx_rtd_theme flake8
    python setup.py install
else
    echo "invalid value for DISTRIB environment variable: $DISTRIB"
    exit 1
fi
