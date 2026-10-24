# accounting-prep-bootcamp · Accounting Competition Prep Engine

> **中文版本 → [README.zh-CN.md](./README.zh-CN.md)**
>
> Result first: 7th Guangdong-Hong Kong-Macao Accounting Knowledge Competition — **Provincial Top 5, advanced to finals** (out of 200 teams).
> This repo is the full arsenal I built as team captain: **1,472 questions, 13 modules, 5-section structure per document**.

## The story

The 7th edition of the competition publishes no official question bank. My solution was a pipeline:

```
Located the 4th-edition question bank (1,000 + 483 questions from two sources)
  → merged & deduplicated into 1,472 questions
  → built Anki decks for my own spaced repetition
  → structured everything in xlsx
  → batch-generated 13 study guides with Claude + WorkBuddy
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

For crunch time: `markdown/00_总复习_知识点与易错点.md` (all-module summary) + `word/考前突击速成手册.docx`.

## Repo layout

- `markdown/` — 13 module guides + master review (AI-generated, human-verified by me)
- `word/` — Word versions distributed to teammates (incl. the crash-review handbook)

## Why this belongs on a resume

- **Information retrieval**: no official bank exists — I reverse-located prior-edition resources from public channels
- **Toolchain**: Anki (spaced repetition) + xlsx (structuring) + AI batch generation + Word (team distribution) — each tool used where it's strongest
- **Team output**: not personal notes — standardized review material for the entire team
