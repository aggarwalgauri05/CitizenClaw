# CitizenClaw

An AI agent that helps Indian citizens navigate government schemes, eligibility checks, and benefit applications via Telegram.

Built with OpenClaw and OpenRouter.

---

## How It Works

Every incoming message is classified by an intent validator before any action is taken. Based on the intent, the agent fetches live government data, runs eligibility checks, writes reports to disk, or delegates to a sub-agent — all through a strict enforcement layer.

**Intent types:**

| Intent | Triggered by | Action |
|--------|-------------|--------|
| `POLICY_QUERY` | "what is", "explain", "tell me about" | Explains the scheme |
| `ELIGIBILITY_CHECK` | "am I eligible", "do I qualify" | Fetches gov site + runs check |
| `BENEFIT_MATCH` | "what schemes", "all benefits" | Matches profile, writes report |
| `APPLICATION_GUIDE` | "how do I apply", "help me apply" | Guides step-by-step, delegates to sub-agent |
| `OUT_OF_SCOPE` | Anything non-civic | Blocked immediately, no tools run |

Every response is prefixed with `[INTENT: ...]` so the decision is always visible.

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Agent Framework | OpenClaw |
| LLM | OpenRouter |
| Channel | Telegram |
| Web Fetching | Python `requests` (gov.in whitelist only) |
| PDF Reading | PyMuPDF |
| News | GNews API / PIB RSS fallback |
| Automation | OpenClaw cron |

---

## Prerequisites

- Node.js v22+
- OpenClaw: `npm install -g openclaw@latest`
- An [OpenRouter API key](https://openrouter.ai/keys)
- A Telegram bot token from `@BotFather`

---

## Setup

**1. Start the gateway and connect Telegram**

```bash
openclaw gateway --port 18789

# In a separate terminal:
openclaw channels login
```

Select Telegram when prompted and paste your bot token.

**2. Configure `~/.openclaw/openclaw.json`**

```json
{
  "channels": {
    "telegram": {
      "allowFrom": ["YOUR_TELEGRAM_USER_ID"],
      "token": "YOUR_TELEGRAM_BOT_TOKEN"
    }
  },
  "providers": {
    "openrouter": {
      "baseUrl": "https://openrouter.ai/api/v1",
      "apiKey": "YOUR_OPENROUTER_API_KEY",
      "model": "auto"
    }
  },
  "agent": {
    "provider": "openrouter",
    "model": "qwen/qwen-2.5-7b-instruct",
    "requestTimeout": 60000
  },
  "tools": {
    "allow": ["read", "write", "exec", "web_fetch", "web_search", "process"]
  },
  "approvals": { "exec": { "enabled": true } },
  "gateway": { "maxConcurrentRequests": 1 }
}
```

Find your Telegram user ID by messaging `@userinfobot`.

**3. Install Python dependencies**

```bash
pip install requests pymupdf
```

**4. Create skills via the Control UI**

Open `http://127.0.0.1:18789` and use the Chat tab to create the following skills:

| Skill | Purpose |
|-------|---------|
| `intent-validator` | Classifies every message before any action |
| `policy-interpreter` | Plain-language scheme explanations |
| `benefit-matcher` | Matches citizen profile to qualifying schemes |
| `application-guide` | Step-by-step application guidance |
| `gov-fetcher` | Fetches `.gov.in` URLs only; all others are blocked |
| `eligibility-checker` | Programmatic eligibility checks |
| `report-writer` | Writes benefit reports to disk |
| `news-fetcher` | Civic news (non-civic queries blocked) |
| `pdf-reader` | Reads official policy PDFs from approved directory |

---

## File Structure

```
~/.openclaw/
├── openclaw.json
└── workspaces/
    └── default/
        ├── AGENTS.md
        ├── skills/
        │   ├── intent-validator/
        │   ├── policy-interpreter/
        │   ├── benefit-matcher/
        │   ├── application-guide/
        │   ├── gov-fetcher/          # fetch.py
        │   ├── eligibility-checker/  # check_eligibility.py
        │   ├── report-writer/        # write_report.py
        │   ├── news-fetcher/         # news.py
        │   └── pdf-reader/           # read_pdf.py
        ├── docs/
        │   └── govt-policies/        # Government PDFs
        └── reports/                  # Generated benefit reports

~/.openclaw/workspace-advocacy/
└── AGENTS.md                         # Sub-agent with bounded scope
```

---

## Sub-Agent (Delegation)

`APPLICATION_GUIDE` intents are delegated to a second bot (`@citizen_advocacy_specialist_bot`) with a restricted scope — it can only assist with the one scheme it was delegated. Any attempt to go beyond that returns `[DELEGATION_BLOCK]`.

```bash
openclaw agents add advocacy-specialist
openclaw agents list --bindings
```

---

## Approved Domains

Only `.gov.in` domains can be fetched. All others are blocked at the script level:

```
myscheme.gov.in, pmkisan.gov.in, pmjay.gov.in, nrega.nic.in,
scholarships.gov.in, pmaymis.gov.in, india.gov.in, labour.gov.in, nfsa.gov.in
```

---

## Security

- Add `openclaw.json` to `.gitignore` — it contains API keys and tokens
- `allowFrom` restricts the bot to your Telegram ID only
- All exec commands require manual approval
- Skill scripts cannot access files outside the workspace

```bash
openclaw security audit
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Bot not responding | Ensure gateway is running; check token in config |
| LLM not responding | Verify OpenRouter API key and credits |
| `[INTENT:]` missing from responses | Resend the persona prompt in the Control UI |
| Script not executing | Check `tools.allow` includes `"exec"` |
| Skill not loading | Run `ls ~/.openclaw/workspaces/default/skills/` |
| `gov-fetcher` failing | `pip install requests` |
| PDF reader failing | `pip install pymupdf` |
| Gateway crashes on start | `cat ~/.openclaw/openclaw.json \| python -m json.tool` |

