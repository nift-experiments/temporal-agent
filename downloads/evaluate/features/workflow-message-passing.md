# Workflow message passing

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Signals write to a running Workflow without waiting, Queries read its current state, and Updates do both and return a result to the caller.

A running [Workflow Execution](/workflow-execution) can receive messages from outside itself.
Its message handlers act on the Workflow's current state, which makes a Workflow behave like a stateful service with its own endpoints.
Temporal has three message types: **Signals** are asynchronous write requests, **Queries** are read requests, and **Updates** are synchronous write requests that return a result.

Each one fits a different job:

- Your shipment-tracking Workflow needs to know when an item leaves the warehouse. **Signal** the Workflow when the driver scans the barcode.
- Your team wants to track the progress of a data migration. **Query** the running batch Workflow for the numbers behind a progress bar.
- Your shopping cart Workflow needs to add an item and render the cart. **Update** it to add the item and get the current contents back in the same call.

## Choose a message type

|                                                        | Signal            | Query | Update              |
| ------------------------------------------------------ | ----------------- | ----- | ------------------- |
| Reads Workflow state                                   | No                | Yes   | Yes                 |
| Changes Workflow state                                 | Yes               | No    | Yes                 |
| Caller waits for the handler                           | No                | Yes   | Yes                 |
| Returns a value to the caller                          | No                | Yes   | Yes                 |
| Recorded in the [Event History](/workflow-execution/event#event-history) | Yes | No    | Yes, once accepted  |
| Handler can block                                      | Yes               | No    | Yes                 |

For **write requests**, the choice is whether the caller needs to know the outcome.
Send a Signal when the caller can move on without a result and shouldn't depend on a Worker being available to accept the request.
Send an Update when the caller needs a result or an error, wants low end-to-end latency, or should be rejected up front by a validator before the request enters the Workflow's Event History.

For **read requests**, start with a Query.
Queries never add Events to the Event History, and they work against completed Workflow Executions.
Because a Query handler cannot block, reading a value that only exists once the Workflow reaches a certain state means either polling with Queries or writing the read as an Update, which is more efficient but does write to the Event History.

For **combined read and write requests**, use an Update.
If the request has to be asynchronous, send a Signal and poll with a Query.

To stream a sequence of events out of a Workflow rather than answer a single request, see [Workflow Streams](/workflow-streams).

## When not to use a message

- **To change state from a Query.** A Query handler can inspect Workflow state but must not mutate it. Use a Signal or an Update.
- **To carry data that's known at start time.** Pass it as a Workflow argument instead of sending a message after the Workflow starts.
- **To reach a Child Workflow from inside a Workflow.** Send Updates from an Activity using a Temporal Client, not from Workflow code.
- **For high fan-in with Updates.** A Workflow Execution can have only a small number of Updates in flight at once, while Signals have no equivalent per-message concurrency cap. See [Limits to plan for](#limits-to-plan-for).
- **To stop a Workflow.** Cancellation and Termination are their own operations. See [Cancellation and Termination](/evaluate/features/cancellation-and-termination).

## Send a message and start a Workflow in one call

Both write types have a variant that starts a Workflow Execution if one isn't already running under the given [Workflow Id](/workflow-execution/workflowid-runid):

- **[Signal-With-Start](/sending-messages#signal-with-start)** Signals a running Workflow Execution, or starts one and immediately Signals it. The operation is atomic, which makes it a way to lazily initialize a Workflow.
- **[Update-With-Start](/sending-messages#update-with-start)** sends an Update and starts the Workflow if needed, in a single round trip, and requires a [Workflow Id conflict policy](/workflow-execution/workflowid-runid#workflow-id-conflict-policy). Unlike Signal-With-Start it is not atomic: the SDK retries the request, but the Update is not guaranteed to succeed. Self-hosted deployments should run [Temporal Server v1.28](https://github.com/temporalio/temporal/releases/tag/v1.28.0) or later.

## Limits to plan for

These figures are for Temporal Cloud. Self-hosted deployments configure their own, starting from the [self-hosted defaults](/self-hosted-guide/defaults).

- A Workflow Execution can receive up to 10,000 Signals. It stops processing Signals after that.
- A Workflow Execution can have at most 10 in-flight Updates, and 2,000 Updates total in its Event History.
- A Workflow Execution can have at most 2,000 incomplete `SignalExternalWorkflowExecution` Commands at a time, which bounds how many Signals it can send to other Workflows at once.
- A single request payload is capped at 2 MB, and any one Event History transaction at 4 MB. Offload larger payloads to [External Storage](/external-storage).

See [System limits](/evaluate/cloud/limits) for the full set.

## Resources

For conceptual depth on the three message types, read the Temporal Encyclopedia or enroll in one of [our courses](https://learn.temporal.io/courses/interacting_with_workflows).

- [Workflow message passing](/encyclopedia/workflow-message-passing): How Signals, Queries, and Updates are delivered and handled, and the guarantees each one carries.
- [Sending messages](/sending-messages): Sending Signals, Queries, and Updates from a Client, the Temporal CLI, or another Workflow.
- [Handling messages](/handling-messages): Writing handlers, validating Updates, and processing a message exactly once.
- [Workflow messaging patterns](/design-patterns/workflow-messaging-patterns): Which pattern to reach for when a caller sends data into a running Workflow and waits on a response.

Or jump straight to the SDK feature guide for implementation details:

- [.NET SDK](/develop/dotnet/workflows/message-passing): Send and handle Signals, Queries, and Updates in C# and .NET.
- [Go SDK](/develop/go/workflows/message-passing): Send and handle Signals, Queries, and Updates in Go.
- [Java SDK](/develop/java/workflows/message-passing): Send and handle Signals, Queries, and Updates in Java and other JVM languages.
- [PHP SDK](/develop/php/workflows/message-passing): Send and handle Signals, Queries, and Updates in PHP.
- [Python SDK](/develop/python/workflows/message-passing): Send and handle Signals, Queries, and Updates in Python.
- [Ruby SDK](/develop/ruby/workflows/message-passing): Send and handle Signals, Queries, and Updates in Ruby.
- [Rust SDK](/develop/rust/workflows/message-passing): Send and handle Signals, Queries, and Updates in Rust.
- [TypeScript SDK](/develop/typescript/workflows/message-passing): Send and handle Signals, Queries, and Updates in TypeScript and JavaScript.
