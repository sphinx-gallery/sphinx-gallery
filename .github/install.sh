#!/bin/bash
#
# License: 3-clause BSD

set -eo pipefail

python -m pip install --upgrade pip setuptools wheel
PLATFORM=$(python -c "import platform; print(platform.system())")
DEP_OPT=""
if [ "$DISTRIB" == "mamba" ]; then
    # memory_profiler is unreliable on macOS and Windows (lots of zombie processes)
    if [ "$PLATFORM" != "Linux" ]; then
        micromamba remove -y memory_profiler
    fi
    PIP_DEPENDENCIES="jupyterlite-sphinx>=0.17.1 jupyterlite-pyodide-kernel libarchive-c numpy sphinx-design>=0.8"
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
    PIP_DEPENDENCIES="--upgrade --pre https://api.github.com/repos/sphinx-doc/sphinx/zipball/master --default-timeout=60 --extra-index-url 'https://pypi.anaconda.org/scientific-python-nightly-wheels/simple' $PIP_DEPENDENCIES"
    # Use after new Sphinx release, before dependencies have supported it
    # PIP_DEPENDENCIES="--upgrade --pre sphinx<10 --default-timeout=60 --extra-index-url 'https://pypi.anaconda.org/scientific-python-nightly-wheels/simple' $PIP_DEPENDENCIES"
elif [ "$SPHINX_VERSION" != "default" ]; then
    PIP_DEPENDENCIES="sphinx==${SPHINX_VERSION}.* $PIP_DEPENDENCIES"
else
    PIP_DEPENDENCIES="sphinx!=7.3.2,!=7.3.3,!=7.3.4,!=7.3.5,!=7.3.6 $PIP_DEPENDENCIES"
fi

set -x
pip install $EXTRA_ARGS $PIP_DEPENDENCIES \
    pytest pytest-cov pytest-xdist coverage pydata-sphinx-theme lxml \
    "sphinxcontrib-video>=0.2.1rc0" \
    -e .${DEP_OPT}
set +x

# "pip install pygraphviz" does not guarantee graphviz binaries exist
if [[ "$DISTRIB" != "mamba" ]]; then
    if [[ "$PLATFORM" == "Linux" ]]; then
        APT_PACKAGES="ffmpeg graphviz"
        # From graphviz 14 (Ubuntu 26.04) neato is a separate plugin package
        # that "graphviz" does not pull in. "neato -V" still works without it,
        # so _has_graphviz() is True but the API usage graphs fail to render.
        if apt-cache show libgvplugin-neato-layout8 &>/dev/null; then
            APT_PACKAGES="$APT_PACKAGES libgvplugin-neato-layout8"
        fi
        sudo apt install $APT_PACKAGES
    else
        # ffmpeg gates all of test_full.py, so without it the tinybuild suite
        # silently disappears. The wheel is a static build, so it beats brew
        # (a dozen bottles, and a from-source build whenever the runner image
        # outpaces the bottled macOS version) and choco (~35 s); it just has to
        # land on PATH under the name matplotlib looks for.
        pip install imageio-ffmpeg
        FFMPEG_DIR=$(python -c "
import os, shutil, sys, imageio_ffmpeg
d = os.path.join(os.path.expanduser('~'), '.local', 'bin')
os.makedirs(d, exist_ok=True)
shutil.copy2(imageio_ffmpeg.get_ffmpeg_exe(),
             os.path.join(d, 'ffmpeg' + ('.exe' if sys.platform == 'win32' else '')))
print(d)")
        if [[ -n "$GITHUB_PATH" ]]; then
            echo "$FFMPEG_DIR" >> "$GITHUB_PATH"
        fi
        echo "Removing pygraphviz on $PLATFORM when DISTRIB=$DISTRIB"
        pip uninstall -y graphviz
    fi
fi
