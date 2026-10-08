# Serverless Workers - Rust SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Write Temporal Workers that run on serverless compute using the Rust SDK.

> **Public Preview**
> Cloud Run support is in Public Preview. APIs and configuration may change before the stable release.

Serverless Workers run on compute that Temporal starts and stops for you, rather than on long-lived processes you operate.

For a general overview of how Serverless Workers work, see [Serverless Workers](/serverless-workers).
For the end-to-end deployment guide, see [Deploy a Serverless Worker](/production-deployment/worker-deployments/serverless-workers).

## Supported providers

- [**GCP Cloud Run**](/develop/rust/workers/serverless-workers/cloud-run) - Run a standard Worker on a Cloud Run worker pool. Covers the versioned Worker setup, connection configuration, and handling scale-in.
