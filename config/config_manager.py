"""Simple configuration management for TriptaFittings.

This module provides a minimal persistent configuration system that
stores user preferences in a JSON file.  It aims to satisfy the
requirements of issue #9 by allowing the plugin to remember settings
such as units, supported standards and export options.
"""
from __future__ import annotations

from pathlib import Path
import json
from typing import Any, Dict


class ConfigurationManager:
    """Manage plugin configuration stored in a JSON file.

    Parameters
    ----------
    config_file:
        Path to the configuration file.  If ``None`` a file named
        ``triptafittings_config.json`` is created in the current
        working directory.
    """

    DEFAULT_CONFIG: Dict[str, Any] = {
        "units": "mm",
        "standards": ["DIN_32676_A"],
        "export_formats": ["STEP", "DXF"],
        "validation_level": "strict",
        "auto_backup": True,
        "backup_interval": 24,  # hours
        "simulation_enabled": False,
        "documentation_language": "en",
    }

    def __init__(self, config_file: str | Path | None = None) -> None:
        self.config_file = Path(config_file) if config_file else Path(
            "triptafittings_config.json"
        )
        self.config: Dict[str, Any] = {}
        self.load_configuration()

    # ------------------------------------------------------------------
    def load_configuration(self) -> None:
        """Load configuration from disk or create defaults.

        If the file does not exist it is created with the default
        configuration.
        """

        try:
            with self.config_file.open("r", encoding="utf-8") as fh:
                self.config = json.load(fh)
        except FileNotFoundError:
            self.config = self.DEFAULT_CONFIG.copy()
            # Ensure parent directory exists before saving
            if not self.config_file.parent.exists():
                self.config_file.parent.mkdir(parents=True, exist_ok=True)
            self.save_configuration()

    # ------------------------------------------------------------------
    def save_configuration(self) -> None:
        """Persist current configuration to disk."""
        with self.config_file.open("w", encoding="utf-8") as fh:
            json.dump(self.config, fh, indent=2)

    # ------------------------------------------------------------------
    def get_setting(self, key: str, default: Any | None = None) -> Any:
        """Return a configuration value."""
        return self.config.get(key, default)

    # ------------------------------------------------------------------
    def set_setting(self, key: str, value: Any) -> None:
        """Update a configuration value and save to disk."""
        self.config[key] = value
        self.save_configuration()
