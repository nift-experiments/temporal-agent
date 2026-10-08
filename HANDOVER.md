# HANDOVER.md
v0.0.8

This is a living handover for working effectively in a Nift project.

Canonical version:

https://nift.dev/HANDOVER.md

Check the version at the top of this file against the canonical copy when the
project is old, unfamiliar, or behaving differently from the current Nift
documentation.

To replace this file with the latest canonical version:

```sh
curl -fsSL https://nift.dev/HANDOVER.md -o HANDOVER.md
```

If this project has project-specific additions, preserve or reapply them when
updating the canonical handover.

This project uses Nift as part of its website build process.

Nift is the project's build-time templating and dependency layer. It does not determine what the website is about or what other technologies the project should use.

Keep the existing project architecture and use the project's normal HTML, CSS, JavaScript, frameworks, backend, and other tooling where appropriate.

Do not introduce Nift-specific machinery where ordinary web tooling is the clearer solution.

## Start here

Before making substantial changes:

1. Inspect `.nift/config.json` and `.nift/tracked.json`.
2. Inspect the existing `content/`, `templates/`, and output structure.
3. Read this project's `README.md` and other project-specific documentation.
4. Run:

```sh
nift status
```

During normal development, build frequently:

```sh
nift build
```

Use this throughout a task, not only at the end. Rebuild after meaningful
changes so Nift can surface template, path, dependency, configuration, and
tracking errors while the cause is still obvious.

In particular, run `nift build` immediately after editing
`.nift/config.json` or `.nift/tracked.json`.

Use:

```sh
nift status
```

when you want to inspect what Nift considers stale and why.

Successful `nift build` output may include indented `↳ ...` lines explaining
why a page was considered stale and rebuilt, such as a missing generated output
or a changed dependency. These are rebuild reasons, not errors. Actual build
failures are reported as errors and cause the build to fail.

Do not delete or recreate `.nift/`.

## Nift's core template model

Most Nift websites need very little Nift-specific syntax.

The three primitives you will use most often are:

```text
@content
@input(...)
@path(...)
```

`@content` inserts the tracked page's content into its template.

```html
<main>
    @content
</main>
```

`@content` should execute exactly once across the rendered template/input graph
for a tracked page. It is normally placed in the page's template; the tracked
content file supplies the content inserted there.

Content files may still use other Nift syntax when needed. If page text needs
to display Nift syntax literally, prefix the active sigil with `\` rather than
leaving it as template syntax:

```html
<code>\@content</code>
<code>\@path('about')</code>
<code>\$[title]</code>
```

This applies whenever `@...`, `$[...]`, or other Nift syntax is intended as
literal output rather than something Nift should execute or resolve.

`@input(...)` inserts a reusable file and automatically makes it a dependency of the output using it.

```html
@input('templates/header.html')

<main>
    @content
</main>

@input('templates/footer.html')
```

### Structured JSON and markup sources

Use name-first `@json` when a template needs immutable structured data:

```text
@json(name, path)
@json(name, schema-path, path)
@json(name, schema-name, path)
@json(name){...}
@json(name, schema-path){...}
@json(name, schema-name){...}
```

Inline bodies are evaluated as Nift templates before JSON parsing. A schema
name refers to an earlier JSON binding. Data and schema files are automatic
dependencies and paths must stay inside the project.

Use `@markup(format){...}` or `@markup(format, path)` for Markdown (`md`),
AsciiDoc (`adoc`) or reStructuredText (`rst`). Nift evaluates template syntax in
the source first, Markup++ converts it once, and the resulting HTML is appended
without being parsed as Nift syntax again. File sources and host-resolved
AsciiDoc/RST includes are automatic dependencies.

`@path(...)` creates project-aware links to tracked pages and local assets.

Nift has additional features including metadata, JSON data, loops, conditionals, pagination, contracts, and explicit dependencies. Use them when the project actually needs them; do not use advanced features merely because they exist.

When writing expressions inside constructs such as `@if(...)`, refer to values directly rather than wrapping them in `$[...]`. For example:

```html
@if(name == 'about'){...}
```

Use `$[...]` when resolving or rendering a value into output, for example `$[title]`. Consult the expressions and control-flow documentation when using more advanced expression syntax.

## Internal links: use `@path`

Use `@path(...)` for internal links.

This applies to:

- links between pages;
- stylesheets;
- JavaScript;
- images and other local assets where Nift should know the relationship.

For pages, link to the **tracked page name**, not its generated file.

```html
<nav>
    <a href="@path('/')">Home</a>
    <a href="@path('about')">About</a>
    <a href="@path('docs')">Docs</a>
    <a href="@path('contact')">Contact</a>
