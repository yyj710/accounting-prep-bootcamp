# accounting-prep-bootcamp · One Autumn, Four Exams, One Set of Notes

> **中文版本 → [README.zh-CN.md](./README.zh-CN.md)**
>
> 一句话：2026 年秋天我同时赶 11/28 竞赛决赛、期末、12/10 ACCA FR、12/11 ACCA FM 四场考试，只整理了一套会计资料，做成 4 个双击就能开的离线刷题网页。最值得看的是[《我怎么和 AI 协作拿结果》](./HOW-I-WORK-WITH-AI.zh-CN.md)：对话原话、九次返工、我自己判断错的地方，以及每一步具体怎么做出来的。

In mid-November 2026 I opened my calendar and found these dates sitting on top of each other:

| Date | What |
|---|---|
| **28 Nov 2026** | Final of the 7th Guangdong–Hong Kong–Macao Accounting Knowledge Competition (I'm team captain) |
| **10 Dec 2026** | ACCA FR global exam |
| **11 Dec 2026** | ACCA FM global exam |
| **End of term** | Primary financial accounting final — date not fixed yet, but revision has to start now |

I'm a first-year student. Four deadlines within about five weeks, and what worried me wasn't that the material was hard — it was **revising the same accounting knowledge four times, each time from page one**. A separate pile of notes per exam, a separate round of highlighting, most of the time spent repeating myself.

So I stopped preparing by *subject* and started preparing by *topic*. How inventory is measured, when revenue is recognised, how statements are put together — the competition tests it, the final tests it, FR and FM test it too. Build it once, use it four times. For the final I just want a good grade; I'm not going to shout a target here. The part I actually worked hard on was making the material **something I'd willingly open every day**.

This repo isn't a file dump. It records a fairly ordinary chain:

> **where I got stuck → what I actually typed in the conversation → what came back → how I clicked through it and where my own judgement was wrong → what ended up being usable**

AI writing code is the easy part. Defining the problem clearly and bothering to check the result is not — and that's the part worth copying.

## Start here

- [How I work with AI to get results](./HOW-I-WORK-WITH-AI.md) — my own words, nine rounds of rework, the calls I got wrong, and what was actually built at each step. **If you read one file, read this one.** (Fuller Chinese version [here](./HOW-I-WORK-WITH-AI.zh-CN.md))
- [Four tools you can just open](./learning-tracks/README.md) — final exam / ACCA FR / ACCA FM / CPA tax
- [The full competition story](./STORY.md) — from 1,472 questions to the provincial top 5

## What you can take away

| If you are… | Take this | How to use it |
|---|---|---|
| Studying primary financial accounting | [Final-exam station](./learning-tracks/01-final-exam/期末复习_满绩冲刺.html) | Double-click, work through 489 questions by chapter, then the accounting-entries drill |
| Sitting ACCA FR (F7) | [FR station](./learning-tracks/02-acca-fr/ACCA_FR_复习站.html) + [condensed notes](./learning-tracks/02-acca-fr/ACCA_FR_考前速记笔记_化简版.md) | Chapter by chapter normally, condensed notes before the exam |
| Sitting ACCA FM (F5) | [FM station](./learning-tracks/03-acca-fm-pm/ACCA_FM_刷题站.html) + [written-answer templates](./learning-tracks/03-acca-fm-pm/FM_文字题模板.md) | Drill → wrong answers back to the quick reference → templates before the exam |
| Studying CPA tax | [Tax self-test site](./learning-tracks/04-cpa-tax/税法CPA复习站.html) | Self-test by chapter, scan the quick-reference tables at the end |
| Not studying accounting, but drowning in a question bank | [The collaboration notes](./HOW-I-WORK-WITH-AI.md) + [the prep approach](./STORY.md) | Reuse the chain: set priorities → write explanations → reorder → split by phase |

All four pages are **a single HTML file each**: no install, no internet, no login. Progress lives in your own browser. Copy it to a USB stick or send it to a classmate and it still opens.

One small thing worth saying out loud: I also revised probability & statistics this term, but that set only matches my own course and isn't tidy enough. **If I wouldn't recommend it to someone else, it doesn't go public.**

## Four lines, one body of knowledge

| Line | When | What I built | Where it stands |
|---|---|---|---|
| Accounting competition | Final **28 Nov** | 1,472 questions regrouped by knowledge point + 13 module guides | Provincial top 5 of 200 teams; preparing for the final |
| Primary accounting final | End of term, date TBC | One offline page: 489 questions, 178 accounting entries | Working; new coursework still being added |
| ACCA FR | **10 Dec** | Offline station + notes rewritten in my own words | In progress |
| ACCA FM | **11 Dec** | Offline drill site + written-answer templates | In progress |
| CPA tax | Not a main line this term | 5-chapter self-test site | Just keeping my hand in |

The first three are the main lines; tax is a fourth tool I keep around so I don't go rusty. Everything is ordered by what the courses actually need — protect the term grade first, and let the competition and ACCA ride on the same material. **Build once, reuse in a different room.** That decision saved me more time than anything else this term.

Most study material is in Chinese; the overviews and the collaboration notes are bilingual.

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
- `learning-tracks/` — the four offline tools built this term

Quality checks: after re-grouping by knowledge point, a character-level diff against the original bank shows zero differences (independent validate.py script); every question belongs to exactly one module; true/false questions originally misplaced under "single choice" were reclassified by label prefix. Details in [archive/README.md](./archive/README.md).

## Added 2026-11-13: the rest of the same semester

Until now this repo held only competition prep. The final, FR, FM and tax material went in together because **they were all built in the same weeks** — splitting them up made the design harder to explain, not easier.

- `learning-tracks/` — four offline pages, each with a short note on where I got stuck and how it turned out.
- `HOW-I-WORK-WITH-AI.md` / `.zh-CN.md` — the part I most want people to read: the original messages, the wrong calls, what was concretely built at each step, and the outcome. Bilingual.
- Raw logs, throwaway scripts and historical snapshots stay in a private worklog repo; textbook PDFs, Word originals and scanned source files are not included. **What's public here is the finished tools, and the thinking that produced them.**
