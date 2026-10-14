"""Inspect a one-iteration Grover search circuit."""

from qiskit_learning_lab import grover_search_circuit, simulate_counts

circuit = grover_search_circuit("11")
print(circuit.draw())
print(simulate_counts(circuit, shots=2048, seed=7))
