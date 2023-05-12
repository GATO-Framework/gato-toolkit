# Package Distribution

## Configure Credentials

### Create a Test PyPI account
If you don't already have a Test PyPI account, you need to create one.
You can do this by going to the [Test PyPI registration page](https://test.pypi.org/account/register/) and filling out the form.

### Create a Test PyPI API token
To create a Test PyPI API token, go to the [Test PyPI website](https://test.pypi.org/manage/account/token/) and click on "Add API token".
Then follow the instructions to create a new token. Once the token is created, PyPI will show you the token value once.
Make sure to copy it and save it in your `.pypirc` file right away, because you won't be able to see it again.

### Create a PyPI account
First, if you don't already have a PyPI account, you need to create one.
You can do this by going to the [PyPI registration page](https://pypi.org/account/register/) and filling out the form.

### Create a PyPI API token
To create an API token, go to the [PyPI website](https://pypi.org/manage/account/token/) and click on "Add API token".
Then follow the instructions to create a new token. Once the token is created, PyPI will show you the token value once.
Make sure to copy it and save it in your `.pypirc` file right away, because you won't be able to see it again.

### Request access to the PyPI repository for this package
In order to publish versions of this package, you must have sufficient permissions.
Only package maintainers will be granted access.

### Store your credentials safely
Next, you need to store your PyPI credentials so that you can use them to upload your package.
The recommended way to do this is to use a `.pypirc` file, which is usually located in your home directory.
This file should look something like this:
```ini
[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmcCJDabc123...  # PyPI token

[testpypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmcCJDxyz789...  # Test PyPI token
```
> This file should **NOT** be checked into source control! It contains sensitive information that could be used to upload packages to PyPI under your name.

The username `__token__` and the password starting with `pypi-` indicate that we are using an API token for authentication, which is more secure than using your PyPI username and password.

## Publish to Test Package Repository
```shell
python setup.py sdist bdist_wheel
twine upload --repository testpypi dist/*
```

## Publish to Production Package Repository
```shell
python setup.py sdist bdist_wheel
twine upload dist/*
```
