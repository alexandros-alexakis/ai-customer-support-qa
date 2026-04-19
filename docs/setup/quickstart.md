# Quickstart

Get from clone to a scored interaction in under 5 minutes.

```bash
git clone https://github.com/alexandros-alexakis/ai-customer-support-qa.git
cd ai-customer-support-qa
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python run_qa.py --demo
```

No API key needed. The demo runs entirely on rule-based scoring.

---

## What the demo does

Runs a sample payment issue interaction through the full pipeline. The demo interaction is intentionally imperfect: the agent collected player ID but missed transaction ID and platform, and did not escalate to billing. The system catches both.

---

## Run your own interaction

```bash
python run_qa.py \
  --ticket "I was charged but nothing arrived" \
  --response "Hi, sorry about that. Can I get your player ID?" \
  --csat 3 \
  --issue-type payment_issue \
  --agent agent_001
```

---

## Run tests

```bash
pytest tests/ -v
```
