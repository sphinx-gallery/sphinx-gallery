#!/bin/bash

set -eo pipefail
sudo apt update
sudo apt --no-install-recommends install -yq \
    libopengl0 libegl1 libosmesa6 mesa-utils \  # 3D
    optipng graphviz python3-venv  # sphinx-gallery
python3 -m venv ~/python_env
echo "set -e" >> "$BASH_ENV"
echo "source ~/python_env/bin/activate" >> "$BASH_ENV"
source ~/python_env/bin/activate
echo "Python: $(which python)"
echo "pip:    $(which pip)"
