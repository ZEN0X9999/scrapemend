"""Command-line interface. Commands (run / check / heal / diff / promote) land in later phases."""

from typing import Annotated

import typer

from scrapemend import __version__

app = typer.Typer(
    name="scrapemend",
    help="Self-healing scraper engine.",
    no_args_is_help=True,
    add_completion=False,
)


def _print_version(value: bool) -> None:
    if value:
        typer.echo(f"scrapemend {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            callback=_print_version,
            is_eager=True,
            help="Show the version and exit.",
        ),
    ] = False,
) -> None:
    """Self-healing scraper engine."""


@app.command()
def version() -> None:
    """Show the version."""
    typer.echo(f"scrapemend {__version__}")
