# Child Workflows

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Child Workflows give part of a business process its own Event History, Workers, and lifecycle, with the limits and trade-offs versus one Workflow.

A **[Child Workflow](/child-workflows)** is a [Workflow Execution](/workflow-execution) started by another Workflow.
The child gets its own [Event History](/workflow-execution/event#event-history), can run on a separate set of [Workers](/workers#worker), and has its own lifecycle.
That lets a Parent Workflow hand off part of a business process instead of running every step itself.

## When to use a Child Workflow

- **[Create a separate service](/child-workflows#create-a-separate-service)**: because a child can be processed by a completely separate set of Workers than its parent, it can act as its own service. Parent and child share no local state and communicate only through asynchronous [Signals](/sending-messages#sending-signals). To compose across Namespace boundaries, or between teams that own separate Temporal Applications, use [Temporal Nexus](/evaluate/features/nexus) instead.
- **[Partition a large workload](/child-workflows#partition-problems-into-smaller-chunks)**: each child has its own Event History, so splitting work across children raises the ceiling on how many steps one business process can take.
- **[Represent a single resource](/child-workflows#represent-a-single-resource)**: map one child to one resource and use its [Workflow Id](/workflow-execution/workflowid-runid) to guarantee uniqueness, which serializes every operation on that resource.
- **[Run periodic logic](/child-workflows#periodic-logic-execution)**: a child can call [Continue-As-New](/workflow-execution/continue-as-new) as many times as it needs and then complete. From the parent's point of view it was a single invocation, so the periodic work never fills the parent's Event History.

## When not to use a Child Workflow

- **For code organization alone.** Use the object-oriented structure and other organizing techniques your language already offers.
- **When the workload has a bounded size.** Start from a single Workflow Definition when you can put a ceiling on the number of Activity Executions and Signals. One Workflow is simpler to reason about than several communicating asynchronously.
- **When Activities would do.** Child Workflow Executions record more Events overall than Activities do, and each Event in an Event History costs compute. Start with a single Workflow that calls Activities, and add Child Workflows once you have a clear reason.

### Child Workflow or Activity?

Both are started from a Workflow, which makes the choice easy to get wrong.
A Child Workflow has access to all Workflow APIs but is subject to the same [deterministic constraints](/workflow-definition#deterministic-constraints) as any other Workflow.
An Activity has the inverse trade-off: no access to Workflow APIs, but no determinism constraints either.
See [Child Workflow versus an Activity](/child-workflows#child-workflow-versus-an-activity) for the full comparison.

## Limits to plan for

These numbers shape how you partition a business process:

- A Workflow Execution's Event History is capped at 51,200 Events or 50 MB, with a warning at 10,240 Events or 10 MB.
- A Workflow Execution can have at most 2,000 incomplete Child Workflows at a time, by default.
- A Parent Workflow's Event History records Events for each child's status, so a single parent should not spawn more than about 1,000 Child Workflow Executions.
- Those figures compound: one parent running 1,000 children that each run 1,000 Activity Executions reaches 1,000,000 Activity Executions, far past what one Workflow Execution can hold.

See [Workflow Execution limits](/workflow-execution/limits) for the full set.

## Parent Close Policy

Every Child Workflow Execution carries a [Parent Close Policy](/parent-close-policy) that decides what happens to the child when its parent reaches a Closed status:

- **Terminate** (the default): the child is forcefully Terminated.
- **Request Cancel**: a Cancellation request is sent to the child.
- **Abandon**: the child keeps running.

Each child can set its own policy, so a parent can terminate some children and leave others running.

## Resources

Read the Temporal Encyclopedia for conceptual depth:

- [Child Workflows](/child-workflows)
- [Parent Close Policy](/parent-close-policy)

Or jump straight to the SDK feature guide for implementation details:

- [.NET SDK](/develop/dotnet/workflows/child-workflows): Start and manage Child Workflows in C# and .NET.
- [Go SDK](/develop/go/workflows/child-workflows): Start and manage Child Workflows in Go.
- [Java SDK](/develop/java/workflows/child-workflows): Start and manage Child Workflows in Java and other JVM languages.
- [PHP SDK](/develop/php/workflows/child-workflows): Start and manage Child Workflows in PHP.
- [Python SDK](/develop/python/workflows/child-workflows): Start and manage Child Workflows in Python.
- [Ruby SDK](/develop/ruby/workflows/child-workflows): Start and manage Child Workflows in Ruby.
- [Rust SDK](/develop/rust/workflows/child-workflows): Start and manage Child Workflows in Rust.
- [TypeScript SDK](/develop/typescript/workflows/child-workflows): Start and manage Child Workflows in TypeScript and JavaScript.
