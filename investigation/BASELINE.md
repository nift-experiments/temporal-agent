# Frozen Temporal baseline — T1

Upstream `temporalio/documentation`, main SHA `5d9703a237a9efc9a7da48ac09f79526823b8182`. Separate clean, complete unfiltered history checkout: sibling `temporal-upstream`; history bundle and full source archive hashes in `t1/preserved-source-manifest.json`. Source/build checkout unchanged; acquisition and build isolated in sibling `temporal-baseline`. Cookbook SHA `2385cc030f9ca1cc67b05082f1990d20cfc3a38c`, full history/archive/bundle and 17 generated MDX files preserved independently.

Source model: **rendered**. Maintain rendered HTML, metadata/navigation and prepared projections. No routine Markdown renderer. Both may retain framework islands. Placeholder starter is not migration.

Complete production command: `yarn build`, automatically prebuild `node bin/sync-ai-cookbook.js`, build `node --max-old-space-size=7168 ./node_modules/@docusaurus/core/bin/docusaurus.mjs build`, postbuild `node bin/check-font-preload-hash.js`. Production Faster options/plugins and memory settings unchanged. Frozen-lockfile dependency acquisition outside publication timing. Toolchain exact versions/hardware in `t1/toolchain.json`. No OS cache control. Timings are serialized exploratory baseline runs, not final medians or dev/HMR.

Reference: sibling `temporal-baseline/reference/t1-complete-history`; independently reproduced under `reference/t1-repeat-warm`. Nift output: this project's `public/`; never compare migration output against itself. Each reference file and route frozen with size/SHA256 manifests in `t1/`. Both full builds succeed, same cookbook revision, upstream source/lockfile clean.

Initial complete run: 295.3996 s; maximum individual descendant RSS 6900.9648 MiB. Warm reproduction: 34.3598 s; RSS 6878.1680 MiB. This RSS is not aggregate simultaneous tree memory. Initial OG plugin: 792 cards rendered, one cache hit, 264919 ms rendering; repeat: zero renders, 793 cache hits. 792 unique OG files (two pages share a hash). Preserve upstream warm cache advantage; do not claim initial generation cost occurs on every build.

Accounting: 777 docs source files plus 17 generated cookbook MDX; main-doc routes 776 (one partial excluded), cookbook 17; **793 primary docs routes**. **962 HTML files** = 793 primary + 150 main tag pages + 16 cookbook tag pages + blog landing + search + 404. **806 Markdown files** = 794 source-derived exports (including excluded partial's projection) + 12 static tooltip definitions. **24 llms*.txt outputs** = root index/full feed + 22 section indexes (plugin log says 24 section definitions; actual file count is authoritative). 567 redirect rules are deployment config, not HTML pages. Complete output: **3984 files**, **265647260 bytes** initially.

Nondeterminism classification: **semantic deterministic / operational sidecar variant**. Reproduction matches all 3983 product/publication files byte-for-byte; only `.og-image-stats.json` differs in render/cache counters and elapsed time. Preserve the varying sidecar and its qualification; exclude only its measurement values from parity comparison, never user-visible content/assets. `t1/reproduction-diff.json` proves this.

Remote boundaries: Algolia crawler/index external; no upload/live query, no private API, analytics, feedback or Kapa MCP calls. Public cookbook clone is required read-only production acquisition. Committed generated permissions/CLI/Snipsync/SDK inputs are pinned; their separate update workflows are not routine builds. Capture deterministic local UI/transport fixtures before scaling; no backend parity claim.

Inherited evidence: 124 Markdown transform warnings, package peer warnings, stale pinned caniuse warning and Node module-format warning. No upstream modification to silence them.

T1 baseline gate passed. Next T2: freeze browser/transport and route/content contract; then T3 architecture proof before broad translation. No migration parity or final benchmark claims yet.
