# Sales Intelligence Research Automation

A multi-agent AI crew built with [CrewAI](https://crewai.com) that researches a prospect before a sales call. Give it an email address and it pulls together company research, CRM history, past email threads, and delivers a ready-to-use sales intelligence report.

> **Want to try it right now?** Open [`demo.ipynb`](demo.ipynb) and run it cell-by-cell -- no setup beyond API keys required.

## What it does

Given a prospect's email, four agents work sequentially:

| Agent | What it does | Tools |
|-------|-------------|-------|
| **Company Research Specialist** | Researches the prospect and their company online | Serper (web search) |
| **HubSpot Data Analyst** | Pulls CRM records, deal history, and past interactions | HubSpot API |
| **Email History Analyst** | Reviews previous email threads for context and tone | Gmail API |
| **Sales Intelligence Report Writer** | Synthesizes everything into an actionable briefing | Context from all above |

The final output is a markdown report with an executive summary, prospect profile, recommended approach, conversation starters, and objection handling.

## Quick start

### Option A: Interactive notebook

The fastest way to run the crew end-to-end. Everything is self-contained -- agent definitions, task configs, and execution are all inline so you can read, tweak, and run without touching the project structure.

```bash
jupyter notebook demo.ipynb
```

API keys are prompted via `getpass` so nothing gets saved in the notebook.

### Option B: CLI

```bash
pip install uv
crewai install
crewai run
```

This uses the YAML configs under `src/sales_intelligence_research_automation/config/` and reads API keys from a `.env` file. Copy `.env.example` or create `.env` with:

```
OPENAI_API_KEY=sk-...
SERPER_API_KEY=...
NVIDIA_NIM_API_KEY=...
```

## Project structure

```
├── demo.ipynb                          # Self-contained notebook demo
├── src/sales_intelligence_research_automation/
│   ├── config/
│   │   ├── agents.yaml                 # Agent roles, goals, backstories
│   │   └── tasks.yaml                  # Task descriptions and expected outputs
│   ├── crew.py                         # Crew orchestration class
│   └── main.py                         # CLI entry point
├── knowledge/                          # Knowledge base resources
└── .env                                # API keys (not committed)
```

## Customizing

- **Agents**: Edit `config/agents.yaml` to change roles, goals, or backstories
- **Tasks**: Edit `config/tasks.yaml` to change task descriptions or expected outputs
- **Tools & logic**: Edit `crew.py` to swap LLMs, add tools, or change the process type
- **Inputs**: Edit `main.py` to change the default prospect email

## Requirements

- Python >= 3.10, < 3.14
- API keys for OpenAI, Serper, and NVIDIA NIM
- HubSpot and Gmail integrations require [CrewAI Apps](https://docs.crewai.com/concepts/tools) platform authentication

## Support

- [CrewAI Documentation](https://docs.crewai.com)
- [GitHub](https://github.com/joaomdmoura/crewai)
- [Discord](https://discord.com/invite/X4JWnZnxPb)
