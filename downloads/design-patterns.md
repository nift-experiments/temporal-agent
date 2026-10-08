# Temporal Design Patterns

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> A catalog of common, reusable, and proven design patterns for Temporal Workflows, organized by problem domain.

Temporal provides a set of durable execution primitives that you can compose into common, reusable, and proven patterns.
Having these patterns in your toolbox helps you solve recurring problems in a battle-tested way.

## Task orchestration patterns

- [Child Workflows](/design-patterns/child-workflows): Decomposes complex Workflows into smaller, reusable units. Each child has an independent Workflow ID, history, and lifecycle.
- [Parallel Execution](/design-patterns/parallel-execution): Executes multiple Activities concurrently for maximum throughput with error handling and controlled parallelism.
- [Pick First (Race)](/design-patterns/pick-first): Races multiple Activities in parallel, returns the first completed result, and cancels the remaining Activities using SDK cancellation scopes.

## Workflow messaging patterns

- [Signal with Start](/design-patterns/signal-with-start): Starts a Workflow when Signaling it if it does not already exist. If already running, it receives the Signal directly.
- [Request-Response via Updates](/design-patterns/request-response-via-updates): Uses a Workflow Update to validate a request, modify Workflow state, and return a typed result to the caller synchronously, with strong consistency.
- [Event Accumulator](/design-patterns/event-accumulator): Durably collect and deduplicate signals from multiple senders, then process the batch after a sliding inactivity timeout.

## Entity & lifecycle patterns

- [Entity Workflow](/design-patterns/entity-workflow): A long-lived business entity — a user account, device, or order — gets one Workflow per instance, with Signals and Updates driving every state transition.
- [Continue-As-New](/design-patterns/continue-as-new): Prevents unbounded history growth by completing the current execution and starting a new one with fresh history.
- [Updatable Timer](/design-patterns/updatable-timer): Dynamically adjustable timers that respond to Signals or Updates. Extend, shorten, or cancel timers based on external events.

## External interaction patterns

- [Polling External Services](/design-patterns/polling): Strategies for polling external resources with varying frequencies: frequent, infrequent, and periodic patterns.
- [Long-Running Activity](/design-patterns/long-running-activity): Long-running Activities report progress via heartbeats and enable resumption after failures with cancellation support.
- [Delayed Start](/design-patterns/delayed-start): Creates Workflows immediately but defers execution until a specified delay expires. Fits one-time scheduled operations and grace periods.
- [Delayed Callback (Webhooks)](/design-patterns/delayed-callback): Webhooks become durable: inbound calls arrive as Signals, outbound calls fire after a durable sleep, and Activities complete later via task tokens.
- [Approval](/design-patterns/approval): Human-in-the-loop Workflows that block until external approval decisions are made. Uses Signals to capture approval data with metadata.

## Distributed transaction patterns

- [Saga Pattern](/design-patterns/saga-pattern): Manages distributed transactions with compensating actions. Each step has a compensation that undoes its effects if subsequent steps fail.
- [Early Return](/design-patterns/early-return): Synchronous initialization with asynchronous completion. Returns results immediately while processing continues in the background.

## Error handling & retry patterns

- [Fixed Count of Retries](/design-patterns/fixed-count-retries): Cap the number of Activity retry attempts to control cost when each attempt consumes a paid or limited resource.
- [Fixed Wall-Time Retries](/design-patterns/fixed-wall-time-retries): Bound the total elapsed time across all retry attempts to enforce a business SLA, regardless of how many individual attempts occur.
- [Non-Retryable Errors](/design-patterns/non-retryable-errors): Mark error types that will never succeed — such as validation failures or missing records — so Temporal fails fast instead of retrying indefinitely.
- [Delayed Retry](/design-patterns/delayed-retry): Override one failure's retry interval with nextRetryDelay on ApplicationFailure, matching the wait time the error reports.
- [Fast/Slow Retries](/design-patterns/fast-slow-retries): Retry fast with a short interval first, then shift to a slow, unlimited interval so the Workflow outlasts an extended downstream outage.
- [Retry Alerting via Metrics](/design-patterns/retry-metrics): Emit a metric from the Activity when attempts cross a threshold, so on-call teams see persistent failures before an SLA breach.
- [Resumable Activity](/design-patterns/resumable-activity): Park the Workflow after retries are exhausted and wait for a human to signal a correction, then resume execution from where it left off.

## Batch processing patterns

- [Fan-Out with Child Workflows](/design-patterns/fanout-child-workflows): Distributes a large record set across parallel Child Workflows for concurrent processing with automatic scaling.
- [Batch Iterator](/design-patterns/batch-iterator): Pages through unbounded datasets using Continue-As-New to prevent history overflow while maintaining exactly-once processing guarantees.
- [Sliding Window](/design-patterns/sliding-window): Maintains a fixed number of concurrently active Child Workflows, starting a new one each time an existing one completes.
- [MapReduce Tree](/design-patterns/mapreduce-tree): Recursively splits a dataset into a binary tree of Child Workflows, processes leaves in parallel, then aggregates results back up the tree.

## QoS & throughput patterns

- [Downstream Rate Limiting](/design-patterns/downstream-rate-limiting): Rate-limits calls to a downstream service by routing throttled Activities to a dedicated Task Queue with a server-enforced throughput cap.
- [Priority](/design-patterns/priority-task-queues): Assigns a priority level to Workflows and Activities so that time-sensitive work dispatches ahead of lower-priority work within a single Task Queue.
- [Fairness](/design-patterns/fairness): Distributes Task dispatches across tenants or users so that a burst from one caller does not starve the others.

## Performance & latency patterns

- [Local Activities](/design-patterns/local-activities): Local Activities run inside the Worker process, skipping server round-trips for short, idempotent Activities on a latency-sensitive path.
- [Early Return + Local Activities](/design-patterns/early-return-local-activities): Extends Early Return by running Phase 1 as Local Activities, so the client's first response comes from in-process work, not a server call.
- [Eager Workflow Start](/design-patterns/eager-workflow-start): Eager Workflow Start sends the first Workflow Task directly to a co-located Worker, skipping the Matching Service to cut startup latency.

## Worker configuration patterns

- [Worker-Specific Task Queues](/design-patterns/worker-specific-taskqueue): Routes Activities to specific Workers using unique Task Queues for Worker affinity and host-specific processing.
- [Activity Dependency Injection](/design-patterns/activity-dependency-injection): Injects external dependencies into Activities at Worker startup, keeping Workflow code deterministic and Activities testable.
