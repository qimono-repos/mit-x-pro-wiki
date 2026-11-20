#!/usr/bin/env python3
"""Normalize image links and, when vision JSONL exists, inline LaTeX at SRT cues."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path("/workspace/mit-x-pro-wiki")
RAW = ROOT / "mit-raw"
VISION = Path("/workspace/artifacts/vision-out")

IMG_RE = re.compile(
    r"!\[\]\((?:/workspace/artifacts/)?/?mit-raw/(week\d+/media/media/[^)\s]+)\)"
    r"(?:\{[^}]*\})?",
    re.S,
)
# pandoc sometimes splits the attribute brace across lines; IMG_RE with re.S handles { ... }
TS_RE = re.compile(
    r"(?P<start>\d{2}:\d{2}:\d{2},\d{3})\s+\\--\\>\s+(?P<end>\d{2}:\d{2}:\d{2},\d{3})"
)


def parse_clock(s: str | None) -> float | None:
    if not s:
        return None
    s = s.strip()
    parts = s.split(":")
    try:
        if len(parts) == 2:
            m, sec = parts
            return int(m) * 60 + float(sec)
        if len(parts) == 3:
            h, m, sec = parts
            return int(h) * 3600 + int(m) * 60 + float(sec)
    except ValueError:
        return None
    return None


def srt_seconds(hms: str) -> float:
    h, m, rest = hms.split(":")
    sec = rest.replace(",", ".")
    return int(h) * 3600 + int(m) * 60 + float(sec)


def load_vision() -> dict[str, dict]:
    out: dict[str, dict] = {}
    if not VISION.exists():
        return out
    for p in sorted(VISION.glob("batch_*.jsonl")):
        for line in p.read_text(errors="replace").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            rel = obj.get("rel")
            if not rel:
                continue
            prev = out.get(rel)
            if prev is None:
                out[rel] = obj
                continue
            def score(o: dict) -> int:
                return len(o.get("latex") or "") + len(o.get("markdown") or "") + (10 if o.get("timestamp") else 0)
            if score(obj) >= score(prev):
                out[rel] = obj
    return out


def normalize_images(text: str) -> str:
    def repl(m: re.Match) -> str:
        rel = m.group(1)
        return f"![](/mit-raw/{rel})"

    return IMG_RE.sub(repl, text)


def render_block(rel: str, meta: dict | None) -> str:
    """Markdown inserted at the matching transcript cue."""
    link = f"![](/mit-raw/{rel})"
    if not meta:
        return link
    if meta.get("drop") or meta.get("kind") == "photo":
        return ""
    kind = meta.get("kind") or ""
    latex = (meta.get("latex") or "").strip()
    md = (meta.get("markdown") or "").strip()
    ts = meta.get("timestamp")
    bits = []
    if ts:
        bits.append(f"<!-- frame {ts} · {kind} · {rel} -->")
    # Formula frames become display math. Everything else keeps the
    # relocated screenshot so the slide is still visible in Obsidian.
    if kind != "formula" or not latex:
        bits.append(link)
    if latex:
        bits.append(latex if "$$" in latex else f"$$\n{latex}\n$$")
    prose = md
    if latex and prose:
        prose = re.sub(r"\$\$.*?\$\$", " ", prose, flags=re.S)
        prose = re.sub(r"\$[^$]+\$", " ", prose)
        prose = re.sub(r"\s+", " ", prose).strip(" -*")
    if prose and len(prose) > 40:
        bits.append(md)
    return "\n\n".join(b for b in bits if b)


def split_pages(text: str) -> list[str]:
    """Split on top-level headings, keeping the heading with its page."""
    parts = re.split(r"(?=^# )", text, flags=re.M)
    return [p for p in parts if p.strip()]


def inject_page(page: str, vision: dict[str, dict]) -> str:
    images = IMG_RE.findall(page) if "![](" in page else []
    # After normalize, links are ![](/mit-raw/rel) without attributes.
    # Run injection on already-normalized text.
    images = re.findall(r"!\[\]\(/mit-raw/(week\d+/media/media/[^)]+)\)", page)
    if not images:
        return page

    cues = list(TS_RE.finditer(page))
    if not cues:
        # No transcript clock: replace each image in place.
        def repl(m: re.Match) -> str:
            rel = m.group(1)
            return render_block(rel, vision.get(rel))

        return re.sub(r"!\[\]\(/mit-raw/(week\d+/media/media/[^)]+)\)", repl, page)

    # Map each image to the cue whose interval contains the frame time,
    # else the nearest cue start.
    assigned: dict[int, list[str]] = {i: [] for i in range(len(cues))}
    untimed: list[str] = []
    cue_spans = []
    for i, c in enumerate(cues):
        a = srt_seconds(c.group("start"))
        b = srt_seconds(c.group("end"))
        cue_spans.append((a, b))

    for rel in images:
        meta = vision.get(rel) or {}
        t = parse_clock(meta.get("timestamp"))
        if t is None:
            untimed.append(rel)
            continue
        hit = None
        for i, (a, b) in enumerate(cue_spans):
            if a - 0.4 <= t <= b + 0.4:
                hit = i
                break
        if hit is None:
            hit = min(range(len(cue_spans)), key=lambda i: abs(cue_spans[i][0] - t))
        assigned[hit].append(rel)

    # Remove the original image gallery lines (the bare embeds).
    page_wo = re.sub(r"\n*!\[\]\(/mit-raw/week\d+/media/media/[^)]+\)\n*", "\n", page)

    # Insert after each cue's text, before the next cue index.
    # Walk cues from the end so offsets stay valid.
    inserts = []
    for i, c in enumerate(cues):
        rels = assigned[i]
        if not rels:
            continue
        block = "\n\n".join(render_block(r, vision.get(r)) for r in rels if render_block(r, vision.get(r)))
        if not block:
            continue
        # end of this cue: start of next cue match, or end of page
        end = cues[i + 1].start() if i + 1 < len(cues) else len(page_wo)
        # The match positions were in `page`, not page_wo. Re-find in page_wo.
        inserts.append((c.group("start"), block))

    # Re-find timestamps in the stripped page and insert after the cue body.
    # Cue body ends at the next timestamp line or a heading.
    for start_hms, block in reversed(inserts):
        m = re.search(re.escape(start_hms) + r"\s+\\--\\>\s+\d{2}:\d{2}:\d{2},\d{3}", page_wo)
        if not m:
            continue
        # insert just before the following timestamp or heading, after cue text
        rest = page_wo[m.end():]
        nxt = re.search(r"\n\d{2}:\d{2}:\d{2},\d{3}\s+\\--\\>", rest)
        nxt_h = re.search(r"\n#{1,3} ", rest)
        cut_rel = len(rest)
        if nxt:
            cut_rel = min(cut_rel, nxt.start())
        if nxt_h:
            cut_rel = min(cut_rel, nxt_h.start())
        at = m.end() + cut_rel
        page_wo = page_wo[:at] + "\n\n" + block + "\n" + page_wo[at:]

    if untimed:
        extra = "\n\n".join(render_block(r, vision.get(r)) for r in untimed)
        extra = "\n".join(x for x in extra.split("\n") if x is not None)
        # park untimed frames under the Images heading if present, else at top of page
        if "## **Images**" in page_wo:
            page_wo = page_wo.replace("## **Images**", "## **Images**\n\n" + extra, 1)
        else:
            page_wo = extra + "\n\n" + page_wo
    return page_wo


def process_week(path: Path, vision: dict[str, dict]) -> None:
    text = path.read_text(errors="replace")
    text = normalize_images(text)
    if vision:
        pages = split_pages(text)
        # If the file does not start with '# ', split_pages still returns the preamble.
        text = "".join(inject_page(p, vision) for p in pages)
        # collapse huge blank runs left by removed galleries
        text = re.sub(r"\n{4,}", "\n\n\n", text)
    path.write_text(text)


def main() -> None:
    vision = load_vision()
    print(f"vision entries: {len(vision)}")
    for w in range(1, 6):
        p = RAW / f"week{w}.md"
        process_week(p, vision)
        txt = p.read_text()
        imgs = len(re.findall(r"!\[\]\(/mit-raw/", txt))
        bad = len(re.findall(r"/workspace/artifacts/", txt))
        latex = txt.count("$$")
        print(f"week{w}: vault images={imgs} bad_abs={bad} dollar_pairs~{latex // 2}")


if __name__ == "__main__":
    main()
