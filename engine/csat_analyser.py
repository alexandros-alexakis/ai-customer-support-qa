"""
CSAT Analyser - analyses why a player gave a below-threshold CSAT score.
"""


class CSATAnalyser:
    LOW_THRESHOLD = 4

    def analyse(self, interaction, qa_result, responsibility):
        csat = interaction.get("csat_score")
        if not csat or csat >= self.LOW_THRESHOLD:
            return {"applicable": False}
        dims = qa_result.get("dimensions", {})
        failures = responsibility.get("failures", [])
        driver, owner, explanation, action = self._driver(interaction, dims, failures, csat)
        return {
            "applicable": True, "csat_score": csat,
            "primary_driver": driver, "owner": owner,
            "explanation": explanation, "recommended_action": action,
            "contributing_factors": [{"dimension": d, "score": s} for d, s in dims.items() if s < 2],
        }

    def _driver(self, interaction, dims, failures, csat):
        policy_f = [f for f in failures if f["owner"] == "policy"]
        ai_f = [f for f in failures if f["owner"] in ["ai_triage", "ai_kb"]]
        if dims.get("correct_routing", 2) == 0:
            return ("Incorrect routing by AI triage", "ai_triage",
                    "Ticket was routed to the wrong team or not escalated.",
                    "Review escalation rules in ai-customer-support-agent. Log an escalation-misfire issue.")
        if dims.get("scope_compliance", 2) == 0:
            return ("Agent exceeded scope", "agent",
                    "Agent made a promise or commitment outside their authority.",
                    "Immediate coaching required.")
        if dims.get("accuracy", 2) < 2 and ai_f:
            return ("Inaccurate information from AI KB", "ai_kb",
                    "Response may contain information without KB backing.",
                    "Review KB for this issue type. Log a KB gap issue.")
        if dims.get("tone_appropriateness", 2) == 0:
            return ("Tone mismatch", "agent",
                    "Agent tone did not match the player's emotional state.",
                    "Coaching: empathy before resolution.")
        if dims.get("information_collection", 2) == 0:
            return ("Insufficient information collected", "agent",
                    "Agent did not collect required information.",
                    "Coaching: required fields per issue type.")
        if policy_f:
            return ("Policy prevented a satisfactory outcome", "policy",
                    "Agent handled correctly but the policy outcome disappointed the player.",
                    "Document for policy review. No agent coaching required.")
        return ("Player dissatisfied despite correct handling", "unavoidable",
                "QA score suggests correct handling. Dissatisfaction is with the outcome.",
                "No coaching action. Document the pattern.")
