# STATUS.md

Resumable migration state. A new agent should be able to read `AGENTS.md`,
`MIGRATION.md`, this file and `HANDOVER.md` and know exactly where the
migration is without reconstructing history.

## Phases

Mark each: not started / in progress / blocked / done.

| Phase | Status | Acceptance criteria | Required evidence | Commands | Commit |
| --- | --- | --- | --- | --- | --- |
| 1 Baseline frozen | done | | | | |
| 2 Parity contract + fixtures | done | | | | |
| 3 Initial Nift structure + compatibility proof | done | | | | |
| 4 Shared shells/templates | done | | | | |
| 5 Authored content | in progress | | | | |
| 6 Source compatibility | in progress | | | | |
| 7 Route/content/render/browser/behaviour parity | not started | | | | |
| 8 Incremental correctness | in progress | | | | |
| 9 Performance campaign | not started | Profiles, general improvements or justified deferrals | | | |
| 10 Final parity revalidation | not started | Complete parity contract after optimization | | | |
| 11 Final benchmark campaign | not started | Optimized, parity-certified production pipeline | | | |
| 12 Clean-checkout verification | not started | | | | |
| 13 Handover / final report | not started | | | | |

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

## T2 parity contract frozen

126 reference states, 25 interaction observations across both viewports, 563 concrete redirect samples, Markdown negotiation/missing-route checks, and complete upstream OG validation are preserved under `investigation/t2`. Remote transport and inherited limitations are explicit in `investigation/PARITY-CONTRACT.md`. T2 complete; T3 architecture proof is next. No migrated corpus or performance claim yet.

## T3 representative proof complete

Seven real routes in each source model pass all body semantics, 42 browser states per migration, 31 desktop/mobile interaction observations, and five incremental-versus-clean publication mutation checks. Retained sidebar positioning additionally verified visually. Evidence: investigation/t3 and T3-ARCHITECTURE.md. Temporary baseline dependency symlink is ignored; final fresh-clone gate still pending.

Next T4: scale ordinary corpus and factor shared shells/navigation with authoritative authored inputs. T5 generated/special, T6 whole-site parity, T7 initial benchmarks/lifecycle, T8 profiling, T9 final campaign remain required. No whole-site parity or benchmark conclusion yet. Full campaign continues automatically; no current exceptional blocker.

## T4 main-document corpus complete

776 routes per project; all 1552 body projections match the immutable reference. Both corrected 42-state matrices match all recorded page fields with zero page errors. Real desktop/mobile sidebar expansion/navigation and mobile TOC/anchor/resizing match. Four shared footer/navigation mutations have full incremental==clean-forced file manifests; inputs restored. Evidence: investigation/t4 and T4-CORPUS.md.

Source models remain distinct: maintained Markdown/MDX/sidebars and derived navigation vs maintained HTML/downloads/explicit navigation metadata. Both use retained sidebar/TOC islands with native document links; no Docusaurus page app or Nift core modification.

Next T5: 17 cookbook routes, generated/special projections and remaining retained interactions; then T6 whole-site/browser acceptance, T7 initial benchmarks/lifecycle, T8 profiling, T9 final comparison/fresh clone. No whole-site acceptance or final performance claim yet. No exceptional blocker; full campaign remains active.
