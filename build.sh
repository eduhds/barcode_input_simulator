#!/bin/sh

rm -rf dist

rm *.pyz || true

mkdir dist

cp __main__.py dist/__main__.py

pipenv run pip install -r <(pipenv requirements) --target dist

if [ "$1" = "standalone" ]; then
    interpreter="-p /usr/bin/python"
else
    interpreter=""
fi

python -m zipapp dist -c -o barcode_input_simulator.pyz $interpreter
