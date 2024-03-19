from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

def draw(circuit: QuantumCircuit, script_name: str, suffix: str):
    """[TODO]"""
    params = {
        'initial_state': True,
        'output': "mpl",
        'filename': f'{script_name}.circuit{suffix}.png'
    }
    circuit.draw(**params)

def simulate(circuit: QuantumCircuit):
    """[TODO]"""
    simulator = AerSimulator()
    return simulator.run(circuit, shots=10000).result()

def plot(counts: dict, script_name: str, suffix: str):
    """[TODO]"""
    histogram = plot_histogram(counts)
    histogram.savefig(f'{script_name}.histogram{suffix}.png')
