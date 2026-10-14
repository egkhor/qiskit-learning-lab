# Core concepts

## State preparation and measurement

A circuit applies gates to a quantum state. Measurement samples outcomes according to the state and measurement basis. Finite-shot counts vary between runs unless a simulator seed and environment are held fixed.

## Bell state

The circuit H(q0), CX(q0, q1) prepares (|00> + |11>)/sqrt(2). Measuring in the computational basis ideally yields `00` and `11` with equal probability.

## GHZ state

For n >= 2, H on the first qubit followed by controlled-X operations from that qubit to the others prepares (|00...0> + |11...1>)/sqrt(2).

## Total variation distance

For discrete distributions P and Q, TVD is 1/2 times the sum of absolute probability differences. It ranges from 0 (identical distributions) to 1 (disjoint support).

## Transpilation

Transpilation maps a logical circuit to a circuit compatible with a target's constraints and basis gates. Output depends on target, optimization settings, and Qiskit version.
