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
    export CONDA_PKGS="python=$PYTHON_VERSION pip numpy scipy setuptools matplotlib pillow pytest pytest-cov coverage seaborn sphinx_rtd_theme memory_profiler"
    if [ "$INSTALL_MAYAVI" == "true" ]; then
        conda create -yn testenv $CONDA_PKGS mayavi
    else
        conda create -yn testenv $CONDA_PKGS
    fi
    source activate testenv
    # The 3.4 on is quite old
    if [ "$PYTHON_VERSION" == "3.4" ]; then
        conda remove -y memory_profiler
    fi
    if [ "$SPHINX_VERSION" != "dev" ]; then
        conda install "sphinx=${SPHINX_VERSION-*}" --yes
    else
        pip install "https://api.github.com/repos/sphinx-doc/sphinx/zipball/master"
    fi
    python setup.py install
elif [ "$PYTHON_VERSION" == "nightly" ]; then
    # Python nightly requires to use the virtual env provided by travis.
    pip install . numpy scipy seaborn sphinx==1.5.5 "six>=1.10.0" pytest-cov sphinx_rtd_theme
elif [ "$DISTRIB" == "minimal" ]; then
    pip install . pytest pytest-cov
elif [ "$DISTRIB" == "ubuntu" ]; then
    # Use a separate virtual environment than the one provided by
    # Travis because it contains numpy and we want to use numpy
    # from apt-get
    deactivate
    virtualenv --system-site-packages testvenv
    source testvenv/bin/activate
    pip install --upgrade pip setuptools wheel pyopenssl
    pip install -U requests[security]  # ensure SSL certificate works
    pip install "tornado<5"
    # The pipe just gets rid of the progress bars
    pip install -r requirements.txt | cat
    # test show_memory=True without memory_profiler by not installing it (not in req)
    pip install seaborn sphinx==1.5.5 pytest "six>=1.10.0" pytest-cov sphinx_rtd_theme
    python setup.py install
else
    echo "invalid value for DISTRIB environment variable: $DISTRIB"
    exit 1
fi
