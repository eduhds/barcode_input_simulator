#!/bin/sh

rm -rf dist

rm *.pyz | true

mkdir dist

cp __main__.py dist/__main__.py

pipenv run pip install -r <(pipenv requirements) --target dist

python -m zipapp dist -o barcode_input_simulator.pyz -c
