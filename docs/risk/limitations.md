# Limitations

---

## Scoring

Rule-based scoring is a proxy, not a judgment. The scorer detects signals, it cannot read nuance or context the way a human reviewer can.

Information collection is keyword-based. An agent who collected info verbally but did not repeat it in the scored response will score lower than they should.

Tone scoring is conservative. It detects specific mismatch signals but misses subtler failures. Human review catches what the scorer misses.

Accuracy flags risk, not confirmed inaccuracy. A score of 1 means the response contained language that may suggest unstated policy. Human review is needed to confirm.

---

## CSAT analysis

CSAT is a trailing indicator. The analysis tells you what went wrong but cannot fix that interaction.

Low CSAT has many causes outside this system's view: game quality, wait time, prior bad experiences, player expectations.

Single interactions are noisy. A single low score is not enough to draw conclusions. Patterns across five or more interactions are meaningful.

---

## Coaching

Coaching output is suggestions, not verdicts. Every note should be reviewed by a human before a 1:1. The engine does not know the agent's history or development stage.

---

## What is not implemented

- Live integration with Zendesk, Klaus, or any QA platform
- Automatic CSAT survey triggering
- Real-time scoring during interactions
- Agent performance ranking or benchmarking
- LLM-assisted qualitative analysis (available in LLM mode but not in the demo)
