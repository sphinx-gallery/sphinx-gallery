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
    conda update --yes conda

    # force no mkl because mayavi requires old version of numpy
    # which then crashes with pandas and seaborn
    conda create --yes -n testenv python=$PYTHON_VERSION pip nomkl numpy\
        setuptools matplotlib pillow sphinx pytest pytest-cov coverage seaborn
    source activate testenv
    if [ "$INSTALL_MAYAVI" == "true" ]; then
        conda install --yes mayavi
    fi
elif [ "$DISTRIB" == "ubuntu" ]; then
    # Use a separate virtual environment than the one provided by
    # Travis because it contains numpy and we want to use numpy
    # from apt-get
    deactivate
    virtualenv --system-site-packages testvenv
    source testvenv/bin/activate
    pip install -U requests[security]  # ensure SSL certificate works
    pip install -r requirements.txt
    pip install seaborn sphinx==1.5.5 pytest "six>=1.10.0" pytest-cov
else
    echo "invalid value for DISTRIB environment variable: $DISTRIB"
    exit 1
fi

python setup.py install

