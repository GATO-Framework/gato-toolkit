#!/bin/bash

# Remove previous distributions
rm -rf dist

# Build distributions
python setup.py sdist bdist_wheel

# Upload distributions to PyPI
twine upload dist/*

# Clean up
rm -rf build dist src/*.egg-info

echo "Release completed successfully."
