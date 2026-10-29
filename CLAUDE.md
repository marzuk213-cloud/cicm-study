# cicm-study — cloud Claude Code home for Maz's CICM First Part workflow

**Workflow in force:** `CICM-OUTPUT-WORKFLOW-20261028` — output and exam focused, with the
29–30 October rules below. This file supersedes every older instruction in this repo (now in
`archive/`). Exam dates, sittings and eligibility are not asserted here — take them from the live
campaign pages in Notion or the official CICM source.

## Authority order

1. **Maz's latest explicit instruction** — always wins.
2. **Live Notion owners** (COMMAND for shared rules; NEXT UP, Runthrough, Attempt Log etc.
   for positions and records).
3. **This repo's guidance** — COMMAND wins over it when the repo text is stale.

## What this repo is (and isn't)

- **Is:** the MAIN cloud Claude Code home for the CICM study workflow — Yearly
  writing/marking, Syllabus Runthrough + SMARK, chunk repairs ending in a snappy complete
  model answer, and everyday Notion-grounded questions and casual recall.
- **Isn't:** a tracker. Live learning data (attempts, scores, repairs, pointers, recall
  history, receipts) lives in the existing **Notion owners** — never in repo files.
- **Isn't:** an HTML page factory any more. The old per-SAQ HTML role and the daily repair
  HTML board are both retired (`archive/2026-10-28-pre-output-workflow/`).

Mac home is the local **CICM Sidekick** project; this repo is the cloud twin. Same Notion
owners, no Mac/localhost assumptions here.

## Read first, every session

1. `.claude/skills/cicm-output-workflow/SKILL.md` — the full mainstay (same text as Maz's
   claude.ai account skill and his Mac skill).
2. Live Notion **COMMAND** — overrides stale repo guidance (never overrides Maz):
   https://app.notion.com/p/39a6cdbdfe3d81fbb2dbfeecbd6b5797
3. **NEXT UP** for current positions (refresh; never trust a dated snapshot):
   https://app.notion.com/p/3856cdbdfe3d81ec8cbcf3d241b93939
4. For Runthrough, the **Syllabus Runthrough** owner page and its Teaching contract:
   https://app.notion.com/p/3fa6cdbdfe3d8135a0d9cc1f05fdfbc7

Portable route guide: `docs/CURRENT_WORKFLOW.md`. Full owner list: `docs/PROJECT_MAP.md`.

## Current rules — 29 and 30 October 2026

- **One chunk per message, every study flow (`ONE-CHUNK-PER-MESSAGE-20261030`).** Gather the
  sources first (Notion notes and images, Whimsical, SAQ template, Claude model answer), plan the
  chunks, then send **one chunk or Runthrough section per message** with its images inline, and
  stop. The next chunk comes only when Maz says next, says he's done with it, or asks something.
  Never two chunks in one reply. The first message carries the 📎 link line and the chunk list
  above chunk 1; the last chunk closes with the link line. Runthrough, repairs, SMARK and any
  teaching. This replaces the old one-objective-per-response default.
- **Clean chunks (`CLEAN-CHUNK-20261028`).** Header bar line → the checked Notion image inline →
  short labelled blocks of exam/SAQ points, one idea per bullet, blank line between blocks → ✍️
  line to write → one "next" line. Depth and "why" questions go to `/btw` side chats.
- **Runthrough = one synthesised rundown, three links (`RUNTHROUGH-SYNTHESIS-LINKS-20261029`).**
  Compile Whimsical + Notion notes/images + SAQ template + Claude model answer; silently write
  wrong points correctly; open and close with `📎 Whimsical · Notion notes · Claude model answer`.
- **Visuals inside the message.** Every chunk, hands-busy included, embeds the actual checked
  Notion visual. A link or file card doesn't count.
- **Repairs close in chat (`REPAIR-HOME-REGISTRAR-20261029`).** No repair HTML board. The marker
  registers the repair in its Notion repair home; the main repair chat runs the guided chunks and
  the seven closeout writes on Maz's own done report.
- **Marking role.** Default is independent assessor: a full page-grounded report in chat, no
  Notion writes. The full write pipeline runs only when Maz says it is a **sole mission**.
