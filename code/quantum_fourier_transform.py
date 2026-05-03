# Quantum Fourier Transform (QFT)

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
import numpy as np

def qft(n):
    qc = QuantumCircuit(n)
    
    for i in range(n):
        qc.h(i)
        for j in range(i+1, n):
            qc.cp(np.pi / (2**(j-i)), j, i)
    
    return qc

# Create circuit
qc = qft(3)
qc.measure_all()

# Simulate
simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled).result()

print("QFT Output:", result.get_counts())
print(qc.draw())
