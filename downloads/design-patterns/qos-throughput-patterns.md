# QoS & Throughput Patterns

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Pattern selection guide for controlling execution rate, protecting downstream services from overload, and providing fair dispatch across tenants.

These patterns control how fast work executes, protect downstream services from overload, and make sure no single caller or tenant dominates dispatch.

## Patterns in this section

- [Downstream Rate Limiting](/design-patterns/downstream-rate-limiting): Rate-limits calls to a downstream service by routing throttled Activities to a dedicated Task Queue with a server-enforced throughput cap.
- [Priority](/design-patterns/priority-task-queues): Assigns a priority level to Workflows and Activities so time-sensitive work dispatches ahead of lower-priority work on the same Task Queue.
- [Fairness](/design-patterns/fairness): Distributes Task dispatches across tenants or users so a burst from one caller does not starve the others.

## Choosing a pattern

**A downstream dependency has a fixed rate limit**: use [Downstream Rate Limiting](/design-patterns/downstream-rate-limiting) to cap throughput at the Worker.

**Urgent work should move ahead of bulk work**: use [Priority](/design-patterns/priority-task-queues).

**Multiple tenants share the same Workers**: use [Fairness](/design-patterns/fairness) to keep one tenant's burst from starving others.

## Related sections

- [Worker Configuration Patterns](/design-patterns/worker-configuration-patterns) — the Task Queue and Worker setup these patterns route through
- [Batch Processing Patterns](/design-patterns/batch-processing-patterns) — rate-control patterns for large record sets
- [Error Handling & Retry Patterns](/design-patterns/error-handling-patterns) — back off and retry when a rate limit is hit
