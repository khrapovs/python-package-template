# {{ cookiecutter.project_slug }}

{{ cookiecutter.project_name }}

## Installation

```shell
pip install {{ cookiecutter.project_slug }}
```

## Usage

TBA

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
