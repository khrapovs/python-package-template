# Python Package Template

![pytest](https://github.com/khrapovs/python-package-template/actions/workflows/tests-lint.yaml/badge.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)

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
