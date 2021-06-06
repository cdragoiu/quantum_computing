from qiskit.circuit import QuantumCircuit
from qiskit.compiler import transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 3 qubits and 3 classical bits
n_bits = 3
circuit = QuantumCircuit(n_bits, n_bits)

# initial state
circuit.h(0)
circuit.h(1)
circuit.x(2)

# toffoli gate
circuit.barrier()
circuit.h(2)
circuit.t(2)
circuit.cx(1, 2)
circuit.tdg(2)
circuit.cx(0, 2)
circuit.t(2)
circuit.cx(1, 2)
circuit.tdg(2)
circuit.h(2)
circuit.barrier()

# measurement
bits_ms = list(range(n_bits))
circuit.measure(bits_ms, bits_ms)

# simulate
simulator = QasmSimulator()
circuit_sim = transpile(circuit, simulator)
job = simulator.run(circuit_sim, shots=1000)

# results
result = job.result()
counts = result.get_counts(circuit)
circuit.draw(output='mpl')
plot_histogram(counts)
plt.show()
