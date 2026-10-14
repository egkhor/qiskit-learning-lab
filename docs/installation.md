# Installation

1. Install Python 3.10+.
2. Create and activate a virtual environment.
3. Run `pip install -e ".[dev,simulation,notebooks]"`.
4. Run `pytest`.
5. Start notebooks with `jupyter lab`.

The `simulation` extra installs Qiskit Aer. The base package provides Qiskit's circuit and quantum-information tools but does not require hardware credentials.
