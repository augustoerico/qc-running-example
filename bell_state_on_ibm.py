"""Quantum Circuit composed by two qubits, an Hadamard, a CNOT operator and measument
for each qubit running on IBM backend"""
import os

from qiskit import QuantumCircuit, transpile
# from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
# from qiskit.visualization import plot_histogram
from qiskit_ibm_runtime import QiskitRuntimeService
# from qiskit.circuit.library import RealAmplitudes
# from qiskit.quantum_info import SparsePauliOp

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

# Run on IBMQ
runtime_service = QiskitRuntimeService(
    channel='ibm_quantum', token=os.environ.get('API_KEY'))
backend = runtime_service.least_busy(operational=True, simulator=False)

circuit = transpile(circuit, backend)
job = backend.run(circuit, shots=10000) # blocking

# Save result to file
JOB_STR = str(job)
print(JOB_STR)

with open(f'{script_name}.job.txt', 'w', encoding='utf-8') as file:
    file.write(JOB_STR)

# pass_manager = generate_preset_pass_manager(backend=backend, optimization_level=1)
# pass_manager.run()

# Transpile for simulation
# simulator = Aer.get_backend('aer_simulator') # never returns? async?
# circuit = transpile(circuit, simulator)

# # Simulate the circuit
# result = simulator.run(circuit, shots=10000).result()
# counts = {
#     '00': 0, '01': 0, '10': 0, '11': 0,
#     **result.get_counts(circuit)
# }

