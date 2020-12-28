#!/bin/bash
# This script is meant to be called by the "Run install.sh" step defined in
# azure-pipelines.yml.
# The behavior of the script is controlled by environment variables defined
# in the azure-pipelines.yml in the top level folder of the project.
#
# License: 3-clause BSD

set -e

make_conda() {
    CONDA_TO_INSTALL="$@"
    conda create -n testev --yes $CONDA_TO_INSTALL
    source activate testev
}

if [ "$DISTRIB" == "conda" ]; then
    CONDA_TO_INSTALL="$CONDA_TO_INSTALL python=$PYTHON_VERSION pip numpy setuptools matplotlib pillow pytest pytest-cov coverage seaborn statsmodels plotly joblib flake8"
    PIP_DEPENDENCIES="$@"
    PIP_DEPENDENCIES="$PIP_DEPENDENCIES sphinx_rtd_theme check-manifest"
    if [ "$PYTHON_VERSION" != "3.5" ] && [ "$PYTHON_VERSION" != "3.6" -o "$LOCALE" != "C" ]; then
        PIP_DEPENDENCIES="${PIP_DEPENDENCIES} memory_profiler vtk https://github.com/enthought/mayavi/zipball/master ipython pypandoc"
    fi
    if [ "$SPHINX_VERSION" == "" ]; then
        PIP_DEPENDENCIES="${PIP_DEPENDENCIES} sphinx"
    elif [ "$SPHINX_VERSION" == "dev" ]; then
        PIP_DEPENDENCIES="${PIP_DEPENDENCIES} https://api.github.com/repos/sphinx-doc/sphinx/zipball/master"
    else
        PIP_DEPENDENCIES="${PIP_DEPENDENCIES} sphinx==${SPHINX_VERSION}"
    fi
    make_conda $CONDA_TO_INSTALL
    # python -m pip install -U pip
    python -m pip install sphinx_rtd_theme check-manifest sphinx
    python setup.py install
# elif [ "$PYTHON_VERSION" == "nightly" ]; then
#     # Python nightly requires to use the virtual env provided by travis.
#     pip install https://api.github.com/repos/cython/cython/zipball/master
#     pip install --no-use-pep517 https://api.github.com/repos/numpy/numpy/zipball/master
#     pip install . sphinx joblib pytest-cov
elif [ "$DISTRIB" == "minimal" ]; then
    python -m pip install --upgrade . pytest pytest-cov coverage
elif [ "$DISTRIB" == "ubuntu" ]; then
    python -m pip install -r dev-requirements.txt | cat
    python -m pip install --upgrade pytest pytest-cov coverage
    # test show_memory=True without memory_profiler by not installing it (not in req)
    python -m pip install sphinx==1.8.3
    python setup.py install
else
    echo "invalid value for DISTRIB environment variable: $DISTRIB"
    exit 1
fi
