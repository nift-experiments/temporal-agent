# Troubleshoot Serverless Workers

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> **Public Preview**
> AWS Lambda and GCP Cloud Run support are in Public Preview.

When a Serverless Worker is not running your Tasks, the failure is almost always in one of three places: the
[Worker Controller Instance (WCI)](/serverless-workers#how-invocation-works) is not starting compute, the compute
provider is rejecting the request, or the Worker starts but cannot do its job.

Every provider follows the same overall shape:

1. You deploy the Worker to the compute provider.
2. You create a [Worker Deployment Version](/worker-versioning#deployment-versions) with a compute configuration. This
   starts a WCI Workflow.
3. A Worker polls the Temporal Service, which binds its [Task Queue](/task-queue) to the Worker Deployment Version.
4. The WCI monitors that Task Queue. The [Matching Service](/temporal-service/temporal-server#matching-service) also
   signals the WCI when a Task arrives with no Worker free to take it.
5. Work arrives, the WCI starts compute, and the Worker processes Tasks.

How the WCI starts compute is where providers differ, and so is most of the diagnosis. On AWS Lambda the WCI invokes a
function per unit of work. On GCP Cloud Run it resizes a long-lived Worker Pool. Pick your provider:

- [**AWS Lambda**](/troubleshooting/serverless-workers/aws-lambda) - Diagnose functions that are never invoked,
  invocation loops, and timeouts that cut Workers short.
- [**GCP Cloud Run**](/troubleshooting/serverless-workers/cloud-run) - Diagnose Worker Pools that never scale up,
  impersonation and IAM failures, and instances stopped mid-Activity.
