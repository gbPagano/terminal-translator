from dynaconf import Dynaconf
from pathlib import Path
import toml

config_path = Path.home() / ".config" / "terminal_translator" / "credentials.toml"
config_path.parent.mkdir(exist_ok=True)
config_path.touch()

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[config_path],
)


def set_project_id(credential: str) -> None:
    configs_json = toml.load(config_path)
    configs_json["project_id"] = credential
    
    configs_toml = toml.dumps(configs_json)
    config_path.write_text(configs_toml)


def set_google_aplication_credentials(json_path: str) -> None:
    json_file = Path(json_path)
    json_file.replace(config_path.parent / json_file.name)
    print("The credential file has been moved to:", config_path / json_file.name)

    configs_json = toml.load(config_path)
    configs_json["google_aplication_credentials"] = str(config_path.parent / json_file.name)
    
    configs_toml = toml.dumps(configs_json)
    config_path.write_text(configs_toml)


