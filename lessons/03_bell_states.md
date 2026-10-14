# Lesson 3 — Bell states and entanglement

```python
from qiskit_learning_lab import bell_circuit, simulate_counts

qc = bell_circuit()
print(qc.draw())
print(simulate_counts(qc, shots=4096, seed=21))
```

Ideal expectation: only `00` and `11` occur, each near half the shots. Finite-shot variation is normal. This local result is simulation, not hardware evidence.
