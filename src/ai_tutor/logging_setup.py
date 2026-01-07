from __future__ import annotations

import logging
from pathlib import Path
import uuid


class RunIdFilter(logging.Filter):
    def __init__(self, run_id: str) -> None:
        super().__init__()
        self.run_id = run_id

    def filter(self, record: logging.LogRecord) -> bool:
        record.run_id = self.run_id
        return True


def setup_logging(level: str = "INFO", log_dir: str = "logs") -> str:
    run_id = uuid.uuid4().hex[:12]
    log_directory = Path(log_dir)
    log_directory.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger()
    logger.handlers.clear()
    logger.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s [%(run_id)s] %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.addFilter(RunIdFilter(run_id))

    file_handler = logging.FileHandler(log_directory / f"run-{run_id}.log")
    file_handler.setFormatter(formatter)
    file_handler.addFilter(RunIdFilter(run_id))

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return run_id
