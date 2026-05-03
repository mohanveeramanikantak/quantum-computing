# Quantum Coin Flip

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

qc = QuantumCircuit(1, 1)

# Superposition = equal chance
qc.h(0)

# Measure
qc.measure(0, 0)

# Simulate multiple times
simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=100).result()

counts = result.get_counts()
print("Coin Flip Results:", counts)

print(qc.draw())
