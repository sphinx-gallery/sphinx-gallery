#!/bin/bash
#
# License: 3-clause BSD

set -eo pipefail

python -m pip install --upgrade pip setuptools wheel
EXTRA_ARGS=""
PLATFORM=$(python -c "import platform; print(platform.system())")
if [ "$DISTRIB" == "mamba" ]; then
    PIP_DEPENDENCIES="jupyterlite-sphinx>=0.8.0,<0.9.0 jupyterlite-pyodide-kernel<0.1.0 libarchive-c"
    if [ "$SPHINX_VERSION" == "dev" ]; then
        PIP_DEPENDENCIES="--pre ${PIP_DEPENDENCIES} https://api.github.com/repos/sphinx-doc/sphinx/zipball/master"
        EXTRA_ARGS="--upgrade --pre"
    elif [ "$SPHINX_VERSION" != "default" ]; then
        PIP_DEPENDENCIES="${PIP_DEPENDENCIES} sphinx==${SPHINX_VERSION}.*"
    fi
    # memory_profiler is unreliable on macOS and Windows (lots of zombie processes)
    if [ "$PLATFORM" != "Linux" ]; then
        conda remove -y memory_profiler
    fi
elif [ "$DISTRIB" == "minimal" ]; then
    PIP_DEPENDENCIES=""
elif [ "$DISTRIB" == "pip" ]; then
    PIP_DEPENDENCIES="-r dev-requirements.txt vtk pyqt6"
    # Need graphviz binaries in addition to pygraphviz
    if [[ "$PLATFORM" == "Linux" ]]; then
        sudo apt install graphviz
    fi
else
    echo "invalid value for DISTRIB environment variable: $DISTRIB"
    exit 1
fi
set -x
pip install $EXTRA_ARGS $PIP_DEPENDENCIES pytest pytest-cov coverage pydata-sphinx-theme

# pygraphviz installs on Windows-pip but there are no graphviz binaries
if [[ "$PLATFORM" == "Windows" ]]; then
    pip uninstall -y graphviz
fi

pip install -e .
