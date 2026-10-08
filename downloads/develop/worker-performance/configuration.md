# Worker performance options

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Configure Worker executor slots, poller options, and Workflow cache options for Temporal SDK performance.

Each Worker can be configured by providing custom Worker options (`WorkerOptions`) at instantiation.
Options are specific to individual Workers and do not affect other members of your fleet.

### Executor slot options

The `maxConcurrentWorkflowTaskExecutionSize` and `maxConcurrentActivityExecutionSize` options define the number of total available Workflow Task and Activity Task slots for a Worker.

> **⚠️ Caution:**
>
> - Worker tuners supersede the existing `maxConcurrentXXXTask` style Worker options.
>   Using both styles will cause an error at Worker initialization time.
>

### Configuring poller options 

#### Recommended approach

The Temporal SDKs support Poller Autoscaling, which automatically selects an appropriate number of pollers based on need. Using this feature results in more efficient poller usage, better throughput, and schedule-to-start latency improvements. You can enable this feature by setting the `*_task_poller_behavior` options to `PollerBehaviorAutoscaling`. Names may vary slightly depending on the SDK. For specific examples of enabling Poller Autoscaling, see the SDK examples section below. Poller Autoscaling will be the default configuration in future versions of Temporal SDKs.

> **💡 Tip:**
>
> `PollerBehaviorAutoscaling` is only enabled in Temporal Server v1.28.0 and later.
>

#### Manual configuration

There are options available to manually configure minimum, maximum, and initial poller counts, but it is not recommended to set these values manually for production use cases. To set these values manually, the following options are available: 

- `maxConcurrentWorkflowTaskPollers` (in the JavaSDK: `workflowPollThreadCount`)
- `maxConcurrentActivityTaskPollers` (in the JavaSDK: `activityPollThreadCount`)

These options define the maximum count of pollers performing poll requests on Workflow and Activity Task Queues, respectively. 

#### SDK examples

Select a concept to highlight the matching poller option:

**Go**

