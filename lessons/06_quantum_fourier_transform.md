# Lesson 6 — The quantum Fourier transform

The quantum Fourier transform (QFT) on `n` qubits is the unitary that maps the basis state |k⟩ to

(1/√N) · Σ_j exp(2πi·jk/N) |j⟩,  with N = 2ⁿ.

It is the same linear map as the discrete Fourier transform (DFT) matrix, but it is built from only O(n²) gates: Hadamards and controlled-phase gates, followed by qubit swaps.

**Bit-order convention:** Qiskit is little-endian, so qubit 0 is the least significant bit and qubit `n-1` is the most significant. We start the transform from the most significant qubit.

```python
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector


def qft_circuit(n: int, swaps: bool = True) -> QuantumCircuit:
    """Textbook QFT from Hadamard and controlled-phase gates."""
    qc = QuantumCircuit(n, name=f"qft_{n}")
    for target in reversed(range(n)):
        qc.h(target)
        for control in range(target):
            qc.cp(np.pi / 2 ** (target - control), control, target)
    if swaps:
        for i in range(n // 2):
            qc.swap(i, n - 1 - i)
    return qc


print(qft_circuit(3).draw())
```

## Check against the DFT matrix

We compare the circuit's unitary with the DFT matrix, entry by entry.

```python
def dft_matrix(n: int) -> np.ndarray:
    size = 2**n
    omega = np.exp(2j * np.pi / size)
    return np.array([[omega ** (j * k) for k in range(size)] for j in range(size)]) / np.sqrt(size)


for n in range(1, 5):
    matches = np.allclose(Operator(qft_circuit(n)).data, dft_matrix(n))
    print(f"n={n}: circuit matches DFT matrix -> {matches}")
```

## The inverse, and the role of the swaps

The inverse QFT is the circuit read backwards with conjugated phases, which `QuantumCircuit.inverse()` does for us. The QFT followed by its inverse should be the identity.

The final swaps only reverse the qubit order. Without them, the circuit is the QFT up to a bit reversal of the output.

```python
qc = qft_circuit(3)
identity = Operator(qc.inverse()).data @ Operator(qc).data
print("inverse undoes the QFT:", np.allclose(identity, np.eye(2**3)))

no_swaps = qft_circuit(3, swaps=False)
print("without swaps equals the DFT:", np.allclose(Operator(no_swaps).data, dft_matrix(3)))

swap_only = QuantumCircuit(3)
swap_only.swap(0, 2)
fixed = no_swaps.compose(swap_only)
print("adding the swap back:", np.allclose(Operator(fixed).data, dft_matrix(3)))
```

## What the QFT does to a basis state

A basis state |k⟩ becomes an equal-magnitude superposition in which the phase of |j⟩ is 2π·jk/N. Below, k = 5 and N = 8, so the phase of |j⟩, measured in units of 2π/8, should be (5·j) mod 8.

```python
n, k = 3, 5
size = 2**n

state = Statevector.from_int(k, size).evolve(qft_circuit(n))
print("probabilities:", np.round(state.probabilities(), 4))

phase_units = (np.round(np.angle(state.data) / (2 * np.pi / size)) % size).astype(int)
print("phase of |j> (units of 2*pi/8):", phase_units)
print("expected (5*j) mod 8:         ", [(k * j) % size for j in range(size)])
```

## Notes and exercises

- Every output probability is 1/N: the QFT turns a definite basis state into a uniform superposition. The information is now stored in the **phases**, which is why a plain measurement of a QFT output is not useful by itself.
- Qiskit also ships a library QFT; its class names have changed across versions, so consult the official documentation for your installed version before comparing against it.
- **Exercise 1:** change `k` and confirm the phase pattern `(k*j) mod N`.
- **Exercise 2:** print `qft_circuit(n).count_ops()` for n = 2…8 and compare how the gate counts grow.
- **Exercise 3:** apply the QFT to a superposition of two basis states and describe the result.
