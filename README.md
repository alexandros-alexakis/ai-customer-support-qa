# Player Care QA and Coaching System

![Status: Prototype](https://img.shields.io/badge/status-prototype-yellow)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

---

> **A QA scoring, CSAT analysis, and coaching toolkit for gaming player care teams. Designed to work alongside the [Player Care AI Support Agent](https://github.com/alexandros-alexakis/ai-customer-support-agent) but runs independently on any support interaction.**
>
> **Alexandros Alexakis**, Vendor Manager and L&D Lead, Player Care

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

## How it connects to the agent repo

The [ai-customer-support-agent](https://github.com/alexandros-alexakis/ai-customer-support-agent) handles triage, escalation, routing, and response strategy.

This repo handles what comes after: did the interaction go well, why did it go wrong, and what do we do about it.

---

## The responsibility split

| What went wrong | Responsibility | Action |
|---|---|---|
| AI triage routed to wrong team | System / AI | Update escalation rules in agent repo |
| AI gave wrong information | System / KB | Update knowledge base in agent repo |
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

- [Quickstart](docs/setup/quickstart.md)
- [Scoring dimensions](docs/guides/scoring-dimensions.md)
- [Failure pattern library](docs/guides/failure-patterns.md)
- [CSAT analysis guide](docs/operations/csat-analysis.md)
- [Coaching framework](docs/operations/coaching-framework.md)
- [Calibration guide](docs/operations/calibration.md)
- [Weekly reporting guide](docs/operations/weekly-reporting.md)
- [Limitations](docs/risk/limitations.md)
- [Responsible use guide](docs/risk/responsible-use.md)

---

## Related

[ai-customer-support-agent](https://github.com/alexandros-alexakis/ai-customer-support-agent) - The Tier 1 player care AI agent this QA system is designed to evaluate.

---

## Author

**Alexandros Alexakis**
Vendor Manager and L&D Lead | Player Care
[LinkedIn](https://www.linkedin.com/in/alexandros-alexakis/)

---

## Status

Prototype. QA scoring engine, CSAT analyser, responsibility assignment, coaching report generator, and failure pattern library.
