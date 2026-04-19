"""
Unit tests for the QA scorer.
"""
import pytest
from engine.scorer import QAScorer

@pytest.fixture
def scorer(): return QAScorer()

def base(**kwargs):
    d = {
        "ticket_id": "T1", "agent_id": "a1", "issue_type": "payment_issue",
        "player_message": "I was charged but nothing arrived.",
        "agent_response": "Sorry to hear that. Could you share your player id, transaction id, and platform?",
        "csat_score": 4, "vip_tier": 0, "contact_count": 1,
        "escalated": True, "escalation_team": "billing", "player_tone": "neutral",
    }
    d.update(kwargs)
    return d

def test_good_interaction_scores_high(scorer):
    r = scorer.score(base())
    assert r["total_score"] >= 9

def test_scope_violation(scorer):
    r = scorer.score(base(agent_response="I can confirm your refund will be processed today."))
    assert r["dimensions"]["scope_compliance"] == 0
    assert "SCOPE_VIOLATION" in r["flags"]

def test_missing_collection(scorer):
    r = scorer.score(base(agent_response="Hi there, how can I help?"))
    assert r["dimensions"]["information_collection"] == 0

def test_routing_failure_ban_appeal(scorer):
    r = scorer.score(base(issue_type="ban_appeal", escalated=False, escalation_team=None))
    assert r["dimensions"]["correct_routing"] == 0
    assert "ROUTING_FAILURE" in r["flags"]

def test_repeat_contact_requires_escalation(scorer):
    r = scorer.score(base(contact_count=3, escalated=False))
    assert r["dimensions"]["correct_routing"] == 0

def test_tone_mismatch_angry(scorer):
    r = scorer.score(base(player_tone="angry",
                          agent_response="As per my previous message, please send your player ID."))
    assert r["dimensions"]["tone_appropriateness"] == 0

def test_accuracy_risk(scorer):
    r = scorer.score(base(agent_response="Our policy states you are entitled to a full refund."))
    assert r["dimensions"]["accuracy"] < 2
    assert "ACCURACY_RISK" in r["flags"]
