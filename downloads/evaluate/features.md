# Temporal development and production features

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Leverage a Temporal SDK to develop robust applications featuring Workflows, Activities, Workers, testing suites, Temporal Clients, Scheduled Workflows, and advanced observability tools.

Through a Temporal SDK, Temporal provides a wide range of features that enable developers to build applications that serve a wide range of use cases.

- [Core primitives](/evaluate/features/core-primitives): Develop and run your application with Workflows, Activities, and Workers.
- [Timeouts and retries](/evaluate/features/timeouts-and-retries): Detect failures with timeouts and configure automatic retries to mitigate them.
- [Child Workflows](/evaluate/features/child-workflows): Break up business processes by data streams, team ownership, or other organization factors.
- [Temporal Nexus](/evaluate/features/nexus): Connect Temporal Applications across (and within) isolated Namespaces for improved modularity, security, debugging, and fault isolation. Nexus supports cross-team, cross-domain, and multi-region use cases.
- [Workflow message passing](/evaluate/features/workflow-message-passing): Build responsive applications that react to events at runtime and enable data retrieval from ongoing Workflows.
- [Cancellation and termination](/evaluate/features/cancellation-and-termination): Cancel or terminate a business process (Workflow) that is already in progress and compensate for any steps already taken.
- [Observability](/evaluate/features/observability): List business processes, view their state, and set up dashboards with metrics.
- [Data encryption](/evaluate/features/data-encryption): Transform data and protect the privacy of the users of your application.
- [Scheduled Workflows](/evaluate/features/schedules): Start a business process at a specific time or on a given time interval.
- [Job queues](/evaluate/features/job-queue): Run any Activity as a durable background job, without the overhead of a Workflow.

Temporal also provides these features:

- **Runtime safeguards**: Prevent avoidable errors and issues from executing during runtime.
- **Versioning**: Support multiple versions of your business logic for long-running business processes.

For detailed information on Temporal feature release stages and criteria, see this [Product Release Stages Guide](/evaluate/product-release-stages).
