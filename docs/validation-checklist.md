# Release validation checklist

Run this checklist before tagging a release or claiming compatibility.

- [ ] Use a clean Python 3.10, 3.11, or 3.12 environment.
- [ ] Install `pip install -e ".[dev,simulation,notebooks]"`.
- [ ] Run `ruff check .`.
- [ ] Run `ruff format --check .`.
- [ ] Run `pytest`.
- [ ] Run all example scripts.
- [ ] Open each notebook and run all cells from a clean kernel.
- [ ] Confirm package metadata and license.
- [ ] Review dependency compatibility against the currently supported Qiskit release.
- [ ] Search the repository for API keys, tokens, private files, and any proprietary or unrelated material.
- [ ] Replace `YOUR-USERNAME` in `CITATION.cff` after creating the public repository.
- [ ] Add a release tag and DOI only after a release has actually been published.

**Current artifact note:** this package was generated in a runtime without Qiskit installed, so its tests and examples have not been executed here. Do not describe it as tested until the checklist passes in a Qiskit-enabled environment.
