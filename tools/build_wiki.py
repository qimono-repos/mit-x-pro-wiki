#!/usr/bin/env python3
"""Build wiki/index.md, wiki/log.md stubs' source pages from raw week files."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path("/workspace/mit-x-pro-wiki")
RAW = ROOT / "mit-raw"
WIKI = ROOT / "wiki"
SRC = WIKI / "sources"

SECTION_RE = re.compile(r"(?=^# )", re.M)


def slug(s: str) -> str:
    s = s.replace("\\'", "'").replace("\\", "")
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:80] or "page"


def clean_title(line: str) -> str:
    t = line.lstrip("#").strip()
    t = re.sub(r"!\[\]\([^)]*\)(?:\{[^}]*\})?", "", t)
    t = t.replace("\\'", "'").replace("\\", "")
    t = re.sub(r"^Page Title:\s*", "", t, flags=re.I)
    t = re.sub(r"\s+", " ", t)
    return t.strip(" -:")


def first_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return ""
    m = re.search(r"^(.{40,220}?[.])\s", text)
    return (m.group(1) if m else text[:180]).strip()


def learn_body(page: str) -> str:
    m = re.search(r"## \*\*Learn\*\*\s*\n(.*?)(?=\n## |\n# |\Z)", page, re.S)
    if not m:
        return ""
    body = m.group(1).strip()
    # drop leftover image embeds from the learn region
    body = re.sub(r"!\[\]\([^)]+\)", "", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def pages_of(week: int) -> list[dict]:
    text = (RAW / f"week{week}.md").read_text(errors="replace")
    chunks = [c for c in SECTION_RE.split(text) if c.startswith("# ")]
    found = []
    for chunk in chunks:
        first = chunk.splitlines()[0]
        title = clean_title(first)
        low = title.lower().strip("* ")
        if low in {"page title", "section", "learn", "images", "transcript", "practice", "transcripts"}:
            continue
        if low.startswith("learn") or low.startswith("images") or low.startswith("practice"):
            continue
        if len(title) < 3:
            continue
        body = learn_body(chunk)
        found.append({"week": week, "title": title, "learn": body, "anchor": title})
    return found


def main() -> None:
    SRC.mkdir(parents=True, exist_ok=True)
    catalog = []
    for w in range(1, 6):
        for i, page in enumerate(pages_of(w), start=1):
            name = f"week-{w}-{i:02d}-{slug(page['title'])}.md"
            rel = f"sources/{name}"
            fm = (
                "---\n"
                f"title: {json_escape(page['title'])}\n"
                "type: source\n"
                f"week: {w}\n"
                f"raw: mit-raw/week{w}.md\n"
                "---\n\n"
            )
            link = f"[Raw week {w}](/mit-raw/week{w}.md)"
            learn = page["learn"] or "_No separate Learn prose on this page; see the raw transcript._"
            body = (
                f"# {page['title']}\n\n"
                f"Source page from week {w}. {link}\n\n"
                "## Learn\n\n"
                f"{learn}\n\n"
                "## Notes for the wiki\n\n"
                "- Frames from this page's video were moved next to the matching SRT cue in the raw file when a player timestamp was read.\n"
                "- Equations are display math (`$$...$$`). Diagrams may still be an image plus a text description.\n"
                "- This page is immutable source commentary. Synthesis belongs in `wiki/concepts/`.\n"
            )
            (SRC / name).write_text(fm + body)
            catalog.append({**page, "file": rel, "summary": first_sentence(page["learn"])})
    write_index(catalog)
    print(f"source pages: {len(catalog)}")


def json_escape(s: str) -> str:
    return '"' + s.replace('"', "'") + '"'


def write_index(catalog: list[dict]) -> None:
    lines = [
        "# Index",
        "",
        "Content catalog for the MIT xPRO QCFx1 LLM wiki. Read this first when answering a question, then open the linked pages.",
        "",
        "## How this vault is organized",
        "",
        "- `mit-raw/` — immutable course capture (Learn prose, SRT transcripts, slides as LaTeX or images).",
        "- `wiki/sources/` — one note per course page, pointing at the raw week file.",
        "- `wiki/concepts/` — synthesized topic pages. The LLM owns this layer.",
        "- `wiki/log.md` — append-only ingest / query / lint log.",
        "",
        "## Concepts",
        "",
        "| Page | Summary |",
        "|---|---|",
        "| [Shor's algorithm](concepts/shors-algorithm.md) | Factoring reduced to order finding, then solved by quantum period finding. |",
        "| [Period finding](concepts/period-finding.md) | Quantum subroutine that estimates the period of $f(x) = a^x \\bmod N$. |",
        "| [Simon's algorithm](concepts/simons-algorithm.md) | Hidden-subgroup precursor that inspired Shor's circuit. |",
        "| [Quantum Fourier transform](concepts/quantum-fourier-transform.md) | Change of basis that turns periodicity into peaks. |",
        "| [Grover's algorithm](concepts/grovers-algorithm.md) | Amplitude amplification for unstructured search. |",
        "| [Adiabatic quantum computing](concepts/adiabatic-quantum-computing.md) | Slow interpolation from a driver Hamiltonian to a problem Hamiltonian. |",
        "| [Quantum annealing](concepts/quantum-annealing.md) | Open-system variant that allows leaving and returning toward the ground state. |",
        "| [BB84](concepts/bb84.md) | Prepare-and-measure quantum key distribution. |",
        "| [Ekert 91](concepts/ekert91.md) | Entanglement-based QKD, with BBM92. |",
        "| [Bell inequality](concepts/bell-inequality.md) | Device-independent test used for certifiable randomness. |",
        "| [Quantum teleportation](concepts/quantum-teleportation.md) | Move an unknown state using entanglement and two classical bits. |",
        "| [Hamiltonian simulation](concepts/hamiltonian-simulation.md) | Approximate $e^{-iHt}$ on a quantum computer. |",
        "| [Trotterization](concepts/trotterization.md) | Product-formula simulation of a sum of local Hamiltonians. |",
        "| [Phase estimation](concepts/phase-estimation.md) | Read an eigenphase into a clock register with the QFT. |",
        "| [VQE](concepts/vqe.md) | Hybrid variational loop for ground-state energy. |",
        "",
        "## Sources",
        "",
    ]
    current = None
    for item in catalog:
        if item["week"] != current:
            current = item["week"]
            lines += ["", f"### Week {current}", ""]
        summary = item["summary"] or "Course page."
        summary = summary.replace("|", "\\|")
        lines.append(f"- [{item['title']}]({item['file']}) — {summary}")
    lines.append("")
    (WIKI / "index.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