</nav>
```

Do this:

```html
<a href="@path('about')">About</a>
```

Do not do this:

```html
<a href="@path('about.html')">About</a>
```

and do not hard-code the generated output path:

```html
<a href="about.html">About</a>
```

The tracked page name is the stable project identity. Its output filename or location may change independently.

CSS and JavaScript includes should also use `@path(...)`:

```html
<link rel="stylesheet" href="@path('public/assets/style.css')">
<script src="@path('public/assets/app.js')"></script>
```

Do not calculate relative paths such as:

```html
<link rel="stylesheet" href="../../assets/style.css">
```

Using `@path` lets Nift resolve the correct output-relative path and check the project relationship during the build.

## Project configuration

`.nift/config.json` contains project-level Nift configuration.

`.nift/tracked.json` describes tracked pages and their metadata, including things such as their content, template, and output relationships.

By default, ordinary CSS, JavaScript, images, fonts and other static assets live
directly in the configured output tree (normally `public/`) and do not have
entries in `.nift/tracked.json`. Edit those files in place. This keeps Nift's
tracked graph focused on content that Nift actually renders and avoids duplicate
source/output copies for files that need no build-time transformation.

Track an asset only when Nift genuinely needs to generate it from content,
templates or build-time data. Template-less tracked entries remain available for
that advanced case; they are not the default asset workflow.

These files are part of the project and should evolve with its structure.

If you add, remove, or reorganise pages, templates, outputs, deployment settings, or other Nift-managed structure, inspect the relevant `.nift` configuration and update it where necessary.

Do not treat `.nift/` as disposable generated state.

Do not invent `.nift/tracked.json` fields or assume arbitrary fields become
`$[...]` metadata. When you need tracking behaviour or metadata that is not
already demonstrated by the project, consult the tracked-files and metadata
documentation rather than guessing.

## Output directory

Do not assume the generated website always lives in `public/`.

A normal Nift project may use `public/`, but deployment targets can use a different output structure appropriate to the platform.

Inspect `.nift/config.json` before making assumptions about output paths.

Edit Nift-managed page sources rather than their generated output. Edit untracked
static assets directly in the configured output tree, unless the project
documents another tool or source directory as their owner.

## Pagination

Pagination has several related pieces across `.nift/tracked.json`, page
content, pagination templates, and generated page links. Do not infer its full
behaviour from this handover.

If working with pagination, read the dedicated documentation first:

https://nift.dev/docs/pagination.html

Preserve the project's existing pagination structure unless the task actually
requires changing it, and run `nift build` frequently while doing so.

## Other stacks and tools

Nift does not need to own the whole application.

A project may use Nift alongside tools such as Vite, React, Vue, Svelte, TypeScript, Go, Node, Python, PHP, serverless functions, or other systems.

Keep responsibilities separated:

- use Nift for build-time composition, tracked relationships, and dependencies;
- use the neighbouring tool for the job it is designed to do.

Do not replace an existing stack with Nift-specific code simply to make more of the project use Nift.

## Before finishing

Run:

```sh
nift build
nift status
```

The build should succeed and `nift status` should report the project up to date.
Spot-check generated output when changes affect paths, templates, tracked
relationships, or deployment structure.

## Documentation

Nift documentation:

https://nift.dev/docs.html

When unfamiliar with the project, prioritise:

1. Getting started — https://nift.dev/docs/getting-started.html
2. the three-primitives/template-language material;
3. paths and tracked files, especially `@path`;
4. project structure;
5. `.nift/config.json` and `.nift/tracked.json`;
6. incremental builds and CLI commands.

Then read feature documentation only when the task requires it, for example:

- JSON and control flow;
- pagination;
- contracts;
- minification;
- deployment targets;
- integration with other application stacks.

Prefer documented Nift behaviour and the existing project structure over guessing based on another website generator or framework.

## Temporal campaign state — T0

Repository: `nift-experiments/temporal-agent`. Maintained source model: **rendered**.

T0 initialized using `nift init --migration`; generated guidance read and preserved under `investigation/init-generated/`. Starter `nift build` succeeds and `nift status` reports one current placeholder page. No migrated content yet.

Follow MIGRATION.md; campaign checkpoints T0–T9 map to its phases. Upstream full-history checkout is separately cloning to sibling `temporal-upstream`; baseline evidence will live in sibling `temporal-baseline`. Pin the exact default-branch SHA, audit production scripts/remote boundaries, preserve source/history and freeze complete publication before translating.

No telemetry, feedback, search uploads or private API calls. No Nift core changes. Maintain rendered HTML and explicit metadata/navigation; no routine Markdown conversion; islands remain available where faithful and maintainable.

Next: complete T1 upstream baseline; then parity contract and representative architecture proof before corpus scaling. Full campaign authorized through T9, with exceptional stop policy from the user brief.

T1 audit recorded in `investigation/T1-SOURCE-AUDIT.md`; preserved baseline tooling/evidence lives in sibling `temporal-baseline`. Current sessions are full-history clone and frozen-lockfile dependency installation. No source translation.

## T1 complete

The full unchanged production baseline and its warm reproduction succeeded. `investigation/BASELINE.md` and `investigation/t1/` contain complete accounting, byte manifests, logs, versions, timings/RSS and exact upstream source/archive pins. Only the operational OG stats sidecar varies. Original immutable reference lives in sibling `temporal-baseline/reference/t1-complete-history`; clean source reference is `temporal-upstream`. Next T2 freezes browser/local-transport fixtures; T3 must prove architecture and incremental/full equality before corpus translation.

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

## Active T5 work in progress

T4 accepted at authored 55e1fb7 / rendered f0e2ecc (both pushed). Current working changes are T5, not an accepted checkpoint. Authored sources now cover 793 primary routes and full 962 HTML route structure including tag/search/404/blog families. Standalone original Markdown/LLM projection stage matches all 831 reference .md/.txt products bytewise (806 Markdown, 24 LLM text plus robots). Rich event-history children are converted once to HTML/step data for retained islands, details now retain the original animated component, and Markdown images retain zoom/NoZoom boundaries. These interaction additions and special families still need browser validation.

Next: finalize portable deployment/sitemap accounting, generated cookbook ownership/update workflow and complete retained rich-child fixtures; then T5 acceptance and T6 full parity. No performance acceptance yet. No exceptional blocker.

## T5 accepted

All 962 HTML routes, 832 Markdown/text/sitemap products, and 1,130 retained non-framework assets verified against the pinned reference. Full representative browser parity: 132 states per project, zero differences/errors; 49 interaction cases per project. Portable redirect/Markdown/404 checks passed. See investigation/T5-SPECIAL-PUBLICATION.md and investigation/t5. Next: T6 whole-site parity, then T7 initial benchmarks and incremental correctness. No formal benchmark accepted yet.
