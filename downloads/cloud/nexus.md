# Nexus

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Temporal Cloud adds global Nexus Registry, built-in access controls, audit logging, and multi-region connectivity on top of core Nexus.

Temporal Cloud builds on the [core Nexus experience](/nexus) with:

- **Global [Nexus Registry](/nexus/registry)** - Scoped to your entire Account across all Namespaces. Workers in any Namespace can host Nexus Services for others to use.
- **Built-in [access controls](/nexus/registry#configure-runtime-access-controls)** - Restrict which caller Namespaces can use a Nexus Endpoint at runtime.
- **[Audit logging](/cloud/audit-logs)** - Stream Nexus Registry actions (create, update, delete Endpoints) to your audit log integration.
- **Multi-region connectivity** - Nexus requests route across Namespaces within and across AWS and GCP using a global mTLS-secured Envoy mesh. Compatible with Namespaces that have [High Availability](/cloud/high-availability) as Endpoint targets.
- **[Terraform support](/cloud/terraform-provider#manage-temporal-cloud-nexus-endpoints-with-terraform)** - Manage Nexus Endpoints with the Temporal Cloud Terraform provider.

![Nexus Overview](/img/cloud/nexus/nexus-overview-short.png)

## Learn more

- [Evaluate Nexus](/evaluate/features/nexus) | [Keynote and demo](https://youtu.be/qqc2vsv1mrU?feature=shared&t=2082)
- [How Nexus works](/nexus) | [Deep dive talk](https://www.youtube.com/watch?v=izR9dQ_eIe4&t=934s)
