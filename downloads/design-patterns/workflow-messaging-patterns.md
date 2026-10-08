# Workflow Messaging Patterns

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Pattern selection guide for sending data into running Workflows and receiving responses or triggering behavior changes.

These patterns cover how external callers communicate with running Workflows — starting them on demand, sending data in, reading results back, and collecting streams of events. They build on Temporal's Signals and Updates.

## Patterns in this section

- [Signal with Start](/design-patterns/signal-with-start): Starts a Workflow and delivers a Signal in a single atomic operation. If the Workflow already runs, it receives the Signal directly.
- [Request-Response via Updates](/design-patterns/request-response-via-updates): Sends a request into a running Workflow through an Update, which validates it, modifies state, and returns a typed result on the same call.
- [Event Accumulator](/design-patterns/event-accumulator): Collects a stream of incoming Signals into a buffer and processes them together as a batch, rather than one at a time.

## Choosing a pattern

**You want to send a message without checking whether the Workflow is running**: use [Signal with Start](/design-patterns/signal-with-start).

**You need a result back from the Workflow, with validation**: use [Request-Response via Updates](/design-patterns/request-response-via-updates).

**You receive many events and want to process them in batches**: use the [Event Accumulator](/design-patterns/event-accumulator) to buffer and flush.

## Related sections

- [Entity & Lifecycle Patterns](/design-patterns/entity-lifecycle-patterns) — long-lived Workflows that consume these messages over time
- [Distributed Transaction Patterns](/design-patterns/distributed-transaction-patterns) — Early Return builds on the Update-with-Start mechanism
