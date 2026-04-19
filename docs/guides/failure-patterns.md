# Failure Pattern Library

Known failure patterns with causes, responsibility, and recommended actions.

---

## FP-01: Routing failure on hard escalation type

A ticket requiring escalation (ban appeal, account compromise, churn risk, fraud) was handled at T1.

**Responsibility:** AI triage or agent depending on whether AI guidance was followed.
**Dimension:** Correct routing (0)
**Action:** Check if AI produced the correct escalation recommendation. If yes: agent coaching. If no: log escalation-misfire in agent repo.

---

## FP-02: Incomplete collection on financial ticket

A payment or refund ticket handled without transaction ID and platform.

**Responsibility:** Agent
**Dimension:** Information collection (0 or 1)
**Action:** Coaching on required fields for payment tickets. Most common collection failure in gaming support.

---

## FP-03: Scope violation with commitment

Agent promised a refund, stated a ban outcome, or confirmed an account action without authority.

**Responsibility:** Agent
**Dimension:** Scope compliance (0)
**Action:** Immediate coaching. Assess whether the commitment creates an expectation that needs managing.

---

## FP-04: Hallucinated policy

Response contained a policy statement not backed by the knowledge base.

**Responsibility:** AI KB (if AI-assisted) or agent (if human-authored)
**Dimension:** Accuracy (1 or 0)
**Action:** Review KB for this issue type. Log a KB gap issue in the agent repo if content is missing.

---

## FP-05: Tone mismatch on high-emotion ticket

Distressed, angry, or threatening player received a response that did not acknowledge their emotional state first.

**Responsibility:** Agent
**Dimension:** Tone appropriateness (0 or 1)
**Action:** Coaching: one sentence of acknowledgment before any troubleshooting step.

---

## FP-06: VIP player not prioritised

Tier 2 or 3 VIP received standard handling: generic tone, no account context review.

**Responsibility:** Agent or AI triage depending on whether VIP flag was surfaced.
**Dimension:** Correct routing (1), tone (0 or 1)
**Action:** Check whether AI surfaced the VIP flag. If yes: agent coaching. If no: review VIP config in agent repo.

---

## FP-07: No next step given

Response ended without a clear next step or offer to help further.

**Responsibility:** Agent
**Dimension:** Player experience (1)
**Action:** Coaching: every response ends with what happens next or an offer to help further.

---

## FP-08: Repeat contact not escalated

Player contacting for the third time handled at T1 again.

**Responsibility:** AI triage or agent
**Dimension:** Correct routing (0)
**Action:** Check whether contact count was passed correctly. If AI still did not escalate: log escalation-misfire.

---

## FP-09: Low CSAT despite correct handling

QA score was good but CSAT was below 4. Player unhappy with outcome, not process.

**Responsibility:** Policy or unavoidable
**Action:** No agent coaching. If this happens consistently on a specific issue type, flag for policy review.
