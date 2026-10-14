import pytest

from qiskit_learning_lab import bell_circuit, ghz_circuit, grover_search_circuit


def test_bell_circuit_structure():
    circuit = bell_circuit()
    assert circuit.num_qubits == 2
    assert circuit.num_clbits == 2
    assert circuit.count_ops()["h"] == 1
    assert circuit.count_ops()["cx"] == 1


def test_unmeasured_bell_circuit():
    circuit = bell_circuit(measure=False)
    assert circuit.num_clbits == 0
    assert circuit.num_qubits == 2


def test_ghz_rejects_single_qubit():
    with pytest.raises(ValueError):
        ghz_circuit(1)


def test_ghz_three_qubits():
    circuit = ghz_circuit(3)
    assert circuit.num_qubits == 3
    assert circuit.count_ops()["cx"] == 2


def test_grover_input_validation():
    with pytest.raises(ValueError):
        grover_search_circuit("not-binary")
