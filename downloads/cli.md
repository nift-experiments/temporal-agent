# Temporal CLI

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

The Temporal CLI (`temporal`) provides direct access to a Temporal Service via the terminal. Use it to manage, monitor,
and debug Temporal applications, plus run an embedded development service when you need fast local feedback.

In addition, we provide and maintain an official extension for the Temporal CLI you can use to interact with Temporal
Cloud. Use the extension to manage your Temporal Cloud control plane resources, including Namespaces, Users, Service
Accounts, API keys, and perform other operational and administrative tasks.

## Install and configure the CLI

Install the CLI and cloud extension, run a local development server, and configure your environment in
[Install and configure the CLI](/cli/setup-cli).

## Use with Temporal Cloud

Connect to Temporal Cloud with [environment configuration](/develop/environment-configuration) and use the Cloud
extension to manage your Temporal Cloud control plane resources in [Use with Temporal Cloud](/cli/cloud).

## Start a development server

The CLI includes a local Temporal development service for fast feedback while building or testing your application.

```bash
temporal server start-dev
```

## CLI basics

Get started with the basics of the CLI in [CLI basics](/cli/common-operations).

## Command reference

Refer to the [command reference](/cli/command-reference) for the complete list of commands.
