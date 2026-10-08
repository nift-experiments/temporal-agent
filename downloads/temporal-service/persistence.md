# Persistence

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> The Temporal Persistence store is a database used by the Temporal Server to persist events generated and processed in your Temporal Service and SDK.

This page discusses the following:

- [Persistence](#persistence)
- [Dependency Versions](#dependency-versions)

## What is Persistence? 

The Temporal Persistence store is a database used by the [Temporal Server](/temporal-service/temporal-server) to persist events generated and processed in your Temporal Service and SDK.

A Temporal Service's only required dependency for basic operation is the Persistence database.
Multiple types of databases are supported.

![Persistence](/diagrams/temporal-database.svg)

The database stores the following types of data:

- Tasks: Tasks to be dispatched.
- State of Workflow Executions:
  - Execution table: A capture of the mutable state of Workflow Executions.
  - History table: An append-only log of Workflow Execution History Events.
- Namespace metadata: Metadata of each Namespace in the Temporal Service.
- [Visibility](/temporal-service/visibility) data: Enables operations like "show all running Workflow Executions".
  For production environments, we recommend using Elasticsearch as your Visibility store.

An Elasticsearch database must be configured in a self-hosted Temporal Service to enable [advanced Visibility](/visibility#advanced-visibility) on Temporal Server versions 1.19.1 and earlier.

With Temporal Server version 1.20 and later, advanced Visibility features are available on SQL databases like MySQL (version 8.0.17 and later), PostgreSQL (version 12 and later), SQLite (v3.31.0 and later), and Elasticsearch.

### Dependency versions

Temporal tests compatibility by spanning the minimum and maximum stable major versions for each supported database.
The following versions are used in our test pipelines and actively tested before we release any version of Temporal:

- **Cassandra v3.11, v4.0, and 5.0.4 and later** (Cassandra 5 versions earlier than 5.0.4 are not supported)
- **PostgreSQL 13.18, 14.15, 15.10 and 16.6**
- **MySQL v5.7 and v8.0** (specifically 8.0.19+ due to a bug)

You can verify supported databases in the [Temporal Server release notes](https://github.com/temporalio/temporal/releases).

- Because Temporal Server primarily relies on core database functionality, we do not expect compatibility to break often.

- We do not run tests with vendors like Vitess and CockroachDB.
- Temporal also supports SQLite v3.x persistence, but this is meant only for development and testing, not production usage.
