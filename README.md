# Architecture-Dependent Expressivity in Quantum Circuits

## 🔬 Key Result

We demonstrate that **circuit depth alone does not determine expressivity** in parameterized quantum circuits.

Under enforced population transfer (with decoherence between layers), the induced decision function becomes:

[
p(1|x) = \sin^2(x/2)
]

**independent of circuit depth.**

**Exact numerical verification:**

```
Max difference (depth 1 vs 3): 2.22e-16
```

![Depth Invariance](results/depth_invariance_exact.png)

---

## 🧠 Core Insight

> Expressivity in quantum circuits is governed by whether **coherence survives across layers**, not by depth itself.

* If coherence accumulates → depth increases expressivity
* If coherence is removed → depth becomes irrelevant

---

## ⚙️ Three Architectural Regimes

We study a minimal two-qubit quantum classifier under controlled modifications:

### 1. Coherent Stacking (No Reset)

* Full quantum coherence preserved
* Depth increases expressivity
* Higher-frequency decision functions emerge

### 2. Partial Reset (Position Qubit Only)

* Partial decoherence
* Distorted, non-systematic behavior
* Neither invariant nor cleanly expressive

### 3. Full Population Transfer (Reset Between Layers)

* Coherence removed between layers
* Measurement depends only on diagonal populations
* **Depth invariance emerges**

---

## 🔬 Methodology

* Simulation: `Qiskit AerSimulator (density_matrix)`
* Exact probability extraction (no sampling noise)
* Controlled circuit modifications:

  * reset placement
  * entanglement timing
  * measurement structure

---

## 📈 What is being computed?

A minimal quantum classifier:

* Input encoded via single-qubit rotation ( R_y(x) )
* Entanglement via CNOT
* Output: probability of measuring `|1⟩` on the second qubit

We analyze how this function changes with **depth and architecture**.

---

## 🎯 Why this matters

This challenges a common assumption in quantum ML:

> “Deeper circuits are more expressive.”

Instead, we show:

* Expressivity is **architecture-dependent**
* Measurement and decoherence can **limit model capacity**
* Circuit design matters more than depth in NISQ settings

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
```

Run the script:

```bash
python expressivity_demo.py
```

Or open the notebook:

```bash
notebooks/expressivity_demo.ipynb
```

---

## 📁 Repository Structure

```
.
├── src/                  # circuit + simulation logic
├── notebooks/            # interactive demos
├── results/              # generated plots
├── figures/              # combined figures (optional)
├── expressivity_demo.py
├── requirements.txt
└── README.md
```

---

## 📚 Conceptual Context

This project connects to research on:

* Expressivity of parameterized quantum circuits
* Fourier structure of PQCs
* Measurement-induced constraints in quantum models

---

## 👤 Author

**Poulastya Kar**
Undergraduate Physics
University of Delhi

---

## 📌 Note

This is a **minimal, analytically tractable model** designed to isolate structural effects in quantum circuit expressivity. The goal is clarity of mechanism, not scale.

---
