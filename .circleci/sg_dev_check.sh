#!/bin/bash

# Ensure we are using local version of SG

set -xeo pipefail
SG_LOC=$(python -c "import sphinx_gallery, pathlib; print(pathlib.Path(sphinx_gallery.__file__).parent)")
test "$SG_LOC" == "$(pwd)/sphinx_gallery"
