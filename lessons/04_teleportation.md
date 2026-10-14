# Lesson 4 — Quantum teleportation

Teleportation moves an **unknown qubit state** from one qubit to another using a shared entangled pair plus two classical bits. It does not transmit information faster than light, and the original state is destroyed by the measurement.

The circuit has three qubits:

- `q0` holds the state we want to send, |ψ⟩.
- `q1` and `q2` form a Bell pair.
- `q2` should end up holding |ψ⟩.

To keep this lesson simple and portable across Qiskit versions, we use the **deferred-measurement** form: the classically controlled corrections are replaced by controlled gates (`cx` from `q1`, `cz` from `q0`). This gives the same result for `q2` and lets us check it exactly with a statevector.

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace, state_fidelity

from qiskit_learning_lab import simulate_statevector


def teleportation_circuit(theta: float, phi: float, correct: bool = True) -> QuantumCircuit:
    """Teleport the state Rz(phi) Ry(theta)|0> from q0 to q2 (deferred measurement)."""
    qc = QuantumCircuit(3, name="teleportation")
    qc.ry(theta, 0)  # prepare the state to send on q0
    qc.rz(phi, 0)
    qc.barrier()
    qc.h(1)  # Bell pair on q1, q2
    qc.cx(1, 2)
    qc.barrier()
    qc.cx(0, 1)  # Bell-basis change on q0, q1
    qc.h(0)
    qc.barrier()
    if correct:
        qc.cx(1, 2)  # X correction, controlled by q1
        qc.cz(0, 2)  # Z correction, controlled by q0
    return qc


print(teleportation_circuit(1.1, 0.7).draw())
```

## Checking that it worked

If teleportation works, the reduced state of `q2` (after ignoring `q0` and `q1`) equals the state we prepared on `q0`. We measure this with the **fidelity**, which is 1 when two states are identical.

```python
def received_fidelity(theta: float, phi: float, correct: bool = True) -> float:
    state = simulate_statevector(teleportation_circuit(theta, phi, correct))
    received = partial_trace(state, [0, 1])  # keep only q2

    reference = QuantumCircuit(1)
    reference.ry(theta, 0)
    reference.rz(phi, 0)
    target = Statevector.from_instruction(reference)
    return float(state_fidelity(received, target))


for theta, phi in [(0.4, 0.2), (1.1, 0.7), (2.5, -1.3)]:
    with_fix = received_fidelity(theta, phi, correct=True)
    without_fix = received_fidelity(theta, phi, correct=False)
    print(
        f"theta={theta:5.2f} phi={phi:5.2f}  "
        f"corrected={with_fix:.4f}  uncorrected={without_fix:.4f}"
    )
```

With the corrections the fidelity should be 1.0000. Without them it should be about 0.5000: averaged over the four possible measurement outcomes, `q2` is maximally mixed, so it carries no information about |ψ⟩ until the corrections are applied.

## Notes and exercises

- This is an ideal statevector calculation, not a noisy or hardware experiment.
- Real teleportation measures `q0` and `q1` mid-circuit and applies the corrections conditioned on the classical results. Qiskit supports this through dynamic circuits (`QuantumCircuit.if_test`); the exact feature set depends on your Qiskit and Aer versions, so consult the official documentation for the version you installed.
- **Exercise 1:** try other values of `theta` and `phi`. Does the fidelity ever drop below 1 with corrections?
- **Exercise 2:** remove only the `cz` correction, then only the `cx` correction. Which fidelities do you get, and why?
- **Exercise 3:** rebuild the circuit with two classical bits, mid-circuit measurements and `if_test`, and sample it with Aer.
