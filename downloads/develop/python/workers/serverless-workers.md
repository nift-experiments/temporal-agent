# Serverless Workers - Python SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Write Temporal Workers that run on serverless compute using the Python SDK.

> **Public Preview**
> AWS Lambda and GCP Cloud Run support are in Public Preview. Amazon Bedrock AgentCore Runtime support is in
> Pre-release. To request AgentCore Runtime access on Temporal Cloud, create a
> [support ticket](/evaluate/cloud/support#support-ticket) or contact your account team. You can also
> [sign up for updates](https://temporal.io/pages/serverless-workers-updates) or try them through self-hosting.

Serverless Workers run on ephemeral, on-demand compute rather than long-lived processes.
Temporal invokes the Worker when Tasks arrive, and the Worker shuts down when the work is done.

For a general overview of how Serverless Workers work, see [Serverless Workers](/serverless-workers).
For the end-to-end deployment guide, see [Deploy a Serverless Worker](/production-deployment/worker-deployments/serverless-workers).

## Supported providers

- [**AWS Lambda**](/develop/python/workers/serverless-workers/aws-lambda) - Use the `lambda_worker` contrib package to run a Worker as a Lambda function. Covers setup, configuration, Lambda-tuned defaults, and observability.
- [**Amazon Bedrock AgentCore Runtime**](/develop/python/workers/serverless-workers/agentcore) - Run a standard Worker from an AgentCore Runtime handler. Covers the handler, Worker Versioning, connection configuration, and Worker shutdown.
- [**GCP Cloud Run**](/develop/python/workers/serverless-workers/cloud-run) - Run a standard Worker on a Cloud Run worker pool. Covers the versioned Worker setup, connection configuration, and handling scale-in.
