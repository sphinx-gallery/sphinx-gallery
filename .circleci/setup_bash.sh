#!/bin/bash

set -eo pipefail
echo "set -eo pipefail" >> "$BASH_ENV"
sudo apt update
sudo apt --no-install-recommends install -yq ffmpeg graphviz optipng python3-venv
python3 -m venv ~/python_env
source ~/python_env/bin/activate
echo "source ~/python_env/bin/activate" >> "$BASH_ENV"
echo "Python: $(which python)"
echo "pip:    $(which pip)"
