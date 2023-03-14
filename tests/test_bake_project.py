from contextlib import contextmanager


PROJECT_NAME = "Python Cookiecutter"
PROJECT_SLUG = PROJECT_NAME.lower().replace(" ", "_").replace("-", "_")
CONFIG_TOML = "pyproject.toml"


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    assert result.exception is None
    yield result


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert CONFIG_TOML in found_toplevel_files
        assert PROJECT_SLUG in found_toplevel_files
        assert "tests" in found_toplevel_files
