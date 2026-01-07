# Running codex in Docker
This directory contains a Dockerfile for running the
[codex CLI tool](https://www.npmjs.com/package/@openai/codex) in a containerized environment.

```
docker run -it --rm --name codex-cli-session -v "$PWD:/workspace" -v "$HOME/.codex:/home/codex/.codex" --network=bridge codex-cli-3

```
```
docker run --rm \
  -v "$PWD:/workspace" \
  -v "$HOME/.codex:/home/codex/.codex" \
  --network=bridge \
  codex-cli exec \
  --sandbox workspace-write --dangerously-bypass-approvals-and-sandbox --skip-git-repo-check --cd /workspace \
  "crie uma pasta chamada teste2 na raiz do workspace e dentro dela crie um arquivo README.md com o texto 'Este é um teste' "
```
```
docker run --rm -it \
  -v "$PWD:/workspace" \
  -v "$HOME/.codex:/home/codex/.codex" \
  --network=bridge \
  bash
```
