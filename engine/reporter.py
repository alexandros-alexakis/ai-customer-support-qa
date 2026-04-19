"""
Weekly Reporter - aggregates QA scores into a weekly report.
"""

import json
from pathlib import Path
from collections import defaultdict


class WeeklyReporter:
    def __init__(self, data_dir="data/scores"):
        self.data_dir = Path(data_dir)

    def generate(self, agent_id=None, week=None):
        scores = self._load(agent_id, week)
        if not scores:
            return "No scores found. Score some interactions first with run_qa.py"
        total = len(scores)
        avg = sum(s["total_score"] for s in scores) / total
        low_csat = [s for s in scores if s.get("csat_score") and s["csat_score"] < 4]
        by_dim = defaultdict(list)
        by_issue = defaultdict(list)
        flag_counts = defaultdict(int)
        for s in scores:
            for d, v in s.get("dimensions", {}).items(): by_dim[d].append(v)
            by_issue[s.get("issue_type", "unknown")].append(s["total_score"])
            for f in s.get("flags", []): flag_counts[f] += 1
        lines = [
            "# Weekly QA Report", "",
            f"Period: {week or 'all'}  |  Agent: {agent_id or 'all'}  |  Interactions: {total}",
            "", "## Summary", "",
            f"Average QA score: {avg:.1f} / 12",
            f"Low CSAT interactions: {len(low_csat)} ({100*len(low_csat)//total}%)",
            "", "## By dimension", "",
        ]
        for d, vals in by_dim.items():
            lines.append(f"- {d.replace('_',' ').title()}: {sum(vals)/len(vals):.1f} / 2")
        lines += ["", "## By issue type", ""]
        for issue, vals in sorted(by_issue.items()):
            lines.append(f"- {issue}: {sum(vals)/len(vals):.1f} / 12 ({len(vals)} tickets)")
        if flag_counts:
            lines += ["", "## Flags", ""]
            for flag, count in sorted(flag_counts.items(), key=lambda x: -x[1]):
                lines.append(f"- {flag}: {count}")
        return "\n".join(lines)

    def _load(self, agent_id, week):
        if not self.data_dir.exists(): return []
        scores = []
        for f in self.data_dir.glob("*.json"):
            try:
                data = json.loads(f.read_text())
                if agent_id and data.get("agent_id") != agent_id: continue
                if week and data.get("week") != week: continue
                scores.append(data)
            except Exception: continue
        return scores
