# Manage users

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Invite users, set account-level roles and Namespace-level permissions, and remove users from a Temporal Cloud account with the Web UI, the CLI, or the Cloud Ops API.

- [How to invite users to your Temporal Cloud account](#invite-users)
- [What are the account-level roles?](#account-level-roles)
- [What are the Namespace-level permissions?](#namespace-level-permissions)
- [How to update an account-level Role in Temporal Cloud](#update-roles)
- [How to update Namespace-level permissions in Temporal Cloud](#update-permissions)
- [How to delete a user from your Temporal Cloud account](#delete-users)
- [How to troubleshoot account access issues](#troubleshoot-access)

## How to invite users to your Temporal Cloud account 

# User management

> Learn how to manage user invitations for Temporal Cloud

**Web UI**

To invite users using the Temporal Cloud UI:

1. In Temporal Web UI, select **Settings** in the left portion of the window.
1. On the **Settings** page, select **Create Users** in the upper-right portion of the window.
1. On the **Create Users** page in the **Email Addresses** box, type or paste one or more email addresses.
1. In **Account-Level Role**, select a [Role](/cloud/manage-access/roles-and-permissions#account-level-roles). The Role
   applies to all users whose email addresses appear in **Email Addresses**.
1. If the account has any Namespaces, they are listed under **Grant access to Namespaces**. To add a permission, select
   the checkbox next to a Namespace, and then select a
   [permission](/cloud/manage-access/roles-and-permissions#namespace-level-permissions). Repeat as needed.
1. When all permissions are assigned, select **Send Invite**.

**Temporal CLI**

Use the [`temporal cloud user invite`](/cli/command-reference/cloud/user#invite) command. Specify the user's email, an
account-level role, and optionally one or more Namespace permissions.

Available account roles: `owner` | `admin` | `developer` | `finance-admin` | `read` | `metrics-read`.

Available Namespace permissions: `admin` | `write` | `read`.

```command
temporal cloud user invite \
  --email <user@example.com> \
  --account-role <role> \
  --namespace-access <namespace.account>=<permission>
```

Repeat `--namespace-access` to grant permissions on more than one Namespace. `--email` takes a single address, so invite
one user per command:

```command
temporal cloud user invite \
  --email user1@example.com \
  --account-role developer \
  --namespace-access ns1.my-account=admin \
  --namespace-access ns2.my-account=write
```

**tcld**

Use the [`tcld user invite`](/cloud/tcld/user/#invite) command. Specify the user's email, an account-level role, and
optionally one or more Namespace permissions.

Available account roles: `admin` | `developer` | `read`.

Available Namespace permissions: `Admin` | `Write` | `Read`.

```command
tcld user invite \
  --user-email <user@example.com> \
  --account-role <role> \
  --namespace-permission <namespace>=<permission>
```

You can invite multiple users and assign multiple Namespace permissions in a single command:

```command
tcld user invite \
  --user-email user1@example.com \
  --user-email user2@example.com \
  --account-role developer \
  --namespace-permission ns1=Admin \
  --namespace-permission ns2=Write
```

### Frequently asked questions

#### Can multiple Temporal Cloud accounts share the same email domain?

Yes. Multiple Temporal Cloud accounts can coexist with users from the same email domain.
Each account has its own independent SAML configuration, tied to its unique Account Id.
We recommend configuring [SAML](/cloud/manage-access/saml) for each account independently.
For the smoother login experience, you can configure SAML for each account separately and use IdP-initiated login: you click the relevant app tile in your identity provider's portal to access the Temporal Cloud account associated with your email address directly.

#### Can the same email be used across different Temporal Cloud accounts?

No. Each email address can only be associated with a single Temporal Cloud account.
If you need access to multiple accounts, you’ll need a separate invite for each one using a different email address.

#### Can I use Google or Microsoft SSO after signing up with email and password?

If you originally signed up for Temporal Cloud using an email and password, you won’t be able to log in using Google or Microsoft single sign-on.

If you prefer SSO, ask your Account Owner to delete your current user and send you a new invitation.
During re-invitation, be sure to sign up using your preferred authentication method.

Use the [CreateUser](https://saas-api.tmprl.cloud/docs/httpapi.html#tag/users) endpoint to invite a user.

```
POST /cloud/users
```

The request body includes a `spec` with the following fields:

- `spec.email` — The email address of the user to invite.
- `spec.access.account_access.role` — The account-level role to assign.
- `spec.access.namespace_accesses` — A map of Namespace names to permissions.

Available roles: `ROLE_ADMIN` | `ROLE_DEVELOPER` | `ROLE_READ` | `ROLE_OWNER` | `ROLE_FINANCE_ADMIN`.

Available Namespace permissions: `PERMISSION_ADMIN` | `PERMISSION_WRITE` | `PERMISSION_READ`.

The new users receive an email with a link to accept the invitation and complete their setup. The new user must use this
link to sign up to be added to your account unless the account has a SAML configuration. If your account has a SAML
configuration, the new user can sign in using their existing SAML credentials and be included in the account
automatically.

> **⚠️ Caution:**
>
> The new user must use the same authentication method they originally signed up with to sign in to Temporal Cloud. If
> they used single sign-on (SSO), they must use the same SSO provider to sign in to Temporal Cloud. If they used email and
> password authentication, they must use the same email and password to sign in to Temporal Cloud, and cannot use SSO,
> even if the underlying email address is the same.
>

## What are the account-level roles for users in Temporal Cloud? 

When an Account Owner or Global Admin invites a user to join an account, they select one of the following roles for that user:

- **Global Admin**
  - Has full administrative permissions across the account, including users and usage
  - Can create and manage [Namespaces](/namespaces) and [Nexus Endpoints](/nexus/endpoints)
  - Has Namespace Admin [permissions](#namespace-level-permissions) on all Namespaces in the account.
    This permission cannot be revoked
- **Developer**
  - Can create Namespaces
  - Is granted [Namespace Admin](/cloud/manage-access/users#namespace-level-permissions) permission for each Namespace they create.
    This permission can be revoked
  - Can create and manage Nexus Endpoints where they are a [Namespace Admin](/cloud/manage-access/users#namespace-level-permissions) on the Endpoint's target Namespace.
    Changing an Endpoint's target Namespace requires Namespace Admin on both the current target Namespace and the new target Namespace.
- **Read-Only**
  - Can read information
  - Can be granted Namespace [permissions](#namespace-level-permissions), for example to read or write Workflow state in a given Namespace
  - Can view all Nexus Endpoints in the account, which have separate [runtime access controls](/nexus/security#runtime-access-controls)

In addition, there are two roles that the Global Admin cannot assign:

- **Account Owner**
  - Has full administrative permissions across the account, including users, usage and [billing](/cloud/billing-and-usage)
  - Can create and manage Namespaces and Nexus Endpoints
  - Has Namespace Admin [permissions](#namespace-level-permissions) on all [Namespaces](/namespaces) in the account.
    This permission cannot be revoked
- **Finance Admin**
  - Has permissions to view [billing](/cloud/billing-and-usage) information and update payment information
  - Otherwise, has the same permissions as Account Read-only users
  - Only an Account Owner can assign Finance Admin to a user, group, or Service Account

> **📝 Note:**
> Default Role
>
> When the account is created, the initial user who logs in is automatically assigned the Account Owner role.
> If your account does not have an Account Owner, please reach out to [Support](https://temporalsupport.zendesk.com/) to assign the appropriate individual to this role.
>

## Using the Account Owner role

The Account Owner role (that is, users with the Account Owner system role) holds the highest level of access in the system.
This role configures account-level parameters and manages Temporal billing and payment information.
It allows users to perform all actions within the Temporal Cloud account.

> **💡 Tip:**
> Best Practices
>
> Temporal strongly recommends the following precautions when assigning the Account Owner role to users:
>
> - Assign the role to at least two users in your organization.
>   Otherwise, limit the number of users with this role.
> - Associate a person’s direct email address to the Account Owner, rather than a shared or generic address, so Temporal Support can contact the right person in urgent situations.
>
> This latter rule is useful for anyone on your team who may need to be contacted urgently, regardless of their Account role.
>

## What are the Namespace-level permissions for users in Temporal Cloud? 

An Account Owner or Global Admin can assign permissions for any [Namespace](/namespaces) in an account.
A Developer can assign permissions for a Namespace they create.

For a Namespace, a user can have one of the following permissions:

- **Namespace Admin:**
  - Can [manage the Namespace](/cloud/namespaces#manage-namespaces) including identities and permissions
  - Can create, rename, update, and delete [Workflows](/workflows) within the Namespace
- **Write:**
  - Can create, rename, update, and delete [Workflows](/workflows) within the Namespace
- **Read-Only:**
  - Can only read information from the Namespace

## How to update an account-level role in Temporal Cloud 

With Global Admin or Account Owner privileges, you can update any user's account-level [role](#account-level-roles) using either the Web UI or the CLI.
The Account Owner role can only be granted by existing Account Owners.

For security reasons, changes to the Account Owner role must be made through Temporal Support.
To change or delete an Account Owner, you must submit a [support ticket](https://temporalsupport.zendesk.com/).

### How to update an account-level role using Web UI

1. In Temporal Web UI, select **Settings** in the left portion of the window.
1. On the **Settings** page, select the user.
1. On the user profile page, select **Edit User**.
1. On the **Edit User** page in **Account Level Role**, select the role.
1. Select **Save**.

### How to update an account-level role using the CLI

**Temporal CLI**

For details, see the [`temporal cloud user set-account-role`](/cli/command-reference/cloud/user#set-account-role) command.

**tcld**

For details, see the [tcld user set-account-role](/cloud/tcld/user/#set-account-role) command.

## How to update Namespace-level permissions in Temporal Cloud 

You can update Namespace-level [permissions](#namespace-level-permissions) by using either the Web UI or the CLI.

### How to use the Web UI to update a user's permissions across multiple Namespaces

1. In Temporal Web UI, select **Namespaces** in the left portion of the window.
1. On the **Namespaces** page, select the Namespace.
1. If necessary, scroll down to the list of permissions
1. On the user profile page in **Namespace permissions**, select the Namespace.
1. On the Namespace page in **Account Level Role**, select the role.
1. Select **Save**.

### How to use the Web UI to update permissions for multiple users within a single Namespace

> **📝 Note:**
>
> A user with the Account Owner or Global Admin account-level [role](#account-level-roles) has Namespace Admin permissions for all Namespaces.
>

1. In Temporal Web UI, select **Settings** in the left portion of the window.
1. On the **Settings** page in the **Users** tab, select the user.
1. On the user profile page, select **Edit User**.
1. On the **Edit User** page in **Namespace permissions**, change the permissions for one or more Namespaces.
1. Select **Save**.

### How to use the CLI to update Namespace-level permissions

**Temporal CLI**

For details, see the [`temporal cloud user set-namespace-permissions`](/cli/command-reference/cloud/user#set-namespace-permissions) command.

**tcld**

For details, see the [tcld user set-namespace-permissions](/cloud/tcld/user/#set-namespace-permissions) command.

## How to delete a user from your Temporal Cloud account 

You can delete a user from your Temporal Cloud Account by using either the Web UI or the CLI.

> **ℹ️ Info:**
>
> To delete a user, a user must have the Account Owner or Global Admin account-level [role](#account-level-roles).
>

### How to delete a user using Web UI

1. In Temporal Web UI, select **Settings** in the left portion of the window.
1. On the **Settings** page, find the user and, on the right end of the row, select **Delete**.
1. In the **Delete User** dialog, select **Delete**.

You can delete a user in two other ways in Web UI:

- User profile page: Select the down arrow next to **Edit User** and then select **Delete**.
- **Edit User** page: Select **Delete User**.

### How to delete a user using the CLI

**Temporal CLI**

For details, see the [`temporal cloud user delete`](/cli/command-reference/cloud/user#delete) command.

**tcld**

For details, see the [tcld user delete](/cloud/tcld/user/#delete) command.

## Account-level roles and Namespace-level permissions 

Temporal account-level roles and Namespace-level permissions provide access to specific Temporal Workflow and Temporal Cloud operational APIs.
The following table provides the API details associated with each account-level role and Namespace-level permission.

#### Account-level role details

This table provides API-level details for the permissions granted to a user through account-level roles. These permissions are configured per user.

| Permission                        | Read-only | Developer | Finance Admin | Global Admin | Account Owner |
| --------------------------------- | --------- | --------- | ------------- | ------------ | ------------- |
| CountIdentities                   | ✅         | ✅         | ✅             | ✅            | ✅             |
| CreateAccountAuditLogSink         |           |           |               | ✅            | ✅             |
| CreateAPIKey                      | ✅         | ✅         | ✅             | ✅            | ✅             |
| CreateNamespace                   |           | ✅         |               | ✅            | ✅             |
| CreateNexusEndpoint               |           | ✅         |               | ✅            | ✅             |
| CreateServiceAccount              |           |           |               | ✅            | ✅             |
| CreateServiceAccountAPIKey        |           |           |               | ✅            | ✅             |
| CreateStripeCustomerPortalSession |           |           | ✅             |              | ✅             |
| CreateUser                        |           |           |               | ✅            | ✅             |
| DeleteAccountAuditLogSink         |           |           |               | ✅            | ✅             |
| DeleteAPIKey                      | ✅         | ✅         | ✅             | ✅            | ✅             |
| DeleteNexusEndpoint               |           | ✅         |               | ✅            | ✅             |
| DeleteServiceAccount              |           |           |               | ✅            | ✅             |
| DeleteUser                        |           |           |               | ✅            | ✅             |
| GetAccount                        | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetAccountAuditLogSink            |           |           |               | ✅            | ✅             |
| GetAccountAuditLogSinks           |           |           |               | ✅            | ✅             |
| GetAccountFeatureFlags            | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetAccountLimits                  | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetAccountSettings                | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetAccountUsage                   |           |           |               | ✅            | ✅             |
| GetAPIKey                         | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetAPIKeys                        | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetAsyncOperation                 | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetAuditLogs                      |           |           |               | ✅            | ✅             |
| GetDecodedCertificate             | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetIdentities                     | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetIdentity                       | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetNamespaces                     | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetNamespacesUsage                |           |           |               | ✅            | ✅             |
| GetNexusEndpoint                  | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetNexusEndpoints                 | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetRegion                         | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetRegions                        | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetRequestStatus                  | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetRequestStatuses                |           |           |               | ✅            | ✅             |
| GetRequestStatusesForNamespace    | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetRequestStatusesForUser         | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetRoles                          | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetRolesByPermissions             | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetServiceAccount                 | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetServiceAccounts                | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetStripeInvoice                  |           |           | ✅             |              | ✅             |
| GetUser[‡](/cloud/manage-access/permissions-reference#user-authorization-behavior) | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetUsers[‡](/cloud/manage-access/permissions-reference#user-authorization-behavior) | ✅         | ✅         | ✅             | ✅            | ✅             |
| GetUsersWithAccountRoles          | ✅         | ✅         | ✅             | ✅            | ✅             |
| InviteUsers                       |           |           |               | ✅            | ✅             |
| ListCreditLedgerEntries           |           |           | ✅             |              | ✅             |
| ListGrants                        |           |           | ✅             |              | ✅             |
| ListMetronomeInvoices             |           |           | ✅             |              | ✅             |
| ListMetronomeInvoicesForNamespace |           |           | ✅             |              | ✅             |
| ListNamespaces                    | ✅         | ✅         | ✅             | ✅            | ✅             |
| ListPromotionGrantBalances        |           |           | ✅             |              | ✅             |
| ResendUserInvite                  |           |           |               | ✅            | ✅             |
| SetAccountSettings                |           |           |               | ✅            | ✅             |
| SyncCurrentUserInvite             | ✅         | ✅         | ✅             | ✅            | ✅             |
| UpdateAccount                     |           |           |               | ✅            | ✅             |
| UpdateAccountAuditLogSink         |           |           |               | ✅            | ✅             |
| UpdateAPIKey                      | ✅         | ✅         | ✅             | ✅            | ✅             |
| UpdateNexusEndpoint               |           | ✅         |               | ✅            | ✅             |
| UpdateServiceAccount              |           |           |               | ✅            | ✅             |
| UpdateUser                        |           |           |               | ✅            | ✅             |
| ValidateAccountAuditLogSink       |           |           |               | ✅            | ✅             |

#### Namespace-level permissions details

This table provides API-level details for the permissions granted to a user through Namespace-level permissions.
These permissions are configured per Namespace per user.

> **📝 Note:**
>
> Account Owners and Global Admins inherit Namespace Admin permissions on all Namespaces.
>

| Permission                         | Read | Write | Namespace Admin |
| ---------------------------------- | ---- | ----- | --------------- |
| CountWorkflowExecutions            | ✅    | ✅     | ✅               |
| CreateExportSink                   |      |       | ✅               |
| CreateSchedule                     |      | ✅     | ✅               |
| DeleteExportSink                   |      |       | ✅               |
| DeleteNamespace                    |      |       | ✅               |
| DeleteSchedule                     |      | ✅     | ✅               |
| DescribeBatchOperation             | ✅    | ✅     | ✅               |
| DescribeNamespace                  | ✅    | ✅     | ✅               |
| DescribeSchedule                   | ✅    | ✅     | ✅               |
| DescribeTaskQueue                  | ✅    | ✅     | ✅               |
| DescribeWorkflowExecution          | ✅    | ✅     | ✅               |
| FailoverNamespace                  |      |       | ✅               |
| GetExportSink                      | ✅    | ✅     | ✅               |
| GetExportSinks                     | ✅    | ✅     | ✅               |
| GetNamespace                       | ✅    | ✅     | ✅               |
| GetNamespaceUsage                  | ✅    | ✅     | ✅               |
| GetReplicationStatus               | ✅    | ✅     | ✅               |
| GetSearchAttributes                | ✅    | ✅     | ✅               |
| GetUsersForNamespace               | ✅    | ✅     | ✅               |
| GetWorkerBuildIdCompatibility      | ✅    | ✅     | ✅               |
| GetWorkerTaskReachability          | ✅    | ✅     | ✅               |
| GetWorkflowExecutionHistory        | ✅    | ✅     | ✅               |
| GetWorkflowExecutionHistoryReverse | ✅    | ✅     | ✅               |
| GlobalizeNamespace                 |      |       | ✅               |
| ListBatchOperations                | ✅    | ✅     | ✅               |
| ListClosedWorkflowExecutions       | ✅    | ✅     | ✅               |
| ListExportSinks                    | ✅    | ✅     | ✅               |
| ListFailoverHistoryByNamespace     | ✅    | ✅     | ✅               |
| ListOpenWorkflowExecutions         | ✅    | ✅     | ✅               |
| ListReplicaStatus                  | ✅    | ✅     | ✅               |
| ListScheduleMatchingTimes          | ✅    | ✅     | ✅               |
| ListSchedules                      | ✅    | ✅     | ✅               |
| ListTaskQueuePartitions            | ✅    | ✅     | ✅               |
| ListWorkflowExecutions             | ✅    | ✅     | ✅               |
| PatchSchedule                      |      | ✅     | ✅               |
| PollActivityTaskQueue              |      | ✅     | ✅               |
| PollWorkflowTaskQueue              |      | ✅     | ✅               |
| QueryWorkflow                      | ✅    | ✅     | ✅               |
| RecordActivityTaskHeartbeat        |      | ✅     | ✅               |
| RecordActivityTaskHeartbeatById    |      | ✅     | ✅               |
| RenameCustomSearchAttribute        |      |       | ✅               |
| RequestCancelWorkflowExecution     |      | ✅     | ✅               |
| ResetStickyTaskQueue               |      | ✅     | ✅               |
| ResetWorkflowExecution             |      | ✅     | ✅               |
| RespondActivityTaskCanceled        |      | ✅     | ✅               |
| RespondActivityTaskCanceledById    |      | ✅     | ✅               |
| RespondActivityTaskCompleted       |      | ✅     | ✅               |
| RespondActivityTaskCompletedById   |      | ✅     | ✅               |
| RespondActivityTaskFailed          |      | ✅     | ✅               |
| RespondActivityTaskFailedById      |      | ✅     | ✅               |
| RespondQueryTaskCompleted          |      | ✅     | ✅               |
| RespondWorkflowTaskCompleted       |      | ✅     | ✅               |
| RespondWorkflowTaskFailed          |      | ✅     | ✅               |
| SetUserNamespaceAccess             |      |       | ✅               |
| SignalWithStartWorkflowExecution   |      | ✅     | ✅               |
| SignalWorkflowExecution            |      | ✅     | ✅               |
| StartBatchOperation                |      | ✅     | ✅               |
| StartWorkflowExecution             |      | ✅     | ✅               |
| StopBatchOperation                 |      | ✅     | ✅               |
| TerminateWorkflowExecution         |      | ✅     | ✅               |
| UpdateExportSink                   |      |       | ✅               |
| UpdateNamespace                    |      |       | ✅               |
| UpdateSchedule                     |      | ✅     | ✅               |
| UpdateSearchAttributes             |      |       | ✅               |
| UpdateUserNamespacePermissions     |      |       | ✅               |
| ValidateExportSink                 |      |       | ✅               |
| ValidateGlobalizeNamespace         |      |       | ✅               |

> **📝 Note:**
> UpdateNamespace settings
>
> `UpdateNamespace` requires Namespace Admin permission and covers these settings:
> - [Retention period](/temporal-service/temporal-server#retention-period)
> - [API key auth](/cloud/api-keys#namespace-authentication)
> - [mTLS certificates](/cloud/certificates)
> - [Certificate filters](/cloud/certificates#manage-certificate-filters)
> - [Codec server](/production-deployment/data-encryption)
> - [Connectivity rules](/cloud/connectivity)
> - [Custom Search Attributes](/search-attribute#custom-search-attribute)
> - [Provisioned capacity (TRUs)](/cloud/capacity-modes#provisioned-capacity)
> - [High Availability](/cloud/high-availability)
>

## How to troubleshoot account access issues 

### Why can't I sign in after my email domain changed? 

If your organization changed its email domain (for example, from `@oldcompany.com` to `@newcompany.com`), you may be unable to sign in to Temporal Cloud with your existing account.

**Why this happens:**
When you sign in using "Continue with Google" or "Continue with Microsoft", Temporal Cloud identifies your account by your email address.
If your email address changes, Temporal Cloud sees this as a different identity and cannot match it to your existing account.

**How to resolve this:**
[Create a support ticket](/evaluate/cloud/support#support-ticket) with the following information:

- Your previous email address (the one originally used to access Temporal Cloud)
- Your new email address
- Your Temporal Cloud Account Id (if known)

Temporal Support can update your account to use your new email address.

> **💡 Tip:**
> Use SAML for enterprise identity management
>
> If your organization frequently changes email domains or wants centralized control over user authentication, consider using [SAML authentication](/cloud/manage-access/saml).
> With SAML, your identity provider (IdP) manages user identities, and email domain changes can be handled within your IdP without affecting Temporal Cloud access.
>
