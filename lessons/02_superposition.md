# Lesson 2 — Superposition and probability

```python
from qiskit_learning_lab import bell_circuit, simulate_statevector

state = simulate_statevector(bell_circuit(measure=False))
print(state)
print(state.probabilities_dict())
```

Compare amplitudes with probabilities. Probabilities are squared amplitude magnitudes; amplitudes also contain phase information.
