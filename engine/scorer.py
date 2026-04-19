"""
QA Scorer - scores a support interaction across six dimensions.
Each dimension scores 0, 1, or 2. Maximum total is 12.
"""

OUT_OF_SCOPE = [
    "refund approved", "ban lifted", "ban overturned", "i can confirm your refund",
    "i can process", "i will refund", "your ban has been",
]
HALLUCINATION_RISK = [
    "our policy states", "you are entitled to", "we guarantee", "within 24 hours you will",
]
TONE_MISMATCH = {
    "threatening": ["calm down", "please be patient"],
    "angry": ["as per", "as i mentioned", "i already told"],
    "distressed": ["unfortunately", "i cannot", "not possible"],
}
INFO_REQUIRED = {
    "payment_issue": ["player id", "transaction id", "platform"],
    "refund_request": ["player id", "transaction id", "purchase date"],
    "account_access": ["player id", "login method"],
    "lost_progress": ["player id", "platform", "game version"],
    "bug_report": ["player id", "device", "os version"],
    "ban_appeal": ["player id", "ban date"],
    "account_compromise": ["player id", "date noticed"],
}
ASSESSMENTS = [
    (11, 12, "Excellent"), (9, 10, "Good"), (7, 8, "Acceptable"),
    (5, 6, "Below standard"), (0, 4, "Failing"),
]


class QAScorer:
    def score(self, interaction: dict) -> dict:
        dims = {
            "correct_routing": self._routing(interaction),
            "information_collection": self._collection(interaction),
            "tone_appropriateness": self._tone(interaction),
            "scope_compliance": self._scope(interaction),
            "accuracy": self._accuracy(interaction),
            "player_experience": self._experience(interaction),
        }
        total = sum(dims.values())
        flags = []
        if dims["scope_compliance"] == 0: flags.append("SCOPE_VIOLATION")
        if dims["accuracy"] < 2: flags.append("ACCURACY_RISK")
        if dims["correct_routing"] == 0: flags.append("ROUTING_FAILURE")
        if interaction.get("vip_tier", 0) >= 2 and dims["tone_appropriateness"] < 2:
            flags.append("VIP_TONE_FAILURE")
        assessment = next((label for lo, hi, label in ASSESSMENTS if lo <= total <= hi), "Unknown")
        return {
            "ticket_id": interaction.get("ticket_id"),
            "agent_id": interaction.get("agent_id"),
            "issue_type": interaction.get("issue_type"),
            "dimensions": dims, "total_score": total,
            "assessment": assessment, "flags": flags,
        }

    def _routing(self, i):
        hard = ["ban_appeal", "fraud_report", "account_compromise", "churn_risk"]
        if i.get("issue_type") in hard and not i.get("escalated"): return 0
        if i.get("contact_count", 1) >= 3 and not i.get("escalated"): return 0
        if i.get("vip_tier", 0) >= 2 and not i.get("escalated"): return 1
        return 2

    def _collection(self, i):
        required = INFO_REQUIRED.get(i.get("issue_type", ""), [])
        if not required: return 2
        resp = i.get("agent_response", "").lower()
        ratio = sum(1 for f in required if f in resp) / len(required)
        return 2 if ratio >= 0.8 else (1 if ratio >= 0.5 else 0)

    def _tone(self, i):
        tone = i.get("player_tone", "neutral")
        resp = i.get("agent_response", "").lower()
        if any(s in resp for s in TONE_MISMATCH.get(tone, [])): return 0
        if tone in ["angry", "threatening", "distressed"]:
            if not any(s in resp for s in ["sorry", "understand", "apologise", "apolog"]):
                return 1
        return 2

    def _scope(self, i):
        resp = i.get("agent_response", "").lower()
        return 0 if any(p in resp for p in OUT_OF_SCOPE) else 2

    def _accuracy(self, i):
        resp = i.get("agent_response", "").lower()
        return 1 if any(p in resp for p in HALLUCINATION_RISK) else 2

    def _experience(self, i):
        resp = i.get("agent_response", "").lower()
        csat = i.get("csat_score")
        if csat and csat <= 2: return 0
        if any(p in resp for p in ["great question", "certainly!", "absolutely!"]): return 1
        if not any(s in resp for s in ["will", "next", "please", "could you", "let me", "i'll"]):
            return 1
        return 2
