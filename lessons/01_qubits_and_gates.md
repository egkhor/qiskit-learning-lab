# Lesson 1 — Qubits and gates

**Objectives:** create a circuit, apply X and H, inspect it, and explain the difference between a basis state and a superposition.

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.x(0)  # |0> -> |1>
qc.h(0)  # |1> -> (|0> - |1>) / sqrt(2)
print(qc.draw())
```

**Think about it:** why does the H gate applied to |1> produce a relative minus sign? What changes if you apply H twice?
