# How I work with AI to turn a course into something I can actually revise with

> **中文版本（更完整，含我在对话里的原话）→ [HOW-I-WORK-WITH-AI.zh-CN.md](./HOW-I-WORK-WITH-AI.zh-CN.md)**

Almost everything in this repo was made sentence by sentence in conversations with AI.

This is not a note about which tools I used. It is about **what I asked for, what came back wrong, how I pushed it back, and what I ended up with**. The thing that decided the result was not whether AI could write code — it was whether I could define the problem clearly and actually check the output.

## Why I had to work this way

> "Time is tight. I want to prepare for the competition *and* the final exam *and* actually learn accounting. I've also registered for the ACCA FR and FM global exams in December."

In autumn 2026 three deadlines sat on top of each other: the Guangdong–Hong Kong–Macao Accounting Knowledge Competition (I was team captain), a primary financial accounting final where I was aiming for a **top grade, not a pass**, and two ACCA global exams in December.

There was no time for three separate revision projects. My call: they all run on the **same accounting knowledge**, so I built one body of material, ordered by what the courses actually need, and let all three lines share it.

## The seven moves

**1. Say exactly what I want, what I don't want, and who it's for.**
The first delivery was two Markdown files. I changed the brief the same day: *not a website, a single HTML file I can open offline; the goal is a top grade, so don't give me only high-frequency traps, cover everything; I'll keep sending new coursework, so it has to keep growing.* Five constraints in one message — and they shaped every decision afterwards.

**2. I check, I don't just accept.**
> "The practice cards have no options, multi-choice and true/false are broken — check the whole thing again. And **write a plan before you start**, tell me what you're going to do, so we don't keep reworking it."

That second half became a standing rule: before any change, write a short plan saying what will be done and how it will be checked. Rework dropped sharply.

**3. Raw textbook text is not revision material.**
> "Why is there no answer or explanation? There *are* answers. Why would you just copy the original text — **can't I read the book myself**? I need it organised so I can actually remember it."

I had been wrong: I checked only the first volume of a workbook and decided it had no answers, when the answer booklet was in the second volume. I deleted 33 pasted text blocks and rebuilt them as chapter summary cards plus questions with three-part explanations (why this answer → the exam point → a memory hook). Lesson: before declaring "there's no answer key", read the whole book.

**4. Simpler practice wins, and I decide.**
For accounting entries, AI proposed a full "pick the account, type the amount, auto-grade" exercise. I cut it: *"Just give me the scenario. I'll work it out in my head — if I got it, I mark it as known; if not, it goes into my mistake book."* The result: 178 debit/credit templates from 11 courseware decks, 182 self-checked exercises, no fancy interface. A feedback loop just needs **checking and reviewing**, not complexity.

**5. I control the pace, not the system.**
> "Can we skip questions I already know? And let me add or remove things from the mistake book manually — some I don't want to do, and some I only guessed right but still need to revise."

That exposed a hidden assumption: the system treated "answered correctly" as "mastered". A lucky guess isn't mastery. So now I can mark a question as done, restore it, force it into the mistake book, and a manually added question is never silently removed after a later correct answer.

**6. When answers disagree, go to the authoritative source.**
I handed over two official answer booklets and asked for a full check. The original answers had been inferred from the question stems and never verified. Of 198 questions, 8 disagreed and 1 was missing. After checking each official explanation, **all 8 were our mistakes** (in one case I had even reworded an option), plus a missing question to restore. Final: **198/198 matched**. AI-written explanations are never the standard — the official key is.

**7. Fix the bug, don't work around it.**
> "Can't submit — there's a bug, please fix it."

Multi-choice questions sat selected but the submit button did nothing. Reproducing it showed only cards with a section tag were affected: the tag and the button shared a class name, so the click landed on the tag. 120 of 167 multi-choice questions were hit. Fixed, then verified with 185 checks.

## What came out

| | |
|---|---|
| Final-exam station | One 486 KB file, double-click to open, no install, no internet: **489 questions**, **178 entry templates**, mistake book, skip marking, auto-saved progress |
| Competition prep | 1,472 questions reorganised by knowledge point + 13 module guides; provincial top 5 of 200 teams, final on 2026-11-28 |
| ACCA FR / FM | One offline practice site each, plus notes rewritten in the way I actually understand things |
| CPA tax | A practice site with a 5-chapter question bank |
| December FR / FM global exams | **In progress** — this repo keeps updating |

## Take these if you want

1. State the goal, the boundaries, the user, and how it will grow — not just "make me some notes".
2. Ask for a plan before the work starts.
3. Deliver something usable, not a pile of source text.
4. Check it yourself and say *specifically* what is wrong.
5. Verify against the authoritative answer key; admit your own mistakes.
6. Practice needs checking and review — but it doesn't have to be auto-graded.
7. Keep a trail, so you can see how your own judgement improved.

## Where to look

- Tools and stories for each line → [learning-tracks/README.md](./learning-tracks/README.md)
- The full competition story → [STORY.md](./STORY.md)
- Repo overview → [README.md](./README.md)
