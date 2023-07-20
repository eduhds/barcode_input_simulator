#!/bin/sh

rm -rf dist

rm *.pyz || true

mkdir dist

cp __main__.py dist/__main__.py

pipenv run pip install -r <(pipenv requirements) --target dist

out=barcode_input_simulator.pyz

if [ "$1" = "standalone" ]; then
    python -m zipapp dist -c -o "$out" -p "/usr/bin/env python"
else
    python -m zipapp dist -c -o  "$out"
fi
