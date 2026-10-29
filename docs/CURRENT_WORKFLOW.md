# Maz's CICM workflow — current guide

**30 Oct 2026:** current rules (one chunk per message, clean chunks, cloud handover, tone) are in `CLAUDE.md` → Current rules, and the full mainstay is `.claude/skills/cicm-output-workflow/SKILL.md`; they win over anything older here.

**Event:** `CICM-OUTPUT-WORKFLOW-20261028` · set by Maz 28 Oct 2026 · supersedes all older
CICM skill defaults. Portable: paste this into any Claude surface (projectless chat,
CICM Sidekick, Cowork, local or cloud Claude Code).

**Authority order:** (1) Maz's latest explicit instruction; (2) the live Notion owners —
COMMAND for shared rules, the owner databases for positions and records; (3) this file. If
this file and COMMAND disagree, this file is stale and COMMAND wins — but neither overrides Maz.
Exam dates and sittings come from the live campaign pages or the official CICM source, not
from this guide.

> **Name of the game:** output and exam focused. Use the Notion databases built over the
> years; pull outside sources only when the situation calls for it.

---

## 1 · Yearly — exact-sitting SAQ writing

`write (15 min) → blind independent marking → full feedback → chunk repair → snappy whole-answer model → explicit done → verified records`

- **15-min practice allowance:** ~1 min plan, 12 write, 2 check.
- **Answer shape:** stem-led headings — preferably 2, generally max 3–4 unless the stem needs more; punchy mark-bearing bullets.
- **Marking:** blind — mark *before* looking at previous scores or model answers.
- **Feedback:** what to write, **Keep / Cut / Missing**, and the full useful teaching retained in the final chat.
- **Identity:** one physical attempt = one **Attempt ID**. The exact stem and actual conditions matter.

## 2 · Syllabus Runthrough + SMARK

- **Runthrough** = personal syllabus study from the existing official V5 notes, images,
  refined templates and Claude model answers. Refresh the Runthrough owner; preserve
  heading/image coverage and the exact checkpoint.
- **Trial format** (recorded as a trial, not a mandate): relevant marked SAQs + actual weak
  points → one SAQ-style prompt/section → assess → show the existing visual → explain the
  whole component. **No invented vignettes, no mandatory quizzes.**
- **SMARK** = topical writing from the permanent Syllabus SAQ Bank via `/smark`, then the
  same repair process.
- Runthrough and SMARK track progress **independently** — neither completes the other.

## 3 · Chunk repair — home, walking or gym

1. Read the **full** exact-attempt feedback page first (a board gist or NEXT UP line is not enough).
2. Count the actual repair points from the marking ledger's losses/corrections.
3. Open with **exact stem + score + repair count**.
4. One useful chunk at a time: progress bar (`▓▓░░░░░ 2/7`) → causal explanation → **the line to write**.
5. Maz bounces ideas, asks tangents, says "next". Correct real science errors bluntly;
   interpret garbled dictation silently (never quote it back).
6. **Finish with the snappy COMPLETE model answer** — concise, exam-writable, covering the
   *whole* stem, not just the misses. **This is what makes the repair.**

- At a screen: relevant checked visuals. Hands-busy spoken mode: no visuals unless asked. No board needs to be open.
- Only Maz's **explicit "done"** closes the exact scope. Delivery or timer expiry doesn't.
- Keep residual recall cues without turning them into unfinished repairs.

## 4 · Everyday questions and tangents

Short natural prompts — "vanc?", "digoxin kinetics", "Michaelis–Menten and phenytoin" —
**must** retrieve Maz's relevant Notion answer templates, syllabus rundowns and corrections.
No `/ts`, `/next` or special wording required.

- Read the relevant full source; show suitable existing Notion visuals; make a checked visual only for a genuine gap. **Retrieval failure ≠ image absence.**
- Link the exact sources. External authoritative sources for verification, conflicts, updates or genuine gaps.
- As short as the question allows — source-backed ≠ essay.
- **Never present generic trained knowledge as retrieved material.**
- Return to the parent repair/Runthrough checkpoint after the tangent.

## 5 · Mixed casual recall

