# CLI basics

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

This page walks through the operations you're most likely to reach for when using the Temporal CLI. For the full set of
commands, see the [command reference](/cli#command-reference).

## Run a development server

The Temporal CLI ships with a complete Temporal binary. Start a local Temporal Service for development with a single
command.

The Temporal Service is available on `localhost:7233` and the Web UI at `http://localhost:8233`.

To keep Workflow data between restarts, specify a database file.

See [Install and configure](/cli/setup-cli#run-a-local-development-server) for more development server options.

```bash
temporal server start-dev
```

```bash
temporal server start-dev --db-filename temporal.db
```

## Start a Workflow

Start a Workflow Execution with `temporal workflow start`.

To start a Workflow and wait for the result, use `temporal workflow execute` instead.

```bash
temporal workflow start \\
  --task-queue my-task-queue \\
  --type MyWorkflow \\
  --workflow-id my-workflow-id \\
  --input '"my-input-value"'
```

```bash
temporal workflow execute \\
  --task-queue my-task-queue \\
  --type MyWorkflow \\
  --workflow-id my-workflow-id \\
  --input '"my-input-value"'
```

## Check Workflow status

List running Workflows.

Get details about a specific Workflow Execution.

View the Event History for a Workflow Execution.

```bash
temporal workflow list
```

```bash
temporal workflow describe --workflow-id my-workflow-id
```

```bash
temporal workflow show --workflow-id my-workflow-id
```

## Send Signals and Queries

Send a [Signal](/sending-messages#sending-signals) to a running Workflow.

[Query](/sending-messages#sending-queries) a running Workflow for its current state.

```bash
temporal workflow signal \\
  --workflow-id my-workflow-id \\
  --name my-signal \\
  --input '"signal-value"'
```

```bash
temporal workflow query \\
  --workflow-id my-workflow-id \\
  --name my-query
```

## Cancel or Terminate a Workflow

Cancel a Workflow Execution. Cancellation allows cleanup logic to run before the Workflow completes.

Terminate a Workflow Execution. Termination stops the Workflow immediately with no cleanup.

```bash
temporal workflow cancel --workflow-id my-workflow-id
```

```bash
temporal workflow terminate --workflow-id my-workflow-id
```

## Log in to Temporal Cloud

Log in to Temporal Cloud with `temporal cloud login`. After login, you can run commands against Temporal Cloud by
providing the address and Namespace.

See [Use with Temporal Cloud](/cli/cloud) for all authentication options.

```bash
temporal cloud login
```

```bash
temporal workflow list \\
  --address <namespace>.<account>.tmprl.cloud:7233 \\
  --namespace <namespace>.<account>
```

## Work with Schedules

Create a [Schedule](/schedule) that starts a Workflow on an interval.

List all Schedules.

Pause and unpause a Schedule.

```bash
temporal schedule create \\
  --schedule-id my-schedule \\
  --interval 1h \\
  --task-queue my-task-queue \\
  --type MyScheduledWorkflow
```

```bash
temporal schedule list
```

```bash
temporal schedule toggle \\
  --schedule-id my-schedule \\
  --pause --reason "maintenance"
```

```bash
temporal schedule toggle \\
  --schedule-id my-schedule \\
  --unpause --reason "maintenance complete"
```

## Manage Namespaces

List available [Namespaces](/namespaces).

Create a new Namespace.

To manage Namespaces on Temporal Cloud, use the Temporal Cloud extension and
[`temporal cloud namespace`](/cli/command-reference/cloud/namespace) commands.

```bash
temporal operator namespace list
```

```bash
temporal operator namespace create --namespace my-namespace
```

## Format and filter output

Use `--output json` to get machine-readable output from any command.

Combine with [jq](https://jqlang.github.io/jq/) for filtering.

```bash
temporal workflow list --output json
```

```bash
temporal workflow list --output json | jq '.[].type.name'
```

## Next steps

- [Use with Temporal Cloud](/cli/cloud) to connect the CLI to Temporal Cloud.
- [Command reference](/cli#command-reference) for the full set of commands and options.
