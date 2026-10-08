# Audit Logs - GCP Pub/Sub

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Audit Logs in Temporal Cloud provides forensic information, integrating with GCP Pub/Sub for secure data handling and supporting key Admin and API Key operations. This streamlines audit and compliance processes.

## Manual setup prerequisites

> **📝 Note:**
>
> These steps are only required for manual setup.
> If you use Terraform for your deployment, you don't need to complete these prerequisites.
>

Before configuring the manual Audit Log sink, complete the following steps in Google Cloud:

1. Create a Pub/Sub topic and make a note of its topic name, such as `test-auditlog`.
1. Set up a service account in the same project in Google Cloud and follow the instructions in the
   Temporal Cloud UI to configure the permissions for that service account.

## Create an Audit Log sink

1. In the Temporal Cloud UI, select **Settings**.
1. On the **Settings** page, select **Audit Logs**.
1. In the **Audit Logs Integration** card, select **Setup**.
1. On the **Audit Log Integration** page, select **Pub/Sub**.
1. In the **service account email** field, enter the email of the service account you created in the prerequisites.
1. In the **Topic name** field, enter the topic name of the Pub/Sub topic you created in the prerequisites.
1. There are two ways to configure the service account to write to the Pub/Sub sink: select **Manual** to configure the account manually, or **Deploy with Terraform** to use Terraform.
   If you use Terraform, you don't need to complete the prerequisite steps above.
1. Follow the instructions in the Temporal Cloud UI for the method you chose.
1. To ensure that audit logs can reach your Pub/Sub topic, you can use the **Verify** button to confirm it is set up correctly. This validates that Temporal can successfully write to your topic.
If everything is configured correctly, you will see a `Success` status indicating Temporal has written to the Pub/Sub topic.
1. Click **Create** to configure the audit log.
   Audit Logs will begin to show up in Pub/Sub within 10 minutes 

![Temporal Cloud UI Setup for Audit Logs with GCP Pub/Sub](/img/cloud/gcp/audit-logging-pub-sub-gcp.png)

> **ℹ️ Info:**
> MORE INFORMATION
>
> For more details, refer to [Audit Logs with Temporal Cloud](/cloud/audit-logs).
>
