"""
Unit tests for the CSAT analyser.
"""
import pytest
from engine.scorer import QAScorer
from engine.responsibility import ResponsibilityAssigner
from engine.csat_analyser import CSATAnalyser

def run(interaction):
    qa = QAScorer().score(interaction)
    resp = ResponsibilityAssigner().assign(interaction, qa)
    csat = CSATAnalyser().analyse(interaction, qa, resp)
    return qa, resp, csat

def base(**kwargs):
    d = {
        "ticket_id": "T1", "agent_id": "a1", "issue_type": "payment_issue",
        "player_message": "help", "agent_response": "sure",
        "csat_score": 5, "vip_tier": 0, "contact_count": 1,
        "escalated": True, "escalation_team": "billing", "player_tone": "neutral",
    }
    d.update(kwargs)
    return d

def test_not_applicable_above_threshold():
    _, _, csat = run(base(csat_score=5))
    assert csat["applicable"] is False

def test_routing_failure_blames_ai():
    _, _, csat = run(base(
        issue_type="ban_appeal", csat_score=2,
        escalated=False, escalation_team=None,
        agent_response="sorry to hear that",
    ))
    assert csat["applicable"] is True
    assert csat["owner"] == "ai_triage"

def test_scope_violation_blames_agent():
    _, _, csat = run(base(
        csat_score=2,
        agent_response="I can confirm your refund will be processed today.",
    ))
    assert csat["applicable"] is True
    assert csat["owner"] == "agent"
