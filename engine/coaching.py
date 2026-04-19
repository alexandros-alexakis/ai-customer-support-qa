"""
Coaching Engine - generates specific coaching notes from a QA result.

Three tracks:
  agent_notes  - for the human agent in a 1:1
  system_flags - for ops to fix in the AI agent repo
  policy_flags - for leadership to review
"""

AGENT_REPO = "https://github.com/alexandros-alexakis/ai-customer-support-agent/issues/new/choose"


class CoachingEngine:
    def generate(self, interaction, qa_result, responsibility):
        agent_notes, system_flags, policy_flags = [], [], []
        dims = qa_result.get("dimensions", {})
        issue = interaction.get("issue_type", "unknown")
        vip = interaction.get("vip_tier", 0)
        csat = interaction.get("csat_score")

        for f in responsibility.get("agent_failures", []):
            dim = f["dimension"]
            if dim == "tone_appropriateness":
                tone = interaction.get("player_tone", "neutral")
                agent_notes.append(f"Tone: player was '{tone}'. Lead with one sentence of empathy before resolution.")
            elif dim == "information_collection":
                agent_notes.append(f"Collection: {issue} tickets require player ID, transaction ID, and platform in the first response.")
            elif dim == "scope_compliance":
                agent_notes.append("Scope: never promise a refund, restoration, or specific outcome. Acknowledge, collect, escalate.")
            elif dim == "player_experience":
                agent_notes.append("Closing: every response needs a clear next step. The player should never be left wondering what happens next.")

        if vip >= 2 and dims.get("tone_appropriateness", 2) < 2:
            agent_notes.append(f"VIP: Tier {vip} player. Personalised, senior-voice response required. No templates.")

        for f in responsibility.get("ai_failures", []):
            if f["owner"] == "ai_triage":
                system_flags.append(f"Routing failure on '{issue}': review engine/escalation.py in agent repo. Log at {AGENT_REPO}")
            elif f["owner"] == "ai_kb":
                system_flags.append(f"KB gap on '{issue}': review knowledge-base/ in agent repo. Log at {AGENT_REPO}")

        for f in responsibility.get("policy_failures", []):
            policy_flags.append(f"Policy review: '{issue}' tickets consistently produce low CSAT despite correct handling.")

        if csat and csat <= 2 and not agent_notes and not system_flags:
            policy_flags.append(f"Low CSAT with no handling failure on '{issue}': player unhappy with outcome, not process.")

        return {
            "agent_notes": agent_notes, "system_flags": system_flags, "policy_flags": policy_flags,
            "has_coaching": bool(agent_notes), "has_system_action": bool(system_flags), "has_policy_action": bool(policy_flags),
        }
