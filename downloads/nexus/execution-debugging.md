# Execution Debugging - Temporal Nexus

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Learn about execution debugging in Temporal Nexus.

Nexus supports end-to-end execution debugging across caller Workflows, Nexus Operations, and handler Workflows - even across [multi-level calls](/nexus#multi-level-calls) spanning multiple Namespaces.

## Bi-directional linking

Bidirectional links connect Nexus Operation events in the caller's Event History to corresponding events in the handler's Event History.
They are automatically wired by SDK builder functions like New-Workflow-Run-Operation, enabling click-through navigation across Namespaces, regions, and clouds in the Temporal UI.

![Bi-directional linking](/img/cloud/nexus/nexus-bi-directional-linking.png)

- **Forward**: From a caller's Nexus Operation event to the handler's Workflow.
- **Backward**: From the handler's Workflow back to the caller's Nexus Operation event.

## Pending Operations

Pending Nexus Operations are displayed in the UI on the Workflow details page and can be listed from the CLI using the `temporal workflow describe` command.

From the UI:

![Pending Operations](/img/cloud/nexus/pending-nexus-operations.png)

From the CLI:

```
temporal workflow describe

Pending Nexus Operations: 1

  Endpoint                 myendpoint
  Service                  my-hello-service
  Operation                echo
  OperationToken
  State                    BackingOff
  Attempt                  6
  ScheduleToCloseTimeout   0s
  NextAttemptScheduleTime  20 seconds from now
  LastAttemptCompleteTime  11 seconds ago
  LastAttemptFailure       {"message":"handler error (INTERNAL): internal error","applicationFailureInfo":{}}
```

[Retryable errors](/nexus/error-handling#errors-in-nexus-handlers) surface in the Pending Operation.
Non-retryable errors resolve the Operation with a [Failed](/references/events#nexusoperationfailed), [TimedOut](/references/events#nexusoperationtimedout), or [Canceled](/references/events#nexusoperationcanceled) event.

## Pending callbacks

Nexus completion callbacks are sent from the handler's Namespace to the caller's Namespace for asynchronous Operations.
These can be viewed in the UI or from the CLI using the `temporal workflow describe` command.

From the UI:

![Pending Callbacks](/img/cloud/nexus/nexus-callback.png)

From the CLI:

```
temporal workflow describe

Callbacks: 1

  URL               https://nexus.phil-caller-Namespace.a2dd6.cluster.tmprl.cloud:7243/Namespaces/phil-caller-Namespace.a2dd6/nexus/callback
  Trigger           WorkflowClosed
  State             Succeeded
  Attempt           1
  RegistrationTime  32 minutes ago
```

## Tracing

Temporal integrates with [OpenTelemetry](https://opentelemetry.io/) and [OpenTracing](https://opentracing.io/) to visualize call graphs across Activities, Nexus Operations, and Child Workflows.
Enable tracing by installing an interceptor on the Client or Worker:

- [Go SDK](https://github.com/temporalio/samples-go/tree/main/opentelemetry)
- [Java SDK](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/tracing)
- [Python SDK](https://github.com/temporalio/samples-python/tree/main/open_telemetry)
- [TypeScript](https://github.com/temporalio/samples-typescript/tree/main/interceptors-opentelemetry)
- [.NET SDK](https://github.com/temporalio/samples-dotnet/tree/main/src/OpenTelemetry)
