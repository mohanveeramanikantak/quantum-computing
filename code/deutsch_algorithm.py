# Deutsch Algorithm (Basic Version)

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

qc = QuantumCircuit(2, 1)

# Initialize
qc.x(1)
qc.h([0, 1])

# Oracle (example: balanced function)
qc.cx(0, 1)

# Interference
qc.h(0)

# Measure
qc.measure(0, 0)

simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled).result()

counts = result.get_counts()
print("Result:", counts)

print(qc.draw())
