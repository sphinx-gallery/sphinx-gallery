#!/bin/bash
# This script is meant to be called by the "Run install.sh" step defined in
# azure-pipelines.yml.
# The behavior of the script is controlled by environment variables defined
# in the azure-pipelines.yml in the top level folder of the project.
#
# License: 3-clause BSD

set -eo pipefail

if [ "$DISTRIB" == "conda" ]; then
    # wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh --progress=dot:mega
    # bash miniconda.sh -b -p ~/miniconda
    # source ~/miniconda/etc/profile.d/conda.sh
    echo "##vso[task.prependpath]$CONDA/bin"
    export PATH=${CONDA}/bin:${PATH}
    CONDA_TO_INSTALL="python=$PYTHON_VERSION pip numpy setuptools matplotlib pillow pytest pytest-cov coverage seaborn statsmodels 'plotly>=4.0' joblib flake8 wheel libiconv graphviz memory_profiler \"ipython!=8.7.0\" pypandoc"
    PIP_DEPENDENCIES="check-manifest jupyterlite-sphinx"
    if [ "$SPHINX_VERSION" == "" ]; then
        PIP_DEPENDENCIES="${PIP_DEPENDENCIES} sphinx jinja2<=3.0.3"
    elif [ "$SPHINX_VERSION" == "dev" ]; then
        # It is a mystery to me why we need black, but we get an error with sphinx that it's needed at the end of the build...
        PIP_DEPENDENCIES="${PIP_DEPENDENCIES} https://api.github.com/repos/sphinx-doc/sphinx/zipball/master black"
    elif [ "$SPHINX_VERSION" == "old" ]; then
        PIP_DEPENDENCIES="${PIP_DEPENDENCIES} sphinx<5 jinja2<=3.0.3"
    else
        PIP_DEPENDENCIES="${PIP_DEPENDENCIES} sphinx==${SPHINX_VERSION} jinja2<=3.0.3"
    fi
    source activate base
    conda install --yes -c conda-forge $CONDA_TO_INSTALL
    conda info --envs
    pytest --version
    python -m pip install $PIP_DEPENDENCIES
    python -m pip install --pre pydata-sphinx-theme
    python setup.py install --user
elif [ "$DISTRIB" == "nightly" ]; then
    echo "##vso[task.prependpath]${HOME}/.local/bin"
    export PATH=~/.local/bin:${PATH}
    sudo apt-get install python${PYTHON_VERSION} python${PYTHON_VERSION}-distutils python${PYTHON_VERSION}-dev libopenblas-dev
    mkdir -p ~/.local/bin
    ln -s /usr/bin/python${PYTHON_VERSION} ~/.local/bin/python
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py --user
    pip install --no-use-pep517 cython
    # This should work but doesn't (version parsing problem):
    #
    # pip install --no-use-pep517 -q https://api.github.com/repos/numpy/numpy/zipball/master
    #
    # And this does work, but it super slow (> 10 min):
    #
    # git clone https://github.com/numpy/numpy.git --depth=1
    # cd numpy && pip install --no-use-pep517 . && cd .. && rm -Rf numpy
    # pip install --no-use-pep517 -q https://api.github.com/repos/matplotlib/matplotlib/zipball/master
    #
    # So for now we'll just live without NumPy.
    pip install -q --upgrade --pre sphinx joblib pytest-cov pygments colorama "jinja2>=2.3" markupsafe>=1.1
    pip install -q .
    pip list
elif [ "$DISTRIB" == "minimal" ]; then
    python -m pip install --upgrade . pytest pytest-cov coverage
elif [ "$DISTRIB" == "ubuntu" ]; then
    sudo apt-get install --fix-missing python3-numpy python3-matplotlib python3-pip python3-coverage optipng graphviz \
      libxkbcommon-x11-0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-xinerama0 libxcb-xfixes0 libopengl0 libegl1 libosmesa6 mesa-utils libxcb-shape0
    python3 -m pip install --upgrade pip setuptools wheel
    python3 -m pip install -r dev-requirements.txt
    python3 -m pip install vtk "pyqt5!=5.15.8"
    python3 -m pip install --no-build-isolation mayavi
    # Make sure that Mayavi works and does not die when making an actual plot (tests Qt + VTK)
    python3 -c "import faulthandler; faulthandler.enable(); from mayavi import mlab; mlab.test_plot3d()"
    python3 -m pip install --upgrade pytest pytest-cov coverage
    # test show_memory=True without memory_profiler by not installing it (not in req)
    python3 -m pip install "sphinx<5" "jinja2<=3.0.3"
    python3 setup.py install --user
    python3 -m pip list
else
    echo "invalid value for DISTRIB environment variable: $DISTRIB"
    exit 1
fi
