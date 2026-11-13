# accounting-prep-bootcamp · One Semester, Three Accounting Deadlines

> **中文版本 → [README.zh-CN.md](./README.zh-CN.md)**

**In one line**: in autumn 2026 I was running three things at once — the 7th Guangdong–Hong Kong–Macao Accounting Knowledge Competition (team captain, final on 2026-11-28), a primary financial accounting final where I was aiming for a **top grade**, and two ACCA global exams (FR and FM) in December. There was no time to revise three times, and all three run on the same accounting knowledge. So I built **one body of material plus four offline practice sites you can open by double-clicking** — worked out sentence by sentence with AI.

This repo is not a file dump. It records **what problem I hit → what I actually asked for in the conversation → what came back → how I checked it and pushed it back → what ended up being usable**.

**Start here**:

- [How I work with AI to get results](./HOW-I-WORK-WITH-AI.md) — my own words, eight rounds of rework, the wrong calls, the outcomes (full Chinese version [here](./HOW-I-WORK-WITH-AI.zh-CN.md))
- [Tools and stories for all four study lines](./learning-tracks/README.md) — final exam / ACCA FR / ACCA FM / CPA tax, every one downloadable and ready to use
- [The full competition story](./STORY.md) — from 1,472 questions to the provincial top 5

## Why three lines share one set of notes

| Line | Goal | What I built | Status |
|---|---|---|---|
| Accounting competition | Lead the team's prep | 1,472 questions regrouped by knowledge point + 13 module guides | Provincial top 5 of 200 teams, into the final |
| Primary accounting final | **Top grade** | One offline page: 489 questions, 178 accounting entries | Working, still improving |
| ACCA FR / FM | December global exams | Two offline practice sites + notes rewritten in my own words | In progress |
| CPA tax | Keep my hand in | A 5-chapter self-test site | Working |

**Useful to you**: all four pages work offline — no install, no internet, no login. Download, double-click, and your progress is saved in your own browser. Most study material is in Chinese; the overviews and the collaboration notes are bilingual.

---

## Where this repo started: competition prep

Study materials from the 7th Guangdong–Hong Kong–Macao Accounting Knowledge Competition. Our team placed in the provincial top 5 out of 200 teams from 32 universities and advanced to the final on 2026-11-28. I was the team captain and produced the preparation materials.

Besides the 13 module guides, this repo keeps the full production process: structured data for 1,472 questions, 24 processing scripts, and intermediate artifacts. The workflow applies to any exam where you need to digest a large question bank quickly.

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

## Added 2026-11-13: study lines and the collaboration notes

- `learning-tracks/` — four study lines (final exam / ACCA FR / ACCA FM / CPA tax), each with an offline page you can open directly and a short "what problem I hit, how I built it" note.
- `HOW-I-WORK-WITH-AI.md` / `HOW-I-WORK-WITH-AI.zh-CN.md` — **the part I most want people to read**: what I asked for, how I checked the output, where my judgement was wrong, and what came out in the end.
- Raw logs, throwaway scripts and historical snapshots stay in a private worklog repo. Textbook PDFs, Word originals and scanned source files are not included here.
