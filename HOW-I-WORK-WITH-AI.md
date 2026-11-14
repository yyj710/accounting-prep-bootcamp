# How I work with AI to turn one semester into something I can actually revise with

> **中文版本（更完整，含对话原话）→ [HOW-I-WORK-WITH-AI.zh-CN.md](./HOW-I-WORK-WITH-AI.zh-CN.md)**

Almost everything in this repo was made sentence by sentence in conversations with AI.

I originally meant to publish only the finished tools. Then it occurred to me that the useful part isn't the files — anyone can download those. It's **why I asked for what I asked for, what was concretely built, where my own judgement was wrong, and how I pushed it back**. So this isn't a note about which tools or scripts were used. It's about the decisions, with enough detail that you could actually repeat them.

If you're also juggling a few exams, or staring at a pile of material with no idea where to start, this file is probably more use to you than the four web pages.

---

## The calendar, and the first call I made

| Date | What |
|---|---|
| **28 Nov 2026** | Final of the 7th Guangdong–Hong Kong–Macao Accounting Knowledge Competition (I'm team captain) |
| **10 Dec 2026** | ACCA FR global exam |
| **11 Dec 2026** | ACCA FM global exam |
| **End of term** | Primary financial accounting final — date not fixed, but revision has to start in November |

I was a bit rattled. Not because the material was hard, but because **the time was shredded**: leading a team, revising for a final, two global exams on consecutive days, and new coursework arriving throughout. Preparing "one set of notes per subject" would have meant writing the same accounting principles out four times.

The first call I made had nothing to do with studying, and saved the most time: **these four exams run on the same body of knowledge**. So I'd build it once, ordered by what the courses actually need — protect the term grade first, and let the competition and ACCA ride on the same material. I also put it all into the competition repo rather than starting a new one, because it was all built in the same weeks; splitting it up made the design harder to explain, not easier.

After that, every argument collapsed into one question: **would I actually open this every day?**

---

## 1. Say exactly what I want, what I don't want, and who it's for

The first delivery was two Markdown files. I changed the brief the same day:

> "Let's do an HTML like we did for the competition — not a website, just something for me to revise with. I want to do well this term, so don't give me only high-frequency traps, cover everything. I'll keep sending new coursework, so it has to keep growing."

**Why I said it**: the final is 40 single-choice / 20 multi-choice / 10 true-false / 30 mixed items in 105 minutes, pass at 60. Heavy and broad, so betting on "key points" felt unsafe. And the courseware arrived *in pieces* — anything built in one shot would be out of date the next day.

Five constraints are packed into that message, and they shaped everything after:

- **Not a website** → one HTML file, double-click, no install, no internet
- **One user, me** → no accounts, no backend, no cloud
- **Full coverage** → no "top traps only" shortcut
- **Keeps growing** → new questions must be addable without rebuilding
- **Actually revisable** → not a pile of text, but something to recite, drill and self-test

**What was actually built**: questions aren't hard-coded into the page. Each is one line of data — id, chapter, type, stem, options, answer, explanation — so adding a question means adding a line, and fixing an explanation touches one cell. Chapter names were normalised to five; the id prefix tells you the source (class practice / Ch3 homework / Ch4 homework / CPA / workbook 1 / workbook 2). Progress is stored in the browser, so new questions don't wipe old progress. Zero external dependencies: it opens offline, from a USB stick, or on someone else's laptop.

**What I learned**: don't say "make me some revision notes". State the goal, the boundaries, the user, and *how it will change later* in one go. That last one is the easiest to forget and the one that decides the whole structure.

---

## 2. I check, I don't just accept

> "The practice cards have no options, multi-choice and true/false are broken — check the whole thing again. And **write a plan before you start**, tell me what you're going to do, so we don't keep reworking it."

**Why**: the first version had stems with no options, multi-choice with no way to submit, and true/false graded as if it were single-choice. That isn't "add a button" — the question bank's type handling was wrong all the way through.

The second half became a standing rule. I'd been asking for one fix at a time and watching a new problem appear each round, so I required a short plan first: what will change, and how will we know it worked.

**What was actually built**: 101 class-practice questions merged in with full options; multi-choice got a submit button, a selected-count, a guard against submitting fewer than two, and selections that survive paging; true/false became √ / × buttons; messy chapter names were normalised and glued-together stems/options split apart. From then on every round started with a plan, and rework dropped sharply.

**What I learned**: AI delivers fast, but "done" and "usable" are different things. I click through it myself, and I don't say "this is bad" — I say which card, which button, under what condition. Vague complaints get vague fixes.

---

## 3. The time I was most unhappy: pasted textbook text

> "Why is there no answer or explanation? There *are* answers. Why would you just copy the original text — **can't I read the book myself**? I need it organised so I can actually remember it."

I was the one who was wrong. I'd flipped through only the first volume of a workbook and decided it had no answers, so scanned source text got pasted into the page as "material". The answer booklet was in the second volume; another workbook printed full answers and explanations. I already owned the book — copying it in accomplished nothing.

**What was actually built**: 33 pasted blocks deleted, replaced with five chapter summary cards. Questions got three-part explanations — *why this answer → the exam point → a memory hook*. Then I said "do workbook 2 as well": its options were laid out horizontally and its answer boxes were pale-blue images, so options were re-ordered by their coordinates, A–H multi-choice was handled, and 63 properly explained questions came out the other end.

**What I learned**: source material isn't revision material until it's been reworked. And the sharper lesson — **before declaring "there's no answer key", read the whole book**. My own bad assumption is harder to catch than an AI mistake, because I naturally believe myself.

---

## 4. Simpler practice wins, and I decide

The final includes writing accounting entries, and entries were scattered across the courseware pages — reading them isn't the same as being able to write them.

> "Did you go through the entries in the slides? The final has journal-entry questions… I think I need to practise them."

AI proposed a "complete" exercise: pick the account, type the amount, auto-grade on direction + account + amount. I cut it:

> "Don't overcomplicate it. Just give me the scenario. I'll work it out **in my head** — if I got it, I mark it as known; if not, or if I check the answer and I'm wrong, it goes into my mistake book."

**Why**: what needs drilling is *seeing a transaction and recalling the debit and credit*, not filling in a form. Auto-grading makes me type out what I already thought, and then argues about account names and number formats.

**What was actually built**: 11 courseware decks went page by page into 178 debit/credit templates, arranged by chapter and transaction type and searchable, plus 4 combined business cases for 182 self-checked exercises. The page does three things: show the scenario → I write the entry mentally → reveal the model answer and tap "✓ got it" or "✗ add to mistake book". Its progress is stored separately from the quiz.

**What I learned**: a feedback loop needs **checking and reviewing**, not complexity. I know how I revise; a "complete" design isn't automatically a design that fits me.

---

## 5. I control the pace, not the system

> "Can we skip questions I already know? And let me add or remove things from the mistake book manually — some I don't want to do, and some I only guessed right but still need to revise."

That exposed a hidden assumption: the system treated "answered correctly" as "mastered". A lucky guess isn't mastery, and the system was quietly letting it through. There were also questions I simply didn't want to spend time on.

**What was actually built**: four states instead of two — done, wrong, skipped, manually flagged. Known questions can be hidden and restored; manually flagged ones carry a marker so a later correct answer never silently clears them; skipped ones are hidden by default but can be shown, and count towards the progress figure.

**What I learned**: I'm the one who decides whether I've mastered something. The tool has to leave that door open.

---

## 6. When answers disagree, go to the authoritative source

I handed over two official homework answer booklets and asked for a full check. The bank's answers had been inferred from the stems and never verified. Of 198 questions, 8 disagreed and 1 was missing.

I didn't just batch-replace with "official wins" — I read each official explanation. **All 8 were our mistakes** (in one case I'd reworded an option earlier and the answer drifted with it), and the missing question was restored. Final: **198/198 matched**.

