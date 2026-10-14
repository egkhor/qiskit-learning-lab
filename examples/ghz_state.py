"""Build a three-qubit GHZ circuit."""

from qiskit_learning_lab import ghz_circuit, simulate_counts, simulate_statevector

print(ghz_circuit(3, measure=False).draw())
print("Ideal statevector:", simulate_statevector(ghz_circuit(3, measure=False)))
print("Counts:", simulate_counts(ghz_circuit(3), shots=2048, seed=7))
