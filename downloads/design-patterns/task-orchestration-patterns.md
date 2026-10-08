# Task Orchestration Patterns

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Compares Child Workflows, Parallel Execution, and Pick First (Race) for decomposing, running concurrently, and racing work inside a single Workflow.

These patterns compose and coordinate multiple units of work within a Workflow — decomposing large processes into reusable pieces, running work concurrently, and racing alternatives against each other.

## Patterns in this section

- [Child Workflows](/design-patterns/child-workflows): Decomposes a complex Workflow into smaller, reusable units. Each child has its own Workflow ID, history, and lifecycle.
- [Parallel Execution](/design-patterns/parallel-execution): Runs multiple Activities concurrently for higher throughput, with error handling and a bound on how many run at once.
- [Pick First (Race)](/design-patterns/pick-first): Races multiple Activities in parallel, takes the first result to arrive, and cancels the rest.

## Choosing a pattern

**A process is large or reused across Workflows**: break it into [Child Workflows](/design-patterns/child-workflows) with independent histories.

**Independent work can run at the same time**: use [Parallel Execution](/design-patterns/parallel-execution) with a concurrency bound.

**Several approaches compete and you want the first to finish**: use [Pick First (Race)](/design-patterns/pick-first) and cancel the losers.

## Related sections

- [Batch Processing Patterns](/design-patterns/batch-processing-patterns) — fan-out orchestration scaled to large record sets
- [Performance & Latency Patterns](/design-patterns/performance-latency-patterns) — reduce the latency of the work each task performs
