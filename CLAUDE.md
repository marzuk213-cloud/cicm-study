# cicm-study — cloud Claude Code home for Maz's CICM First Part workflow

**Workflow in force:** `CICM-OUTPUT-WORKFLOW-20261028` — output and exam focused. This
file supersedes every older instruction in this repo (now in `archive/`). Exam dates,
sittings and eligibility are not asserted here — take them from the live campaign pages in
Notion or the official CICM source.

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
  history, timers, receipts) lives in the existing **Notion owners** — never in repo files.
- **Isn't:** an HTML page factory any more. The old "build an interactive HTML page per SAQ"
  role is archived (`archive/2026-10-28-pre-output-workflow/`).

Mac home is the local **CICM Sidekick** project; this repo is the cloud twin. Same Notion
owners, no Mac/localhost assumptions here.

## Read first, every session

1. `docs/CURRENT_WORKFLOW.md` — the eight routes (portable guide).
2. Live Notion **COMMAND** — overrides stale repo guidance (never overrides Maz):
   https://app.notion.com/p/39a6cdbdfe3d81fbb2dbfeecbd6b5797
3. **NEXT UP** for current positions (refresh; never trust a dated snapshot):
   https://app.notion.com/p/3856cdbdfe3d81ec8cbcf3d241b93939

Full owner list: `docs/PROJECT_MAP.md`.

## Routing

| Maz says / needs | Do |
|---|---|
| Written attempt photos/attachments, "mark this" | Route 1 Yearly or SMARK marking — `saq-marker` skill; blind first |
| "repair", "next repair", walking/gym chunks | Route 3 chunk repair — full feedback first, end with the complete model answer |
| Runthrough / "next syllabus point" / `/smark` | Route 2 — Runthrough owner or SMARK bank, independent progress |
| Short question: "vanc?", "digoxin kinetics" | Route 4 — retrieve his Notion templates/rundowns first, answer short, link sources |
| "quiz me", casual recall | Route 5 — one source-backed question at a time, shared history first |
| Daily repair **board** HTML build/rebuild | Specialist: **`marzuk213-cloud/repair-board-builder`** (+ `saq-repair-board` skill) |
| New/corrected graph, diagram, image | Specialist: **`marzuk213-cloud/cicm-exam-visuals`**; Notion-first, reuse checked assets |

## Retired — do not trigger

Archived, not deleted; run only if Maz **names one explicitly** for maintenance:
`saq-template-study` (/ts), `cicm-systematic-study` (old /next menus), `cicm-study-buddy`,
`cicm-tangent-buddy`, `cicm-study-html`, `cicm-revision-html`, `cicm-speechify-extract`,
`saq-autopipeline`, `saq-craft-refiner`, `craft-migrator`, `cicm-exam-layer`,
`corpus-merge`, `pharmacopeia-populator`; plus READ, generic Socratic study-buddy mode,
minimal-tool/no-source tangent defaults, and this repo's old per-SAQ HTML delivery rule.

Mainstay skills that stay live: `saq-marker`, `saq-repair-board`, `airdrop-handwriting`
(cloud = actual attachments only), `cicm-recall-deck` (explicit Rapid Recall route only),
`hq-command-centre`, `cicm-organizer`, `whimsical-lookup`, and all non-CICM skills.

## Hard rules

- **Sources:** Maz's Notion first; external authoritative sources (CICM, Deranged
  Physiology, LITFL, Part One, Jenny's Jam Jar, CICM Wrecks, standard texts) only for
  verification, conflicts, updates or genuine gaps. Never present trained knowledge as
  retrieved material. Retrieval failure ≠ image absence.
- **Records:** refresh before every write, preserve other writers, dedupe, read back.
  Never invent XP, mastery, attempts, scores or completion. Board build/delivery and timer
  expiry are never completion — only Maz's explicit "done" closes an exact scope.
- **Time:** check live Sydney time (`TZ=Australia/Sydney date`) before any time claim.
- **Style:** informal, direct, mobile-friendly. Fix dictation silently; correct real
  science errors bluntly. Keep answers as short as the question allows.
- **Repo:** commit only workflow docs/config here. No study records, trackers, boards or
  timers in git. Don't edit the specialist repos from this project.
