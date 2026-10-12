# Contributing

Thanks for your interest in scrapemend. For architectural changes, please open an issue to discuss before sending a PR.

## Setup

```sh
python -m venv .venv
# activate it, then:
pip install -e ".[dev]"
pre-commit install
```

## Before opening a PR

```sh
ruff check . && ruff format --check .
mypy
pytest
```

## Ground rules

- **Synthetic fixtures only.** Never commit real scraped data, snapshots of real sites, credentials, or server details.
- **Generic engine only.** No code targeting a specific real website. Site-specific behavior belongs in plugins outside this repo.
- **No evasion.** No CAPTCHA solving, block evasion, proxy rotation for evasion, or login bypass. PRs adding these will be closed.
- **LLMs propose data, never code.** Repair output must be a structured spec diff validated by Pydantic.
- **Type hints everywhere.** `mypy --strict` must pass.
