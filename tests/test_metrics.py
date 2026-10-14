import pytest

from qiskit_learning_lab.metrics import counts_to_probabilities, total_variation_distance


def test_counts_normalize():
    assert counts_to_probabilities({"00": 3, "11": 1}) == {"00": 0.75, "11": 0.25}


def test_tvd_identical_distributions_is_zero():
    assert total_variation_distance({"0": 0.5, "1": 0.5}, {"0": 0.5, "1": 0.5}) == 0


def test_tvd_disjoint_distributions_is_one():
    assert total_variation_distance({"0": 1.0}, {"1": 1.0}) == 1.0


def test_tvd_rejects_bad_sum():
    with pytest.raises(ValueError):
        total_variation_distance({"0": 0.2}, {"0": 1.0})


def test_counts_reject_empty():
    with pytest.raises(ValueError):
        counts_to_probabilities({})
