#!/bin/bash

set -eo pipefail
echo "set -eo pipefail" >> "$BASH_ENV"
# Give up on a stalled mirror connection quickly and retry, rather than hanging
# until CircleCI's 10 min no-output timeout kills the job (mne-tools gh-14103).
APT_OPTS="-o Acquire::Retries=3 -o Acquire::http::Timeout=30 -o Acquire::https::Timeout=30"
sudo apt update $APT_OPTS
# The Qt6 list below is kept in sync with mne-tools/tools/setup_xvfb.sh, which
# is where the MNE integration build gets its rendering deps. libxml2 there is
# a SONAME-versioned name that changed in 26.04, so pick it per release rather
# than hard-coding one and breaking whenever the image tag moves.
if [[ $(lsb_release -rs) == "26.04" ]]; then
    XML_DEP=libxml2-16
else
    XML_DEP=libxml2
fi
sudo apt --no-install-recommends install -yq $APT_OPTS ffmpeg graphviz optipng python3-venv \
    xvfb libxkbcommon-x11-0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-xinerama0 libxcb-xfixes0 libopengl0 libegl1 libosmesa6 mesa-utils libxcb-shape0 libxcb-cursor0 $XML_DEP \
    r-base libtirpc-dev

python3 -m venv ~/python_env
source ~/python_env/bin/activate
echo "source ~/python_env/bin/activate" >> "$BASH_ENV"
echo "Python: $(which python)"
echo "pip:    $(which pip)"

# Start a display
/sbin/start-stop-daemon --start --quiet --pidfile /tmp/custom_xvfb_99.pid --make-pidfile --background --exec /usr/bin/Xvfb -- :99 -screen 0 1400x900x24 -ac +extension GLX +render -noreset
echo "export DISPLAY=:99" >> "$BASH_ENV"
