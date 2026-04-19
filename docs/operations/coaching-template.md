# Agent Coaching Template

## Overview

This template structures coaching conversations following a QA review. Coaching should be conducted within 5 business days of the reviewed interaction.

Before using this template, check the responsibility output from `run_qa.py`. If the primary failures are system-owned (AI triage, AI KB), fix the system first. This template is for agent-owned failures only.

---

## Coaching Session Header

| Field | Details |
|---|---|
| Agent name | |
| Coach name | |
| Date of session | |
| Ticket(s) reviewed | |
| Automated QA score (out of 12) | |
| Full QA score (out of 100, if completed) | |
| Performance band | |
| Primary failure type | |
| Responsibility: agent-owned failures | |

---

## 1. Opening (2-3 minutes)

Start with something the agent did well. This is not optional. It sets the tone and keeps the agent receptive to feedback.

- What did the agent handle well in this interaction?
- Acknowledge effort and any improvement since last review

---

## 2. Review the Interaction Together (5-10 minutes)

- Walk through the ticket together, not just the score
- Ask the agent to narrate their thinking: "What were you trying to do here?"
- Listen before explaining. The agent may identify the issue themselves.
- If the automated scorer flagged something, show them what triggered it

---

## 3. Identify the Gap (5 minutes)

Be specific about what fell below standard and why it matters:

- What specifically happened?
- Which dimension did it affect?
- What was the impact on the player?

Avoid vague feedback like "your tone was off." Instead: "In the third message, when the player said they were frustrated, the response moved straight to troubleshooting without acknowledging their frustration first. That's what scored 0 on tone."

If the low score was driven by an AI triage failure, be explicit: "The routing failure here was not your decision. That is a system issue being logged separately. What I want to focus on is the information collection step."

---

## 4. Agree on Improvement Actions (5 minutes)

| Action | How to Practice | Target Date |
|---|---|---|
| | | |
| | | |

---

## 5. Close (2 minutes)

- Ask the agent how they feel about the session
- Confirm the follow-up date
- Reiterate confidence in their ability to improve

---

## Coach Notes

Free text for observations not captured above. Note whether any system flags were identified and whether they have been logged in the agent repo issue tracker.

---

## Agent Sign-Off

The agent confirms they have received and understood the feedback:

Agent signature / acknowledgement: _______________
Date: _______________
