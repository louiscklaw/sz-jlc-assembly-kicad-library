#!/bin/bash

set -eu

die() {
  echo "build failed !!"
  exit "$1"
}
