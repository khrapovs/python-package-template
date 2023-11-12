# python-package-template

A template for creating a Python package

## Usage

Install [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/index.html):
```shell
pip install cookiecutter
```
Clone this repository and create a project from it:
```shell
git clone git@github.com:khrapovs/python-package-template.git
cookiecutter python-package-template
```

## Contribute

Create a virtual environment and activate it:
```shell
python -m venv venv
source venv/bin/activate
```
Install development dependencies:
```shell
pip install -e .[dev]
```
and use pre-commit to make sure that your code is formatted automatically:
```shell
pre-commit install
```
Run tests:
```shell
pip install -e .[test]
pytest
```
