#!/bin/sh

app_name=$(basename "$PWD")

rm -rf dist 2> /dev/null || true && mkdir dist

mkdir dist/$app_name

cp __main__.py dist/$app_name

pipenv run pip install -r <(pipenv requirements) \
    --target dist/$app_name

python -m zipapp dist/$app_name -c \
    -o dist/$app_name.pyz \
    -p "/usr/bin/env python"
