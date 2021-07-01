#!/bin/sh
rm -rf dist/*
python -m build
twine upload dist/*