#!/bin/sh
set -o errexit
set -o nounset


echo "Test Start"
echo "[TEST] programs/"
cd programs/
for file in `\find ./*.psm -maxdepth 1 -type f`; do
    echo "[Start]" $file
    upprism $file
    code=$?
    if [ ${code} -eq 0 ]; then
      echo "[Success]" $file
    else
      exit 1
    fi
done
echo ""
echo "================"
echo "[TEST] irregular_programs/"
cd ../irregular_programs/
for file in `\find ./*.psm -maxdepth 1 -type f`; do
    echo "[Start]" $file
    upprism $file
    code=$?
    if [ ${code} -ne 0 ]; then
      echo "[Success] successfully detected errors:" $file
    else
      exit 1
    fi
done
