"""Small, documented circuit constructors for educational use."""

from qiskit import QuantumCircuit


def bell_circuit(measure: bool = True) -> QuantumCircuit:
    """Create a two-qubit Bell-state circuit.

    The ideal state before measurement is (|00> + |11>) / sqrt(2).
    """
    circuit = QuantumCircuit(2, 2 if measure else 0, name="bell_state")
    circuit.h(0)
    circuit.cx(0, 1)
    if measure:
        circuit.measure([0, 1], [0, 1])
    return circuit


def ghz_circuit(num_qubits: int = 3, measure: bool = True) -> QuantumCircuit:
    """Create an n-qubit GHZ circuit for n >= 2."""
    if num_qubits < 2:
        raise ValueError("num_qubits must be at least 2")
    circuit = QuantumCircuit(num_qubits, num_qubits if measure else 0, name=f"ghz_{num_qubits}")
    circuit.h(0)
    for target in range(1, num_qubits):
        circuit.cx(0, target)
    if measure:
        circuit.measure(range(num_qubits), range(num_qubits))
    return circuit


def grover_search_circuit(marked_state: str = "11", measure: bool = True) -> QuantumCircuit:
    """Create one Grover iteration for a small, explicitly marked bit string.

    The string is written in conventional display order: leftmost bit is the
    highest-index qubit. This educational constructor supports 2+ qubits and
    one marked basis state. One iteration is not guaranteed optimal for every
    search-space size; use it as a circuit-construction lesson.
    """
    if len(marked_state) < 2 or set(marked_state) - {"0", "1"}:
        raise ValueError("marked_state must be a binary string of length >= 2")

    n = len(marked_state)
    circuit = QuantumCircuit(n, n if measure else 0, name="grover_one_iteration")
    circuit.h(range(n))

    # Oracle: apply phase -1 to the requested computational basis state.
    # Convert displayed bit order to qubit index order.
    zero_qubits = [i for i, bit in enumerate(reversed(marked_state)) if bit == "0"]
    for qubit in zero_qubits:
        circuit.x(qubit)
    circuit.h(n - 1)
    circuit.mcx(list(range(n - 1)), n - 1)
    circuit.h(n - 1)
    for qubit in zero_qubits:
        circuit.x(qubit)

    # Diffusion operator: H^n X^n multi-controlled-Z X^n H^n.
    circuit.h(range(n))
    circuit.x(range(n))
    circuit.h(n - 1)
    circuit.mcx(list(range(n - 1)), n - 1)
    circuit.h(n - 1)
    circuit.x(range(n))
    circuit.h(range(n))

    if measure:
        circuit.measure(range(n), range(n))
    return circuit
