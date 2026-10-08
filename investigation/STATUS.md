# STATUS.md

Resumable migration state. A new agent should be able to read `AGENTS.md`,
`MIGRATION.md`, this file and `HANDOVER.md` and know exactly where the
migration is without reconstructing history.

## Phases

Mark each: not started / in progress / blocked / done.

| Phase | Status | Acceptance criteria | Required evidence | Commands | Commit |
| --- | --- | --- | --- | --- | --- |
| 1 Baseline frozen | | | | | |
| 2 Parity contract + fixtures | | | | | |
| 3 Initial Nift structure + compatibility proof | | | | | |
| 4 Shared shells/templates | | | | | |
| 5 Authored content | | | | | |
| 6 Source compatibility | | | | | |
| 7 Route/content/render/browser/behaviour parity | | | | | |
| 8 Incremental correctness | | | | | |
| 9 Performance campaign | | Profiles, general improvements or justified deferrals | | | |
| 10 Final parity revalidation | | Complete parity contract after optimization | | | |
| 11 Final benchmark campaign | | Optimized, parity-certified production pipeline | | | |
| 12 Clean-checkout verification | | | | | |
| 13 Handover / final report | | | | | |

GATE: compatibility proof must precede broad content translation. Do not mark
phase 5 in progress until phases 1-4 acceptance criteria are met.
GATE: complete parity precedes profiling/optimization; full parity revalidation
after the campaign precedes final benchmarking.

## Architecture and campaign evidence

- Significant retained/introduced islands and reasons (parity, source model,
  accessibility, shared state, maintenance and bundle/runtime cost):
- Island/bundle preparation and mounting commands:
- Profiles/hotspots and before/after measurements:
- General improvements, tradeoffs and deliberately deferred bottlenecks:

## Current

- Checkpoint:
- Commit SHA:
- Known blockers:
- Next checkpoint:

## Temporal campaign T0

T0 done: generated init preserved/read, starter build/status pass; source model rendered. T1 in progress: full upstream clone, exact revision and production workflow pending. T2–T9 not started. No migration or performance claims. No current exceptional blocker.

T1 pinned `5d9703a237a9efc9a7da48ac09f79526823b8182` and cookbook `2385cc030f9ca1cc67b05082f1990d20cfc3a38c`. Source audit: `T1-SOURCE-AUDIT.md`. Complete publication not yet frozen; history/dependencies in progress. Baseline gate remains closed.

T1 complete: unchanged production lifecycle repeated, 3984-file reference frozen, 793 primary/962 total HTML routes reconciled; one understood operational stats difference. Full history/source/generated inputs preserved. See BASELINE.md and t1/. T2 in progress (real-route fixture candidates prepared); T3–T9 not started.

## T2 parity contract frozen

126 reference states, 25 interaction observations across both viewports, 563 concrete redirect samples, Markdown negotiation/missing-route checks, and complete upstream OG validation are preserved under `investigation/t2`. Remote transport and inherited limitations are explicit in `investigation/PARITY-CONTRACT.md`. T2 complete; T3 architecture proof is next. No migrated corpus or performance claim yet.

## T2 parity contract frozen

126 reference states, 25 interaction observations across both viewports, 563 concrete redirect samples, Markdown negotiation/missing-route checks, and complete upstream OG validation are preserved under `investigation/t2`. Remote transport and inherited limitations are explicit in `investigation/PARITY-CONTRACT.md`. T2 complete; T3 architecture proof is next. No migrated corpus or performance claim yet.
