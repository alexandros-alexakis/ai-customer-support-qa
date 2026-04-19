# Player Care QA and Coaching System

![Status: Prototype](https://img.shields.io/badge/status-prototype-yellow)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

---

> **A QA scoring, CSAT analysis, and coaching toolkit for gaming player care teams. Designed to work alongside the [Player Care AI Support Agent](https://github.com/alexandros-alexakis/ai-customer-support-agent) but runs independently on any support interaction.**
>
> **Alexandros Alexakis**, Vendor Manager and L&D Lead, Player Care

---

## Part of a two-repo toolkit

This repo handles **what comes after the interaction**: scoring, CSAT analysis, and coaching.

The companion repo handles the **intake layer**: triage, escalation, routing, and response strategy.

| Repo | What it does |
|---|---|
| [ai-customer-support-agent](https://github.com/alexandros-alexakis/ai-customer-support-agent) | Detects urgency, identifies VIP players, routes to the right team, generates response strategy |
| [ai-customer-support-qa](https://github.com/alexandros-alexakis/ai-customer-support-qa) (this repo) | Scores interactions, analyses low CSAT, assigns responsibility, generates coaching notes |

The agent produces the interaction. This system evaluates it.

---

## What this is

A working prototype that takes a support interaction and tells you three things:

1. **Was the process correct?** QA scoring across six dimensions: routing, information collection, tone, scope compliance, accuracy, and player experience.
2. **Why was the player unhappy?** When CSAT comes back below 4 stars, the system analyses which dimension failed and who is responsible: the AI triage, the agent, the policy, or nobody.
3. **What should change?** Specific coaching notes per agent and per failure pattern. Separate tracks for AI/system improvements vs human coaching vs policy gaps.

---

## What this is not

- A deployed production system
- A live integration with Zendesk, Klaus, or any QA platform
- A replacement for human QA judgment
- A performance management tool

Every score this system produces is a starting point for a human conversation, not a verdict.

---

## The responsibility split

| What went wrong | Responsibility | Action |
|---|---|---|
| AI triage routed to wrong team | System / AI | Update escalation rules in [agent repo](https://github.com/alexandros-alexakis/ai-customer-support-agent/issues/new/choose) |
| AI gave wrong information | System / KB | Update knowledge base in [agent repo](https://github.com/alexandros-alexakis/ai-customer-support-agent/issues/new/choose) |
| Agent had correct triage but poor response | Agent | Human coaching |
| Policy made a good outcome impossible | Leadership / Ops | Policy review |
| Player was always going to be unhappy | None | Document, no action |

Coaching an agent for a failure caused by a bad AI triage is not just useless, it is actively harmful.

---

## Quickstart

```bash
git clone https://github.com/alexandros-alexakis/ai-customer-support-qa.git
cd ai-customer-support-qa
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python run_qa.py --demo
```

---

## Run modes

```bash
# Demo
python run_qa.py --demo

# Score your own interaction
python run_qa.py --ticket "Player message" --response "Agent response" --csat 3

# Weekly report
python run_qa.py --report --agent agent_001 --week 2024-W15

# Run tests
pytest tests/ -v
```

---

## Documentation

**Getting started**
- [Quickstart](docs/setup/quickstart.md)

**Understanding the system**
- [QA framework](docs/guides/qa-framework.md) - full scoring model with 5 categories and fatal errors
- [Scoring dimensions](docs/guides/scoring-dimensions.md) - the 6-dimension automated scorer explained
- [Failure pattern library](docs/guides/failure-patterns.md) - known failure types with causes and actions
- [Failure analysis](docs/guides/failure-analysis.md) - 10 detailed failure modes with impact and mitigations

**Operations**
- [CSAT analysis guide](docs/operations/csat-analysis.md) - how to use the CSAT analyser and act on results
- [CSAT bias analysis](docs/operations/csat-bias-analysis.md) - why comparing AI vs human CSAT directly is misleading
- [Coaching framework](docs/operations/coaching-framework.md) - how to use coaching output in practice
- [Coaching template](docs/operations/coaching-template.md) - structured 1:1 session template with sign-off
- [Calibration guide](docs/operations/calibration.md) - how to align reviewers before scoring begins
- [Weekly reporting guide](docs/operations/weekly-reporting.md) - how to generate and read the weekly report

**Risk and limits**
- [Limitations](docs/risk/limitations.md) - what this system cannot do
- [Responsible use guide](docs/risk/responsible-use.md) - how to use this without causing harm

---

## When to log issues in the agent repo vs this repo

| Issue type | Where to log |
|---|---|
| Scorer gave wrong score | [This repo](https://github.com/alexandros-alexakis/ai-customer-support-qa/issues/new/choose) - scoring disagreement template |
| AI routed a ticket incorrectly | [Agent repo](https://github.com/alexandros-alexakis/ai-customer-support-agent/issues/new/choose) - escalation misfire template |
| KB gave wrong or missing information | [Agent repo](https://github.com/alexandros-alexakis/ai-customer-support-agent/issues/new/choose) - KB gap template |
| Coaching output seems wrong | [This repo](https://github.com/alexandros-alexakis/ai-customer-support-qa/issues/new/choose) - improvement template |
| New failure pattern not in library | [This repo](https://github.com/alexandros-alexakis/ai-customer-support-qa/issues/new/choose) - missing failure pattern template |
| Agent scope violation | [Agent repo](https://github.com/alexandros-alexakis/ai-customer-support-agent/issues/new/choose) - scope creep template |

---

## Author

**Alexandros Alexakis**
Vendor Manager and L&D Lead | Player Care
[LinkedIn](https://www.linkedin.com/in/alexandros-alexakis/)

---

## Status

Prototype. QA scoring engine, CSAT analyser, responsibility assignment, coaching report generator, failure pattern library, and full QA framework documentation.
