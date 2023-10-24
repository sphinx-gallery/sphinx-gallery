#!/bin/bash
#
# License: 3-clause BSD

set -eo pipefail

python -m pip install --upgrade pip setuptools wheel
PLATFORM=$(python -c "import platform; print(platform.system())")
if [ "$DISTRIB" == "mamba" ]; then
    # memory_profiler is unreliable on macOS and Windows (lots of zombie processes)
    if [ "$PLATFORM" != "Linux" ]; then
        conda remove -y memory_profiler
    fi
    PIP_DEPENDENCIES="jupyterlite-sphinx>=0.8.0,<0.9.0 jupyterlite-pyodide-kernel<0.1.0 libarchive-c"
elif [ "$DISTRIB" == "minimal" ]; then
    PIP_DEPENDENCIES=""
elif [ "$DISTRIB" == "pip" ]; then
    PIP_DEPENDENCIES="-r dev-requirements.txt vtk pyqt6"
else
    echo "invalid value for DISTRIB environment variable: $DISTRIB"
    exit 1
fi

# Sphinx version
if [ "$SPHINX_VERSION" == "dev" ]; then
    PIP_DEPENDENCIES="--upgrade --pre https://api.github.com/repos/sphinx-doc/sphinx/zipball/master $PIP_DEPENDENCIES"
elif [ "$SPHINX_VERSION" != "default" ]; then
    PIP_DEPENDENCIES="sphinx==${SPHINX_VERSION}.* $PIP_DEPENDENCIES"
fi

set -x
pip install $EXTRA_ARGS $PIP_DEPENDENCIES pytest pytest-cov coverage pydata-sphinx-theme -e .
set +x

# "pip install pygraphviz" does not guarantee graphviz binaries exist
if [[ "$DISTRIB" != "mamba" ]]; then
    if [[ "$PLATFORM" == "Linux" ]]; then
        sudo apt install graphviz
    else  # could use brew on macOS pip but it'll take time to install
        echo "Removing pygraphviz on $PLATFORM when DISTRIB=$DISTRIB"
        pip uninstall -y graphviz
    fi
fi
