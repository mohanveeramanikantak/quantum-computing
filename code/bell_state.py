# Bell State Creation using Qiskit

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

# Create circuit
qc = QuantumCircuit(2, 2)

# Apply gates
qc.h(0)        # Superposition
qc.cx(0, 1)    # Entanglement

# Measurement
qc.measure([0, 1], [0, 1])

# Simulate
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit).result()

# Get results
counts = result.get_counts()
print("Measurement Results:", counts)

# Draw circuit
print(qc.draw())
