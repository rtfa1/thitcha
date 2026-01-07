# AI Tutor Agent Prototype - Development Plan

## 1. Goal and Success Criteria

### Goal
Deliver a local, Python-based AI tutor agent prototype that teaches through action: answering questions, creating code examples, controlling VS Code, and producing simple diagrams.

### Success Criteria
- User can ask a C++ question and receive a short lesson plan, explanation, and a runnable code example.
- Agent can open VS Code, create a file, and write the example step-by-step with narration.
- Agent can output a text-based diagram (Mermaid) related to the lesson.
- Safety confirmations appear before any OS-level action.
- All actions are logged and reproducible.

---

## 2. Scope

### In Scope (Prototype)
- Single-subject focus (C++ basics).
- CLI-driven interaction.
- Basic lesson planning and teaching flow.
- VS Code automation (open, create file, type code).
- Text-only diagrams (Mermaid in markdown).
- Local file and log management.

### Out of Scope (For Now)
- Full autonomous OS control.
- Rich GUI or web UI.
- Multi-user support.
- Real-time screen understanding.
- Performance tuning.

---

## 3. Architecture Overview

### Components
1. Pedagogical Planner
   - Converts question to a simple lesson plan.
2. LLM Reasoning Core
   - Generates explanations and code.
3. Tool Router
   - Maps intents to actions (edit file, open VS Code, render diagram).
4. OS/App Controller
   - Automates VS Code via OS tooling (pyautogui/pynput or AppleScript).
5. Visual Presenter
   - Produces Mermaid diagrams in markdown.
6. Safety Layer
   - Requires confirmation before OS actions.

### Data Flow (High Level)
User Question -> Plan -> Actions -> Explanation + Code + Diagram -> Follow-up

---

## 4. Technology Stack

- Language: Python 3.11+
- LLM SDK: OpenAI or Anthropic SDK (select one for prototype)
- UI Automation: pyautogui or pynput; AppleScript where needed
- Diagrams: Mermaid (markdown output)
- Logging: Python logging + simple JSON trace

---

## 5. Phased Plan

### Phase 0 - Repo and Dev Setup (Day 1)
- Set up Python project structure.
- Add basic configuration and logging.
- Define prompt templates for teaching and lesson planning.

Deliverables
- Minimal runnable CLI skeleton.
- Logging and config file.

### Phase 1 - Lesson Planning and Teaching Output (Days 2-3)
- Implement Pedagogical Planner.
- Implement LLM Reasoning Core.
- Generate explanation, code example, and Mermaid diagram.

Deliverables
- CLI command: ask question -> outputs lesson plan, explanation, code, diagram.

### Phase 2 - Tool Router and File Ops (Days 4-5)
- Implement tool router actions: create file, write code, open file.
- Add safety confirmations before actions.

Deliverables
- Agent can create a local file with the generated code.
- Confirmations required for all file writes.

### Phase 3 - VS Code Automation (Days 6-7)
- Add OS control to open VS Code and type code step-by-step.
- Add fallback for manual steps if automation fails.

Deliverables
- Agent can open VS Code and populate file with code.

### Phase 4 - Polishing and Demo Flow (Days 8-9)
- Add structured logs and replayable traces.
- Create demo script and sample questions.

Deliverables
- End-to-end demo on one C++ topic.

---

## 6. Detailed Tasks

### 6.1 Project Setup
- Create directories: src/, docs/, tests/, examples/.
- Add config file for model settings and tool toggles.
- Add logging utilities.

### 6.2 Prompting and Planning
- Create prompts for lesson plan, explanation, and follow-up.
- Add guardrails for scope and brevity.

### 6.3 Tool Router
- Define actions: open_editor, create_file, write_code, render_diagram.
- Implement safety confirmation for each action.

### 6.4 OS Control
- Implement VS Code open and focus.
- Implement typing code with delays and section highlights.
- Add fallbacks for manual steps.

### 6.5 Visual Output
- Generate Mermaid code block based on lesson.
- Save diagram in markdown output.

### 6.6 Logging and Trace
- Log inputs, decisions, and actions with timestamps.
- Store in a local trace file for demo replay.

---

## 7. Risks and Mitigations

- OS automation brittle -> Provide fallback instructions and manual mode.
- LLM output variability -> Use prompt constraints and templates.
- Safety concerns -> Require explicit confirmation for each action.
- VS Code focus issues -> Detect failures, provide manual fallback.

---

## 8. Testing and Validation

### Manual Tests
- Ask a C++ question and verify lesson plan output.
- Confirm code example compiles and runs.
- Verify VS Code automation works on target machine.

### Smoke Test Checklist
- CLI runs without errors.
- Logs saved correctly.
- Mermaid output renders in markdown.
- Safety confirmations triggered.

---

## 9. Deliverables Summary

- CLI prototype (Python).
- Lesson plan output with explanation, code, and diagram.
- VS Code automation and file creation.
- Logging and demo script.

---

## 10. Next Steps (After Prototype)

- Add browser-based visual canvas.
- Improve interactive questioning.
- Add basic screen understanding.
