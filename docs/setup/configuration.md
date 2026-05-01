# Configuration

---

## Environment variables

Copy the example file:
```bash
cp .env.example .env   # macOS/Linux
copy .env.example .env # Windows
```

Never commit `.env`. It is in `.gitignore`.

| Variable | Required | Purpose |
|---|---|---|
| `ANTHROPIC_API_KEY` | No | Only needed if extending the system to generate coaching notes via Claude. The scorer, CSAT analyser, and reporter all run without it. |

Get an API key at: https://console.anthropic.com

---

## No other configuration required

The QA system is self-contained. There are no database connections, no webhook configurations, and no third-party service dependencies beyond the optional Anthropic API key.

All scoring logic is defined in `engine/scorer.py`. The rubric weights and thresholds can be adjusted directly in that file.

---

## Logging

All output goes to stdout. No log configuration is required for prototype use.
