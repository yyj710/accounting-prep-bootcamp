# accounting-prep-bootcamp · Accounting Competition Prep

> **中文版本 → [README.zh-CN.md](./README.zh-CN.md)**

Study materials from the 7th Guangdong–Hong Kong–Macao Accounting Knowledge Competition. Our team placed in the provincial top 5 out of 200 teams from 32 universities and advanced to the final on 2026-11-28. I was the team captain and produced the preparation materials.

Besides the 13 module guides, this repo keeps the full production process: structured data for 1,472 questions, 24 processing scripts, and intermediate artifacts. The workflow applies to any exam where you need to digest a large question bank quickly.

(All documents are in Chinese.)

## Approach

Questions came from prior-edition banks found through public channels — two sources (1,000 + 483 questions), merged and deduplicated into 1,472.

The preparation ran on several tracks:

1. **Set priorities.** Question distribution showed enterprise and government accounting standards made up over half the bank, so the strategy shifted from full coverage to focused breakthroughs.
2. **Fix the explanations.** Official answers were one-liners I couldn't learn from. I had Claude Code generate per-question explanations and mnemonics, while working through 700 junior-accounting practice questions myself to build foundations.
3. **Order by frequency.** Every question was tagged by knowledge point, clustered, and sorted by frequency — high-frequency topics first.
4. **Restructure.** For topics that still didn't stick, modules were rebuilt as "teach first (mnemonics + everyday analogies), then drill" — the question bank became a textbook.
5. **Split by phase.** Before the exam, content was divided into a deep-understanding track and a memorize-and-score track, plus a one-page sheet of high-frequency rules. Hard, low-frequency topics (long-term equity investments, leases) were dropped.
6. **Distribute.** All guides were exported to Word and shared with the team so everyone prepared from the same material.

## Document structure

Each module guide has five parts:

1. Knowledge framework overview
2. Core exam points (definitions + comparison tables + mnemonics)
3. Top 10 trap questions (wrong claim vs right claim)
4. Quick-reference tables (numbers / ratios / deadlines)
5. Full question practice (with answers and sources)

## Modules and question counts

| Module | Questions | Priority |
|--------|-----------|----------|
| 02 Enterprise Accounting Standards | 280 | Highest |
| 03 Government Accounting Standards | 272 | Highest |
| 01 Accounting Law | 189 | High |
| 04 Internal Control Standards | 184 | High |
| 13 Comprehensive Regulations | 162 | Medium |
| 8 other modules (tax / budget / archives / IT / management accounting…) | 385 | Medium-Low |

For final review: `markdown/00_总复习_知识点与易错点.md` and `word/考前突击速成手册.docx`.

## Repo layout

- `markdown/` — 13 module guides + master review, Markdown sources
- `word/` — Word versions distributed to the team, including the crash-review handbook and a teach-first sample
- `archive/` — production archive
  - `scripts/` — 24 Python scripts: question parsing (parse), assembly (build), character-level validation (validate), Markdown-to-Word conversion (md2docx)
  - `data/` — structured JSON for all 1,472 questions (no / label / type / stem / answer)
  - `knowledge-points/`, `review-cards/`, `lectures/` — knowledge-point lists, module review cards, 12 lecture scripts for the Enterprise Accounting Standards module
  - `master/`, `crash/`, `sample/` — Markdown sources for the master review, crash handbook, and teach-first sample

Quality checks: after re-grouping by knowledge point, a character-level diff against the original bank shows zero differences (independent validate.py script); every question belongs to exactly one module; true/false questions originally misplaced under "single choice" were reclassified by label prefix. Details in [archive/README.md](./archive/README.md).
