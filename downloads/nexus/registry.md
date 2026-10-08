# Nexus Registry

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Use the Nexus Registry to manage Nexus Endpoints.

The [Nexus Registry](/glossary#nexus-registry) manages [Nexus Endpoints](/nexus/endpoints). 
Developers can advertise available Endpoints and Services, so others can find and use them in their caller Workflows.
Adding an Endpoint to the Registry deploys it for immediate runtime use.
Endpoint names must be unique within the Registry.
In Temporal Cloud, the Registry is global across your entire Account, spanning all Namespaces.
Endpoint names remain unique Account-wide, and caller Workflows in any Namespace can use an Endpoint if they are on its allowlist.
The Endpoint resource is Project-scoped for management. Creating, updating, and deleting an Endpoint requires access to that Project **and** Namespace Admin on the target Namespace. See [Roles and permissions](#roles-and-permissions) and [Use Nexus across Projects](/cloud/projects#use-nexus-across-projects).
In self-hosted deployments, the Registry is scoped to a Cluster.

## View and manage Nexus Endpoints

Manage Endpoints using the Temporal UI, CLI, Terraform provider, or [Cloud Ops API](/ops).

> **💡 Tip:**
> RESOURCES
>
> - [Terraform support](/cloud/terraform-provider#manage-temporal-cloud-nexus-endpoints-with-terraform) for Temporal Cloud.
> - [tcld nexus](/cloud/tcld/nexus) for Temporal Cloud.
> - [temporal operator nexus](/cli/command-reference/operator#nexus) for self-hosted deployments.

### Search for a Nexus Endpoint

Search by Endpoint name or target Namespace.

![Nexus Endpoints](/img/cloud/nexus/nexus-endpoints-ss.png)

The details page shows the target Namespace, Task Queue, and description rendered as markdown.

![Nexus Billing](/img/cloud/nexus/nexus-billing-ss.png)

### Create a Nexus Endpoint

Creating an Endpoint includes setting an Access Policy - the allowlist of caller Namespaces permitted to use the Endpoint.
No callers are allowed by default, even if in the same Namespace as the Endpoint target.

![Create Nexus Endpoint](/img/cloud/nexus/create-nexus-endpoint-ss.png)

### Edit a Nexus Endpoint

Everything except the Endpoint name can be edited.
New Operations route to the updated target immediately.

> **⚠️ Caution:**
> Changing the target Namespace
>
> - **In-flight async Operations** - Completion callbacks point to the original handler Namespace and are unaffected, but Cancel requests route to the new target.
> - **Workflow ID uniqueness** - IDs are scoped per Namespace. Signal-With-Start creates a new Workflow in the new target even if the same ID is active in the old target, resulting in potential duplicates.
> - **Recommendation:** Drain existing Nexus Operations and underlying handler Workflows before changing the target Namespace.
>

![Edit Nexus Endpoint](/img/cloud/nexus/target-namespace-ss.png)

### Configure runtime access controls

The Access Policy controls which caller Namespaces can use an Endpoint at runtime.
No callers are allowed by default.

See [Runtime Access Controls](/nexus/security#runtime-access-controls) for details.

![Configure runtime access controls](/img/cloud/nexus/create-nexus-endpoint-ss.png)

## Roles and permissions

> **ℹ️ Info:**
>
> The Nexus Registry uses default roles in Temporal Cloud. For self-hosted deployments, you can implement [custom Authorizers](/self-hosted-guide/security#authorizer-plugin) to restrict access.
>

In Temporal Cloud, Nexus Registry respects RBAC permissions, and restricts functionality based on user role:

| Action                     | Required permissions                                      |
|---------------------------|-----------------------------------------------------------|
| View or search Endpoints  | Read-only role (or higher) at the Account level           |
| Manage Endpoints          | Account Developer (or higher), or Project Contribute (or higher) on the Endpoint's Project, **and** Namespace Admin on the target Namespace. Effective Namespace Admin on the target Namespace is required separately. Changing an Endpoint's target Namespace requires Namespace Admin on both the current target Namespace and the new target Namespace. |

See [Nexus security in Temporal Cloud](/cloud/nexus/security).

## Automate Nexus Endpoint provisioning and lifecycle management

There are two ways to automate endpoint provisioning and lifecycle management: Terraform and the Operator API.

> **💡 Tip:**
> RESOURCES
>
> - [Terraform support](/cloud/terraform-provider#manage-temporal-cloud-nexus-endpoints-with-terraform) for Temporal Cloud.
> - [Cloud Ops API](/ops) for Temporal Cloud.
> - [Operator API](https://github.com/temporalio/api/blob/main/temporal/api/operatorservice/v1/service.proto) for self-hosted deployments.
>
