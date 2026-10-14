"""Simulation helpers with optional Qiskit Aer support."""

from collections.abc import Mapping

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def simulate_statevector(circuit: QuantumCircuit) -> Statevector:
    """Return an ideal statevector for a circuit with measurement removed.

    This helper is for ordinary state-preparation circuits. It excludes
    measurement and barrier instructions; circuits with classical control,
    reset, or other non-unitary operations need a dedicated simulation path.
    """
    clean = QuantumCircuit(circuit.num_qubits)
    for item in circuit.data:
        if item.operation.name in {"measure", "barrier"}:
            continue
        qargs = [circuit.find_bit(qubit).index for qubit in item.qubits]
        clean.append(item.operation, qargs)
    return Statevector.from_instruction(clean)


def simulate_counts(
    circuit: QuantumCircuit, shots: int = 1024, seed: int | None = 1234
) -> Mapping[str, int]:
    """Sample a circuit using Qiskit Aer if installed, otherwise raise guidance."""
    if shots < 1:
        raise ValueError("shots must be at least 1")
    try:
        from qiskit_aer import AerSimulator
    except ImportError as exc:
        raise RuntimeError(
            "Count simulation requires the optional dependency. Install with: "
            'pip install -e ".[simulation]"'
        ) from exc

    measured = circuit.copy()
    if measured.num_clbits == 0:
        measured.measure_all()
    simulator = AerSimulator()
    result = simulator.run(measured, shots=shots, seed_simulator=seed).result()
    return result.get_counts()
