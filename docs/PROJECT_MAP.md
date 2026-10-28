# CICM project map

Snapshot 28 Oct 2026. Positions live in Notion — refresh them; this map only says *who owns what*.

## Claude Code projects (GitHub, `marzuk213-cloud`)

| Repo | Role | Use it for |
|---|---|---|
| **`cicm-study`** (this repo) | **Main cloud workflow home** | Yearly marking, Runthrough + SMARK, chunk repairs, everyday Notion-grounded questions, casual recall |
| `repair-board-builder` (private) | Specialist | Building/rebuilding the daily repair board HTML (route 7) |
| `cicm-exam-visuals` (private) | Specialist | New or materially corrected graphs, diagrams, images (route 6) |
| `cicm-mechanism-playground` (private) | Not part of the mainstay | Left untouched; not routed to by this workflow |

These three serve the workflow — no new repos needed. Each specialist repo is maintained by
its own sessions; don't edit them from here. Open a cloud session on the specialist repo when
the job is a board build or a visual build.

## Other surfaces

| Surface | Role |
|---|---|
| **CICM Sidekick** (local Claude project on the Mac) | Mac home: local AirDrop handwriting intake, Rize/session timers, local files |
| CICM Sidekick chats / Cowork, projectless Claude chats | Same workflow via account preferences + COMMAND mirror |
| Codex / ChatGPT | Co-writer on the same Notion owners; shared recall history |

## Notion owners (the data)

| Owner | Holds |
|---|---|
| COMMAND | Shared rules — overrides stale repo text; Maz's latest explicit instruction overrides it |
| NEXT UP | Current Yearly / SMARK / Runthrough positions |
| Runthrough owner | Syllabus Runthrough checkpoint |
| SAQ Practice | Past SAQs, refined templates, model answers |
| Attempt Log | Physical attempts (one Attempt ID each), scores, feedback |
| Syllabus Point Bank · Topic Registry | V5 objectives, rundowns, topic notes |
| Permanent SMARK bank · SMARK administration | Topical SAQ bank and its progress |
| Running Recall Log | Casual recall history |
| Repair Boards | Daily repair boards and their states |
| Daily Planner | Scheduling and receipts |

Links: [`docs/CURRENT_WORKFLOW.md`](CURRENT_WORKFLOW.md#live-sources-refresh-positions-dont-hard-code).

## Repo housekeeping

- Root `2017A_Q11–Q14_*_Interactive.html` — legacy outputs kept at their original URLs;
  their production route is retired.
- `archive/2026-10-28-pre-output-workflow/` — archive copies of all six per-SAQ pages and
  the superseded instructions.
- Open PR [marzuk213-cloud/cicm-study#1](https://github.com/marzuk213-cloud/cicm-study/pull/1)
  (Cursor static-server config for the old HTML pages, 1 Sep) is superseded by this
  workflow. Left untouched — Maz's call to close it.
