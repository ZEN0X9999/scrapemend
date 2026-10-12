from typer.testing import CliRunner

import scrapemend
from scrapemend.cli import app

runner = CliRunner()


def test_version_is_set() -> None:
    assert scrapemend.__version__


def test_cli_version_flag() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert scrapemend.__version__ in result.output


def test_cli_version_command() -> None:
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert scrapemend.__version__ in result.output
