# Temporal Nexus

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Nexus connects Temporal Applications across Namespace, team, and region boundaries.

**[Temporal Nexus](/nexus)** connects Temporal Applications across isolated Namespaces, regions, and clouds.
Each team keeps its own Namespace, Workers, and deployment lifecycle, and exposes a service contract that other teams call with the same durability, observability, and access control as the rest of Temporal.
Callers get a durable, atomic handoff instead of a network call they have to make reliable themselves.
Watch the [Nexus overview](https://www.youtube.com/watch?v=tJ1OwSFokOg&t=117s) for a walkthrough.

## When to use Nexus 

Use Nexus when a business process crosses a boundary you put in place on purpose:

- **Separate teams or domains** - Each team owns its Namespace, Workers, and release cadence, and shares capability through a service contract instead of shared internals.
- **Security and fault isolation** - Grant access to a Nexus Endpoint rather than to a whole Namespace. A misbehaving Worker affects its own Namespace, not its callers.
- **Multiple regions or clouds** - Temporal Cloud routes Nexus requests across Namespaces in AWS and GCP over a global mTLS-secured mesh.
- **Compliance and data residency** - Isolated Namespaces keep sensitive data (PCI, PII) under their own encryption, access controls, and audit trail.
- **Shared internal services** - A registered Endpoint is discoverable, so teams can adopt an existing service instead of rebuilding it.

Use the following decision tree to help determine if Nexus is right for your use case:

## When not to use Nexus

- **One team in one Namespace** - [Child Workflows](/evaluate/features/child-workflows) and [Activities](/activities) already compose work inside a Namespace, and an Endpoint is one more thing to register and operate. If you expect to split into separate Namespaces later, Nexus is still worth adopting now. It separates the contract from the implementation, so the migration is mostly configuration.
- **Synchronous calls that can't finish fast** - A [Synchronous Operation](/nexus/operations#operation-lifecycle) has to complete within the 10-second handler deadline. Anything slower or less predictable belongs in an Asynchronous Operation.

### Nexus, Child Workflows, or Activities?

Connecting Namespaces without Nexus is possible, but each option costs you something:

- **Child Workflows** are limited to the same Namespace. Using them across Namespaces leaks implementation details because the caller has to manage the target Namespace, Task Queue, and Workflow options.
- **Activity wrappers** need a per-target mTLS client, so you take on configuration and certificate management. They tend to be over-permissioned, have no built-in cross-Namespace observability, and need error-prone boilerplate for asynchronous results.
- **A gateway service** is not durable, is hard to debug across services, and is one more service to run and patch.

Nexus replaces all three with a contract between caller and handler, less code, and first-class observability.

## Limits to plan for

- Nexus is available in the Go, Java, Python, TypeScript, .NET, and Rust SDKs. PHP and Ruby don't support it.
- A Synchronous Operation must complete within a [10-second handler deadline](/evaluate/cloud/limits#nexus-operation-request-timeout). An Asynchronous Operation has a [maximum ScheduleToClose duration of 60 days](/evaluate/cloud/limits#nexus-operation-duration-limits).
- A Workflow Execution can have 30 in-flight Nexus Operations at a time, and a handler Workflow accepts 2,000 callbacks, which sets how many callers can attach to it.
- Temporal Cloud defaults to 100 Nexus Endpoints per Account and 1,000 caller Namespaces per Endpoint. Support can raise both.
- The global Nexus Registry, runtime access controls, audit logging, and cross-region routing are Temporal Cloud features. On a self-hosted Temporal Service, you enable the HTTP API and Nexus dynamic configuration yourself, and external Nexus calls are still experimental.

See [Nexus limits](/cloud/nexus/limits) for the full set.

## How teams use Nexus

- **Duolingo** uses Nexus for self-service infrastructure ([case study](https://temporal.io/resources/case-studies/duolingo-temporal-nexus) | [webinar](https://www.youtube.com/watch?v=tJ1OwSFokOg&t=524s)).
- **Netflix** uses it to orchestrate infrastructure across teams ([Replay talk](https://www.youtube.com/watch?v=izR9dQ_eIe4&t=470s) | [webinar](https://www.youtube.com/watch?v=At1FfqGQiu0&t=1295s)).
- **Miro** uses it for cross-region data migration ([Replay talk](https://youtu.be/YLmFR-IAC3M?feature=shared&t=1488)).

For more architectural patterns built on Temporal, see [use cases and design patterns](/evaluate/use-cases-design-patterns).

## Resources 

Join the [#nexus](https://temporalio.slack.com/archives/C07LQN0JK9B) channel in [Temporal Slack](https://t.mp/slack) to connect with the Nexus community.

Read the Temporal Encyclopedia for conceptual depth:

- [How Nexus works](/nexus)
- [Nexus Security](/nexus/security)
- [Nexus Patterns](/nexus/patterns)

Or jump straight to an SDK quick start:

- [.NET SDK](/develop/dotnet/nexus): Define, register, and call Nexus Services in C# and .NET.
- [Go SDK](/develop/go/nexus): Define, register, and call Nexus Services in Go.
- [Java SDK](/develop/java/nexus): Define, register, and call Nexus Services in Java and other JVM languages.
- [Python SDK](/develop/python/nexus): Define, register, and call Nexus Services in Python.
- [Rust SDK](/develop/rust/nexus): Define, register, and call Nexus Services in Rust.
- [TypeScript SDK](/develop/typescript/nexus): Define, register, and call Nexus Services in TypeScript and JavaScript.

Then set up Nexus on the deployment you run:

- [Temporal Cloud](/cloud/nexus): Global Nexus Registry, runtime access controls, audit logging, and multi-region connectivity.
- [Self-hosted deployment](/production-deployment/self-hosted-guide/nexus): Enable the HTTP API and Nexus dynamic configuration on a self-hosted Temporal Service.
