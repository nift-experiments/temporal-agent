# Security - Temporal Nexus

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Learn about security in Temporal Nexus

Nexus security in Temporal Cloud:

- **[Runtime access controls](/nexus/security#runtime-access-controls)** - Endpoint allowlists restrict which caller Namespaces can use an Endpoint. See [configuring access controls](/nexus/registry#configure-runtime-access-controls).
- **[Secure connectivity](/nexus/security#secure-connectivity)** - mTLS for all Nexus communication across cells and regions. Endpoints are only accessible within a Temporal Cloud Account.
- **[Payload encryption](/nexus/security#payload-encryption-data-converter)** - Same Data Converter as Workflows and Activities, with three approaches for cross-Namespace encryption.
- **[Registry roles and permissions](/nexus/registry#roles-and-permissions)** - Controls who can view, create, edit, and delete Endpoints.
