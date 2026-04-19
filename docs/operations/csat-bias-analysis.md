# AI CSAT Bias Analysis

## Overview

This document addresses a known measurement problem in AI-assisted gaming support: when AI handles simple tickets and human agents handle complex ones, comparing their CSAT scores produces a misleading picture that favours AI and unfairly penalises agents.

This is not a theoretical concern. It is an observable pattern in operations that have deployed AI without controlling for ticket complexity in their measurement framework. Understanding this bias is essential before using CSAT as a signal to expand or reduce AI scope.

---

## The Problem

AI agents in gaming support are typically deployed on Tier 1: payment delivery issues, basic account access, standard FAQ questions. Players get fast, consistent answers and rate the interaction positively.

Human agents increasingly handle what is left: escalations, billing disputes, ban appeals, frustrated repeat contacts, churn risk conversations. These interactions are inherently harder to resolve satisfactorily regardless of agent quality.

The result:

| Handler | Ticket Type | Average CSAT |
|---|---|---|
| AI agent | Simple, fast-resolution queries | High |
| Human agents | Complex, emotionally charged, unresolved issues | Low |

This comparison tells you nothing useful about either. It tells you that easy tickets get better ratings than hard ones, which was always true.

---

## Why This Matters in Gaming Support Specifically

Gaming support has a sharper version of this problem than most industries:

- VIP players and high-emotion tickets (ban appeals, churn risk, chargebacks) are disproportionately complex and almost always handled by humans
- AI handles the high-volume, low-complexity queue: missing item reports, basic login issues, standard FAQs
- Gaming communities share support experiences publicly, so CSAT perception matters beyond just the score

Organisations making scope decisions based on raw CSAT comparisons will expand AI into territory it is not ready for, and they will blame agents for scores that reflect ticket difficulty, not agent performance.

---

## The Fix: Complexity-Controlled Measurement

### Step 1: Score each ticket at the point of routing

| Factor | Low (1) | Medium (2) | High (3) |
|---|---|---|---|
| Resolution type | Standard FAQ | Requires investigation | Requires specialist action |
| Emotional intensity | Neutral | Frustrated | Angry or distressed |
| Contact history | First contact | Second contact | Third or more |
| Financial impact | None | Minor | Significant |
| Policy sensitivity | Standard | Gray area | Exception required |

Total range: 5 (simplest) to 15 (most complex).

### Step 2: Segment CSAT into bands

| Band | Score | Description |
|---|---|---|
| Simple | 5-7 | Standard queries, clear resolution available |
| Moderate | 8-11 | Requires investigation or judgment |
| Complex | 12-15 | High sensitivity, specialist involvement likely |

### Step 3: Compare only within the same band

| Band | AI CSAT | Human CSAT | Valid? |
|---|---|---|---|
| Simple | Measurable | Measurable | Yes |
| Moderate | Measurable (if in scope) | Measurable | Yes |
| Complex | Not applicable | Measurable | No |

### Step 4: Stop reporting aggregate CSAT

Report AI CSAT for tickets within AI scope, human CSAT by complexity band, and overall CSAT as a blended metric with clear methodology notes. Never a single number that mixes both.

---

## How This Connects to the QA System

The CSAT analyser in this repo (`engine/csat_analyser.py`) analyses individual interactions when CSAT falls below threshold. The complexity-controlled measurement framework described here is the layer above that: how you aggregate and report CSAT across your whole queue without misleading yourself.

Before expanding AI scope beyond the current Tier 1 boundaries:

1. Establish a complexity baseline for current Tier 1 tickets
2. Measure CSAT within that complexity band only
3. Compare against human agent CSAT on equivalent tickets
4. Only expand if performance holds at the next complexity level

Expanding based on inflated simple-ticket CSAT is a measurement error, not a performance signal.

---

## Further Reading

- Simpson's Paradox: aggregate statistics that reverse when data is segmented
- Selection bias in AI evaluation benchmarks
- Goodhart's Law: when a measure becomes a target, it ceases to be a good measure
