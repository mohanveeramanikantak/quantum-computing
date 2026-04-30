# Simplified Grover's Algorithm using Qiskit

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

# Create circuit with 2 qubits
qc = QuantumCircuit(2, 2)

# Step 1: Superposition
qc.h([0, 1])

# Step 2: Oracle (mark |11>)
qc.cz(0, 1)

# Step 3: Diffusion Operator
qc.h([0, 1])
qc.x([0, 1])
qc.h(1)
qc.cx(0, 1)
qc.h(1)
qc.x([0, 1])
qc.h([0, 1])

# Measurement
qc.measure([0, 1], [0, 1])

# Simulate
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit).result()

counts = result.get_counts()
print("Search Result:", counts)

# Draw circuit
print(qc.draw())
