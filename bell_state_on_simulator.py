"""Quantum Circuit composed by two qubits, an Hadamard, a CNOT operator and measument
for each qubit running on simulated backend"""
import os

from qiskit import QuantumCircuit, transpile
from qiskit.result import Result
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator


script_name = os.path.basename(__file__)[:-len('.py')]


# Circuit
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure_all()

circuit.draw(
    initial_state=True,
    output="mpl",
    filename=f'{script_name}.circuit.png'
)

# Backend
backend = AerSimulator()

# Simulate
transpiled_circuit = transpile(circuit, backend)
job = backend.run(transpiled_circuit, shots=10000) # blocking

# Save result to file
result: Result = job.result()

with open(f'{script_name}.results.txt', 'w', encoding='utf-8') as file:
    file.write(str(result))

plot_histogram(result.data()['counts'], filename=f'{script_name}.histogram.png')
