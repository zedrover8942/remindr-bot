# remindr-bot

Small discord.py bot with reminders and quote of the day

Side project, maintained when I have time.

## Examples

```bash
python bot.py
# then /remind 10m stretch and /quote in your server
```

## Installation

```bash
pip install -r requirements.txt
cp .env.example .env  # put your token in .env
```

## Highlights

- Rate-limit friendly: single task loop
- Recurring reminders stored in a JSON file
- Slash commands via discord.py app_commands
- Graceful shutdown flushing state to disk

## Project structure

```text
├── .github/
│   ├── dependabot.yml
│   └── pull_request_template.md
├── docs/
│   ├── configuration.md
│   ├── development.md
│   ├── roadmap.md
│   └── usage.md
├── examples/
│   └── quickstart.md
├── .editorconfig
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── bot.py
└── requirements.txt
```

## Changelog

- `0.1.1` - fix edge case in argument parsing
- `0.1.0` - first working version

## License

MIT licensed, see LICENSE.
