#!/bin/bash

# Remove old distributions
rm -rf dist

# Build source and wheel distribution
python setup.py sdist bdist_wheel

# Upload the distributions to Test PyPI
twine upload --repository testpypi dist/*

# Cleanup
rm -rf distc build src/*.egg-info

echo "Test release completed successfully."
