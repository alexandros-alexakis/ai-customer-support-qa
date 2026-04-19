# CSAT Analysis Guide

How to use the CSAT analyser and act on the results.

---

## When it runs

Automatically when a scored interaction has CSAT below 4. Threshold configurable in `.env`:
```
CSAT_LOW_THRESHOLD=4
```

---

## The responsibility split

| Primary driver | Owner | What this means |
|---|---|---|
| Routing failure | AI triage | AI sent the ticket to the wrong place. Fix the escalation rules, not the agent. |
| Scope violation | Agent | Agent made an unauthorized commitment. Coaching required. |
| Accuracy risk | AI KB | AI responded without KB backing. Fix the knowledge base. |
| Tone mismatch | Agent | Agent tone did not fit the situation. Coaching required. |
| Incomplete collection | Agent | Agent did not gather the right information. Coaching required. |
| Policy outcome | Policy | Agent did everything right. No coaching. |
| Unavoidable | None | QA was good. Document, no action. |

---

## Acting on results

**AI triage or AI KB:** Do not coach the agent. Open the relevant issue template in the agent repo: https://github.com/alexandros-alexakis/ai-customer-support-agent/issues/new/choose

**Agent:** Generate coaching output, review patterns before the 1:1, focus on one or two specific behaviours, set a concrete observable target.

**Policy:** Log for policy review. Ask: is the policy the problem, or is how we communicate the outcome the problem?

**Unavoidable:** Document and move on. Not every low CSAT has an actionable cause.

---

## CSAT and QA are different things

A high QA score does not guarantee a high CSAT. Always segment CSAT by issue type and outcome type. Aggregate CSAT is misleading.
