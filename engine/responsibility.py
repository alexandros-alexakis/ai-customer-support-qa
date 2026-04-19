"""
Responsibility Assigner - determines who owns each QA failure.
"""


class ResponsibilityAssigner:
    def assign(self, interaction, qa_result):
        failures = []
        dims = qa_result.get("dimensions", {})
        flags = qa_result.get("flags", [])
        issue = interaction.get("issue_type", "unknown")

        if dims.get("correct_routing", 2) == 0:
            failures.append({"dimension": "correct_routing", "owner": "ai_triage",
                "description": f"Routing failure on '{issue}': check escalation rules in agent repo.",
                "action": "Log an escalation-misfire issue."})
        if "ACCURACY_RISK" in flags:
            failures.append({"dimension": "accuracy", "owner": "ai_kb",
                "description": f"Accuracy risk on '{issue}': response may contain unstated policy.",
                "action": "Review KB. Log a KB gap issue if content is missing."})
        if dims.get("tone_appropriateness", 2) < 2:
            failures.append({"dimension": "tone_appropriateness", "owner": "agent",
                "description": "Tone mismatch: response did not match player's emotional state.",
                "action": "Agent coaching: empathy before resolution."})
        if dims.get("information_collection", 2) < 2:
            failures.append({"dimension": "information_collection", "owner": "agent",
                "description": f"Incomplete information collection for '{issue}'.",
                "action": "Agent coaching: review required fields per issue type."})
        if "SCOPE_VIOLATION" in flags:
            failures.append({"dimension": "scope_compliance", "owner": "agent",
                "description": "Scope violation: agent made commitment outside their authority.",
                "action": "Immediate coaching. Assess whether commitment needs managing."})
        if dims.get("player_experience", 2) < 2 and not any(
            f["dimension"] in ["tone_appropriateness", "information_collection"] for f in failures):
            failures.append({"dimension": "player_experience", "owner": "agent",
                "description": "Player experience below standard: unclear or no next step.",
                "action": "Agent coaching: every response needs a clear next step."})
        return {
            "failures": failures,
            "ai_failures": [f for f in failures if f["owner"] in ["ai_triage", "ai_kb"]],
            "agent_failures": [f for f in failures if f["owner"] == "agent"],
            "policy_failures": [f for f in failures if f["owner"] == "policy"],
        }
