#!/bin/bash

set -eu

die() {
  echo "build failed !!"
  exit "$1"
}


bash ./test/kicad_test.sh

bash ./scripts/build_doc.sh
