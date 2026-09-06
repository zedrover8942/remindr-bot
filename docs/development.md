# Development

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env  # put your token in .env
```

## Tests

```bash
python -m pytest -q
```

## Conventions

- functions stay small; extract early
- comments explain *why*, not *what*
- no new dependencies without a good reason
