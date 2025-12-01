#!/bin/bash
#
# License: 3-clause BSD

set -eo pipefail

python -m pip install --upgrade pip setuptools wheel
PLATFORM=$(python -c "import platform; print(platform.system())")
DEP_OPT=""
if [ "$DISTRIB" == "mamba" ]; then
    conda config --set solver libmamba
    # memory_profiler is unreliable on macOS and Windows (lots of zombie processes)
    if [ "$PLATFORM" != "Linux" ]; then
        conda remove -y memory_profiler
    fi
    PIP_DEPENDENCIES="jupyterlite-sphinx>=0.17.1 jupyterlite-pyodide-kernel libarchive-c numpy sphinx-design"
elif [ "$DISTRIB" == "minimal" ]; then
    PIP_DEPENDENCIES=""
elif [ "$DISTRIB" == "pip" ]; then
    PIP_DEPENDENCIES="pillow pyqt6"
    DEP_OPT="[dev]"
    # No VTK on Python 3.12 pip yet
    if [[ "$(python -c "import sys; print(sys.version)")" != "3.12"* ]]; then
        PIP_DEPENDENCIES="$PIP_DEPENDENCIES vtk"
    fi
else
    echo "invalid value for DISTRIB environment variable: $DISTRIB"
    exit 1
fi

# Sphinx version
if [ "$SPHINX_VERSION" == "dev" ]; then
    # TODO: Reenable once sphinx-design and pydata-sphinx-theme are 9.0+ compatible,
    # Then also add a sphinx-9 test job
    # PIP_DEPENDENCIES="--upgrade --pre https://api.github.com/repos/sphinx-doc/sphinx/zipball/master --default-timeout=60 --extra-index-url 'https://pypi.anaconda.org/scientific-python-nightly-wheels/simple' $PIP_DEPENDENCIES"
    PIP_DEPENDENCIES="--upgrade --pre 'sphinx<9' --default-timeout=60 --extra-index-url 'https://pypi.anaconda.org/scientific-python-nightly-wheels/simple' $PIP_DEPENDENCIES"
elif [ "$SPHINX_VERSION" != "default" ]; then
    PIP_DEPENDENCIES="sphinx==${SPHINX_VERSION}.* $PIP_DEPENDENCIES"
else
    PIP_DEPENDENCIES="sphinx!=7.3.2,!=7.3.3,!=7.3.4,!=7.3.5,!=7.3.6 $PIP_DEPENDENCIES"
fi

set -x
pip install $EXTRA_ARGS $PIP_DEPENDENCIES \
    pytest pytest-cov coverage pydata-sphinx-theme lxml \
    "sphinxcontrib-video>=0.2.1rc0" \
    -e .${DEP_OPT}
set +x

# "pip install pygraphviz" does not guarantee graphviz binaries exist
if [[ "$DISTRIB" != "mamba" ]]; then
    if [[ "$PLATFORM" == "Linux" ]]; then
        sudo apt install ffmpeg graphviz
    else  # could use brew on macOS pip but it'll take time to install
        echo "Removing pygraphviz on $PLATFORM when DISTRIB=$DISTRIB"
        pip uninstall -y graphviz
    fi
fi
