# mit-x-pro-wiki

Obsidian vault for MIT xPRO QCFx2 (Introduction to Quantum Computing), structured as an [LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Open it

1. Obsidian → Open folder as vault → this directory.
2. Start at [wiki/index.md](wiki/index.md).
3. The maintenance rules for an LLM assistant are in [AGENTS.md](AGENTS.md).

## Layout

```
AGENTS.md          schema (ingest, query, lint)
mit-raw/           immutable course capture, one markdown file per week
  weekN.md
  weekN/media/media/*.png
wiki/
  index.md         catalog — read this first
  log.md           append-only operations log
  sources/         one note per course page
  concepts/        synthesized topics (Shor, Grover, QKD, VQE, ...)
```

Image links are vault-absolute (`/mit-raw/week5/media/media/image26.png`), which is what Obsidian and a folder-root markdown preview resolve. They are not `/workspace/...` paths.

Slides that are equations were transcribed to `$$ ... $$` and placed on the SRT cue whose interval contains the player clock (the time in the lower-left of the video frame). Diagrams keep the image plus a short description. Hardware photos were dropped.

## What is not done

Not every frame had a readable clock, and a few slides are still images when the transcription pass did not return LaTeX. Re-run `python3 tools/build_raw.py` after adding JSONL under the vision output directory if you extend the transcription. Then `python3 tools/build_wiki.py` to refresh source notes from the Learn sections.
