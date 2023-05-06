from pathlib import Path

import toml
from dynaconf import Dynaconf
from rich.console import Console
from typer import Argument, Option, Typer

from .version import get_version

config_path = Path.home() / ".config" / "terminal_translator" / "credentials.toml"
config_path.parent.parent.mkdir(exist_ok=True)  # create .config/
config_path.parent.mkdir(exist_ok=True)  # create terminal_translator/
config_path.touch()

settings = Dynaconf(
    envvar_prefix="",
    settings_files=[config_path],
)

console = Console()
app_config = Typer(add_completion=False)


@app_config.command()
def configure_credentials(
    project_id: str = Argument(
        ..., help="Project ID of Google Cloud API", show_default=False
    ),
    google_api_credentials: str = Argument(
        ..., help="Path of the json API service key", show_default=False
    ),
    _version: bool = Option(
        None,
        "--version",
        "-V",
        callback=get_version,
        is_eager=True,
        help="Display the current version.",
    ),
):
    set_project_id(project_id)
    set_google_application_credentials(google_api_credentials)


def set_project_id(credential: str) -> None:
    """Receives the project-id as a parameter and puts it in the configuration file

    Args:
        credential (str): project-id
    """
    configs_json = toml.load(config_path)
    configs_json["project_id"] = credential

    configs_toml = toml.dumps(configs_json)
    config_path.write_text(configs_toml)
    console.print("The project id has been set", style="green")


def set_google_application_credentials(json_path: str) -> None:
    """Receives the json_path credentials as a parameter,move the file to the
    configuration directory and update its path in the configuration file

    Args:
        json_path (str): json_path credentials
    """
    json_path = json_path.replace("~", str(Path().home()))
    json_file = Path(json_path)
    json_file.replace(config_path.parent / json_file.name)
    console.print(
        f"The credential file has been moved to: {config_path.parent / json_file.name}",
        style="yellow",
    )

    configs_json = toml.load(config_path)
    configs_json["google_application_credentials"] = str(
        config_path.parent / json_file.name
    )

    configs_toml = toml.dumps(configs_json)
    config_path.write_text(configs_toml)
    console.print("The google aplication credential has been set", style="green")
