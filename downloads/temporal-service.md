# Temporal Service

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> This page provides a comprehensive technical overview of a Temporal Service, detailing its components and subsystems, including the Temporal Server, Frontend Service, History Service, Matching Service, and Worker Service.

> **ℹ️ Info:**
> Please note an important update in our terminology.
>
> We now refer to the Temporal Cluster as the Temporal Service.

This guide provides a comprehensive technical overview of a Temporal Service.

A Temporal Service is the group of services, known as the [Temporal Server](/temporal-service/temporal-server), combined with [Persistence](/temporal-service/persistence) and [Visibility](/temporal-service/visibility) stores, that together act as a component of the Temporal Platform.

See the Self-hosted Temporal Service [production deployment guide](/self-hosted-guide) for implementation guidance.

![A Temporal Service (Server + persistence)](/diagrams/temporal-cluster.svg)
