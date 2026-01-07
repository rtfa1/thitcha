# AI Tutor Agent Prototype – Technical Blueprint

## 1. Vision

Build a **local AI tutor agent** capable of teaching technical subjects (e.g. C++) by **actively interacting with the user's computer**, behaving similarly to a human tutor or pair programmer.

The agent should:
- Answer questions verbally/textually
- Create and edit real code examples
- Open and control developer tools (e.g. VS Code)
- Present visual explanations (diagrams, memory layouts, flows)
- Blend explanation + action into a teaching experience

This is **not** a passive chatbot. It is an **agentic, environment-aware tutor**.

---

## 2. Core Concept

The prototype focuses on **teaching through action**:

Example scenario:
1. User asks: "What are C++ references?"
2. Agent plans a lesson
3. Agent opens VS Code
4. Agent creates a small `references.cpp`
5. Agent writes and explains code step-by-step
6. Agent optionally draws a memory diagram
7. Agent asks follow-up questions

This mimics **pair programming + whiteboard teaching**.

---

## 3. Why This Does Not Fully Exist Yet

- Full OS-level AI control is still risky and experimental
- Safety, permissions, and UX constraints block mainstream adoption
- Existing tools focus on *assistance*, not *teaching*

However, **all technical building blocks already exist**.

---

## 4. Recommended Prototyping Language

### ✅ Primary Language: **Python**

Python is chosen because it excels at:
- LLM orchestration
- Tool calling
- OS automation
- Rapid iteration
- Vision + screen analysis

Python is ideal for **exploration and prototyping**, not final polish.

---

## 5. High-Level Architecture

```
Python Agent
│
├─ Pedagogical Planner
├─ LLM Reasoning Core
├─ Tool Router
├─ OS / App Controller
├─ Visual Presenter
└─ Safety & Confirmation Layer
```

Each component can start simple and evolve.

---

## 6. Key Responsibilities

### 6.1 Pedagogical Planner
- Converts user questions into a lesson plan
- Decides:
  - explain only
  - code example
  - visual explanation
  - interactive exercise

### 6.2 LLM Reasoning Core
- Generates explanations
- Decides next steps
- Reflects on user feedback

### 6.3 Tool Router
Maps intent → concrete action:
- open editor
- create file
- write code
- draw diagram
- ask question

### 6.4 OS / App Controller
Controls the local environment:
- Open VS Code
- Create files
- Type code
- Highlight sections

Possible tools:
- `pyautogui`
- `pynput`
- OS scripting (AppleScript on macOS)

### 6.5 Visual Presenter
- Generates diagrams (memory, flow, architecture)
- Uses:
  - Mermaid
  - PlantUML
  - SVG / PNG exports
- Optionally opens browser-based canvases

### 6.6 Safety Layer
- No silent actions
- Confirmation before OS-level changes
- Dry-run / simulation mode

---

## 7. Example Teaching Flow (C++)

```
User Question
   ↓
Lesson Plan
   ↓
Code Example Generation
   ↓
VS Code Interaction
   ↓
Step-by-step Explanation
   ↓
Optional Diagram
   ↓
Follow-up Question
```

---

## 8. Initial Tooling Stack

### Python Libraries
| Purpose | Tool |
|------|------|
| LLM | OpenAI / Anthropic SDK |
| UI automation | pyautogui / pynput |
| Screen capture | mss / pillow |
| Diagrams | Mermaid / graphviz |
| Browser control | Playwright |
| File ops | pathlib / os |

---

## 9. What the First Prototype Should Do

**Week 1 Goals:**
- CLI-based agent
- Single-subject teaching (e.g. C++)
- Controlled VS Code interaction
- File generation + explanation
- Text-only diagrams (Mermaid)

Focus on:
- Flow
- Believability
- Teaching clarity

Not polish.

---

## 10. What Is Explicitly Out of Scope (for now)

- Full autonomous OS control
- Background execution without user approval
- Perfect UX
- Performance optimization
- Multi-user support

---

## 11. Future Evolution Path

### Phase 2
- Visual canvas UI (browser / Electron)
- IDE extensions
- More interactive questioning

### Phase 3
- Vision-based screen understanding
- Adaptive difficulty
- Multi-agent teaching roles

---

## 12. Long-Term Vision

A **true AI tutor** that:
- Teaches by doing
- Sees what the user sees
- Acts like a human mentor
- Combines language, code, and visuals seamlessly

This prototype is the **first concrete step** toward that future.

---

## 13. Guiding Principle

> "The agent should never just explain — it should *show* and *do*."

