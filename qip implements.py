
import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

sim = AerSimulator(method="density_matrix")
shots = 2000


def minimal_population_transfer(alpha, depth):
    qc = QuantumCircuit(2, 1)

    for i in range(depth):
        # Reset BOTH qubits → fresh start each layer
        qc.reset(0)
        qc.reset(1)

        qc.ry(alpha, 0)
        qc.cx(0, 1)

        # Only keep final layer for measurement
        if i < depth - 1:
            qc.reset(1)

    qc.measure(1, 0)
    return qc


from qiskit.quantum_info import DensityMatrix

from qiskit.quantum_info import DensityMatrix

def run_exact(qc):
    qc_no_meas = qc.remove_final_measurements(inplace=False)

    # 🔥 REQUIRED: tell simulator to output density matrix
    qc_no_meas.save_density_matrix()

    result = sim.run(qc_no_meas).result()
    rho = result.data(0)['density_matrix']

    dm = DensityMatrix(rho)

    probs = dm.probabilities()

    p1 = 0
    for i, p in enumerate(probs):
        if i % 2 == 1:
            p1 += p

    return p1
x_vals = np.linspace(0, np.pi, 50)
depths = [1, 2, 3]

all_probs = {}

for d in depths:
    probs = []
    for x in x_vals:
        qc = minimal_population_transfer(x, d)
        probs.append(run_exact(qc))   # use your exact function
    
    all_probs[d] = np.array(probs)


    
    all_probs[d] = np.array(probs)
    plt.plot(x_vals, probs, label=f"depth={d}")

plt.title("Depth Invariance (Population Transfer with Reset)")
plt.xlabel("x")
plt.ylabel("p(1|x)")
plt.legend()
plt.grid()
plt.show()
diff = np.max(np.abs(all_probs[1] - all_probs[3]))
print("Max difference (depth 1 vs 3):", diff)
from qiskit_aer import AerSimulator

