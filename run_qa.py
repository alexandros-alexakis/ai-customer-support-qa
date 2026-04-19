"""
Player Care QA and Coaching System - Entry point

Usage:
    python run_qa.py --demo
    python run_qa.py --ticket "message" --response "response" --csat 3
    python run_qa.py --report --agent agent_001 --week 2024-W15
"""

import argparse
import json
from engine.scorer import QAScorer
from engine.csat_analyser import CSATAnalyser
from engine.responsibility import ResponsibilityAssigner
from engine.coaching import CoachingEngine
from engine.reporter import WeeklyReporter

DEMO = {
    "ticket_id": "DEMO-001", "agent_id": "agent_demo",
    "issue_type": "payment_issue",
    "player_message": "I was charged 9.99 for coins but they never appeared. Transaction ID: TXN-884521",
    "agent_response": "Hi! Thanks for reaching out. Sorry to hear about this. Could you send me your player ID and we'll look into it?",
    "csat_score": 3, "vip_tier": 0, "contact_count": 1,
    "escalated": False, "escalation_team": None, "player_tone": "neutral",
}

def run_demo():
    print("=" * 60)
    print(" PLAYER CARE QA SYSTEM - DEMO")
    print("=" * 60)
    scorer = QAScorer()
    qa = scorer.score(DEMO)
    print("\nQA SCORE")
    for dim, score in qa["dimensions"].items():
        bar = "*" * score + "." * (2 - score)
        print(f"  {dim:<30} {bar} {score}/2")
    print(f"  {'TOTAL':<30} {qa['total_score']}/12  [{qa['assessment']}]")
    assigner = ResponsibilityAssigner()
    resp = assigner.assign(DEMO, qa)
    print("\nRESPONSIBILITY")
    for f in resp["failures"]:
        print(f"  [{f['owner']}] {f['description']}")
    analyser = CSATAnalyser()
    csat = analyser.analyse(DEMO, qa, resp)
    if csat["applicable"]:
        print("\nCSAT ANALYSIS")
        print(f"  Driver:  {csat['primary_driver']}")
        print(f"  Owner:   {csat['owner']}")
        print(f"  Action:  {csat['recommended_action']}")
    coach = CoachingEngine()
    coaching = coach.generate(DEMO, qa, resp)
    print("\nCOACHING OUTPUT")
    for note in coaching["agent_notes"]:
        print(f"  [agent]  {note}")
    for flag in coaching["system_flags"]:
        print(f"  [system] {flag}")
    print("\n" + "=" * 60)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--ticket", type=str)
    parser.add_argument("--response", type=str)
    parser.add_argument("--csat", type=int)
    parser.add_argument("--issue-type", type=str, default="unknown")
    parser.add_argument("--agent", type=str)
    parser.add_argument("--week", type=str)
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()
    if args.demo:
        run_demo()
    elif args.ticket and args.response:
        interaction = {
            "ticket_id": "CLI-001", "agent_id": args.agent or "unknown",
            "issue_type": args.issue_type, "player_message": args.ticket,
            "agent_response": args.response, "csat_score": args.csat,
            "vip_tier": 0, "contact_count": 1, "escalated": False,
            "escalation_team": None, "player_tone": "neutral",
        }
        print(json.dumps(QAScorer().score(interaction), indent=2))
    elif args.report:
        print(WeeklyReporter().generate(agent_id=args.agent, week=args.week))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