**What I learned**: a smooth AI-written explanation is never the standard. If an official key or the textbook exists, check against it question by question. When it turns out I was wrong, just admit it and fix it — this is for my own exam, there's no face to save.

---

## 7. Fix the bug, don't work around it

> "Can't submit — there's a bug, please fix it."

Multi-choice questions sat selected but the submit button did nothing. The tempting move is a refresh or another browser, but the closer the exam gets, the less affordable that is.

**What was actually built**: reproduce first, and a pattern appeared — **only cards with a section tag were affected**. Tags like "cash" shared a class name with the submit button, so the click handler landed on the tag. 120 of 167 multi-choice questions were hit. The tag class was renamed and the binding tightened, then a headless browser clicked through the bank: 185 checks passed, plus a screenshot to confirm the answer, explanation and highlighting all rendered.

**What I learned**: locate before you touch. "I can work around it" isn't "it's fixed". Small bugs are exactly the ones that surface in the last few days before an exam, when they hurt most.

---

## 8. Leave a trail when you finish

> "Make a habit of it: keep a worklog, tidy the folders afterwards, sync my GitHub… I want to see the change on every branch."

**Why**: after this many rounds, a single final file tells me nothing about which step corrected which judgement. Branches, human-readable commit messages and tags are notes to my future self.

**What was actually built**: after each round → tidy folders → one line in the timeline saying what changed and why → a commit message in plain language → push; tags at milestones, old versions kept so I can page back. Raw logs, throwaway scripts and source textbooks live in a private repo. **This public one holds only the usable tools and the thinking above.**

**What I learned**: the trail isn't for other people. It's so I can go back and check whether my judgement at the time was actually right.

---

## 9. This time I made it research first, not guess

