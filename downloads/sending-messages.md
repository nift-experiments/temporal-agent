# Sending Signals, Queries, & Updates

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Signals, Queries, and Updates facilitate interactions with Workflow Executions.

This section will help you write clients that send messages to Workflows which includes:

- [Sending Signals](#sending-signals)
- [Sending Updates](#sending-updates)
- [Sending Queries](#sending-queries)

### Sending Signals 

You can send Signals from any Temporal Client, the Temporal CLI, or you can Signal one Workflow to another.

You can also Signal-With-Start to lazily initialize a Workflow while sending a Signal.

#### Send a Signal from a Temporal Client or the CLI

**Related:**

- [Send a Signal using the Temporal CLI](/cli/command-reference/workflow#signal)
- [Send Signals with the Go SDK](/develop/go/workflows/message-passing#send-signal-from-client)
- [Send Signals with the Java SDK](/develop/java/workflows/message-passing#send-signal-from-client)
- [Send Signals with the PHP SDK](/develop/php/workflows/message-passing#send-signal-from-client)
- [Send Signals with the Python SDK](/develop/python/workflows/message-passing#send-signal-from-client)
- [Send Signals with the TypeScript SDK](/develop/typescript/workflows/message-passing#send-signal-from-client)
- [Send Signals with the .NET SDK](/develop/dotnet/workflows/message-passing#send-signal-from-client)
- [Send Signals with the Ruby SDK](/develop/ruby/workflows/message-passing#signals)
- [Send Signals with the Rust SDK](/develop/rust/workflows/message-passing#signals)

#### Send a Signal from one Workflow to another

**Related:**

- [Send Signals from Workflows with the Go SDK](/develop/go/workflows/message-passing#send-signal-from-workflow)
- [Send Signals from Workflows with the Java SDK](/develop/java/workflows/message-passing#send-signal-from-workflow)
- [Send Signals from Workflows with the PHP SDK](/develop/php/workflows/message-passing#send-signal-from-workflow)
- [Send Signals from Workflows with the Python SDK](/develop/python/workflows/message-passing#send-signal-from-workflow)
- [Send Signals from Workflows with the TypeScript SDK](/develop/typescript/workflows/message-passing#send-signal-from-workflow)
- [Send Signals from Workflows with the .NET SDK](/develop/dotnet/workflows/message-passing#send-signal-from-workflow)
- [Send Signals from Workflows with the Ruby SDK](/develop/ruby/workflows/message-passing#send-signal-from-workflow)
- [Send Signals from Workflows with the Rust SDK](/develop/rust/workflows/message-passing#from-a-workflow)

#### Signal-With-Start 

Signal-With-Start is a great tool for lazily initializing Workflows. When you send this operation, if there is a running Workflow Execution with the given Workflow Id, it will be Signaled. Otherwise, a new Workflow Execution starts and is immediately sent the Signal.

**Related:**

- [Signal-With-Start using the Go SDK](/develop/go/workflows/message-passing#signal-with-start)
- [Signal-With-Start using the Java SDK](/develop/java/workflows/message-passing#signal-with-start)
- [Signal-With-Start using the PHP SDK](/develop/php/workflows/message-passing#signal-with-start)
- [Signal-With-Start using the Python SDK](/develop/python/workflows/message-passing#signal-with-start)
- [Signal-With-Start using the TypeScript SDK](/develop/typescript/workflows/message-passing#signal-with-start)
- [Signal-With-Start using the .NET SDK](/develop/dotnet/workflows/message-passing#signal-with-start)
- [Signal-With-Start using the Ruby SDK](/develop/ruby/workflows/message-passing#signal-with-start)
- [Signal-With-Start using the Rust SDK](/develop/rust/workflows/message-passing#signal-with-start)

### Sending Updates 

> **📝 Note:**
>
> To use the Workflow Update feature in versions prior to v1.25.0, it must be manually enabled.
>
> Set the [frontend.enableUpdateWorkflowExecution](https://github.com/temporalio/temporal/blob/main/common/dynamicconfig/constants.go) and [frontend.enableUpdateWorkflowExecutionAsyncAccepted](https://github.com/temporalio/temporal/blob/main/common/dynamicconfig/constants.go) dynamic config values to `true`.
>
> For example, with the Temporal CLI, run these commands:
>
> ```command
> temporal server start-dev --dynamic-config-value frontend.enableUpdateWorkflowExecution=true
> temporal server start-dev --dynamic-config-value frontend.enableUpdateWorkflowExecutionAsyncAccepted=true
> ```
>

Updates can be sent from a Temporal Client or the Temporal CLI to a Workflow Execution. This call is synchronous and will call into the corresponding Update handler. If you’d rather make an asynchronous request, you should use Signals.

In most languages (except Go), you may call `executeUpdate` to complete an Update and get its result.

Alternatively, to start an Update, you may call `startUpdate` and pass in the Workflow Update Stage as an argument. You have two choices on what to await:

- Accepted - wait until the Worker is contacted, which ensures that the Update is persisted. See [Update Validators](/handling-messages#update-validators) for more information.
- Completed - wait until the handler finishes and returns a result. (This is equivalent to `executeUpdate`.)

The start call will give you a handle you can use to track the Update, determine whether it was Accepted, and ultimately get its result or an error.

If you want to send an Update to another Workflow such as a Child Workflow from within a Workflow, you should do so within an Activity and use the Temporal Client as normal.

There are limits on the total number of Updates that may occur during a Workflow Execution run, and also on the number of concurrent in-progress Updates that a Workflow Execution may have.
Use [Update Validators](/handling-messages#update-validators) and [Update IDs](/handling-messages#exactly-once-message-processing) to stay within the system limits in both [Cloud](/evaluate/cloud/limits#per-workflow-execution-update-limits) and [Self-Hosted](/self-hosted-guide/defaults).

**Related:**

- [Send Updates in Go](/develop/go/workflows/message-passing#send-update-from-client)
- [Send Updates in Java](/develop/java/workflows/message-passing#send-update-from-client)
- [Send Updates in PHP](/develop/php/workflows/message-passing#send-update-from-client)
- [Send Updates in Python](/develop/python/workflows/message-passing#send-update-from-client)
- [Send Updates in TypeScript](/develop/typescript/workflows/message-passing#send-update-from-client)
- [Send Updates in .NET](/develop/dotnet/workflows/message-passing#send-update-from-client)
- [Send Updates in Ruby](/develop/ruby/workflows/message-passing#send-update-from-client)
- [Send Updates in Rust](/develop/rust/workflows/message-passing#send-update-from-client)

#### Update-With-Start 

> **💡 Tip:**
>
> For open source server users, Temporal Server version [Temporal Server version 1.28](https://github.com/temporalio/temporal/releases/tag/v1.28.0) is recommended.
>

Update-with-Start sends an Update request, starting a Workflow if necessary.
A [`WorkflowIDConflictPolicy`](/workflow-execution/workflowid-runid#workflow-id-conflict-policy) must be specified.
Workflow ID and Update ID can be used as idempotency keys as follows:

- If the Workflow exists and you provided an Update ID, and the Update exists in the latest Workflow Run, then Update-With-Start attaches to the existing Update (regardless of `WorkflowIDConflictPolicy`)
  - If the Workflow is closed, it attaches only if the Update has completed.
- Otherwise it uses [`WorkflowIDConflictPolicy`](/workflow-execution/workflowid-runid#workflow-id-conflict-policy) and [`WorkflowIDReusePolicy`](/workflow-execution/workflowid-runid#workflow-id-reuse-policy) as usual to determine whether to start a Workflow, and then starts a new Update immediately.

Update-With-Start is great for latency-sensitive use cases:

- **Lazy Initialization** -
  Instead of making separate Start Workflow and Update Workflow calls, Update-With-Start allows you to send them together in a single roundtrip.
  For example, a shopping cart can be modeled using Update-With-Start.
  Updates let you add and remove items from the cart.
  Update-With-Start lets the customer start shopping, whether the cart already exists or they've just started shopping.
  It ensures the cart, modeled by a Workflow Execution, exists before applying any Update that changes the state of items within the cart.
  Set your `WorkflowIDConflictPolicy` to `USE_EXISTING` for this pattern.
- **Early Return** -
  Using Update-With-Start you can begin a new Workflow Execution and synchronously receive a response, while the Workflow Execution continues to run to completion.
  For example, you might model a payment process using Update-With-Start.
  This allows you to send the payment validation results back to the client synchronously, while the transaction Workflow continues in the background.
  Set your `WorkflowIDConflictPolicy` to `FAIL` and use a unique Update ID for this pattern if you want to assert it does not reuse an existing Workflow.

> **⚠️ Caution:**
>
> Unlike Signal-with-Start - Update-With-Start is _not_ atomic.
> If the Update can't be delivered, for example, because there's no running Worker available, a new Workflow Execution will still start.
> The SDKs will retry the Update-With-Start request, but there is no guarantee that the Update will succeed.
>

**Related:**

- [Update-With-Start with the Go SDK](/develop/go/workflows/message-passing#update-with-start)
- [Update-With-Start with the Java SDK](/develop/java/workflows/message-passing#update-with-start)
- [Update-With-Start with the PHP SDK](/develop/php/workflows/message-passing#update-with-start)
- [Update-With-Start with the Python SDK](/develop/python/workflows/message-passing#update-with-start)
- [Update-With-Start with the TypeScript SDK](/develop/typescript/workflows/message-passing#update-with-start)
- [Update-With-Start with the .NET SDK](/develop/dotnet/workflows/message-passing#update-with-start)
- [Update-With-Start with the Ruby SDK](/develop/ruby/workflows/message-passing#update-with-start)
- [Update-With-Start with the Rust SDK](/develop/rust/workflows/message-passing#update-with-start)

### Sending Queries 

Queries can be sent from a Temporal Client or the Temporal CLI to a Workflow Execution--even if this Workflow has Completed. This call is synchronous and will call into the corresponding Query handler.
You can also send a built-in "Stack Trace Query" for debugging.

**Related:**

- [Send a Query using the Temporal CLI](/cli/command-reference/workflow#query)
- [Send a Query with the Go SDK](/develop/go/workflows/message-passing#send-query)
- [Send a Query with the Java SDK](/develop/java/workflows/message-passing#send-query)
- [Send a Query with the PHP SDK](/develop/php/workflows/message-passing#send-query)
- [Send a Query with the Python SDK](/develop/python/workflows/message-passing#send-query)
- [Send a Query with the TypeScript SDK](/develop/typescript/workflows/message-passing#send-query)
- [Send a Query with the .NET SDK](/develop/dotnet/workflows/message-passing#send-query)
- [Send a Query with the Ruby SDK](/develop/ruby/workflows/message-passing#send-query)
- [Send a Query with the Rust SDK](/develop/rust/workflows/message-passing#send-query)

#### Stack trace Query 

In many SDKs, the Temporal Client exposes a predefined `__stack_trace` Query that returns the call stack of all the threads owned by that Workflow Execution.
This is a great way to troubleshoot a Workflow Execution in production.
For example, if a Workflow Execution has been stuck at a state for longer than an expected period of time, you can send a `__stack_trace` Query to return the current call stack.
The `__stack_trace` Query name does not require special handling in your Workflow code.

> **📝 Note:**
>
> Stack Trace Queries are available only for running Workflow Executions.
>
