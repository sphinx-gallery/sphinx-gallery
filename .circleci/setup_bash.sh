#!/bin/bash

set -eo pipefail
sudo apt update
sudo apt --no-install-recommends install -yq \
    texlive texlive-latex-extra latexmk optipng tex-gyre graphviz \
    python3-venv
python3 -m venv ~/python_env
echo "set -e" >> "$BASH_ENV"
echo "source ~/python_env/bin/activate" >> "$BASH_ENV"
/sbin/start-stop-daemon --start --quiet --pidfile /tmp/custom_xvfb_99.pid --make-pidfile --background --exec /usr/bin/Xvfb -- :99 -screen 0 1400x900x24 -ac +extension GLX +render -noreset
source ~/python_env/bin/activate
echo "Python: $(which python)"
echo "pip:    $(which pip)"
