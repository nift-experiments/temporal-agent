# Pricing for Temporal Nexus

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Learn about the pricing structure for using Nexus.

Nexus pricing:

- **One Action to start or cancel a Nexus Operation** in the caller Namespace.
  Underlying primitives (Workflows, Activities, Signals) and their retries created by the handler result in normal Actions.
- **No Action for handling or retrying the Nexus Operation itself**.
  However, billable actions initiated by the handler (such as Activities) are charged if they fail and retry.

See [Pricing](/cloud/pricing) for details.
