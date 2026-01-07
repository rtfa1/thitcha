# Instructions for AI Assistants
The folder `.ai` contains all relevant files for AI assistants to operate effectively within this project. Below are the key instructions and guidelines for using these files.

## Global Instructions
1. **Familiarize Yourself with Documentation**: Before engaging with users, thoroughly read the documentation files in the `docs/` directory to understand the project's goals, architecture, and development plans.
2. **Do Not Use `.ai` for Product Code or Artifacts**: The `.ai` directory is for assistant metadata only. All project code, logs, configs, and artifacts must live in the workspace root (e.g., `src/`, `docs/`, `tests/`, `examples/`) and not under `.ai/`.

## Files and Directories
- `instructions.md`: This file (you are reading it now) contains instructions for AI assistants on how to utilize the other files in the `.ai` directory.

- `./.ai/docs/`: This directory contains documentation files related to the AI assistant's functionality and development.

- `./.ai/docs/features.md`: This file outlines the features and modules for task grouping, providing a structured overview of the project's scope and related tasks.

- `./.ai/docs/development-plan.md`: This file outlines the development plan for building an AI assistant that can teach programming concepts, generate code examples, and create diagrams. It includes sections on architecture, technology stack, and a phased development plan.

- `./.ai/board/`: This directory is intended for tracking tasks, issues, and feature requests. 

- `./.ai/board/board.json`: This file contains metadata about the task board, including the project name, description, and version.

- `./.ai/board/tasks`: This directory is intended for tracking tasks, issues, and feature requests. Each file within this directory represents a specific task or issue. 

- `./.ai/board/tasks/archived/`: This subdirectory contains archived tasks and issues that have been completed or are no longer active.

- ./.ai/board/progress/: This subdirectory contains progress/logs of actions taken on tasks and issues, providing a history of changes and updates.

- `./.ai/board/progress/progress.txt`: This file contains a chronological progress/log of all actions taken on tasks and issues within the `./.ai/board/` directory.

## Working with Tasks
1. **Understanding Task Files**: Each task file in the `.ai/board/tasks/` directory follows a structured format, including sections for description, priority, dependencies, status, steps, details, and guidelines. Familiarize yourself with this format to effectively manage and execute tasks.
2. **Task Statuses**: Tasks can have various statuses such as `todo`, `in-progress`, and `done`. Ensure to update the status of tasks as you work on them.
3. **Dependencies**: Some tasks may depend on the completion of other tasks. Pay attention to the `depends_on` field to understand task dependencies and plan your work accordingly.
4. **Logging Actions**: Maintain a log of all actions taken on tasks in the `.ai/board/progress/progress.txt` file to ensure transparency and traceability of changes.
5. **Archiving Completed Tasks**: Once a task is completed, change its status to `done` in the task file and in the board.json file.
