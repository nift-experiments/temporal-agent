# Worker Configuration Patterns

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Pattern selection guide for configuring how Workers are set up, how work is routed, and how Activities access external dependencies.

These patterns cover how you set up Workers, route work to them, and give Activities the external dependencies they need — while keeping Workflow code deterministic and testable.

## Patterns in this section

- [Worker-Specific Task Queues](/design-patterns/worker-specific-taskqueue): Routes Activities to a specific Worker using a unique Task Queue, for Worker affinity and host-specific processing.
- [Activity Dependency Injection](/design-patterns/activity-dependency-injection): Injects external dependencies — clients, connections, configuration — into Activities at Worker startup, keeping Workflow code deterministic and Activities testable.

## Choosing a pattern

**A sequence of Activities must run on the same Worker host**: use [Worker-Specific Task Queues](/design-patterns/worker-specific-taskqueue) to pin them to one Worker.

**Activities depend on external resources**: use [Activity Dependency Injection](/design-patterns/activity-dependency-injection) to supply them at startup rather than constructing them inside each Activity.

## Related sections

- [QoS & Throughput Patterns](/design-patterns/qos-throughput-patterns) — Task Queue routing for rate control and fairness
- [Performance & Latency Patterns](/design-patterns/performance-latency-patterns) — run Activities in-process with Local Activities
