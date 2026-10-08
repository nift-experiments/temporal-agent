# Temporal Platform references

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

- [API reference](/references/api-reference): API documentation for the Temporal SDKs, Temporal Server, Temporal CLI, and Temporal Cloud.
- [Temporal Service metrics](/references/service-metrics): Metrics a self-hosted Temporal Service emits, covering request rates, latencies, errors, and Nexus Operations.
- [SDK metrics](/references/sdk-metrics): Metrics emitted by Temporal Clients and Workers, with each metric's type and SDK availability.
- [Environment configuration](/references/client-environment-configuration): Environment variables and TOML keys that configure a Temporal Client or the Temporal CLI.
- [Temporal Service configuration](/references/service-configuration): The development.yaml settings for global options, persistence, service roles, and archival.
- [Dynamic configuration](/references/dynamic-configuration): Keys that tune rate limits, size limits, and retry defaults without restarting the Temporal Service.
- [Temporal Web UI configuration](/references/web-ui-configuration): YAML keys for the Web UI Server, covering Frontend connectivity, Workflow actions, auth, TLS, CORS, and Codec Server.
- [Web UI environment variables](/references/web-ui-environment-variables): Environment variables that configure the Temporal Web UI in Docker, such as TEMPORAL_ADDRESS and TLS.
- [Server options](/references/server-options): ServerOption functions for embedding the Temporal Server in a Go application, including auth, TLS, and metrics.
- [Commands](/references/commands): Every Command a Worker can issue after completing a Workflow Task, and its corresponding Event.
- [Errors](/references/workflow-task-errors): Workflow Task failure causes and Resource Exhausted causes, with how to resolve each one.
- [Events](/references/events): Every Event that can appear in a Workflow Execution's Event History.
- [Failures](/references/failures): Failure types for Workflows, Activities, and Nexus Operations, and their SDK classes or exceptions.
- [Temporal Cloud operations](/references/operation-list): Operations Temporal Cloud rate-limits per Namespace, with each operation's priority and throttling effect.
- [Glossary](/glossary): Definitions of terms used across the Temporal Platform.
