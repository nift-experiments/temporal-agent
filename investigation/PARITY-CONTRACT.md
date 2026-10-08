# T2 — frozen observable parity contract

Pinned source: `5d9703a237a9efc9a7da48ac09f79526823b8182`. Observable reference: the complete successful T1 production publication, not the live mutable website. T2 defines requirements; it does not establish migration parity.

## Inventory and acceptance scope

Preserve 962 HTML routes (793 main/cookbook docs and 169 ancillary routes), 806 Markdown files, 24 LLM projections, 792 unique document OG images, static publication assets, title/canonical/description/social metadata, headings/anchors, tables/code, links, and deployment route behavior. Compare publication inventories independently from browser observations. The operational `.og-image-stats.json` varies with cache state; its counters are evidence, not product byte equality.

## Representative browser matrix

`fixtures.json` maps 21 actual source/page families to routes. `browser/observations.json` captures all 126 states: desktop 1440×1000 and mobile 390×844, each in dark/light/system (system preference light). Capture requested theme, effective theme and `data-theme-choice` separately. Set the actual namespaced upstream preference `theme-014`; system removes that preference. Compare main text, headings, links, tab state, diagram count, overflow and visible controls, with screenshots for the homepage. The fixture families cover ordinary/SDK tabs, setup steps, best practices, generated CLI/permissions, cookbook/AI, architecture/event history, integrations, four interactive demos, cloud tooltips, search and 404 content.

## Interaction requirements

`interactions/observations.json` captures both viewport families: theme switching; mobile navigation; tab click and manual-selection keyboard focus; exact published Markdown copy with source prefix; code copy; integration filtering; retry-simulator state change; diagram zoom; deterministic search hit and navigation; assistant delegation; feedback modal opening without submission. Preserve the upstream desktop diagram zoom and mobile non-opening behavior. Arrows move tab focus; they do not immediately select a different tab. Clipboard tests use a local clipboard fixture, not the OS clipboard.

## Deployment and social contracts

`deployment.json` checks 563 concrete samples against ordered upstream redirect matching from 567 rules, trailing-slash redirects, HTML and Markdown missing-route responses, and Markdown content negotiation. Four regex rules are retained in the configuration but excluded from the simple sample generator; do not call the samples exhaustive hosted Vercel validation. `/404.html` is a direct content fixture (200); an unknown path is the actual 404 status check. Preserve pinned deployment headers, rewrites, conditional rules and Markdown fallback handlers as maintained deployment source; the local gateway is a bounded fixture harness, not a Vercel implementation. The upstream OG validator passed all 793 doc metadata/files plus 169 non-doc default cards; retain that validation separately from browser claims.

## External systems

Every browser request is intercepted. Public PushFeedback scripts/styles are frozen at resolved version 0.1.87 with hashes; its public project response is a local fixture. Google Fonts stylesheet and seven Inter subsets are frozen for this fixture browser. Algolia receives a deterministic local record for `workflow`; no live index is queried or mutated. Kapa is a local delegation stub, not an assistant implementation. Consent country/region response is local. Analytics, telemetry and insights requests are answered locally and never forwarded. Feedback forms are never submitted. See `fixtures/remote-assets` and `tools/local-transports.cjs`. Static test assets are independently pinned runtime inputs, not extra files in the 3,984-file upstream publication.

## Known reference qualifications

The earlier v2 matrix set an unnamespaced `theme` key and therefore tested matching OS preferences rather than explicit saved choice. It is preserved under `reference-draft-v2` and superseded by v3 using `theme-014`, with v6 interactions. The initial 108-state draft was superseded by the 126-state capture: it omitted explicit tab families and used an incorrect Mermaid SVG selector. Failed interaction attempts were test-locator/request-shape corrections, preserved as investigation history. They are not product defects. The frozen reference has mobile horizontal overflow on the homepage and two demo pages; retain this in comparison rather than redesigning the reference. Upstream Markdown projection logged 124 inherited transformation warnings. Backend search/feedback/assistant and hosted deployment behavior are not exercised. No migration parity claim is permitted until T3/T6.