[Go SDK docs](https://pkg.go.dev/go.temporal.io/sdk/worker#PollerBehaviorAutoscalingOptions)
  annotations={[
    {
      label: 'Workflow Task poller',
      description: 'Autoscales the number of pollers for Workflow Tasks based on load.',
      lines: [2],
    },
    {
      label: 'Activity Task poller',
      description: 'Autoscales the number of pollers for Activity Tasks based on load.',
      lines: [3],
    },
    {
      label: 'Nexus Task poller',
      description: 'Autoscales the number of pollers for Nexus Tasks based on load.',
      lines: [4],
    },
  ]}
>
```go
w := worker.New(c, "my-task-queue", worker.Options{
  WorkflowTaskPollerBehavior: worker.NewPollerBehaviorAutoscaling(worker.PollerBehaviorAutoscalingOptions{}),
  ActivityTaskPollerBehavior: worker.NewPollerBehaviorAutoscaling(worker.PollerBehaviorAutoscalingOptions{}),
  NexusTaskPollerBehavior: worker.NewPollerBehaviorAutoscaling(worker.PollerBehaviorAutoscalingOptions{}),
})
```

**Java**

[Java SDK docs](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/worker/tuning/PollerBehaviorAutoscaling.html)
  annotations={[
    {
      label: 'Workflow Task poller',
      description: 'Autoscales the number of pollers for Workflow Tasks based on load.',
      lines: [7],
    },
    {
      label: 'Activity Task poller',
      description: 'Autoscales the number of pollers for Activity Tasks based on load.',
      lines: [8],
    },
    {
      label: 'Nexus Task poller',
      description: 'Autoscales the number of pollers for Nexus Tasks based on load.',
      lines: [9],
    },
  ]}
>
```java
public class WorkerExample {
    public static void main(String[] args) {
        WorkflowServiceStubs service = WorkflowServiceStubs.newLocalServiceStubs();
        WorkflowClient client = WorkflowClient.newInstance(service);
        WorkerFactory factory = WorkerFactory.newInstance(client);
        WorkerOptions workerOptions = WorkerOptions.newBuilder()
            .setWorkflowTaskPollersBehavior(new PollerBehaviorAutoscaling())
            .setActivityTaskPollersBehavior(new PollerBehaviorAutoscaling())
            .setNexusTaskPollersBehavior(new PollerBehaviorAutoscaling())
            .build();

        Worker worker = factory.newWorker("my-task-queue", workerOptions);
    }
}
```

**Python**

[Python SDK docs](https://python.temporal.io/temporalio.worker.PollerBehaviorAutoscaling.html)
  annotations={[
    {
      label: 'Workflow Task poller',
      description: 'Autoscales the number of pollers for Workflow Tasks based on load.',
      lines: [7],
    },
    {
      label: 'Activity Task poller',
      description: 'Autoscales the number of pollers for Activity Tasks based on load.',
      lines: [8],
    },
    {
      label: 'Nexus Task poller',
      description: 'Autoscales the number of pollers for Nexus Tasks based on load.',
      lines: [9],
    },
  ]}
>
```python
worker = Worker(
    client,
    task_queue="my-task-queue",
    workflows=[MyWorkflow],
    activities=[my_activity],

    workflow_task_poller_behavior=PollerBehaviorAutoscaling(),
    activity_task_poller_behavior=PollerBehaviorAutoscaling(),
    nexus_task_poller_behavior=PollerBehaviorAutoscaling(),
)
```

**TypeScript**

[TypeScript SDK docs](https://typescript.temporal.io/api/interfaces/proto.temporal.api.sdk.v1.WorkerConfig.IAutoscalingPollerBehavior)
  annotations={[
    {
      label: 'Workflow Task poller',
      description: 'Autoscales the number of pollers for Workflow Tasks based on load.',
      lines: [7],
    },
    {
      label: 'Activity Task poller',
      description: 'Autoscales the number of pollers for Activity Tasks based on load.',
      lines: [8],
    },
    {
      label: 'Nexus Task poller',
      description: 'Autoscales the number of pollers for Nexus Tasks based on load.',
      lines: [9],
    },
  ]}
>
```ts
const worker = await Worker.create({
  connection,
  taskQueue: 'my-task-queue',
  workflowsPath: require.resolve('./workflows'),
  activities,

  workflowTaskPollerBehavior: PollerBehavior.autoscaling(),
  activityTaskPollerBehavior: PollerBehavior.autoscaling(),
  nexusTaskPollerBehavior: PollerBehavior.autoscaling(),
});
```

**.NET**

[DotNet SDK docs](https://dotnet.temporal.io/api/Temporalio.Worker.Tuning.PollerBehavior.Autoscaling.html)
  annotations={[
    {
      label: 'Workflow Task poller',
      description: 'Autoscales the number of pollers for Workflow Tasks based on load.',
      lines: [5],
    },
    {
      label: 'Activity Task poller',
      description: 'Autoscales the number of pollers for Activity Tasks based on load.',
      lines: [6],
    },
    {
      label: 'Nexus Task poller',
      description: 'Autoscales the number of pollers for Nexus Tasks based on load.',
      lines: [7],
    },
  ]}
>
```csharp
using var worker = new TemporalWorker(
    client,
    new TemporalWorkerOptions("my-task-queue")
    {
        WorkflowTaskPollerBehavior = new PollerBehavior.Autoscaling(),
        ActivityTaskPollerBehavior = new PollerBehavior.Autoscaling(),
        NexusTaskPollerBehavior = new PollerBehavior.Autoscaling(),
    }
    .AddWorkflow<MyWorkflow>()
    .AddActivity(MyActivities.MyActivity)
);
```

**Ruby**

[Ruby SDK docs](https://ruby.temporal.io/Temporalio/Worker/PollerBehavior/Autoscaling.html)
  annotations={[
    {
      label: 'Workflow Task poller',
      description: 'Autoscales the number of pollers for Workflow Tasks based on load.',
      lines: [7],
    },
    {
      label: 'Activity Task poller',
      description: 'Autoscales the number of pollers for Activity Tasks based on load.',
      lines: [8],
    },
    {
      label: 'Nexus Task poller',
      description: 'Autoscales the number of pollers for Nexus Tasks based on load.',
      lines: [9],
    },
  ]}
>
```ruby
worker = Temporalio::Worker.new(
  client,
  'my-task-queue',
  workflows: [MyWorkflow],
  activities: [MyActivity],

  workflow_task_poller_behavior: Temporalio::Worker::PollerBehavior::Autoscaling.new,
  activity_task_poller_behavior: Temporalio::Worker::PollerBehavior::Autoscaling.new,
  nexus_task_poller_behavior: Temporalio::Worker::PollerBehavior::Autoscaling.new,
)
```

### Cache options (Java SDK) 

A [Workflow Cache](/workflow-execution#workflow-cache) is created and shared between all Workers on a single host.
It's designed to limit the resources used by the cache for each host/process.
These options are defined on `WorkerFactoryOptions`:

- `WorkerFactoryOptions#workflowCacheSize` defines the maximum number of cached Workflow Executions.
  Each cached Workflow contains at least one Workflow thread and its resources (memory, etc.).
- `maxWorkflowThreadCount` defines the maximum number of Workflow threads that may exist concurrently at any time.

These cache options limit the resource consumption of the in-memory Workflow cache.
Workflow cache options are shared between all Workers because the Workflow cache is tightly integrated with the resource consumption of the entire host.
This includes memory and the total thread count, which should be limited per host/JVM.

For Go, use [`SetStickyWorkflowCacheSize`](https://pkg.go.dev/go.temporal.io/sdk/worker#SetStickyWorkflowCacheSize). For Python, use the `max_cached_workflows` Worker option.

### "Large value" drawbacks

There are drawbacks when you use "large values everywhere."
As with any multithreading system, specifying excessively large values without monitoring with the SDK and system metrics leads to constant resource contention/stealing
This decreases the total throughput and increases latency jitter of the system.

### Invariants (JavaSDK only) 

These properties should always be true for a Worker's configuration.

Perform this sanity check after the adjustments to Worker settings.

1. `workflowCacheSize` should be ≤ `maxWorkflowThreadCount`. Each Workflow has at least one Workflow thread.
2. `maxConcurrentWorkflowTaskExecutionSize` should be ≤ `maxWorkflowThreadCount`. It's recommended that `maxWorkflowThreadCount` be at least 2x of `maxConcurrentWorkflowTaskExecutionSize`. This is because having more Worker slots than the Workflow cache size will lead to resource allocation issues between executors and cause unpredictable delays.
3. `maxConcurrentWorkflowTaskPollers` should be significantly ≤ `maxConcurrentWorkflowTaskExecutionSize`. And `maxConcurrentActivityTaskPollers` should be significantly ≤ `maxConcurrentActivityExecutionSize`. The number of pollers should always be lower than the number of executors.
