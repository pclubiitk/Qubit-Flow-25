from qiskit import QuantumCircuit, Aer, execute

# Create circuit with 3 qubits and 2 classical bits
qc = QuantumCircuit(3, 2)

# Prepare qubit 0 in state to teleport (|+⟩ state here)
qc.h(0)

# Entangle qubit 1 and 2 (shared between Alice and Bob)
qc.h(1)
qc.cx(1, 2)

# Bell measurement on qubit 0 and 1
qc.cx(0, 1)
qc.h(0)
qc.measure(0, 0)
qc.measure(1, 1)

# Conditional operations on Bob's qubit (qubit 2)
qc.x(2).c_if(qc.cregs[0], 1)
qc.z(2).c_if(qc.cregs[0], 2)

# Simulate the final state
backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
state = result.get_statevector()

# Print the final state
print(state)
