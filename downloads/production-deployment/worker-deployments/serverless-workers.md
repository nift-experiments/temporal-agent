# Serverless Workers

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> **Public Preview**
> AWS Lambda and GCP Cloud Run support are in Public Preview. Amazon Bedrock AgentCore Runtime support is in
> Pre-release. To request AgentCore Runtime access on Temporal Cloud, create a
> [support ticket](/evaluate/cloud/support#support-ticket) or contact your account team. You can also
> [sign up for updates](https://temporal.io/pages/serverless-workers-updates) or try them through self-hosting.

Serverless Workers let you run Temporal Workers on serverless compute. Deploy your Worker code to a serverless provider,
configure a compute provider for the Worker Deployment Version, and Temporal starts and stops Workers in response to
work on the Task Queue. There is no always-on Worker fleet to provision or scale.

Temporal monitors Task Queues that have a compute provider configured. When a Task arrives and no Worker is free to take
it, the [Worker Controller Instance (WCI)](/serverless-workers#how-invocation-works) starts compute. How it starts
compute is where the providers differ. On AWS Lambda and AgentCore Runtime, the WCI invokes compute in response to
unmet Task Queue demand. On GCP Cloud Run, it resizes a Worker Pool of long-lived instances that poll continuously.

## Supported providers

- [**AWS Lambda**](/production-deployment/worker-deployments/serverless-workers/aws-lambda) - Deploy a Serverless Worker
  as a Lambda function. Temporal assumes an IAM role in your AWS account to invoke the function when Tasks arrive.
- [**GCP Cloud Run**](/production-deployment/worker-deployments/serverless-workers/cloud-run) - Deploy a Serverless
  Worker to a Cloud Run Worker Pool. Temporal impersonates a service account in your GCP project to scale the pool as
  Tasks arrive and drain.
- [**Amazon Bedrock AgentCore Runtime**](/production-deployment/worker-deployments/serverless-workers/agentcore) -
  Deploy a Serverless Worker to AgentCore Runtime. Temporal assumes an IAM role in your AWS account to invoke the
  Runtime endpoint as Tasks arrive.

## Try it locally 

To evaluate Serverless Workers on AWS Lambda without an AWS account, you can run the entire loop on your machine with
[LocalStack](https://www.localstack.cloud/) and the Temporal development server. See
[Test a Serverless Worker locally with LocalStack](/production-deployment/worker-deployments/serverless-workers/aws-lambda/local-development).
