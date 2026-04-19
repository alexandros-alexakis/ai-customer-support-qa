# Failure Analysis

## Overview

This document catalogues known failure modes for the Tier 1 support assistant. Each failure mode is defined, its likely cause identified, its operational impact quantified, and a mitigation proposed.

This is not a theoretical exercise. Every failure mode here has a real-world analogue in support operations. Identifying them in advance is how you design a system that fails predictably rather than catastrophically.

---

## Failure Mode 1: Over-escalation

**Description:** The assistant escalates tickets that could and should be resolved at Tier 1. Simple mechanic questions, routine payment delivery delays, and basic troubleshooting cases get routed to specialist teams unnecessarily.

**Likely cause:**
- Overly conservative confidence threshold
- Keyword signal matches a high-priority intent when the context is benign
- System prompt escalation rules are too broad

**Operational impact:**
- Increases specialist team workload with tickets they should not be handling
- Increases response time for players with straightforward issues
- Inflates escalation rate metric, making it unreliable as a signal

**Mitigation:**
- Define minimum evidence required before escalation for each issue type
- Introduce a pre-escalation check: has Tier 1 resolution been attempted?
- Review false positive escalation rate weekly and adjust classifier signals

---

## Failure Mode 2: Under-escalation

**Description:** The assistant attempts to resolve a ticket at Tier 1 when it should have been escalated. A legal threat is missed. A VIP player is not identified. A repeat contact is treated as a new ticket.

**Likely cause:**
- Hard escalation triggers not comprehensive enough
- Legal language phrased in a way the classifier does not recognise
- VIP flag not passed correctly from the support platform
- Contact history not available or not checked

**Operational impact:**
- Legal risk if threats are not escalated to compliance
- Player loss if churn risk signals are missed
- Repeat contacts deepen player frustration if not recognised

**Mitigation:**
- Expand legal threat signal dictionary to cover jurisdiction-specific terminology
- Make VIP status a required parameter, fail loudly if missing
- Implement mandatory contact history check before any Tier 1 resolution attempt

---

## Failure Mode 3: Hallucinated Policy

**Description:** The assistant states a policy, rule, or outcome that does not exist in the knowledge base. It invents a refund window, confirms a ban will be lifted, or speculates on a TOS clause.

**Likely cause:**
- System prompt does not sufficiently prohibit speculation
- LLM fills knowledge gaps with plausible-sounding information
- Knowledge base has gaps that create pressure on the model to infer

**Operational impact:**
- Players may cite assistant statements in disputes
- Creates implied commitments the business cannot honour
- Potential legal liability in consumer protection jurisdictions

**Mitigation:**
- System prompt explicitly prohibits inventing policy
- KB gaps should result in escalation, not inference
- Regular adversarial testing: ask about policies not in the KB and verify it escalates
- QA review should check policy statements against the KB

---

## Failure Mode 4: Insufficient Evidence Gathering

**Description:** The assistant escalates a ticket without collecting the information the specialist team needs. The ticket bounces back. The player has to be contacted again.

**Likely cause:**
- Escalation decision made too quickly before collection is complete
- Information collection rules not enforced for the specific issue type
- Player is hostile and the assistant de-prioritises collection

**Operational impact:**
- Increases average handling time
- Specialist teams receive incomplete tickets they cannot action
- FCR metric suffers

**Mitigation:**
- Information collection requirements defined per issue type
- System prompt mandates collection before escalation except for hard triggers
- Track incomplete escalation rate as a QA metric

---

## Failure Mode 5: Wrong Issue Classification

**Description:** The assistant classifies the issue incorrectly. A compromised account is handled as a standard login issue. A churn risk signal is treated as a bug report.

**Likely cause:**
- Keyword signals overlap between issue types
- Player describes issue in an unusual way
- Confidence score is above threshold but classification is still wrong

**Operational impact:**
- Wrong information is collected
- Wrong team receives the escalation
- Player frustration increases when handling is visibly wrong

**Mitigation:**
- Confidence threshold acts as a safety valve: low confidence routes to human
- Classification is logged at every step for audit
- Weekly review of misclassification cases from QA sampling

---

## Failure Mode 6: Over-questioning

**Description:** The assistant asks too many questions before taking any action. The player provides their issue and receives five clarifying questions in response.

**Likely cause:**
- System prompt asks for too much information upfront
- Information collection rules not ordered by priority
- No constraint on number of questions per turn

**Operational impact:**
- Players abandon the interaction
- CSAT drops even when the issue is eventually resolved
- Interaction feels bureaucratic rather than helpful

**Mitigation:**
- System prompt mandates one question per turn when clarification is needed
- Information collection is ordered: ask for the most critical item first
- QA checklist includes unnecessary follow-up rate as a metric

---

## Failure Mode 7: Premature Closure

**Description:** The assistant closes or marks a ticket as resolved before confirming the player's issue is actually resolved.

**Likely cause:**
- No mandatory confirmation step before closure
- Escalation is treated as resolution
- Player says "ok thanks" and the assistant interprets this as resolution

**Operational impact:**
- Player recontacts, increasing repeat contact rate
- FCR metric is artificially inflated
- Player frustration when they have to re-explain the issue

**Mitigation:**
- System prompt requires ending every interaction with a clear next step or confirmation question
- Escalation is not closure. Ticket remains open until specialist team confirms resolution.
- Player saying "ok" or "thanks" should not trigger automatic closure

---

## Failure Mode 8: Failure to Detect Incident Pattern

**Description:** Multiple players report the same issue in a short window. The assistant handles each ticket individually and never flags the pattern.

**Likely cause:**
- No cross-session signal aggregation
- Each ticket is processed in isolation

**Operational impact:**
- Incident response is delayed
- Players receive individual troubleshooting for a problem requiring a backend fix
- Support volume spikes while root cause goes unaddressed

**Mitigation:**
- Incident detection requires external aggregation (known limitation, see roadmap)
- At Tier 1, agents trained to manually flag multiple identical reports
- Volume spike monitoring should be in place at the platform level

---

## Failure Mode 9: Emotional De-escalation Failure

**Description:** An angry or distressed player becomes more hostile because the assistant's responses feel dismissive, robotic, or defensive.

**Likely cause:**
- Tone rules followed technically but feel formulaic
- Standard troubleshooting delivered without acknowledging emotional context first
- Response is too long and structured when a short human acknowledgment is needed

**Operational impact:**
- Escalation becomes necessary for tickets that could have been resolved at Tier 1
- CSAT is lower than it would have been with a human agent
- Negative reviews or public complaints are more likely

**Mitigation:**
- Tone instructions mandate acknowledgment before any troubleshooting
- QA specifically scores emotional de-escalation
- Sample conversations include hostile player examples for style reference

---

## Failure Mode 10: Inconsistency Across Similar Cases

**Description:** Two players with identical issues receive materially different responses: different timeframes stated, different levels of empathy, different policy statements.

**Likely cause:**
- LLM response generation is non-deterministic
- System prompt rules not specific enough to constrain variation
- Knowledge base is ambiguous on specific policy points

**Operational impact:**
- Players compare responses in community forums and lose trust
- Creates implied policy differences that do not exist
- Undermines the purpose of a standardised support system

**Mitigation:**
- Timeframe commitments should come from the decision table, not the LLM
- System prompt provides exact language for escalation acknowledgments
- Consistency testing: run identical inputs multiple times and compare outputs
- QA calibration sessions specifically check for consistency across similar ticket types
