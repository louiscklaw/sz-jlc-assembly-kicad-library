#!/usr/bin/env sh
LIB_RESULT_DIR=$PWD

set -ex

echo 'test to load kicad library'

cd _util/kicad-library-utils/schlib

rm -rf tmp/*

for filename in $LIB_RESULT_DIR/*.lib; do
  # echo ./test_schlib.sh $filename
  ./test_schlib.sh $filename &
done

wait

echo 'test load done'

cd ../../..