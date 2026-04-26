# =========================
# 0. Setup
# =========================
import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, amplitude_damping_error, phase_damping_error

sim = AerSimulator()
shots = 2000
def minimal_circuit(alpha, depth):
    qc = QuantumCircuit(2, 1)
    
    for _ in range(depth):
        qc.ry(alpha, 0)
        qc.cx(0, 1)
    
    qc.measure(1, 0)
    return qc


def run_circuit(qc, noise_model=None):
    result = sim.run(qc, shots=shots, noise_model=noise_model).result()
    counts = result.get_counts()
    return counts.get('1', 0) / shots
x_vals = np.linspace(0, np.pi, 50)
depths = [1, 2, 3]

plt.figure()

for d in depths:
    probs = []
    for x in x_vals:
        qc = minimal_circuit(x, d)
        p = run_circuit(qc)
        probs.append(p)
    
    plt.plot(x_vals, probs, label=f"depth={d}")

plt.title("Depth Invariance (Population Transfer Architecture)")
plt.xlabel("x")
plt.ylabel("p(1|x)")
plt.legend()
plt.grid()
plt.show()
def deferred_circuit(alpha, depth):
    qc = QuantumCircuit(2, 1)
    
    for _ in range(depth):
        qc.ry(alpha, 0)
    
    qc.cx(0, 1)
    qc.measure(1, 0)
    
    return qc
plt.figure()

for d in depths:
    probs = []
    for x in x_vals:
        qc = deferred_circuit(x, d)
        p = run_circuit(qc)
        probs.append(p)
    
    plt.plot(x_vals, probs, label=f"depth={d}")

plt.title("Frequency Growth (Deferred Entanglement)")
plt.xlabel("x")
plt.ylabel("p(1|x)")
plt.legend()
plt.grid()
plt.show()
def get_dephasing_noise(gamma):
    noise = NoiseModel()
    error = phase_damping_error(gamma)
    noise.add_all_qubit_quantum_error(error, ['ry'])
    return noise


def get_amplitude_noise(gamma):
    noise = NoiseModel()
    error = amplitude_damping_error(gamma)
    noise.add_all_qubit_quantum_error(error, ['ry'])
    return noise
gamma = 0.3

dephasing_noise = get_dephasing_noise(gamma)
amplitude_noise = get_amplitude_noise(gamma)

clean_probs = []
dephase_probs = []
damp_probs = []

for x in x_vals:
    qc = minimal_circuit(x, depth=1)
    
    clean_probs.append(run_circuit(qc))
    dephase_probs.append(run_circuit(qc, dephasing_noise))
    damp_probs.append(run_circuit(qc, amplitude_noise))
plt.figure()

plt.plot(x_vals, clean_probs, label="Clean")
plt.plot(x_vals, dephase_probs, '--', label="Dephasing")
plt.plot(x_vals, damp_probs, ':', label="Amplitude Damping")

plt.title("Noise Asymmetry")
plt.xlabel("x")
plt.ylabel("p(1|x)")
plt.legend()
plt.grid()
plt.show()
probs_d1 = []
probs_d3 = []

for x in x_vals:
    qc1 = minimal_circuit(x, 1)
    qc3 = minimal_circuit(x, 3)
    
    probs_d1.append(run_circuit(qc1))
    probs_d3.append(run_circuit(qc3))

probs_d1 = np.array(probs_d1)
probs_d3 = np.array(probs_d3)

print("Max difference (depth 1 vs 3):",
      np.max(np.abs(probs_d1 - probs_d3)))
plt.plot(x_vals, probs_d1 - probs_d3)
plt.title("Difference (depth 1 - depth 3)")
plt.axhline(0, linestyle='--')
plt.grid()
plt.show()