#!/bin/bash
# This script is meant to be called by the "Run install.sh" step defined in
# azure-pipelines.yml.
# The behavior of the script is controlled by environment variables defined
# in the azure-pipelines.yml in the top level folder of the project.
#
# License: 3-clause BSD

set -e

if [ "$DISTRIB" == "conda" ]; then
    export CONDA_DEPENDENCIES="pip numpy setuptools matplotlib pillow pytest pytest-cov coverage seaborn statsmodels plotly joblib flake8 check-manifest"
    echo $CONDA_DEPENDENCIES
    echo "$CONDA_DEPENDENCIES"
    export PIP_DEPENDENCIES="sphinx_rtd_theme"
    if [ "$PYTHON_VERSION" != "3.5" ] && [ "$PYTHON_VERSION" != "3.6" -o "$LOCALE" != "C" ]; then
        export PIP_DEPENDENCIES="${PIP_DEPENDENCIES} memory_profiler vtk https://github.com/enthought/mayavi/zipball/master ipython pypandoc"
    fi
    if [ "$SPHINX_VERSION" != "dev" ]; then
        export PIP_DEPENDENCIES="${PIP_DEPENDENCIES} sphinx${SPHINX_VERSION}"
    else
        export PIP_DEPENDENCIES="${PIP_DEPENDENCIES} https://api.github.com/repos/sphinx-doc/sphinx/zipball/master"
    fi
    conda create -n testenv --yes python=$PYTHON_VERSION "$CONDA_DEPENDENCIES"
    source activate testenv
    python -m pip install "$PIP_DEPENDENCIES"
    python setup.py install
# elif [ "$PYTHON_VERSION" == "nightly" ]; then
#     # Python nightly requires to use the virtual env provided by travis.
#     pip install https://api.github.com/repos/cython/cython/zipball/master
#     pip install --no-use-pep517 https://api.github.com/repos/numpy/numpy/zipball/master
#     pip install . sphinx joblib pytest-cov
elif [ "$DISTRIB" == "minimal" ]; then
    pip install --upgrade . pytest pytest-cov coverage
elif [ "$DISTRIB" == "ubuntu" ]; then
    pip install -r dev-requirements.txt | cat
    pip install --upgrade pytest pytest-cov coverage
    # test show_memory=True without memory_profiler by not installing it (not in req)
    pip install sphinx==1.8.3
    python setup.py install
else
    echo "invalid value for DISTRIB environment variable: $DISTRIB"
    exit 1
fi
