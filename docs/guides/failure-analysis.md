# Failure Analysis

## Overview

This document catalogues known failure modes for gaming Tier 1 AI support. Each failure mode is defined, its likely cause identified, its operational impact described, and a mitigation proposed.

Every failure mode here has a real-world analogue in gaming support operations. The automated scorer in this repo (`engine/scorer.py`) catches several of these programmatically. The ones it cannot catch reliably are noted, and those require human QA review.

---

## Failure Mode 1: Over-escalation

**Description:** The system escalates tickets that could and should be resolved at Tier 1. Routine payment delivery delays and basic troubleshooting cases get routed to specialist teams unnecessarily.

**Caught by scorer:** Partially. The scorer checks routing but cannot distinguish between necessary and unnecessary escalation without knowing the full context.

**Operational impact:** Increases specialist team workload, increases response time, inflates escalation rate as a metric.

**Mitigation:** Define minimum evidence required before escalation per issue type. Review false positive escalation rate weekly. Log escalation-misfire issues in the [agent repo](https://github.com/alexandros-alexakis/ai-customer-support-agent/issues/new/choose).

---

## Failure Mode 2: Under-escalation

**Description:** The system attempts to resolve a ticket at Tier 1 when it should have escalated. A legal threat is missed. A VIP player is not identified. A repeat contact is treated as a new ticket.

**Caught by scorer:** Yes. `ROUTING_FAILURE` flag fires on hard escalation types not escalated and on third+ contacts not escalated.

**Operational impact:** Legal risk, player loss from missed churn signals, repeat contacts deepening frustration.

**Mitigation:** Expand legal threat signal dictionary. Make VIP status a required parameter. Log escalation-misfire issues in the agent repo.

---

## Failure Mode 3: Hallucinated Policy

**Description:** The response states a policy, rule, or outcome not backed by the knowledge base. A refund window is invented. A ban outcome is confirmed. A TOS clause is speculated on.

**Caught by scorer:** Partially. `ACCURACY_RISK` flag fires on specific language patterns. Does not catch all hallucinations.

**Operational impact:** Players may cite AI statements in disputes. Creates implied commitments. Potential legal liability.

**Mitigation:** KB gaps should result in escalation, not inference. Run regular adversarial tests: ask about policies not in the KB and verify escalation. QA review should check policy statements against the KB. Log KB gap issues in the [agent repo](https://github.com/alexandros-alexakis/ai-customer-support-agent/issues/new/choose).

---

## Failure Mode 4: Insufficient Evidence Gathering

**Description:** The ticket is escalated without collecting what the specialist team needs. The ticket bounces back. The player is contacted again.

**Caught by scorer:** Yes. `information_collection` dimension scores 0 when required fields are missing.

**Operational impact:** Increases average handling time. Specialist teams receive incomplete tickets. FCR suffers.

**Mitigation:** Information collection requirements defined per issue type in the scorer. Track incomplete escalation rate as a QA metric.

---

## Failure Mode 5: Wrong Issue Classification

**Description:** The system classifies the issue incorrectly. A compromised account is handled as a standard login issue. A churn risk signal is treated as a bug report.

**Caught by scorer:** Indirectly. Wrong classification leads to wrong routing, which the scorer catches as a routing failure.

**Operational impact:** Wrong information collected. Wrong team gets the ticket. Player frustration increases when handling is visibly wrong.

**Mitigation:** Confidence threshold routes to human when classification is uncertain. Weekly review of misclassification cases from QA sampling. Log escalation-misfire issues in the agent repo.

---

## Failure Mode 6: Over-questioning

**Description:** The agent asks too many questions before taking any action. The player states their issue and receives five clarifying questions before any acknowledgment.

**Caught by scorer:** Partially. Indirectly visible in player experience score. Not directly detected.

**Operational impact:** Players abandon the interaction. CSAT drops even when the issue is eventually resolved.

**Mitigation:** One question per turn when clarification is needed. Ask for the most critical item first. QA checklist includes unnecessary follow-up rate.

---

## Failure Mode 7: Premature Closure

**Description:** The ticket is marked resolved before confirming the player's issue is actually resolved. Escalation is treated as closure.

**Caught by scorer:** Not directly. Visible in repeat contact patterns over time.

**Operational impact:** Player recontacts, increasing repeat contact rate. FCR is artificially inflated.

**Mitigation:** Every response ends with a clear next step or confirmation question. Escalation is not closure.

---

## Failure Mode 8: Failure to Detect Incident Pattern

**Description:** Multiple players report the same issue in a short window. Each ticket is handled individually. The pattern is never flagged.

**Caught by scorer:** No. The scorer processes individual interactions. Cross-ticket pattern detection is not in scope.

**Operational impact:** Incident response delayed. Players receive individual troubleshooting for a problem needing a backend fix.

**Mitigation:** This requires an external aggregation layer. See [docs/operations/incident-detection.md](https://github.com/alexandros-alexakis/ai-customer-support-agent/blob/main/docs/operations/incident-detection.md) in the agent repo. Agents should manually flag multiple identical reports.

---

## Failure Mode 9: Emotional De-escalation Failure

**Description:** An angry or distressed player becomes more hostile because the response feels dismissive, robotic, or defensive.

**Caught by scorer:** Yes. `tone_appropriateness` dimension scores 0 on specific mismatch signals.

**Operational impact:** Escalation becomes necessary for tickets resolvable at Tier 1. CSAT lower than it would have been with a human agent.

**Mitigation:** Acknowledge before any troubleshooting. QA specifically scores tone. See [docs/operations/coaching-framework.md](../operations/coaching-framework.md) for how to coach this.

---

## Failure Mode 10: Inconsistency Across Similar Cases

**Description:** Two players with identical issues receive materially different responses: different timeframes, different levels of empathy, different policy statements.

**Caught by scorer:** No. Consistency requires comparing multiple interactions, not scoring one.

**Operational impact:** Players compare responses in gaming communities and lose trust. Creates implied policy differences that do not exist.

**Mitigation:** Run identical inputs through the scorer multiple times and compare outputs. QA calibration sessions check for consistency across similar ticket types. See [docs/operations/calibration.md](../operations/calibration.md).
