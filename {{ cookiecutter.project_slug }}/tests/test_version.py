from {{ cookiecutter.__project_slug_underscore }} import __version__


def test_version() -> None:
    assert isinstance(__version__, str)
