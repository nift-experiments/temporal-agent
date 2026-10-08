# Debugging - Python SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Debug Workflows in development and production environments using the Temporal Python SDK, Web UI, Temporal CLI, replay, tracing, logging, and performance metrics.

This page shows how to do the following:

- [Debug in a development environment](#debug-in-a-development-environment)
- [Debug in a production environment](#debug-in-a-production-environment)

### Debug in a development environment 

When developing Workflows, you can use the normal development tools of logging and a debugger to see what’s happening in your Workflow.
In addition to the normal development tools of logging and a debugger, you can also see what’s happening in your Workflow by using the [Web UI](/web-ui) or [Temporal CLI](/cli).

### Debug in a production environment 

You can debug production Workflows using:

- [Web UI](/web-ui)
- [Temporal CLI](/cli)
- [Replay](/develop/python/best-practices/testing-suite#replay)
- [Tracing](/develop/python/platform/observability#tracing)
- [Logging](/develop/python/platform/observability#logging)

You can debug and tune Worker performance with metrics and the [Worker performance guide](/develop/worker-performance).
For more information, see [Observability ▶️ Metrics](/develop/python/platform/observability#metrics) for setting up SDK metrics.

Debug Server performance with [Cloud metrics](/cloud/metrics/openmetrics) or [self-hosted Server metrics](/self-hosted-guide/production-checklist#scaling-and-metrics).
