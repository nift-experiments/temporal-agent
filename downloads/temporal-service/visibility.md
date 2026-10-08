# Visibility

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> The term Visibility, within the Temporal Platform, refers to the subsystems and APIs that enable an operator to view, filter, and search for Workflow Executions that currently exist within a Temporal Service.

This page discusses [Visibility](#visibility).

## What is Visibility? 

The term [Visibility](/visibility), within the Temporal Platform, refers to the subsystems and APIs that enable an operator to view, filter, and search for Workflow Executions that currently exist within a Temporal Service.

The [Visibility store](/self-hosted-guide/visibility) in your Temporal Service stores persisted Workflow Execution Event History data and is set up as a part of your [Persistence store](/temporal-service/persistence) to enable listing and filtering details about Workflow Executions that exist on your Temporal Service.

- [How to set up a Visibility store](/self-hosted-guide/visibility)

With Temporal Server v1.21, you can set up [Dual Visibility](/dual-visibility) to migrate your Visibility store from one database to another.

Support for separate standard and advanced Visibility setups will be deprecated from Temporal Server v1.21 onwards.
Check [Supported databases](/self-hosted-guide/visibility) for updates.
