#!/bin/bash
set -euo pipefail

if [ -z "${1-}" ]; then
  echo "Usage: $0 <iterations>"
  exit 1
fi

for ((i=1; i<=$1; i++)); do
  # Build the prompt (keeps the original instructions and references to repo files)
  read -r -d '' PROMPT <<'EOF' || true
YOUR MAIN INSTRUCTIONS ARE LOCATED IN THE FILE: /workspace/.ai/instructions.md 
READ THAT FILE FIRST
1. Find the highest priority task to work on and focus solely on that task until completion. This should be the one YOU decide has the highest priority, not necessarily the first one on the list.
2. Check if the tests are passing. 
3. Update the board.json file to reflect the current status of tasks.
4. Update the task file with the work that was done.
5. Append you progress to the progress.txt file. Use this to leave notes for yourself and others working in the codebase.
6. Make a git commit with a meaningful message about the work that was done.
ONLY WORK ON ONE TASK AT A TIME.
If, while implementing a task, you find that there is a blocking issue (e.g., a dependency that needs to be resolved, or a question that needs answering), make a note of it in progress.txt and move on to the next highest priority task.
If, while working on a task, you notice the status is done, output <task>DONE</task> and exit.
EOF

  # Run `codex` inside the Docker image, mounting the repo and config.
  # Do NOT allocate a TTY (-t) when running from a non-interactive script; use -i only.
  # Use the non-interactive `exec` subcommand so Codex does not require a TTY
  result=$(docker run --rm \
  -v "$PWD:/workspace" \
  -v "$HOME/.codex:/home/codex/.codex" \
  --network=bridge \
  codex-cli exec \
  --sandbox workspace-write --dangerously-bypass-approvals-and-sandbox --skip-git-repo-check --cd /workspace \
  "$PROMPT")

  echo "$result"

  if [[ "$result" == *"<task>DONE</task>"* ]]; then
    echo "Done, exiting."
    exit 0
  fi
done