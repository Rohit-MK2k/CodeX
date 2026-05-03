<div align="center">

# ⬡ CodeX

### AI Codebase Onboarding Agent

**Chat with any codebase. Understand it fast.**

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

</div>

---

## What is CodeX?

CodeX is a **local, privacy-first AI tool** that lets you understand any codebase through plain English questions.

Point it at a repo. Ask anything. Get answers with exact file and line citations — instantly openable in your editor.

Built for developers who:
- Join a new company and need to ramp up fast
- Explore an open source project they've never seen
- Return to their own code written months ago

> CodeX turns days of codebase exploration into minutes.

---

## The Problem

Understanding an unfamiliar codebase takes days — sometimes weeks. You jump between files, grep for function names, and still miss the big picture.

Existing AI tools like Copilot or ChatGPT help you *write* new code. None of them help you *understand* existing code — especially not offline, privately, and cleanly.

---

## Features

### CLI — Index any repo with one command

```bash
codex index .
```

- Scans your repo and understands its structure
- Shows a live progress bar while indexing
- Automatically respects `.gitignore`
- Skips junk folders like `node_modules`, `dist`, `__pycache__`
- Opens your browser automatically when done

Other commands:

```bash
codex index <path>        # Index a repo at a specific path
codex index . --refresh   # Re-index after code changes
codex list                # See all indexed repos with stats
codex remove <name>       # Remove a repo from the index
codex start               # Start the local server + open browser
codex stop                # Stop the server
```

---

### Chat UI — Ask anything about your codebase

Everything happens in the browser. No data leaves your machine.

**Repo Selector**
- View all indexed repos in a card layout
- See stats: total chunks, detected language, last indexed date
- Switch repos in one click

**Chat & Q&A**
- Ask questions in plain English
- Answers stream word-by-word in real time
- Every answer includes **file + line number citations**
- Click a citation → jumps to that exact line in your editor
- Follow-up questions are context-aware — not one-shot

**Multiple Chat Sessions**
- Create independent sessions per repo (e.g. "Auth flow", "Payment pipeline")
- Fully persisted history — continue any session anytime
- Delete sessions you no longer need

**File Tree Panel**
- Browse the full repo structure in a sidebar
- Click any file → auto-asks "Explain this file"

**Model Switcher**
- Switch AI provider mid-conversation:
  - **Claude** (Anthropic) — best reasoning quality
  - **GPT-4o** (OpenAI) — fast and reliable
  - **Ollama** (local) — fully offline, zero API cost

---

### Editor Integration — Click to open at exact line

When CodeX cites a file and line number, you can click it. It opens your editor at that exact location.

| Editor | Command used |
|--------|-------------|
| VS Code | `code --goto auth/jwt.py:42` |
| Cursor | `cursor --goto auth/jwt.py:42` |
| Zed | `zed auth/jwt.py:42` |

Without this — citations are just text. With this — one click and you're exactly where you need to be.

---

### Privacy First

- Everything runs locally on your machine
- No data is sent anywhere (unless you use a cloud LLM like Claude or GPT-4o — your choice)
- API keys are stored in a local `config.toml` file — never transmitted
- Full offline mode available via Ollama

---

### Settings

- Add and update API keys (Anthropic, OpenAI)
- Set your default LLM and embedding model
- Set your default editor (VS Code, Cursor, or Zed)
- Configure folders to skip during indexing

---

## Offline Mode

CodeX works fully offline with [Ollama](https://ollama.ai). No internet. No API costs. Just run Ollama locally and select it as your provider.
