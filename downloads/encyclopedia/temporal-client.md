# Temporal Client

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> A Temporal Client acts as the bridge for communication between your applications and the Temporal Service, enabling you to start Workflow Executions, send Signals and Queries, and retrieve results.

A Temporal Client allows you to communicate with the [Temporal Service](/temporal-service).

The most common operations that a Temporal Client allows you to perform are the following:
- Start a Workflow Execution
- Get the result of Workflow Execution
- List Workflow Executions
- Query a Workflow Execution
- Signal a Workflow Execution
- Start and manage [Standalone Activities](/standalone-activity) directly, without involving a Workflow
- Start a [Standalone Nexus Operation](/standalone-nexus-operation) directly, without using a caller Workflow

A Standalone Activity is a top-level [Activity Execution](/activity-execution) started directly by a Client, without using a Workflow.
A Standalone Nexus Operation is a top-level [Nexus Operation Execution](/nexus/operations) started directly by a Client, without using a caller Workflow.

## SDK guides 

- [Temporal Client - Go](/develop/go/client/temporal-client)
- [Temporal Client - Java](/develop/java/client/temporal-client)
- [Temporal Client - PHP](/develop/php/client/temporal-client)
- [Temporal Client - Python](/develop/python/client/temporal-client)
- [Temporal Client - Ruby](/develop/ruby/client/temporal-client)
- [Temporal Client - Rust](/develop/rust/client/temporal-client)
- [Temporal Client - TypeScript](/develop/typescript/client/temporal-client)
- [Temporal Client - .NET](/develop/dotnet/client/temporal-client)
