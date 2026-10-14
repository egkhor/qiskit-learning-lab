# Lesson 7 — Transpilation

```python
from qiskit import transpile
from qiskit_learning_lab import ghz_circuit

logical = ghz_circuit(3, measure=False)
compiled = transpile(logical, optimization_level=2, seed_transpiler=42)
print("Logical depth:", logical.depth())
print("Compiled depth:", compiled.depth())
print("Compiled operations:", compiled.count_ops())
```

For meaningful hardware-specific comparisons, transpile against a defined backend target and record Qiskit version, target, optimization level, and seed. Generic transpilation is not a physical-device performance measurement.
