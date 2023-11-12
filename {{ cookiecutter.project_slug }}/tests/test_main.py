from {{ cookiecutter.__project_slug_underscore }}.main import add_numbers


def test_add_numbers() -> None:
    assert add_numbers(a=1, b=2) == 3
