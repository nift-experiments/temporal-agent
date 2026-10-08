# Core primitives

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Discover Temporal's Workflow, Activity, and Worker framework; orchestrate steps, encapsulate business logic, and execute code efficiently using the Temporal SDK in your favorite language.

[Workflows](/workflows), [Activities](/activities), [Standalone Activities](/standalone-activity), and [Workers](/workers) form the core parts of a Temporal Application.

**[Workflows](/workflows)**: A Workflow defines the overall flow of the application.
You write it in your programming language of choice using the Temporal SDK.
Conceptually, a Workflow specifies a sequence of steps and orchestrates the execution of Activities.

**[Activities](/activities)**: An Activity is a method or function that encapsulates business logic prone to failure (for example, calling a service that may go down).
The system can automatically retry these Activities upon some failures.
Activities perform a single, well-defined action, such as calling another service, transcoding a media file, or sending an email message.

**[Standalone Activities](/standalone-activity)**: A Standalone Activity is a top-level [Activity Execution](/activity-execution) started directly by a [Client](/encyclopedia/temporal-client), without using a Workflow. Use a [Workflow](/workflows) to orchestrate multiple Activities, but if you just need to execute a single Activity, use a [Standalone Activity](/standalone-activity). Standalone Activities are Temporal's job queue.

**[Workers](/workers)**: A Worker executes your Workflow and Activity code.

## Resources

Follow one of our [tutorials](https://learn.temporal.io/getting_started/) to develop Workflows and Activities and run them in Worker Processes, or enroll in one of [our courses](https://learn.temporal.io/courses/).

Read the Temporal Encyclopedia pages for each core primitive:

- [Temporal Workflows](/workflows)
- [Temporal Activities](/activities)
- [Temporal Standalone Activities](/standalone-activity)
- [Temporal Workers](/workers)

Or jump straight to a Temporal SDK develop docs:

- [.NET SDK](/develop/dotnet): Write Workflows, Activities, and Workers in C# and .NET.
- [Go SDK](/develop/go): Write Workflows, Activities, and Workers in Go.
- [Java SDK](/develop/java): Write Workflows, Activities, and Workers in Java and other JVM languages.
- [PHP SDK](/develop/php): Write Workflows, Activities, and Workers in PHP.
- [Python SDK](/develop/python): Write Workflows, Activities, and Workers in Python.
- [Ruby SDK](/develop/ruby): Write Workflows, Activities, and Workers in Ruby.
- [Rust SDK](/develop/rust): Write Workflows, Activities, and Workers in Rust.
- [TypeScript SDK](/develop/typescript): Write Workflows, Activities, and Workers in TypeScript and JavaScript.
