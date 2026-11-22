"""Generate the phase-estimation circuit diagrams used in wiki/concepts/phase-estimation.md.

Run from the repo root:  python3 tools/circuits/phase_estimation.py
Outputs (committed, so Obsidian needs no Python):
  wiki/media/circuits/phase-estimation.svg   rendered diagram (matplotlib drawer)
  wiki/media/circuits/phase-estimation.txt   ASCII diagram (text drawer)
It also simulates the circuit and prints the most likely readouts.
"""
from math import pi
from pathlib import Path

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import QFTGate
from qiskit.quantum_info import Statevector

N_CLOCK = 4          # first register: n counting qubits
THETA = 5 / 16       # exactly representable in 4 bits: 0.0101 -> readout 0101 = 5
OUT = Path("wiki/media/circuits")


def qpe(theta: float, n: int, measure: bool = True) -> QuantumCircuit:
    clock = QuantumRegister(n, "c")
    target = QuantumRegister(1, "u")
    qc = QuantumCircuit(clock, target)
    qc.x(target[0])                        # |u> = |1> is the eigenstate of P(phi) with eigenvalue e^{i phi}
    qc.h(clock)                            # step 1: superposition on the first register
    for j in range(n):                     # step 2: controlled U^{2^j}, controlled by clock qubit j
        qc.cp(2 * pi * theta * 2**j, clock[j], target[0])
    qc.append(QFTGate(n).inverse(), clock)  # step 3: inverse QFT on the first register
    if measure:
        creg = ClassicalRegister(n, "m")
        qc.add_register(creg)
        qc.measure(clock, creg)
    return qc


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    qc = qpe(THETA, N_CLOCK)
    qc.draw("mpl", fold=-1, filename=str(OUT / "phase-estimation.svg"))
    (OUT / "phase-estimation.txt").write_text(str(qc.draw("text", fold=-1)) + "\n")

    for theta in (THETA, 0.3):  # exact vs not exactly representable in 4 bits
        probs = Statevector(qpe(theta, N_CLOCK, measure=False)).probabilities_dict(qargs=list(range(N_CLOCK)))
        top = sorted(probs.items(), key=lambda kv: -kv[1])[:3]
        print(f"theta={theta}: " + ", ".join(f"{b} (={int(b, 2)}/16={int(b, 2)/16:.4f}) p={p:.3f}" for b, p in top))
