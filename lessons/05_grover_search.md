# Lesson 5 — Grover search

```python
from qiskit_learning_lab import grover_search_circuit, simulate_counts

qc = grover_search_circuit("11")
print(qc.draw())
print(simulate_counts(qc, shots=4096, seed=21))
```

Inspect the oracle and diffusion structure. The provided helper is a teaching example with one iteration; it is not guaranteed to be optimal for arbitrary search sizes.