- One brief, source-backed question at a time; balanced physiology/pharmacology across systems, including PK numbers.
- Prioritise documented misses and eligible older material.
- First read the shared COMMAND fact history + relevant **Running Recall Log**; dedupe by underlying fact, not wording.
- Keep outcome states distinct: unanswered · correct unaided · clue-assisted · wrong/corrected · taught.
- Previously asked facts return only for requested deliberate revision. One shared history across Claude and ChatGPT.
- Formal **Rapid Recall Bank / Foundation Sweep** (`cicm-recall-deck`) is a separate explicit route.

## 6 · Visuals

- Notion-first; reuse existing checked assets; inspect actual pixels; show the actual graph when explaining it. Colour is not a graph.
- Current starred favourites govern new illustrations (suitable two-star preferred ~2:1; fit and accuracy first), plus Visualize when useful.
- Save accepted new/materially corrected visuals beside the matching explanation in the
  **syllabus rundown AND relevant refined SAQ template(s)** unless Maz narrows it; check the saved rendering; no duplicate teaching pages.
- Specialist build work → `marzuk213-cloud/cicm-exam-visuals`.

## 7 · Repair production

- Claude owns the current **daily repair HTML**: one board across Yearly + SMARK; later
  batches extend it; verified unfinished carryover keeps original Attempt IDs/day/progress.
- Build / view / download / archive / worked-through completion are **separate states**.
  **Board creation never creates repair credit.**
- Recent jobs use normal Claude chat when Maz selects it. Specialist build work → `marzuk213-cloud/repair-board-builder`.

## 8 · Shared coordination

- Use existing owners/receipts; refresh before writes; preserve other writers; dedupe; read back.
- Share exact full-scope answers across Yearly/SMARK without extra physical attempts.
- Handwriting intake: `airdrop-handwriting` locally (every page, originals, duplicate protection); cloud uses the actual attachments only.
- Session + Rize timers on actual study starts/changes/done (repair 45 min, answering 15 min/question); preserve running elapsed time. Where a timer can't be reached from the cloud, say so — don't pretend.
- Orbit is the solving projection, not authority. **Daily Planner** owns scheduling/receipts.
- **Never invent XP, mastery, attempts or completion.** Notes prepared ≠ notes studied.
- Phone/cloud resumes the same Notion owners — no Mac/localhost assumptions.

---

## Retired (archived, not deleted)

Run only when Maz names one explicitly for maintenance; broad triggers must not hijack study:
`/ts` template-study progression (`saq-template-study`), old `/next` teaching menus
(`cicm-systematic-study`), READ, generic Socratic `cicm-study-buddy`, minimal-tool/no-source
`cicm-tangent-buddy`, `cicm-study-html`, `cicm-revision-html`, `cicm-speechify-extract`,
`saq-autopipeline`, `saq-craft-refiner`, `craft-migrator`, `cicm-exam-layer`, `corpus-merge`,
`pharmacopeia-populator`, and superseded migration/build/HTML routines.

**Live mainstay skills:** `saq-marker`, `saq-repair-board`, `airdrop-handwriting`,
`cicm-recall-deck` (explicit route), `hq-command-centre`, `cicm-organizer`, `whimsical-lookup`,
`icu-bed-list`, `icu-visuals-library`, and all non-CICM skills.

## Live sources (refresh positions; don't hard-code)

| Owner | Link |
|---|---|
| COMMAND / shared rules | https://app.notion.com/p/39a6cdbdfe3d81fbb2dbfeecbd6b5797 |
| NEXT UP | https://app.notion.com/p/3856cdbdfe3d81ec8cbcf3d241b93939 |
| Runthrough owner | https://app.notion.com/p/3fa6cdbdfe3d8135a0d9cc1f05fdfbc7 |
| SAQ Practice | https://app.notion.com/p/2b042c719bce494e8962754a348ac92c |
| Attempt Log | https://app.notion.com/p/52c89955fecc4cc1bfaba1d839003a43 |
| Syllabus Point Bank | https://app.notion.com/p/275ca13470624918a642dc35e48f6b16 |
| Topic Registry | https://app.notion.com/p/e326d00cbb174be49487763c80eb35f3 |
| Permanent SMARK bank | https://app.notion.com/p/3d36cdbdfe3d819f9e36e07bcbdb91a8 |
| SMARK administration | https://app.notion.com/p/3d46cdbdfe3d81ea9254e919798d8358 |
| Running Recall Log | https://app.notion.com/p/3ef6cdbdfe3d81268d3cc6d4722beac9 |
| Repair Boards | https://app.notion.com/p/9966b5fd438f44c6b24ce450bf38fa17 |
