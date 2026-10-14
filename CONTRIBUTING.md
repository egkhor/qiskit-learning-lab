# Contributing

Thanks for considering a contribution.

## Before opening a pull request

1. Open an issue describing the proposed lesson, bug fix, or feature.
2. Keep examples small and runnable on a standard laptop where possible.
3. Add or update tests for code changes.
4. Include expected output or explain nondeterministic results.
5. Cite primary documentation for technical claims.
6. Never commit API keys, tokens, personal data, or proprietary code.

## Local checks

```bash
pip install -e ".[dev,simulation]"
ruff check .
ruff format --check .
pytest
```

## Lesson guidelines

Each lesson should state its learning objectives, prerequisites, runnable code, expected observations, interpretation, and limitations. Distinguish ideal simulation from noisy simulation and physical hardware.
