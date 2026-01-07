# Project Setup and CLI Skeleton

description: Create the Python project scaffold, config loading, and logging utilities. Add a minimal CLI entry point to run the agent.
priority: High
depends_on: none
features: Foundation and Runtime
status: done

## Steps
1. Create base folders: `src/`, `tests/`, `examples/`, `docs/`, `logs/`.
2. Add project metadata files: `README.md`, `LICENSE`, `CHANGELOG.md`, and `CODE_OF_CONDUCT.md` (minimal templates are fine).
3. Add packaging and tooling config in `pyproject.toml` (dependencies, CLI entry point, lint/format settings).
4. Add a minimal CLI entry point (e.g., `src/cli.py`) that accepts a question and prints a placeholder response.
5. Add config loading (e.g., `config.yaml` plus `.env.example`) with model/provider and feature toggles.
6. Add logging setup with console + file output and a consistent log format; default log path under `logs/`.
7. Add a minimal `pytest` smoke test for the CLI.
8. Wire CLI to load config, validate it, and initialize logging on startup.

## Details
- Suggested structure:
  - `src/` for app code.
  - `tests/` for unit tests and smoke checks.
  - `examples/` for sample prompts and outputs.
  - `docs/` for developer notes.
  - `logs/` for local run logs.
- Metadata expectations:
  - `README.md` includes install, run, and basic usage examples.
  - `LICENSE` is explicit MIT.
  - `CHANGELOG.md` can start with an "Unreleased" section.
  - `CODE_OF_CONDUCT.md` can reference Contributor Covenant.
- Packaging expectations:
  - `pyproject.toml` defines build system and optional dev dependencies.
  - Provide a CLI entry point (e.g., `ai-tutor`).
- Config should support:
  - Model/provider name.
  - API key env var name.
  - Feature flags for OS control and diagram output.
- Config validation:
  - Fail fast with a clear error message if required keys are missing.
- Logging should capture:
  - Timestamp, level, module, message.
  - A run/session id for correlating later tasks.
- Testing expectations:
  - One smoke test that exercises `--help` or a dry-run path.

## Guidelines
- Keep the CLI simple; avoid adding features from later phases.
- Use clear defaults so the CLI runs with a minimal config file.
- Prefer dependency-light libraries unless required.
- Keep file paths relative to the project root.
- Add minimal doc comments only where the flow is non-obvious.
- Ensure the project is installable via `pip` or `pipx` from the repo root.

## Updates
- Added project scaffold with CLI, config loading, logging, and smoke test.
- Created metadata files, config templates, and base directories.
