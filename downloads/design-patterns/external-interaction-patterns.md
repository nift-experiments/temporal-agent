# External Interaction Patterns

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Compares five patterns for waiting on external systems and human decisions: polling, heartbeating Activities, delayed start, webhooks, and approval.

These patterns cover how a Workflow waits on or interacts with the world outside it — external APIs, human decisions, scheduled delays, and inbound or outbound callbacks — while staying durable across failures.

## Patterns in this section

- [Polling External Services](/design-patterns/polling): Checks an external resource on a schedule until it reaches the state you need, with frequent, infrequent, and periodic variants.
- [Long Running Activity](/design-patterns/long-running-activity): Reports progress via heartbeats and resumes after failures, with cancellation support, for Activities that run for minutes to hours.
- [Approval](/design-patterns/approval): Blocks the Workflow until an external decision arrives, capturing the approval and its metadata through a Signal.
- [Delayed Start](/design-patterns/delayed-start): Creates the Workflow immediately but defers execution until a delay expires.
- [Delayed Callback (Webhooks)](/design-patterns/delayed-callback): Webhooks become durable: inbound calls arrive as Signals, outbound calls fire after a durable sleep, and Activities complete later via task tokens.

## Choosing a pattern

**The external system offers no notification**: use [Polling External Services](/design-patterns/polling) and tune the interval to the expected latency.

**One Activity runs for a long time**: use a [Long Running Activity](/design-patterns/long-running-activity) with heartbeats so failures resume instead of restarting.

**A person or external system must decide**: use [Approval](/design-patterns/approval) to block on a Signal.

**Execution should begin later**: use [Delayed Start](/design-patterns/delayed-start).

**You send or receive HTTP callbacks**: use [Delayed Callback (Webhooks)](/design-patterns/delayed-callback).

## Related sections

- [Error Handling & Retry Patterns](/design-patterns/error-handling-patterns) — retry strategies for the external calls these patterns make
- [Workflow Messaging Patterns](/design-patterns/workflow-messaging-patterns) — the Signals that deliver external decisions into a Workflow
