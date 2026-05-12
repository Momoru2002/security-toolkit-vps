import yaml
from pathlib import Path

CONFIG_PATH = Path("config/default.yml")


def load_config():

    if not CONFIG_PATH.exists():
        return {}

    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)