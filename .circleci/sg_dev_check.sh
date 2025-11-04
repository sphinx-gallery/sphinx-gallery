#!/bin/bash

# Ensure we are using local version of SG

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
SG_SRC_DIR=$(dirname "$SCRIPT_DIR")/sphinx_gallery

set -xeo pipefail
SG_IMPORT_LOC=$(python -c "import sphinx_gallery, pathlib; print(pathlib.Path(sphinx_gallery.__file__).parent)")
test "$SG_IMPORT_LOC" == "$SG_SRC_DIR"
