# Context Propagation

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Pass custom key-value data across Workflow, Activity, and Child Workflow boundaries using Temporal headers.

Context propagation lets you pass custom key-value data from a Client to Workflows, and from Workflows to Activities and Child Workflows, without threading values through every function signature.

Common use cases:

- Propagating distributed tracing IDs (for example, OpenTelemetry trace context)
- Passing tenant IDs for multi-tenant applications
- Forwarding auth tokens or request-scoped metadata

Each SDK provides a **context propagator** interface you implement to control which values are injected and extracted. You register propagators on the Client, and the SDK calls them automatically at every boundary.

## Implementing context propagation

Here are SDK-specific guides:

- [Go](/develop/go/best-practices/context-propagation)
