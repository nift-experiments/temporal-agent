# Serverless Workers - Go SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Write Temporal Workers that run on serverless compute using the Go SDK.

> **Public Preview**
> AWS Lambda and GCP Cloud Run support are in Public Preview.

Serverless Workers run on ephemeral, on-demand compute rather than long-lived processes.
Temporal invokes the Worker when Tasks arrive, and the Worker shuts down when the work is done.

For a general overview of how Serverless Workers work, see [Serverless Workers](/serverless-workers).
For the end-to-end deployment guide, see [Deploy a Serverless Worker](/production-deployment/worker-deployments/serverless-workers).

## Supported providers

- [**AWS Lambda**](/develop/go/workers/serverless-workers/aws-lambda) - Use the `lambdaworker` package to run a Worker as a Lambda function. Covers setup, configuration, Lambda-tuned defaults, observability, and the invocation lifecycle.
- [**GCP Cloud Run**](/develop/go/workers/serverless-workers/cloud-run) - Run a standard Worker on a Cloud Run worker pool. Covers the versioned Worker setup, connection configuration, and handling scale-in.
