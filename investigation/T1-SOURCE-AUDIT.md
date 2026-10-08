# T1 source audit — baseline in progress

Pinned documentation SHA: `5d9703a237a9efc9a7da48ac09f79526823b8182`; default branch main. Complete source archive preserved separately at `../temporal-baseline/source-5d9703a.tar.gz`, SHA256 `c95851279ccdd1725200b7445f81bc57c20250103672ea76579df7dda005a501`. Full-history upstream clone is still downloading; do not substitute an archive for Git-history preservation.

Pinned cookbook source SHA: `2385cc030f9ca1cc67b05082f1990d20cfc3a38c`; full history, source archive and bundle preserved separately. `prebuild` clones its main branch every time. Baseline must verify resulting clone SHA and reject its offline placeholder fallback; repeat/final measurements must freeze this independently moving input and disclose transport boundary.

Production workflow is `yarn build`, Node 24, Yarn frozen-lockfile install outside build timing. Yarn Classic automatically runs `prebuild` synchronization, then exact `node --max-old-space-size=7168 ./node_modules/@docusaurus/core/bin/docusaurus.mjs build`, then `postbuild` font-preload-hash validation. Keep all configured Faster options, plugins, heap settings intact. OG content-hash cache is upstream behavior, not removed.

Source inventory: 1,484 tracked blobs; 777 Markdown/MDX docs inputs. Raw scans show 53 files with Mermaid fences, 47 with populated Snipsync markers, one underscore partial. These are input counts, not publication page counts. Regex imports/JSX scans include fenced-code false positives and are not a component parser.

Production plugins: cloud region counts; cookbook metadata; Markdown page exports and llms indexes/full feed; OG cards; feedback. Algolia index/crawler managed externally; no build-side upload located. UI supports custom search, Kapa assistant, analytics and consent; no private services or submissions will be exercised. Deterministic fixtures will intercept every nonlocal request, not merely upstream's Amplitude blocklist.

Deployment includes 567 ordered redirects, three header rules, three rewrite rules, `Accept: text/markdown` middleware, and a Markdown missing-page/redirect function. Preserve these as deployment contracts, not guessed extra static HTML.

Maintained source model: rendered. Baseline is not frozen: dependency acquisition and full-history clone still running. No content translation or performance claim. Next: finish install/history, build unchanged source in a separate build checkout with full Git metadata, preserve logs/timing/RSS/publication hashes, then reproduce/classify nondeterminism and reconcile routes.
