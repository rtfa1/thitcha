from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys


def test_cli_help() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    env = os.environ.copy()
    env_path = str(repo_root / "src")
    env["PYTHONPATH"] = env_path + os.pathsep + env.get("PYTHONPATH", "")

    result = subprocess.run(
        [sys.executable, "-m", "ai_tutor.cli", "--help"],
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "usage" in result.stdout.lower()
