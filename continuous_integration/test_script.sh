#!/bin/bash
# License: 3-clause BSD

set -eo pipefail
set -x

pytest sphinx_gallery -v --tb=short

if [ "$DISTRIB" == "minimal" ] || [ "$DISTRIB" != "nightly" ]; then
    exit 0
fi
if [[ $(python -c "import platform; print(platform.system())") != "Linux" ]]; then
    echo "Windows: Removing show_memory and compress_images"
    sed -i '/show_memory/d' doc/conf.py
    sed -i '/compress_images/d' doc/conf.py
fi

printf %"$COLUMNS"s | tr " " "-"
make -C doc SPHINXOPTS= html-noplot

printf %"$COLUMNS"s | tr " " "-"
make -C doc SPHINXOPTS=${SPHINXOPTS} html -j 2
