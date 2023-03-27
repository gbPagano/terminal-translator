from dynaconf import Dynaconf
from pathlib import Path
import toml
from rich.console import Console
from typer import Typer, Argument

config_path = Path.home() / ".config" / "terminal_translator" / "credentials.toml"
config_path.parent.mkdir(exist_ok=True)
config_path.touch()

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[config_path],
)

console = Console()
app_config = Typer(add_completion=False)


@app_config.command()
def configure_credentials(
    project_id: str = Argument(..., help="Project ID of Google Cloud API", show_default=False),
    google_api_credentials: str = Argument(..., help="Path of the json API service key", show_default=False),
):
    set_project_id(project_id)
    set_google_aplication_credentials(google_api_credentials)


def set_project_id(credential: str) -> None:
    configs_json = toml.load(config_path)
    configs_json["project_id"] = credential
    
    configs_toml = toml.dumps(configs_json)
    config_path.write_text(configs_toml)
    console.print("The project id has been set", style="green")


def set_google_aplication_credentials(json_path: str) -> None:
    json_path = json_path.replace("~", str(Path().home()))
    json_file = Path(json_path)
    json_file.replace(config_path.parent / json_file.name)
    console.print(f"The credential file has been moved to: {config_path / json_file.name}", style="yellow")

    configs_json = toml.load(config_path)
    configs_json["google_aplication_credentials"] = str(config_path.parent / json_file.name)
    
    configs_toml = toml.dumps(configs_json)
    config_path.write_text(configs_toml)
    console.print("The google aplication credential has been set", style="green")