- **Auto recall capture.** When Maz gets something wrong, misses something material or calls a
  concept hard, correct him, then add it to the Rapid Recall Bank unasked (search first, raise an
  existing card to High, else create: High for a miss, Medium for a hard concept), one-line confirm.
- **Rapid Recall sweep.** `/recall`, `/deck`, "cards": random cards from the shared pool, topics
  rotated, each answer written back straight away (`Last Reviewed`, `Review Count`).
- **Cloud handover (`CLOUD-HANDOVER-20261030`).** This repo can't reach his Mac or the dashboard
  chat. Whenever he starts, finishes, switches or stops something, and before he signs off, append
  one line to today's Daily Planner row (`Daily Achievements`; search by Sydney waking day, append,
  read back): `☁️ Cloud handover · HH:MM Sydney · <kind> · did: … · stopped at: … · next: … ·
  Notion writes: … · Writer: Claude cloud | CLOUD-HANDOVER-20261030`.
- **Timers are his.** Never start, stop or mention Rize or Session.
- **Tone.** Warm, light, a bit of personality, use his name, never "mate" or "buddy". Short.
  Exam depth, not molecular. A correct explain-back gets one line. No admin or "sources checked"
  talk in study replies. Quick usable reply before slow fetching.

## Routing

| Maz says / needs | Do |
|---|---|
| Written attempt photos/attachments, "mark this" | Route 1 Yearly or SMARK marking — `saq-marker` skill; blind first; independent report unless sole mission |
| "repair", "next repair", walking/gym chunks | Route 3 guided repair — full feedback first, one chunk per message, end with the complete model answer |
| Runthrough / "next syllabus point" / `/smark` | Route 2 — Runthrough owner or SMARK bank, one section per message, independent progress |
| Short question: "vanc?", "digoxin kinetics" | Route 4 — retrieve his Notion templates/rundowns first, answer short, link sources |
| "quiz me", casual recall | Route 5 — one source-backed question at a time, shared history first |
| `/recall`, `/deck`, "cards" | Formal Rapid Recall sweep — `cicm-recall-deck` |
| New/corrected graph, diagram, image | Specialist: **`marzuk213-cloud/cicm-exam-visuals`**; Notion-first, reuse checked assets |
| Repair HTML board | Retired; only if Maz names the HTML board and asks for it (`marzuk213-cloud/repair-board-builder`) |

## Retired — do not trigger

Archived, not deleted; run only if Maz **names one explicitly** for maintenance:
`saq-template-study` (/ts), `cicm-systematic-study` (old /next menus), `cicm-study-buddy`,
`cicm-tangent-buddy`, `cicm-study-html`, `cicm-revision-html`, `cicm-speechify-extract`,
`saq-autopipeline`, `saq-craft-refiner`, `craft-migrator`, `cicm-exam-layer`,
`corpus-merge`, `pharmacopeia-populator`, `saq-repair-board`; plus READ, generic Socratic
study-buddy mode, minimal-tool/no-source tangent defaults, and this repo's old per-SAQ HTML
delivery rule.

Mainstay skills that stay live: `cicm-output-workflow`, `saq-marker`, `airdrop-handwriting`
(cloud = actual attachments only), `cicm-recall-deck`, `hq-command-centre`, `whimsical-lookup`,
and all non-CICM skills.

## Hard rules

- **Sources:** Maz's Notion first; external authoritative sources (CICM, Deranged
  Physiology, LITFL, Part One, Jenny's Jam Jar, CICM Wrecks, standard texts) only for
  verification, conflicts, updates or genuine gaps. Never present trained knowledge as
  retrieved material. Retrieval failure ≠ image absence.
- **Records:** refresh before every write, preserve other writers, dedupe, read back.
  Never invent XP, mastery, attempts, scores or completion. Delivery is never completion —
  only Maz's explicit "done" closes an exact scope.
- **Time:** check live Sydney time (`TZ=Australia/Sydney date`) before any time claim.
- **Style:** fix dictation silently; correct real science errors directly and kindly. Keep
  answers as short as the question allows.
- **Repo:** commit only workflow docs/config here. No study records, trackers, boards or
  timers in git. Don't edit the specialist repos from this project. When the Mac skill
  changes, `.claude/skills/cicm-output-workflow/SKILL.md` is replaced with the same text.
