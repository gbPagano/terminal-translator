from pathlib import Path

import toml
from rich.console import Console
from typer import Exit

console = Console()


def get_version(value: bool):
    """Returns the current version of the application."""
    if value:
        path = Path() / "pyproject.toml"
        pyproject = toml.loads(open(str(path)).read())
        version = pyproject["tool"]["poetry"]["version"]
        console.print(f"tt-terminal-translator {version}")
        raise Exit()
