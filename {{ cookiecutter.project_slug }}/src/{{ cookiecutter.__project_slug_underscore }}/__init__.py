from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("{{ cookiecutter.project_slug }}")
except PackageNotFoundError:
    # package is not installed
    pass
