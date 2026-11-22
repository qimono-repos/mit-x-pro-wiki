"""Generate circuit diagrams (SVG + text) for the wiki, and check each circuit by simulation.

Run from the repo root:  python3 tools/circuits/circuits.py
Outputs go to wiki/media/circuits/<name>.svg and <name>.txt (both committed).
Each builder returns (circuit_to_draw, check) where check() prints a simulation result.
Phase estimation lives in phase_estimation.py.
"""
from math import pi, asin, sqrt
from pathlib import Path

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import QFTGate, UnitaryGate
from qiskit.quantum_info import Operator, Statevector, partial_trace, state_fidelity

OUT = Path("wiki/media/circuits")


def save(name: str, qc: QuantumCircuit) -> None:
    qc.draw("mpl", fold=-1, filename=str(OUT / f"{name}.svg"))
    (OUT / f"{name}.txt").write_text(str(qc.draw("text", fold=-1)) + "\n")


# ── QFT on 3 qubits, gate by gate ────────────────────────────────────────────
def qft(n: int = 3) -> QuantumCircuit:
    qc = QuantumCircuit(n, name="QFT")
    for j in reversed(range(n)):           # most significant qubit first
        qc.h(j)
        for k in reversed(range(j)):
            qc.cp(pi / 2 ** (j - k), k, j)   # R_m rotations: pi/2, pi/4, ...
        qc.barrier()
    for i in range(n // 2):
        qc.swap(i, n - 1 - i)              # reverse qubit order
    return qc


def check_qft() -> None:
    same = Operator(qft(3)).equiv(Operator(QFTGate(3)))
    print(f"QFT(3) gate-by-gate == Qiskit QFTGate(3): {same}")


# ── Grover, 3 qubits, marked |101>, 2 iterations ────────────────────────────
MARKED = "101"


def grover(n: int = 3, marked: str = MARKED, iterations: int = 2, measure: bool = True) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    qc.h(range(n))
    for _ in range(iterations):
        qc.barrier(label="oracle")
        zeros = [i for i, b in enumerate(reversed(marked)) if b == "0"]
        qc.x(zeros) if zeros else None     # map |marked> to |11...1>
        qc.h(n - 1); qc.mcx(list(range(n - 1)), n - 1); qc.h(n - 1)   # multi-controlled Z
        qc.x(zeros) if zeros else None
        qc.barrier(label="diffusion")
        qc.h(range(n)); qc.x(range(n))
        qc.h(n - 1); qc.mcx(list(range(n - 1)), n - 1); qc.h(n - 1)
        qc.x(range(n)); qc.h(range(n))
    if measure:
        qc.measure_all()
    return qc


def check_grover() -> None:
    N = 8
    theta = 2 * asin(1 / sqrt(N))        # course convention: sin(theta/2) = sqrt(M/N)
    for r in (1, 2, 3):
        p = Statevector(grover(iterations=r, measure=False)).probabilities_dict()[MARKED]
        print(f"Grover N=8, {r} iteration(s): P(|{MARKED}>) = {p:.3f}  (theory sin^2((2r+1)theta/2) = {np.sin((2*r+1)*theta/2)**2:.3f})")


# ── BB84: 4 rounds side by side ─────────────────────────────────────────────
ALICE_BITS = [0, 1, 1, 0]
ALICE_BASES = ["Z", "X", "Z", "X"]
BOB_BASES = ["Z", "Z", "X", "X"]


def bb84() -> QuantumCircuit:
    q = QuantumRegister(4, "round")
    c = ClassicalRegister(4, "bob")
    qc = QuantumCircuit(q, c)
    for i, (b, a) in enumerate(zip(ALICE_BITS, ALICE_BASES)):   # Alice prepares
        if b: qc.x(i)
        if a == "X": qc.h(i)
    qc.barrier(label="channel")
    for i, bb in enumerate(BOB_BASES):                           # Bob measures
        if bb == "X": qc.h(i)
    qc.measure(q, c)
    return qc


def check_bb84() -> None:
    qc = bb84().remove_final_measurements(inplace=False)
    probs = Statevector(qc).probabilities_dict()
    for i in range(4):
        p1 = sum(p for k, p in probs.items() if k[::-1][i] == "1")
        keep = ALICE_BASES[i] == BOB_BASES[i]
        print(f"BB84 round {i}: Alice {ALICE_BITS[i]} in {ALICE_BASES[i]}, Bob in {BOB_BASES[i]} -> P(Bob reads 1) = {p1:.2f}  {'KEEP' if keep else 'discard'}")


# ── Teleportation with classical feed-forward ───────────────────────────────
PSI_ANGLE = 1.1  # |psi> = RY(1.1)|0>


def teleport() -> QuantumCircuit:
    q = QuantumRegister(3, "q")
    m = ClassicalRegister(2, "m")
    qc = QuantumCircuit(q, m)
    qc.ry(PSI_ANGLE, 0)                    # state to send, on Alice's q0
    qc.barrier()
    qc.h(1); qc.cx(1, 2)                   # Bell pair: q1 (Alice), q2 (Bob)
    qc.barrier()
    qc.cx(0, 1); qc.h(0)                   # Bell-basis measurement
    qc.measure(0, m[0]); qc.measure(1, m[1])
    with qc.if_test((m[1], 1)):
        qc.x(2)
    with qc.if_test((m[0], 1)):
        qc.z(2)
    return qc


def check_teleport() -> None:
    qc = QuantumCircuit(3)                 # deferred-measurement equivalent
    qc.ry(PSI_ANGLE, 0); qc.h(1); qc.cx(1, 2); qc.cx(0, 1); qc.h(0); qc.cx(1, 2); qc.cz(0, 2)
    bob = Statevector(qc).probabilities_dict(qargs=[2])
    ref = QuantumCircuit(1); ref.ry(PSI_ANGLE, 0)
    print(f"Teleportation: Bob's P(0) = {bob.get('0', 0):.3f}, P(1) = {bob.get('1', 0):.3f}; "
          f"|psi> has P(0) = {np.cos(PSI_ANGLE/2)**2:.3f}, P(1) = {np.sin(PSI_ANGLE/2)**2:.3f}")
    rho_bob = partial_trace(Statevector(qc), [0, 1])
    print(f"Teleportation fidelity (Bob vs |psi>): {state_fidelity(rho_bob, Statevector(ref)):.6f}")


# ── Shor order finding: N = 15, a = 7, 4 counting qubits ────────────────────
A, N_MOD, N_COUNT = 7, 15, 4


def mult_mod_gate(a: int, N: int, label: str) -> UnitaryGate:
    dim = 16
    U = np.zeros((dim, dim))
    for x in range(dim):
        U[(a * x) % N if x < N else x, x] = 1   # permutation on 4 qubits; x >= 15 left alone
    return UnitaryGate(U, label=label)


def shor_order_finding(measure: bool = True) -> QuantumCircuit:
    cnt = QuantumRegister(N_COUNT, "c")
    work = QuantumRegister(4, "w")
    qc = QuantumCircuit(cnt, work)
    qc.x(work[0])                          # work register starts in |1>
    qc.h(cnt)
    for j in range(N_COUNT):
        aj = pow(A, 2 ** j, N_MOD)
        g = mult_mod_gate(aj, N_MOD, f"×{aj} mod 15").control(1)
        qc.append(g, [cnt[j], *work])
    qc.append(QFTGate(N_COUNT).inverse(), cnt)
    if measure:
        m = ClassicalRegister(N_COUNT, "m")
        qc.add_register(m)
        qc.measure(cnt, m)
    return qc


def check_shor() -> None:
    probs = Statevector(shor_order_finding(measure=False)).probabilities_dict(qargs=list(range(N_COUNT)))
    top = {k: v for k, v in probs.items() if v > 1e-6}
    out = ", ".join(f"{k} (={int(k,2)} → {int(k,2)}/16) p={v:.2f}" for k, v in sorted(top.items()))
    print(f"Shor N=15, a=7: {out}  → phases s/4, order r = 4; gcd(7^2±1, 15) = 3, 5")


BUILDERS = {
    "qft-3": (lambda: qft(3), check_qft),
    "grover-3q": (lambda: grover(), check_grover),
    "bb84-4-rounds": (bb84, check_bb84),
    "teleportation": (teleport, check_teleport),
    "shor-order-finding-15": (lambda: shor_order_finding(), check_shor),
}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (build, check) in BUILDERS.items():
        save(name, build())
        check()
