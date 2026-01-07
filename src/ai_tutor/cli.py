from __future__ import annotations

import argparse
import logging
import sys

from ai_tutor.config import load_config
from ai_tutor.logging_setup import setup_logging


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="AI Tutor CLI scaffold.",
    )
    parser.add_argument(
        "question",
        nargs="?",
        help="Question to ask the tutor.",
    )
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to the configuration file.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        config = load_config(args.config)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Config error: {exc}", file=sys.stderr)
        return 1

    setup_logging(level=config.logging.level, log_dir=config.logging.directory)
    logger = logging.getLogger("ai_tutor.cli")
    logger.info("Loaded config for provider %s", config.model_provider)

    if args.question:
        response = f"Placeholder response for: {args.question}"
        print(response)
    else:
        print("No question provided. Use --help for usage.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
