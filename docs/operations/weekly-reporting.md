# Weekly Reporting Guide

---

## Generating a report

```bash
python run_qa.py --report
python run_qa.py --report --agent agent_001
python run_qa.py --report --week 2024-W15
```

Reports are generated from scored interactions in `data/scores/`.

---

## How to read it

A dimension averaging below 1.5 / 2 across the week is systematic, not a one-off. A dimension above 1.8 is healthy.

If a specific issue type consistently scores lower than others: the KB may not cover it well, the escalation path may be unclear, or required fields are not communicated clearly in training. Each has a different fix.

---

## CSAT segmentation

Never report aggregate CSAT. Always segment by issue type and outcome type. A team handling mostly refund denials will show lower aggregate CSAT than one handling gameplay questions. That comparison is meaningless.

---

## Weekly ops review agenda

1. QA score trend vs last week
2. Any dimensions that dropped more than 0.2 points
3. Issue types with systematic low scores
4. System flags generated this week: were they actioned in the agent repo?
5. Policy flags: any patterns needing leadership attention?
6. Low CSAT interactions: how many, what were the primary drivers?
