# Qiskit Learning Lab

[![tests](https://github.com/egkhor/qiskit-learning-lab/actions/workflows/tests.yml/badge.svg)](https://github.com/egkhor/qiskit-learning-lab/actions/workflows/tests.yml)

An independent, open-source learning toolkit for quantum circuits, simulation, measurement, and hardware-aware transpilation using Qiskit.

**Status:** initial educational release. The core examples are intended for local execution; real-hardware access is optional and is not required for the lessons or tests.

## What you can learn

- Build and inspect quantum circuits.
- Explore Bell and GHZ states.
- Simulate measurement counts and compare them with theoretical probabilities.
- Calculate total variation distance (TVD) between distributions.
- Inspect circuit depth and gate counts before and after transpilation.
- Run the test suite locally and contribute new lessons.

## Quick start

Requires Python 3.10 or later.

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -e ".[dev,simulation]"
pytest
```

Run examples:

```bash
python examples/bell_state.py
python examples/ghz_state.py
python examples/grover_search.py
```

Run notebooks with Jupyter:

```bash
pip install -e ".[notebooks]"
jupyter lab
```

## Project layout

- `src/qiskit_learning_lab/`: reusable Python functions.
- `examples/`: small runnable scripts.
- `lessons/`: guided Jupyter notebooks and Markdown lesson notes.
- `tests/`: automated tests.
- `docs/`: teaching and contribution notes.

## Design principles

1. **Educational clarity:** examples favor readability over clever abstractions.
2. **Reproducibility:** seeds and dependency ranges are documented where relevant.
3. **Evidence-aware claims:** simulation is not real-hardware evidence; noisy simulation is not a physical device.
4. **Optional hardware:** hardware use requires a user's own account and credentials and is outside the core test suite.
5. **Independent project:** this repository is self-contained and uses only public Qiskit APIs and original educational material.

## Important scientific notes

- Measurement counts are stochastic finite-shot samples.
- Circuit depth and gate counts depend on the transpiler version, target basis, and backend constraints.
- TVD is defined here as `0.5 * sum(abs(p_i - q_i))` over the union of observed/expected outcomes.
- Statevector simulation is generally an ideal mathematical simulation, not a model of a particular quantum device.
- The examples are educational and do not claim quantum advantage.

## Development

```bash
ruff check .
ruff format --check .
pytest
```

## License

MIT. See `LICENSE`.
