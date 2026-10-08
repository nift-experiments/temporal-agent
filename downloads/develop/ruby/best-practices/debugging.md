# Debugging - Ruby SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Debug Workflows in development and production environments using Temporal Ruby SDK. Use logging, debugger, CLI, replay, tracing, and more.

## Debugging 

This page shows how to do the following:

- [Debug in a development environment](#debug-in-a-development-environment)
- [Debug in a production environment](#debug-in-a-production-environment)

## Debug in a development environment 

In developing Workflows, you can use the normal development tools of logging and a debugger to see what’s happening in your Workflow.

In addition to the normal development tools of logging and a debugger, you can also see what’s happening in your Workflow by using the [Web UI](/web-ui) or [Temporal CLI](/cli).
The Web UI provides insight into your Workflows, making it easier to identify issues and monitor the state of your Workflows in real time.

## Debug in a production environment 

For production Workflows, debugging options include:

- [Web UI](/web-ui)
- [Temporal CLI](/cli)
- [Replay](/develop/ruby/best-practices/testing-suite#replay-test)
- [Tracing](/develop/ruby/platform/observability#tracing)
- [Logging](/develop/ruby/platform/observability#logging)

You can analyze Worker performance using:

- [Metrics](/develop/ruby/platform/observability#metrics)
- [Worker performance guide](/develop/worker-performance)

To monitor Server performance:

- Use [Cloud metrics](/cloud/metrics/openmetrics) if you're on Temporal Cloud
- Or [self-hosted Server metrics](/self-hosted-guide/production-checklist#scaling-and-metrics) if running your own deployment
