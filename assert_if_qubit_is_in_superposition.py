"""Running Example Article - Fig. 6 Circuit to assert whether a
qubit is in superposition or not"""
import os
from qiskit import QuantumCircuit
from common import draw, simulate, plot

# Circuit
def assert_if_qubit_is_in_superposition(params: str, qubits: list[int]):
    """[TODO]""" 
    circuit = QuantumCircuit(2, 1) # initialize with 2 qubits and 1 cbits
    circuit.initialize(params, qubits)

    circuit.cx(0, 1) # CX on qubit 1 controlled by qubit 0
    circuit.h(0) # Hadamard on qubit 0
    circuit.h(1) # Hadamard on qubit 1
    circuit.cx(0, 1) # CX on qubit 1 controlled by qubit 0
    circuit.measure(1, 0) # measure qubit 1 and place into cbit 0

    return circuit

# Helper functions
def run_case(circuit: QuantumCircuit, script_name: str, suffix: str):
    """[TODO]"""
    draw(circuit, script_name, suffix)
    result = simulate(circuit)
    counts = { '0': 0, '1': 0,
               **result.get_counts() }
    plot(counts, script_name, suffix)

def run_case_1(script_name):
    """[TODO]"""
    params, qubits = '00', [0, 1] # initialize q0 and q1 with |0>
    circuit = assert_if_qubit_is_in_superposition(params, qubits)
    suffix = '1'
    run_case(circuit, script_name, suffix)

def run_case_2(script_name):
    """[TODO]"""
    params, qubits = '1', [0] # initialize q0 with |1>
    circuit = assert_if_qubit_is_in_superposition(params, qubits)
    suffix = '2'
    run_case(circuit, script_name, suffix)

def run_case_3(script_name):
    """[TODO]"""
    params, qubits = '11', [0, 1] # q0 = |1>, q1 = |1>
    circuit = assert_if_qubit_is_in_superposition(params, qubits)
    suffix = '3'
    run_case(circuit, script_name, suffix)

# Main
def main():
    """[TODO]"""
    script_name = os.path.basename(__file__)[:-len('.py')]
    run_case_1(script_name)
    run_case_2(script_name)
    run_case_3(script_name)

if __name__ == '__main__':
    main()
