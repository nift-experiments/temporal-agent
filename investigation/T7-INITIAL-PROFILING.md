# T7 initial profiling and lifecycle

T7 passes. T8 optimization and T9 final comparison/clean-checkout verification remain required; these are initial results, not a final benchmark claim.

The first faithful T6 implementation has five serialized warm full-production samples per implementation. Maximum individual descendant/phase RSS and separate 50 ms sampled descendant-RSS sums are recorded. The latter double-count shared resident pages, are not PSS, and may miss peaks. Dependencies were acquired outside timing; OS caches were uncontrolled. Upstream retains its complete Yarn prebuild/build/postbuild, Faster configuration, 7168 MiB Node heap, cookbook synchronization, OG plugin and font check. No development-server/HMR claim is made.

| Initial warm full | Median wall seconds | Range | Median max individual RSS MiB |
|---|---:|---:|---:|
| upstream | 37.867 | 35.153–40.636 | 6898.0 |
| temporal | 27.366 | 26.259–30.420 | 1141.6 |
| temporal-agent | 11.434 | 9.905–13.016 | 844.9 |

The initial authored implementation spends approximately 11.56 seconds in MDX conversion and 5.76 seconds in shared-shell preparation (medians of individual components). The rendered implementation spends approximately 6.57 seconds in shared-shell preparation. Bare Nift composition is approximately 0.39 seconds in either implementation; complete publication includes the other stages. These timings are not native Nift Markdown-renderer performance.

Lifecycle hardening then added source-derived routing/frontmatter/navigation metadata, actual retained footer rendering, content-hashed island assets under immutable publication headers, selective OG maintenance, and generated-product retirement. The subsequent unchanged-command and edit measurements are a separate single-sample cohort of this hardened implementation. Their raw logs are retained; they should not be mixed with the earlier warm-full sample median.

Twenty changed-input cases (ten per project: 1/10/100 bodies, metadata, layout, navigation, diagram, local cookbook source, search-visible content, and island source) and six add/rename/delete lifecycle cases pass full file-manifest equality against independent clean forced recomputation. Fixture sources are restored. The authored Markdown/MDX path derives its projections. Rendered-source edits own HTML, explicit metadata and pre-derived downloads/LLM views; coordinated projection maintenance remains an architectural responsibility. Search-visible checks exercise publication inputs and local outputs, not a live Algolia recrawl/upload. Prototype body-only cases measure maintained HTML edits, without claiming automatic cross-projection derivation in the rendered source model.

Existing OG assets are maintained under `static/img/og` and copied unchanged in normal builds. Metadata changes require explicit `node tools/refresh-og.cjs --route PATH`; the representative change renders one image. Rendered-source component changes can use explicit `node tools/refresh-islands.cjs --island Retry` to update maintained initial markup; the normal build does not parse Markdown. Explicit maintenance timings remain separate and included in whole-operation case costs.

Route addition verifies HTML, Markdown download, sitemap and (authored) derived tag output. Rename removes the old HTML/download and updates the new canonical route. Delete retires publication products and the authored derived tag. These standalone fixtures establish retirement, not a promise that source-authored hardcoded links or rendered-source pre-derived indices update themselves.

Revalidation after restoration passes 962 routes in each project, 4544 code blocks each, 1924 navbar active-state checks, 264 browser states with zero page errors, 832 byte-identical ancillary products each, and 1130 byte-identical retained assets each. All remote browser transports are intercepted; backend functionality remains untested as declared in the parity contract.

Rejected drafts are preserved: the fixture's initial tag assertion missed Docusaurus's `t-7` slug normalization; the first retirement implementation also removed static terms/robots and was corrected to protect maintained static products; Blog/404 title regressions were corrected. The route tests now pass independently. Source libraries and Nift core were not changed.

T8 targets: avoid repeat conversion of unchanged MDX, repeated server bundling/startup, unchanged body/shell rendering and unchanged Markdown/LLM transformation; preserve independent force bypasses and content-verified dependencies. Retain fixed fan-out costs and ownership qualifications honestly. T9 will repeat complete scenarios, verify clean public clones, report ranges and component/whole costs, give the three-way maintenance judgement and complete the init review.
