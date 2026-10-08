# Interceptors

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Add cross-cutting behavior like observability, authorization, and header manipulation before and after SDK operations.

Interceptors let you add cross-cutting behavior before and after SDK operations such as starting a Workflow, executing an Activity, or handling a Signal. They work like middleware: each interceptor wraps the next, forming a chain that executes around the underlying operation.

Common use cases:

- Observability (logging, metrics, tracing)
- Authorization and authentication checks
- Header manipulation (propagating metadata)
- Input/output validation

## Implementing Interceptors

Here are SDK-specific guides:

- [Go](/develop/go/workers/interceptors)
- [Java](/develop/java/workers/interceptors)
- [Python](/develop/python/workers/interceptors)
- [TypeScript](/develop/typescript/workers/interceptors)
- [.NET](/develop/dotnet/workers/interceptors)
