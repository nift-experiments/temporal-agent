# Receive Temporal Cloud notifications

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Receive updates about Temporal Cloud including when certificates will expire, billing updates, and when a failover has completed.

## Get notified about Temporal Cloud status 

In the event of an incident, Temporal updates the [Temporal Cloud status page](https://status.temporal.io/) with important updates.
Users can subscribe to updates in their preferred mode, such as email, Slack, or SMS, by visiting this page.

## Get notified about administrative events 

Temporal Cloud sends emails to notify users of important administrative events.

| Reason for email | Who receives email |
|------------------ | -------------------|
| Certificate Expiring in 15 days | Global Administrator, Namespace Administrator, Account Owner |
| Certificate Expiring in 10 days | Global Administrator, Namespace Administrator, Account Owner |
| Certificate Expiring in 5 days  | Global Administrator, Namespace Administrator, Account Owner |
| API Key Expiring in 30 days     | Global Administrator, Account Owner, individual user (if API Key has an owner) |
| API Key Expiring in 20 days     | Global Administrator, Account Owner, individual user (if API Key has an owner) |
| API Key Expiring in 10 days     | Global Administrator, Account Owner, individual user (if API Key has an owner) |
| Sign up credit expiring in 30 days | Account Owner, Finance Administrator |
| Sign up credit expiring in 14 days | Account Owner, Finance Administrator |
| Sign up credit expiring in  7 days | Account Owner, Finance Administrator |
| Sign up credit expiring in  1 days | Account Owner, Finance Administrator |
| Sign up credit is 50% consumed     | Account Owner, Finance Administrator |
| Sign up credit is 90% consumed     | Account Owner, Finance Administrator |
| Account plan type changed          | Global Administrator, Account Owner, Finance Administrator |
| Namespace Failover Completed/Failed | Global Administrator, Namespace Administrator, Account Owner |

To ensure that you receive email notifications, configure your junk-email filters to permit email from
`noreply@temporal.io`.

To provide feedback on notifications or request changes, [create a support ticket](/evaluate/cloud/support#support-ticket).
