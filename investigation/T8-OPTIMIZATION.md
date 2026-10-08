# T8 — profile, optimize, and revalidate

T8 preserves the authored and rendered source models. Nift core remains unchanged. Normal publication is `node tools/publish.cjs` (`yarn build`); independent recomputation is `node tools/publish.cjs --force` (`yarn build:force`). Bare `nift build` composes prepared products and is not the complete production workflow.

## Profiling response

T7 showed repeated conversion, server/browser bundling, React rendering, shared-shell preparation and Markdown/LLM transformation even for unchanged inputs. The project tools now use SHA-256 input signatures and verify every cached product's bytes before reuse. Force bypasses every stage cache and rebuilds all Nift pages. Records are transient under `.cache/stage-records`, written atomically, and can be discarded.

Authored MDX caching retains the official pinned Docusaurus MDX compiler, frontmatter behavior, Markdown link resolution and actual corpus components. Imported MDX, emitted assets and source assets remain tracked; body signatures cover reachable compiled MDX modules and runtime/context inputs. Rendered publication reads maintained HTML directly, without a Markdown renderer. Both cache retained browser/server bundles, transient bodies, shells and complete ancillary projection sets. Static assets and generated runtime assets remain content-checked and owned outputs are retired. Cookbook conversion writes only changed bytes.

The authored region-count plugin is the pinned upstream implementation: it counts headings in maintained AWS/GCP reference Markdown. Derived cookbook and document route context likewise comes from authoritative authored sources. Rendered metadata/context remains explicit and derives only the document-ID/path index required by the actual retained components; maintained projection consistency is its separate maintenance responsibility.

## Correctness and rejected drafts

All 20 optimized changed-input tests and all six route add/rename/delete tests produce complete byte manifests identical to independent forced computation. Rendered edit fixtures coordinate relevant Markdown downloads and LLM text rather than merely changing body HTML. Route fixtures verify canonical/download/sitemap and LLM entry retirement; authored tag products are additionally derived and retired. They do not promise automatic rewriting of arbitrary hardcoded source links.

Eleven injected-corruption tests repair body HTML, shell prefixes, browser/server bundles, downloads and authored compiled MDX to independently built publication bytes. A real included AWS reference edit changes the derived region count from 14 to 15 and now matches independent forced computation across every publication file.

The first included-reference probe caught a stale TOC on two consumer pages. Body/runtime invalidation was insufficient: the TOC cache also needed transitive compiled-MDX imports. This was corrected and the rejected probe retained. Earlier cache prototypes and the incorrect special-route OG guard are also retained as rejected evidence, not accepted benchmark results.

## Cost boundaries and remaining work

T8 probes demonstrate substantially cheaper routine changes, especially direct maintained-HTML edits. The first body-1 measurements include cache initialization after implementation changes and are excluded from warm-iteration claims. T9 will establish the final scenario cohort and retime warm changed-input cases.

Forceful authored conversion, route/catalogue invalidation, shared-shell/navigation fan-out, retained component bundling/SSR, content verification and publication copying still cost time. Content-verified caching adds bookkeeping; it is not guaranteed to improve forced full builds. Do not replace the forced definition with a cache-using command to improve the headline. Dependency pruning and finer validated invalidation are future tooling work.

Projection timing includes input/product verification on cache hits. Source catalogue/context timing is separate in the authored path; command wall time includes startup and other preparation not attributed to a named phase. No timings represent native Nift `@markup` performance. Mermaid remains retained browser behavior; no invented server Mermaid-generation phase is claimed. Search UI/local transport fixtures are tested; Algolia indexing/uploads and live backend operations are not exercised.

## Revalidation contract

Acceptance requires restored 962-route semantic parity per project, 4,544 highlighted code blocks each, navbar/link audits, all 832 ancillary products and 1,130 retained non-framework assets byte-identical, 264 representative browser states with zero errors/differences and 49 interaction observations per project. Representative layout checks retain T6's explicit tiny rasterization qualification; geometry must match. Remote requests are fulfilled/blocked locally before first navigation.

The `investigation/t8` tree preserves probes, failures, corrected equality checks and restored parity artifacts with a SHA-256 manifest. T9 remains required: public clean clones, final serialized benchmark cohort, three-way maintenance judgment and migration-init review.
