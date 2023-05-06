import importlib.metadata

from rich.console import Console
from typer import Exit

console = Console()


def get_version(value: bool):
    """Returns the current version of the application."""
    if value:
        version = importlib.metadata.version("tt-terminal-translator")
        console.print(f"tt-terminal-translator {version}")
        raise Exit()
