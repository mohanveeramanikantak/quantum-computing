# Quantum Computing Demo using Qiskit

from qiskit import QuantumCircuit

def create_circuit():
    qc = QuantumCircuit(2)
    qc.h(0)       # Superposition
    qc.cx(0, 1)   # Entanglement
    return qc

if __name__ == "__main__":
    circuit = create_circuit()
    print(circuit.draw())
