# accounting-prep-bootcamp · Accounting Competition Prep Engine

> **中文版本 → [README.zh-CN.md](./README.zh-CN.md)**
>
> Result first: 7th Guangdong-Hong Kong-Macao Accounting Knowledge Competition — **Provincial Top 5, advanced to the final** (32 universities / 200 teams; final on 2026-11-28).
> This repo is the full arsenal I built as team captain, plus the complete process archive: **1,472 questions, 13 modules, 24 automation scripts**.

## The story

I treated this competition as a checkpoint to verify my accounting foundations. Full version (including a 90-second interview script) in [简历故事.md](./简历故事.md) (Chinese). The action chain:

```
Located prior-edition question banks from public channels (1,000 + 483 questions)
  → merged & deduplicated into 1,472 questions
  → distribution analysis locked the focus: enterprise + government accounting dominate
  → human-AI parallel: Claude Code wrote per-question deep explanations + mnemonics in the
    background while I worked through 700 junior-accounting practice questions myself
  → tagged every question by knowledge point, clustered and ranked by frequency
    — review order became data-driven
  → structural upgrade: each module now "teaches first (mnemonics + everyday analogies),
    then drills" — the question bank became a textbook
  → pre-exam split: "deep-understanding" vs "memorize-and-score" tracks + a one-page
    cheat sheet; deliberately skipped low-frequency hard topics (long-term equity, leases)
  → exported Word versions and distributed to the whole team
```

Preparing alone is studying. **Arming the whole team is captaincy.**

## The 5-section structure of every guide (`markdown/`)

1. **Knowledge framework** — mind-map-style overview
2. **Core exam points** — definitions + comparison tables + mnemonics
3. **Top 10 trap questions** — "wrong claim vs right claim" format
4. **Quick-reference tables** — key numbers / ratios / deadlines for last-minute review
5. **Full question practice** — with answers and sources

## Module map (1,472 questions)

| Module | Questions | Priority |
|--------|-----------|----------|
| 02 Enterprise Accounting Standards | 280 | Highest |
| 03 Government Accounting Standards | 272 | Highest |
| 01 Accounting Law | 189 | High |
| 04 Internal Control Standards | 184 | High |
| 13 Comprehensive Regulations | 162 | Medium |
| 8 other modules (tax / budget / archives / IT / management accounting…) | 385 | Medium-Low |

For crunch time: `markdown/00_总复习_知识点与易错点.md` + `word/考前突击速成手册.docx` (all content in Chinese).

## Repo layout

- `markdown/` — 13 module guides + master review (AI-generated, human-verified md sources)
- `word/` — Word versions distributed to teammates (incl. crash-review handbook and the teach-first sample)
- `archive/` — the full process archive, proving how this material was engineered:
  - `scripts/` — 24 Python scripts: question parsing (parse) → assembly (build) → independent validation (validate) → md-to-docx conversion (reusable)
  - `data/` — structured JSON source data for all 1,472 questions (no / label / type / stem / answer)
  - `knowledge-points/` `review-cards/` `lectures/` — knowledge-point lists, module review cards, 12 lecture scripts for the Enterprise Accounting Standards module
  - `master/` `crash/` `sample/` — md sources for the all-module master review, crash handbook, and teach-first sample

**Quality record**: after re-grouping, a character-level diff against the original bank shows **zero differences** (validated by an independent script, not by AI self-report); every question belongs to exactly one module; true/false questions originally misplaced under "single choice" were reclassified by label prefix. See [archive/README.md](./archive/README.md).

## The three most valuable takeaways

1. **Data-driven decisions**: set strategy from question distribution, order revision by knowledge-point frequency — no gut-feel studying
2. **Human-AI division of labor**: AI batch-writes explanations; humans build foundations — two parallel tracks, no blocking
3. **Knowing what to skip**: long-term equity and leases were dropped — exam prep is score maximization under constraints, not coverage maximization
