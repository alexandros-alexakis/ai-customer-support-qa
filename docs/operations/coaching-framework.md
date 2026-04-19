# Coaching Framework

How to use the coaching output in practice.

---

## The three tracks

**Agent notes** - for the human agent in a 1:1. Only agent-owned failures.

**System flags** - for ops to action in the AI agent repo. Never shared with the agent as coaching.

**Policy flags** - for leadership. Patterns where correct handling produces bad outcomes.

Coaching an agent for an AI failure is not just useless, it is harmful.

---

## Before the 1:1

1. Run the agent's recent interactions through the scorer
2. Look for patterns: same dimension failing repeatedly? Same issue type?
3. Check the responsibility split: how many failures are agent-owned vs system-owned?
4. Pick one or two specific behaviours to focus on

---

## During the 1:1

Do: start with a specific interaction, show the QA score, focus on the behaviour not the person, set a concrete observable target, distinguish agent failures from system failures explicitly.

Do not: bring system flags into the coaching session as the agent's fault, give generic feedback without a specific example, cover more than two areas in a single session.

---

## What good coaching looks like

Not this: "Your QA scores were low. You need to work on your tone."

This: "In ticket SAMPLE-001, you collected the player ID but missed the transaction ID and platform. For payment issues, those three fields need to be in your first response. Next week, I'd like to see every payment ticket with all three collected on first contact."
