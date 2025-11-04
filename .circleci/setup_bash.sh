#!/bin/bash

set -eo pipefail
echo "set -eo pipefail" >> "$BASH_ENV"
sudo apt update
sudo apt --no-install-recommends install -yq ffmpeg graphviz optipng python3-venv \
    xvfb libxkbcommon-x11-0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-xinerama0 libxcb-xfixes0 libopengl0 libegl1 libosmesa6 mesa-utils libxcb-shape0 libxcb-cursor0 libxml2

python3 -m venv ~/python_env
source ~/python_env/bin/activate
echo "source ~/python_env/bin/activate" >> "$BASH_ENV"
echo "Python: $(which python)"
echo "pip:    $(which pip)"

# Start a display
/sbin/start-stop-daemon --start --quiet --pidfile /tmp/custom_xvfb_99.pid --make-pidfile --background --exec /usr/bin/Xvfb -- :99 -screen 0 1400x900x24 -ac +extension GLX +render -noreset
echo "export DISPLAY=:99" >> "$BASH_ENV"
