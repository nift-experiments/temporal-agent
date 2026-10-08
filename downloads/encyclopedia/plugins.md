# Plugins

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Bundle interceptors, context propagators, data converters, and built-in definitions into reusable packages.

A Plugin bundles multiple extensibility primitives - interceptors, context propagators, data converters, and built-in Workflow/Activity/Nexus definitions - into a single reusable package. Plugins let platform teams and library authors ship ready-made functionality that application developers can adopt with a single registration call.

Common use cases:

- AI Agent SDKs (for example, OpenAI Agents, Pydantic AI, LangGraph)
- Observability packages (tracing, logging, metrics)
- Encryption or compliance middleware
- Shared infrastructure integrations (messaging, payments, LLM calls)

## Implementing Plugins

See the [Plugins guide](/develop/plugins-guide) for how to build and use plugins across all supported SDKs.
