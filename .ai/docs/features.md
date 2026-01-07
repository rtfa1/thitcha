# Features / Modules for Task Grouping

This document groups the prototype scope into features/modules so tasks can be assigned by context.

## 1. Foundation and Runtime
Scope: project scaffold, config loading, CLI entry point, logging basics.
- Includes: repo structure, config file format, env handling, run session ID.

## 2. Pedagogical Planning
Scope: convert user question into a short teaching plan and learning goals.
- Includes: planner prompt, structured plan output, guardrails for scope.

## 3. LLM Teaching Core
Scope: generate explanations, code examples, and follow-up questions from the plan.
- Includes: model interface, prompt templates, output validation.

## 4. Teaching Flow Orchestration (CLI)
Scope: end-to-end CLI flow that runs planner -> LLM -> outputs lesson, code, diagram.
- Includes: command interface, output formatting, basic error handling.

## 5. Tool Routing and File Operations
Scope: map intents to actions, create/write/open files, confirm before changes.
- Includes: tool router, safety confirmation prompts, file IO utilities.

## 6. IDE Automation (VS Code)
Scope: open VS Code, focus editor, and type code step-by-step with fallback.
- Includes: OS automation layer, retries, manual fallback instructions.

## 7. Visual Explanations (Mermaid)
Scope: generate text-based diagrams and include them in outputs.
- Includes: Mermaid template prompt, markdown rendering, saving artifacts.

## 8. Observability and Traceability
Scope: structured logging and JSON traces for replay and debugging.
- Includes: log schema, trace file writer, run metadata.

## 9. Demo and Validation Assets
Scope: demo script, sample prompts, and manual verification checklist.
- Includes: sample C++ questions, expected outputs, smoke steps.

## 10. Safety and Confirmation Layer (Cross-Cutting)
Scope: user confirmations before OS-level actions and destructive changes.
- Includes: dry-run mode, confirmation UX, safety guardrails.

## 11. Visual/UI Future Extensions (Out of Scope for Prototype)
Scope: browser canvas, IDE extensions, vision-based screen understanding.
- Includes: phase 2/3 ideas for future grouping.
