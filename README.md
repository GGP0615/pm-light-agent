# LIGHT AI Agent

**LIGHT** is your personal Product‑Manager Copilot: Slack‑native, integrated with Gmail, Asana, and Google Calendar. Automate summaries, drafts, updates, and daily standups—all from Slack.

## Setup
1. Create GitHub repo and add files.
2. Copy `.env.example` → `.env`, fill credentials.
3. `make build && make deploy`

## Commands (Slack)
- `/light inbox` → lists unread threads.
- `/light summarize [channel] [range]` → summary + send button.
- `/light tasks` → shows upcoming/overdue tasks.

## Architecture
See [architecture.md].

## Contributing
PRs welcome. CI runs on every push.
