# Schema — MIT xPRO QCFx2 LLM wiki

This vault is a [Karpathy LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a persistent, interlinked markdown knowledge base an LLM maintains, not a RAG pile that is re-derived on every question.

The course material is MIT xPRO QCFx1 (Introduction to Quantum Computing), captured from the edX pages the student saved: Learn prose, SRT transcripts, and video-frame screenshots.

## Three layers

| Layer | Path | Who writes it |
|---|---|---|
| Raw sources | `mit-raw/` | Nobody. Immutable. The course capture is the source of truth. |
| Wiki | `wiki/` | The LLM. Summaries, concepts, comparisons, the index, the log. |
| Schema | `AGENTS.md` (this file) | Human, occasionally. Conventions for ingest, query, and lint. |

Obsidian vault root is this directory. Image embeds use vault-absolute paths: `![](/mit-raw/week5/media/media/image26.png)`. Do not use `/workspace/...` paths.

## Raw conventions

- `mit-raw/weekN.md` is one week. Course pages inside it start at a level-1 heading.
- Each page is roughly: Learn prose, then a transcript in SRT cue form (`00:00:00,000 \--> 00:00:02,580`).
- A video frame belongs at the SRT cue that contains its player clock (lower-left current time, not the duration).
- Equations are KaTeX display math (`$$ ... $$`). Do not put a formula-only slide back in as a bare image when LaTeX exists.
- Diagrams and UI screenshots may keep the image plus a text description.
- Photos of hardware or people with no teaching content are omitted on purpose.

## Wiki conventions

- `wiki/index.md` — catalog. One link and one-line summary per page. Update it on every ingest. Read it before answering a question.
- `wiki/log.md` — append-only. Every entry starts with `## [YYYY-MM-DD] op | title` so `grep "^## \[" wiki/log.md` works.
- `wiki/sources/` — one note per course page. Points at the raw week file and quotes the Learn section. Do not copy the whole transcript here.
- `wiki/concepts/` — one idea per file. Title is the concept name. Open with a two-sentence claim, then the math, then links to the source notes that support it. Prefer `[[concepts/grovers-algorithm]]` wikilinks between concepts and markdown links to sources.
- File names are lowercase kebab-case. No spaces.
- When two pages disagree, do not silently pick one. Record the conflict in the log and on both pages.
- Cite a claim with a link to the source note or a heading in `mit-raw/weekN.md`. Do not invent lecture results, gate counts, or experimental numbers that are not in the raw files.

## Operations

### Ingest

1. Drop the new source under `mit-raw/` (or a new file beside the week notes). Do not edit older raw files except to fix a broken embed path.
2. Read the source. Discuss the takeaways if a human is present.
3. Add or update `wiki/sources/...`.
4. Update every concept page the source actually changes. A single lecture often touches several concepts.
5. Update `wiki/index.md`.
6. Append an ingest entry to `wiki/log.md`.

### Query

1. Read `wiki/index.md`.
2. Open only the pages that can answer the question.
3. Answer with citations to those notes.
4. If the answer is worth keeping, file it as a new page under `wiki/concepts/` or `wiki/analyses/` and index it. That is how the wiki compounds.

### Lint

Periodically check for:

- contradictions between concept pages
- claims with no source link
- orphan notes (not in the index, or linked by nobody)
- concept pages that should mention a source but do not
- raw frames that are still only images even though they are equations

Record the lint pass in the log. Suggest the next source or question. Do not mass-rewrite raw transcripts during lint.

## Obsidian

Open this folder as a vault. Graph view should show concepts linking to source notes. The raw week files are long; browse them from the source notes rather than scrolling a week from the top.
