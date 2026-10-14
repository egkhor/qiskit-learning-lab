"""Educational quantum circuit utilities built on Qiskit."""

from .circuits import bell_circuit, ghz_circuit, grover_search_circuit
from .metrics import counts_to_probabilities, total_variation_distance
from .simulation import simulate_counts, simulate_statevector

__all__ = [
    "bell_circuit",
    "ghz_circuit",
    "grover_search_circuit",
    "counts_to_probabilities",
    "total_variation_distance",
    "simulate_counts",
    "simulate_statevector",
]

__version__ = "0.1.0"
