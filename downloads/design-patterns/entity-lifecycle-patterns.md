# Entity & Lifecycle Patterns

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Pattern selection guide for modeling long-lived stateful entities and managing Workflow history growth over time.

These patterns model long-lived business entities as Workflows and keep those Workflows healthy as they run for days, months, or indefinitely. They cover how an entity holds and mutates state, how you bound Workflow history growth, and how you manage timers that change over time.

## Patterns in this section

- [Entity Workflow](/design-patterns/entity-workflow): Models a long-lived business entity — a user account, device, or order — as a single Workflow, with Signals and Updates driving every state transition.
- [Continue-As-New](/design-patterns/continue-as-new): Prevents unbounded history growth by completing the current execution and starting a fresh one that carries forward the current state.
- [Updatable Timer](/design-patterns/updatable-timer): Provides a timer you can extend, shorten, or cancel in response to Signals or Updates while the Workflow waits.

## Choosing a pattern

**You are modeling something with an ongoing lifecycle** — an account, a device, a subscription: use an [Entity Workflow](/design-patterns/entity-workflow) as the single source of truth for that entity.

**Your Workflow runs long enough to grow a large history**: apply [Continue-As-New](/design-patterns/continue-as-new) to reset history while preserving state.

**You need a wait that responds to new information**: use an [Updatable Timer](/design-patterns/updatable-timer) instead of a fixed sleep.

## Related sections

- [Workflow Messaging Patterns](/design-patterns/workflow-messaging-patterns) — the Signals and Updates that drive entity state transitions
- [Task Orchestration Patterns](/design-patterns/task-orchestration-patterns) — decompose a large entity into child Workflows
