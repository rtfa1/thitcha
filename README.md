# AI Tutor CLI

A minimal CLI scaffold for an AI tutoring assistant. This project will grow into an interactive teaching agent that can generate lesson plans, explanations, and code examples.

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Run

```bash
ai-tutor "Explain Python lists"
```

## Configuration

Edit `config.yaml` and set the API key environment variable listed in `api_key_env`.

## Development

```bash
pip install -e .[dev]
pytest
```
