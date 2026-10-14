"""Build and simulate a Bell state."""

from qiskit_learning_lab import bell_circuit, simulate_counts, simulate_statevector

circuit = bell_circuit(measure=False)
print("Circuit:")
print(circuit.draw())
print("\nIdeal statevector:")
print(simulate_statevector(circuit))

print("\nMeasurement counts (requires qiskit-aer):")
print(simulate_counts(bell_circuit(), shots=2048, seed=7))
