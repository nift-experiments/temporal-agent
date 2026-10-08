# Nexus services

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Nexus Services are named collections of arbitrary-duration Nexus Operations that provide a microservice contract suitable for sharing across team boundaries.

[Nexus Services](/glossary#nexus-service) are named collections of [Nexus Operations](/nexus/operations) that provide a contract for sharing across team boundaries.
A [Nexus Endpoint](/nexus/endpoints) exposes Services for callers to use.

Services are registered in a Worker that polls the Endpoint's target Task Queue.
Multiple Services can run in the same Worker.
Services typically run alongside the Workflows they abstract, or in a dedicated router Worker using the [router-queue pattern](/nexus/patterns#router-queue-pattern).

Callers reference a Service by name when executing a Nexus Operation.

You can hand-write a Service definition, or generate it from a schema file with [NexGen](/nexus/nexgen), which emits the definition along with typed models and runtime validators for each language.
