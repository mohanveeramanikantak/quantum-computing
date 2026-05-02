# Quantum Teleportation using Qiskit

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

qc = QuantumCircuit(3, 3)

# Step 1: Create entanglement between qubit 1 and 2
qc.h(1)
qc.cx(1, 2)

# Step 2: Prepare state to teleport (qubit 0)
qc.h(0)

# Step 3: Bell measurement
qc.cx(0, 1)
qc.h(0)

# Step 4: Measure qubits 0 and 1
qc.measure([0, 1], [0, 1])

# Step 5: Conditional operations
qc.cx(1, 2)
qc.cz(0, 2)

# Measure final qubit
qc.measure(2, 2)

# Simulate
simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled).result()

counts = result.get_counts()
print("Teleportation Result:", counts)

print(qc.draw())
