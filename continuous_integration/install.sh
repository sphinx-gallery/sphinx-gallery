#!/bin/bash
#
# License: 3-clause BSD

set -eo pipefail

python -m pip install --upgrade pip setuptools wheel
if [ "$DISTRIB" == "mamba" ]; then
    PIP_DEPENDENCIES="jupyterlite-sphinx>=0.8.0,<0.9.0 jupyterlite-pyodide-kernel<0.1.0 libarchive-c"
    if [ "$SPHINX_VERSION" == "dev" ]; then
        PIP_DEPENDENCIES="--pre ${PIP_DEPENDENCIES} https://api.github.com/repos/sphinx-doc/sphinx/zipball/master"
    elif [ "$SPHINX_VERSION" == "old" ]; then
        PIP_DEPENDENCIES="${PIP_DEPENDENCIES} sphinx<5"
    else
        PIP_DEPENDENCIES="${PIP_DEPENDENCIES} sphinx==${SPHINX_VERSION}"
    fi
elif [ "$DISTRIB" == "minimal" ]; then
    PIP_DEPENDENCIES=""
elif [ "$DISTRIB" == "pip" ]; then
    PIP_DEPENDENCIES="-r dev-requirements.txt vtk pyqt6"
else
    echo "invalid value for DISTRIB environment variable: $DISTRIB"
    exit 1
fi
pip install --upgrade $PIP_DEPENDENCIES pytest pytest-cov coverage pydata-sphinx-theme
python setup.py install