# Quantum Random Number Generator

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

qc = QuantumCircuit(1, 1)

# Put qubit in superposition
qc.h(0)

# Measure
qc.measure(0, 0)

simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=10).result()

counts = result.get_counts()
print("Random Results:", counts)

print(qc.draw())
