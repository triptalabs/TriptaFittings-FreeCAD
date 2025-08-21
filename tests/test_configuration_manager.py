import json
from pathlib import Path

from config.config_manager import ConfigurationManager


def test_loads_default_config_and_creates_file(tmp_path):
    config_path = tmp_path / "config.json"
    mgr = ConfigurationManager(config_file=config_path)

    # File should be created with default config
    assert config_path.exists()
    assert mgr.get_setting("units") == "mm"
    # Ensure contents in file match what manager has
    data = json.loads(config_path.read_text())
    assert data == mgr.config


def test_set_and_persist_configuration(tmp_path):
    config_path = tmp_path / "config.json"
    mgr = ConfigurationManager(config_file=config_path)

    mgr.set_setting("units", "inch")
    assert mgr.get_setting("units") == "inch"

    # Reload from disk and ensure persistence
    mgr2 = ConfigurationManager(config_file=config_path)
    assert mgr2.get_setting("units") == "inch"

    # Unknown keys should return default value if provided
    assert mgr2.get_setting("missing", "default") == "default"
