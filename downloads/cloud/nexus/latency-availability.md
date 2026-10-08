# Latency and Availability - Temporal Nexus

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Learn about Nexus latency and availability

Nexus latency and availability in Temporal Cloud:

- **SLOs and the SLA** - Nexus operations (for example, `RespondWorkflowTaskCompleted`, `PollNexusTaskQueue`, `RespondNexusTaskCompleted`, and `RespondNexusTaskFailed`) have the same [latency SLOs](/cloud/slo#latency) as other Worker requests in both caller and handler Namespaces. For contractual coverage, see the [Temporal Cloud SLA](https://temporal.io/sla).
- **[Nexus metrics](/nexus/metrics)** - SDK and Cloud latency metrics for monitoring Nexus performance.
- **Cross-Namespace connectivity** - Traffic routes through a global mTLS-secured Envoy mesh. Same-region Namespaces have low latency; cross-region latency varies by provider. See [secure connectivity](/nexus/security#secure-connectivity).
