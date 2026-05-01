# Setup Guide

Full installation instructions for all operating systems.

---

## Prerequisites

| Requirement | Minimum version | How to check |
|---|---|---|
| Python | 3.10 | `python --version` |
| Git | Any | `git --version` |
| Anthropic API key | Optional | — |

The QA scorer runs without an API key. The API key is only needed if you extend the system to use Claude for coaching note generation.

---

## Setup

**macOS / Linux:**
```bash
git clone https://github.com/alexandros-alexakis/ai-customer-support-qa.git
cd ai-customer-support-qa
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows (Command Prompt):**
```
git clone https://github.com/alexandros-alexakis/ai-customer-support-qa.git
cd ai-customer-support-qa
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Activate the virtual environment every new terminal session before running any commands.**

---

## Validate

```bash
python run_qa.py --demo
pytest tests/ -v
```

Both should pass with no errors.

---

## Common issues

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | Activate venv: `source venv/bin/activate` |
| `python: command not found` | Use `python3` instead |
| Tests fail with import error | Run pytest from the project root directory |

See [quickstart.md](quickstart.md) for usage examples.
