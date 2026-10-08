# Dynamic handler

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Dynamic Handlers can serve as fallback mechanisms for handling Workflows, Activities, Signals, Queries, or Updates that aren't registered by name.

This page discusses [Dynamic Handler](#dynamic-handler).

## What is a Dynamic Handler? 

Temporal supports Dynamic Workflows, Activities, Signals, and Queries.

> **📝 Note:**
>
> Currently, the Temporal SDKs that support Dynamic Handlers are:
>
> - [Java](/develop/java/workflows/message-passing#dynamic-handler)
> - [Python](/develop/python/workflows/message-passing#dynamic-handler)
> - [.NET](/develop/dotnet/workflows/message-passing#dynamic-handler)
> - [Go](/develop/go/workflows/dynamic-workflow)
> - [Ruby](/develop/ruby/workflows/message-passing#dynamic-handler)
>

These are unnamed handlers that are invoked if no other statically defined handler with the given name exists.

Dynamic Handlers provide flexibility to handle cases where the names of Workflows, Activities, Signals, or Queries aren't known at run time.

> **⚠️ Caution:**
>
> Dynamic Handlers should be used judiciously as a fallback mechanism rather than the primary approach.
> Overusing them can lead to maintainability and debugging issues down the line.
>
> Instead, Workflows, Activities, Signals, and Queries should be defined statically whenever possible, with clear names that indicate their purpose.
> Use static definitions as the primary way of structuring your Workflows.
>
> Reserve Dynamic Handlers for cases where the handler names are not known at compile time and need to be looked up dynamically at runtime.
> They are meant to handle edge cases and act as a catch-all, not as the main way of invoking logic.
>
