# Archive

Reversible archive. **Nothing here is deleted** and nothing here drives normal study.
Retrieve a file only on Maz's explicit maintenance request.

## `2026-10-28-pre-output-workflow/`

Archived for `CICM-OUTPUT-WORKFLOW-20261028` (28 Oct 2026, authorised by Maz). Superseded
by `CLAUDE.md` and `docs/CURRENT_WORKFLOW.md`.

| Path | What it was | Origin |
|---|---|---|
| `study-pages/2017A_Q11_Tracheostomy_Interactive.html` | Interactive SAQ page | `main`, 18 May 2026 |
| `study-pages/2017A_Q12_Oxycodone_Interactive.html` | Interactive SAQ page | `main`, 18 May 2026 |
| `study-pages/2017A_Q13_DorsalisPedis_Interactive.html` | Interactive SAQ page | `main`, 18 May 2026 |
| `study-pages/2017A_Q14_Respiratory_Compliance_Interactive.html` | Interactive SAQ page | `main`, 18 May 2026 |
| `study-pages/2009A_Q20_Organophosphate_Interactive.html` | Interactive SAQ page | branch `claude/clever-cori-5udi2j`, 12 Oct 2026 (never merged) |
| `study-pages/2009A_Q21_Antidepressants_Interactive.html` | Interactive SAQ page | branch `claude/trusting-edison-497g9b`, 12 Oct 2026 (never merged) |
| `superseded-instructions/CLAUDE.md.2026-10-12-artifact-delivery.md` | Old CLAUDE.md: "build per-SAQ HTML, always publish as Artifact" | `claude/clever-cori-5udi2j` |
| `superseded-instructions/README.md.2026-05-18.md` | Old README ("Interactive HTML study pages") | `main` |
| `maintenance-tools/artifact_copy.py` | Strips doctype/html/head/body to make an Artifact publish copy | `claude/clever-cori-5udi2j` |

**Retired = the production route, not the outputs.** The route that built one interactive
HTML page per SAQ (and the 12 Oct "always publish as Artifact" rule) is retired. The
outputs themselves are kept:

- The four 2017A pages that were on `main` **also stay at their original repo-root paths,
  byte-for-byte identical** (same git blob SHAs as `main` at `e71f2a5`), so existing links
  keep working. The copies here are archive copies.
- The two 2009A pages were never on `main`; they live only here. Their branches
  (`claude/clever-cori-5udi2j`, `claude/trusting-edison-497g9b`) were merged, not copied,
  so their original commits are preserved.

### SHA-256 at archive time

```
1469bf3fa371c5a4a91ee3f8d2679939b8896ec9ada782713cdc261fcce6e967  study-pages/2017A_Q11_Tracheostomy_Interactive.html
fe72405eabe4d18560699786e06b10e1df6601db8ee4366514b0274af2654da4  study-pages/2017A_Q12_Oxycodone_Interactive.html
11d3ac4d78e3216ac0eff995616a2fb4bcce89ce8748573c3621bea1b148e24a  study-pages/2017A_Q13_DorsalisPedis_Interactive.html
b8a5ae769835f2891e71d8324110d422c910a92cb90d6f40fd363d22d3337b8e  study-pages/2017A_Q14_Respiratory_Compliance_Interactive.html
9a8147b27a00be36053c04ed5890e17195408e7b5bb93fa23c892c7f9a7d9626  study-pages/2009A_Q20_Organophosphate_Interactive.html
6675a25ce3ae8368b9b1a2fe39b3b9e4faf22c495b990473c286cb59d908985b  study-pages/2009A_Q21_Antidepressants_Interactive.html
cd0090ededced59ec901d38103b537e9263099497d1c96d8bfe27fea1ce2b793  superseded-instructions/CLAUDE.md.2026-10-12-artifact-delivery.md
c6c9b7194f52b9ad3a5d6e7d399d7001c01371800a67413f86a1807c6b42656c  superseded-instructions/README.md.2026-05-18.md
ca158d47aa66bc8930e680c7d8330e1d3c8a3131242f5fba248e4fdc52882b4e  maintenance-tools/artifact_copy.py
```

Verify: `cd archive/2026-10-28-pre-output-workflow && sha256sum -c` with the block above.
The four repo-root 2017A pages have the same SHA-256 values as their archive copies.

### Restore

Copy `archive/2026-10-28-pre-output-workflow/<path>` to the destination with `cp`, then commit. To view a page, open
it in a browser, or publish it as a private Artifact via `maintenance-tools/artifact_copy.py`.
