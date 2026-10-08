# Observability

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Query live and closed Workflow Executions by your own business identifiers, export Prometheus-compatible metrics, and trace Executions across Worker processes.

Temporal records every Workflow Execution as a durable [Event History](/workflow-execution/event#event-history): the inputs, every Activity result, every timer, and every message, in order.
Logs and metrics tell you what a process reported while it was running.
The Event History lets you replay what a Workflow actually did, including one that finished last week.

Around that history, Temporal gives you three things you would otherwise assemble yourself.

## Query Executions by your own identifiers

[Visibility](/visibility) indexes running and closed Workflow Executions so you can list, filter, and count them with a SQL-like [List Filter](/list-filter).
[Custom Search Attributes](/search-attribute#custom-search-attribute) put your own identifiers into that index like, an order Id, customer, region, or tier.
An operator can then answer "which orders are stuck in payment retry" from the [Web UI](/web-ui) or the [CLI](/cli), without querying your application database.

Visibility is a search index that Temporal updates asynchronously, so a List or Count query can return results that are a few seconds stale.
It's built for finding Executions across many, not for reading the authoritative state of one.

## Metrics from both sides of the connection

Temporal emits two independent, Prometheus-compatible metric sets, and you need both:

- **[SDK metrics](/references/sdk-metrics)** come from your Workers and Clients: task slot availability, Schedule-To-Start latency, Activity failures. They tell you whether your Workers are keeping up with the work.
- **Temporal Service metrics** come from the Service: request rates, latencies, and errors. On Temporal Cloud these stream from the [OpenMetrics endpoint](/cloud/metrics/openmetrics) into Datadog, Grafana Cloud, New Relic, or your own Prometheus. Self-hosted deployments scrape [Temporal Service metrics](/references/service-metrics) directly.

Watching one side alone hides the most common failure mode: the Service is accepting and serving work normally while Tasks pile up in a Task Queue because the Workers are under-provisioned.

## Tracing and logs that survive process boundaries

A Workflow Execution can span days, several Activities, and multiple Worker restarts, which is where hand-rolled tracing usually loses the thread.
Temporal SDKs ship OpenTelemetry interceptors that propagate trace context from the Client into the Workflow and out to each Activity, across Worker processes, so one trace covers the whole Execution.

SDKs also expose a logger for Workflow and Activity code that suppresses duplicate output during replay, so a retried or resumed Workflow doesn't repeat every log line it already emitted.

## What you operate

What you run yourself depends on where the Temporal Service runs:

- **Temporal Cloud.** Visibility is enabled by default, and metrics come from the OpenMetrics endpoint. There's no Visibility store to size or upgrade. Both the [number of custom Search Attributes](/evaluate/cloud/limits#number-of-custom-search-attributes) and the [Visibility API rate limit](/evaluate/cloud/limits#visibility-api-rate-limit) are scoped per Namespace.
- **Self-hosted.** You choose and operate the [Visibility store](/self-hosted-guide/visibility): MySQL v8.0.17+ or PostgreSQL v12+ on Temporal Server v1.20 and later, or Elasticsearch and OpenSearch. [Dual Visibility](/dual-visibility) covers migrating between them without downtime.

On both, the Namespace [Retention Period](/temporal-service/temporal-server#retention-period) bounds how long closed Workflow Executions stay queryable. To keep Event Histories past that window, configure [Archival](/temporal-service/archival).

## Resources

- [Visibility](/visibility): How Temporal indexes Workflow Executions, what the index can answer, and when to use something else.
- [Search Attributes](/search-attribute): Default and custom Search Attributes, supported types, and the limits on how many you can define.
- [List Filter](/list-filter): The SQL-like query syntax for filtering Workflow Executions, and the operators it supports.
- [Monitor Temporal Cloud](/cloud/monitor): Set up Cloud and SDK metrics to monitor service and Worker health.
- [Worker alerting](/best-practices/worker-alerting): A recommended alert set for Temporal Workers, with tag filters, thresholds, and triage guidance.
- [Performance bottlenecks](/troubleshooting/performance-bottlenecks): Which metric to read when Workflows are slow, and what each symptom points to.

Or jump straight to the SDK feature guide for implementation details:

- [.NET SDK](/develop/dotnet/platform/observability): Emit metrics, set up tracing, configure logging, and use Search Attributes in C# and .NET.
- [Go SDK](/develop/go/platform/observability): Emit metrics, set up tracing, configure logging, and use Search Attributes in Go.
- [Java SDK](/develop/java/platform/observability): Emit metrics, set up tracing, configure logging, and use Search Attributes in Java and other JVM languages.
- [PHP SDK](/develop/php/platform/observability): Emit metrics, set up tracing, configure logging, and use Search Attributes in PHP.
- [Python SDK](/develop/python/platform/observability): Emit metrics, set up tracing, configure logging, and use Search Attributes in Python.
- [Ruby SDK](/develop/ruby/platform/observability): Emit metrics, set up tracing, configure logging, and use Search Attributes in Ruby.
- [TypeScript SDK](/develop/typescript/platform/observability): Emit metrics, set up tracing, configure logging, and use Search Attributes in TypeScript and JavaScript.
