import os
from contextlib import contextmanager
from pathlib import Path
from shlex import split
from shutil import rmtree
from subprocess import check_call
from typing import Generator

from pytest_cookies.plugin import Cookies


@contextmanager
def bake_in_temp_dir(cookies: Cookies) -> Generator[Cookies, None, None]:
    result = cookies.bake()
    try:
        yield result
    finally:
        rmtree(result.project_path)


@contextmanager
def inside_dir(path: Path) -> Generator[None, None, None]:
    old_path = Path.cwd()
    try:
        os.chdir(path)
        path_to_add = (path / "src").absolute().as_posix()
        if "PYTHONPATH" not in os.environ:
            os.environ["PYTHONPATH"] = path_to_add
        else:
            os.environ["PYTHONPATH"] = path_to_add + os.pathsep + os.environ["PYTHONPATH"]
        yield
    finally:
        os.chdir(old_path)


def run_inside_dir(command: str, path: Path) -> int:
    with inside_dir(path=path):
        return check_call(split(command))


def test_bake_not_open_source(cookies: Cookies) -> None:
    with bake_in_temp_dir(cookies=cookies) as result:
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.is_dir()
        assert result.project_path.name == "python-package-boilerplate"
        found_toplevel_files = [f.name for f in result.project_path.glob("*")]
        expected_toplevel_files = [
            "docs",
            "src",
            "tests",
            ".coveragerc",
            ".github",
            ".gitignore",
            ".pre-commit-config.yaml",
            "mkdocs.yaml",
            "pyproject.toml",
            "README.md",
        ]
        assert sorted(found_toplevel_files) == sorted(expected_toplevel_files)
        found_src_folders = [f.name for f in (result.project_path / "src").glob("*")]
        assert found_src_folders == [result.context["__project_slug_underscore"]]


def test_using_pytest(cookies: Cookies) -> None:
    with bake_in_temp_dir(cookies=cookies) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir(command="pytest tests/test_main.py", path=result.project_path) == 0
