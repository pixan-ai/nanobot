"""Configuration loading utilities."""

import json
import os
from pathlib import Path

from pydantic.alias_generators import to_camel

from nanobot.config.schema import Config


# Global variable to store current config path (for multi-instance support)
_current_config_path: Path | None = None


def set_config_path(path: Path) -> None:
    """Set the current config path (used to derive data directory)."""
    global _current_config_path
    _current_config_path = path


def get_config_path() -> Path:
    """Get the configuration file path."""
    if _current_config_path:
        return _current_config_path
    return Path.home() / ".nanobot" / "config.json"


def load_config(config_path: Path | None = None) -> Config:
    """
    Load configuration from file or create default.

    Environment variables with the ``NANOBOT_`` prefix override values
    loaded from the config file, following the standard precedence:
    env vars > config file > defaults.

    Args:
        config_path: Optional path to config file. Uses default if not provided.

    Returns:
        Loaded configuration object.
    """
    path = config_path or get_config_path()

    if path.exists():
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            data = _migrate_config(data)
            _apply_env_overrides(data)
            return Config.model_validate(data)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Warning: Failed to load config from {path}: {e}")
            print("Using default configuration.")

    return Config()


def save_config(config: Config, config_path: Path | None = None) -> None:
    """
    Save configuration to file.

    Args:
        config: Configuration to save.
        config_path: Optional path to save to. Uses default if not provided.
    """
    path = config_path or get_config_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    data = config.model_dump(by_alias=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def _apply_env_overrides(data: dict) -> None:
    """Apply ``NANOBOT_*`` environment variables on top of *data*.

    ``Config.model_validate()`` bypasses pydantic-settings' env-var
    loading, so env vars are silently ignored when a config file exists.
    This function injects matching env vars into the raw dict **before**
    validation, giving them precedence over file values.

    Variable format: ``NANOBOT_<SECTION>__<SUBSECTION>__<FIELD>=value``
    Example: ``NANOBOT_PROVIDERS__DEEPSEEK__API_KEY=sk-xxx``
    """
    prefix = "NANOBOT_"
    delimiter = "__"

    for key, value in os.environ.items():
        if not key.startswith(prefix) or not value:
            continue

        parts = key[len(prefix):].lower().split(delimiter)
        if not parts:
            continue

        # Walk the dict tree, creating intermediate dicts as needed.
        d = data
        for part in parts[:-1]:
            camel = to_camel(part)
            if camel in d:
                next_d = d[camel]
            elif part in d:
                next_d = d[part]
            else:
                d[camel] = {}
                next_d = d[camel]
            if not isinstance(next_d, dict):
                break
            d = next_d
        else:
            # Set the leaf value, respecting whichever key style the
            # config file already uses (camelCase or snake_case).
            leaf = parts[-1]
            camel_leaf = to_camel(leaf)
            if camel_leaf in d:
                d[camel_leaf] = value
            elif leaf in d:
                d[leaf] = value
            else:
                d[camel_leaf] = value


def _migrate_config(data: dict) -> dict:
    """Migrate old config formats to current."""
    # Move tools.exec.restrictToWorkspace → tools.restrictToWorkspace
    tools = data.get("tools", {})
    exec_cfg = tools.get("exec", {})
    if "restrictToWorkspace" in exec_cfg and "restrictToWorkspace" not in tools:
        tools["restrictToWorkspace"] = exec_cfg.pop("restrictToWorkspace")
    return data