Two weeks before the final I reopened the wrong-answer book and something felt wrong: all 144 items showed the answer as soon as the page loaded. Scanning them felt like studying, but it was just re-reading. The pills on every card — source, chapter, question type — were labels, not filters; if I wanted only the Chapter 3 homework mistakes, I had to scroll and hunt.

What I sent was offhand:

> "Can I get an option to redo these? And sort them by which section they came from. Go look at how proper wrong-answer books are designed."

That last sentence was the point. I didn't want to describe the UI again — we'd already proved I can't, and it can't guess. **Having it study working products beats me writing a spec from my head.**

**What it did**: it checked Fenbi, Shuashuati, Anki, Quizlet, ACCA's exam interface and old-fashioned paper error notebooks, then came back with a comparison table. Nearly all of them treat *independent redo* as the core action — hide the explanation, answer first, check afterwards; filter by subject / module / question type; remove only once you've actually got it right. It also listed what it would **not** copy: error-cause tags, three-level self-ratings, spaced-repetition scheduling, auto-removal after three correct answers, a second "favourites" notebook. I'd rejected exactly those on 13 November as "one judgement split into four buttons", and Anki's own docs say the days before an exam are the wrong moment to start an SRS.

Then, instead of touching my file, it built **four clickable prototypes** with real questions from my bank — filtering, answering, submitting and removing all worked. I answered with one letter: "A". It implemented that one.

**What I took from it**: I wasn't asking for two features, I was asking not to make design decisions two weeks before an exam. Research first, clickable options second, one letter from me. Nice side effect: it found `src` and `ch` already stored on every wrong answer, so **not one byte of saved progress changed** — the 144 items stayed exactly where they were.

---

## A few less flattering things

I'm writing these down because they're more useful than the results:

- **My own assumption nearly wrecked a whole section.** Half a book, one confident "there's no answer key", and I pasted raw text into the page. AI mistakes are easy to find; my preconceptions aren't.
- **The multi-choice cards still have no "I don't know, just show me" button.** I have to pick something at random and submit before I can read the explanation. It's clumsy. I haven't fixed it because it touches all 167 questions and I'm not taking that risk close to an exam. Noted for later.
- **The filename still says "满绩冲刺" ("full-marks sprint").** I named it in early November to psych myself up; in hindsight it's a bit much. Renaming would break links and the progress stored in browsers, so it stays — a small fossil.
- **The question range follows my own courseware and homework.** Other universities may cover different ground; check the syllabus before using it as-is.
- **The probability & statistics set isn't here.** Not tidy enough, not general enough — no reason to take up anyone's time.
- **The explanations are my own study notes, not official wording.** The two homework chapters were verified against the official key (198/198); for everything else, defer to the textbook, ACCA examiner reports and current regulations.

---

## If you also have only a few weeks, here's the order I'd use

1. **Write the calendar down first.** See which exams actually test the same thing. Costs five minutes, decides whether you do the work four times.
2. **Pick one container you can build once and reuse.** Mine was a single HTML file plus one-line-per-question data: adding questions doesn't change the structure. A spreadsheet or a flashcard deck works too — the key is that it **accepts increments**.
3. **Use the first delivery only to find problems.** Don't start adding content yet. My two Markdown files died this way.
4. **Ask for a plan before the work starts** — what changes, how it'll be checked. I added this rule in round two; one round earlier would have saved two reworks.
5. **Verify against the authoritative key**, never against inferred answers; if the mistake is yours, fix it without ceremony.
6. **Keep the practice loop light.** Checking plus reviewing is enough; it doesn't have to be auto-graded.
7. **Separate "known / lucky guess / don't know"** — don't let the system decide mastery for you.
8. **Leave one trace per round**, so you can later see how your own judgement got better.
9. **If you can't describe an interface, don't try.** Have it research how existing products solve it, then show clickable versions you can pick from with one letter.

---

## What came out

| | |
|---|---|
| Final-exam station | One 494 KB file, double-click to open, no install, no internet: **489 questions**, **178 entry templates**, mistake book (one-click redo, filter by source / chapter), skip marking, auto-saved progress |
| Competition prep | 1,472 questions reorganised by knowledge point + 13 module guides; provincial top 5 of 200 teams, final on **28 Nov** |
| ACCA FR / FM | One offline practice site each, plus notes rewritten in the way I actually understand things (FR uses a five-block template: plain language / everyday example / how it connects / exam hint / common traps). **FR 10 Dec, FM 11 Dec — in progress** |
| CPA tax | A practice site with a 5-chapter question bank |
| This file | The nine rounds of judgement, rework and concrete steps above |

Not every number is impressive, but every one of them opens, clicks and works.

---

## Where to look

- Tools and stories for each line → [learning-tracks/README.md](./learning-tracks/README.md)
- The full competition story → [STORY.md](./STORY.md)
- Repo overview → [README.md](./README.md)
