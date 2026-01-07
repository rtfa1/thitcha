from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv


@dataclass(frozen=True)
class FeatureFlags:
    os_control: bool
    diagram_output: bool


@dataclass(frozen=True)
class LoggingConfig:
    level: str = "INFO"
    directory: str = "logs"


@dataclass(frozen=True)
class AppConfig:
    model_provider: str
    api_key_env: str
    features: FeatureFlags
    logging: LoggingConfig


def _validate_required_keys(raw: dict[str, Any]) -> None:
    missing: list[str] = []
    if "model_provider" not in raw:
        missing.append("model_provider")
    if "api_key_env" not in raw:
        missing.append("api_key_env")
    if "features" not in raw:
        missing.append("features")
    elif not isinstance(raw["features"], dict):
        raise ValueError("Config key 'features' must be a mapping")
    else:
        for flag in ("os_control", "diagram_output"):
            if flag not in raw["features"]:
                missing.append(f"features.{flag}")

    if missing:
        raise ValueError(f"Missing required config keys: {', '.join(missing)}")


def load_config(path: str | Path) -> AppConfig:
    load_dotenv()
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    raw = yaml.safe_load(config_path.read_text())
    if not isinstance(raw, dict):
        raise ValueError("Config file must contain a mapping at the top level")

    _validate_required_keys(raw)

    features = raw["features"]
    logging_block = raw.get("logging", {})
    logging_cfg = LoggingConfig(
        level=str(logging_block.get("level", "INFO")),
        directory=str(logging_block.get("directory", "logs")),
    )

    return AppConfig(
        model_provider=str(raw["model_provider"]),
        api_key_env=str(raw["api_key_env"]),
        features=FeatureFlags(
            os_control=bool(features["os_control"]),
            diagram_output=bool(features["diagram_output"]),
        ),
        logging=logging_cfg,
    )
