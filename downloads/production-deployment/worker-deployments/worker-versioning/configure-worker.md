# Configure a Worker for Versioning

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Enable Worker Versioning on your Workers with UseVersioning, Deployment Version, and default Versioning Behavior.

You'll need to add a few additional configuration parameters to your Workers to toggle on Worker Versioning. There are
three new parameters, with different names depending on the language:

- `UseVersioning`: This enables the Versioning functionality for this Worker.
- A `Version` to identify the revision that this Worker will be allowed to execute. This is a combination of a
  deployment name and a build ID number.
- (Optional) The [Default Versioning Behavior](/production-deployment/worker-deployments/worker-versioning#definition). If unset, you'll be required to specify the behavior on
  each Workflow. Or you can default to Pinned or Auto-Upgrade.

Follow the example for your SDK below. Select a concept to highlight the matching lines:

**Go**

  annotations={[
    {
      label: 'UseVersioning',
      description:
        'Enables Worker Versioning for this Worker so Tasks are matched to Deployment Versions.',
      lines: [4],
    },
    {
      label: 'Version',
      description:
        'Identifies the revision this Worker may execute: a deployment name plus a Build ID.',
      lines: [5, 6, 7, 8],
    },
    {
      label: 'Default Versioning Behavior',
      description:
        'Optional. If unset, you must set the Versioning Behavior on each Workflow. Otherwise default to Pinned or Auto-Upgrade.',
      lines: [9],
    },
  ]}
>
```go
buildID := mustGetEnv("MY_BUILD_ID")
w := worker.New(c, myTaskQueue, worker.Options{
  DeploymentOptions: worker.DeploymentOptions{
    UseVersioning: true,
    Version: worker.WorkerDeploymentVersion{
      DeploymentName: "llm_srv",
      BuildID: buildID,
    },
    DefaultVersioningBehavior: workflow.VersioningBehaviorUnspecified,
  },
})
```

**Java**

  annotations={[
    {
      label: 'UseVersioning',
      description:
        'Enables Worker Versioning for this Worker so Tasks are matched to Deployment Versions.',
      lines: [10],
    },
    {
      label: 'Version',
      description:
        'Identifies the revision this Worker may execute: a deployment name plus a Build ID.',
      lines: [9],
    },
    {
      label: 'Default Versioning Behavior',
      description:
        'Optional. If unset, you must set the Versioning Behavior on each Workflow. Otherwise default to Pinned or Auto-Upgrade.',
      lines: [11],
    },
  ]}
>
```java
import io.temporal.worker.WorkerOptions;
import io.temporal.common.VersioningBehavior;
import io.temporal.common.WorkerDeploymentVersion;
import io.temporal.worker.WorkerDeploymentOptions;

WorkerOptions.newBuilder()
  .setDeploymentOptions(
      WorkerDeploymentOptions.newBuilder()
      .setVersion(new WorkerDeploymentVersion("llm_srv", "1.0"))
      .setUseVersioning(true)
      .setDefaultVersioningBehavior(VersioningBehavior.AUTO_UPGRADE)
      .build())
  .build();
```

**Python**

  annotations={[
    {
      label: 'UseVersioning',
      description:
        'Enables Worker Versioning for this Worker so Tasks are matched to Deployment Versions.',
      lines: [13],
    },
    {
      label: 'Version',
      description:
        'Identifies the revision this Worker may execute: a deployment name plus a Build ID.',
      lines: [10, 11, 12],
    },
    {
      label: 'Default Versioning Behavior',
      description:
        'Optional. If unset, you must set the Versioning Behavior on each Workflow. Otherwise default to Pinned or Auto-Upgrade.',
      lines: [14],
    },
  ]}
>
```python
from temporalio.common import WorkerDeploymentVersion, VersioningBehavior
from temporalio.worker import Worker, WorkerDeploymentConfig

Worker(
    client,
    task_queue="mytaskqueue",
    workflows=workflows,
    activities=activities,
    deployment_config=WorkerDeploymentConfig(
        version=WorkerDeploymentVersion(
            deployment_name="llm_srv",
            build_id=my_env.build_id),
        use_worker_versioning=True,
        default_versioning_behavior=VersioningBehavior.UNSPECIFIED
    ),
)
```

**TypeScript**

  annotations={[
    {
      label: 'UseVersioning',
      description:
        'Enables Worker Versioning for this Worker so Tasks are matched to Deployment Versions.',
      lines: [5],
    },
    {
      label: 'Version',
      description:
        'Identifies the revision this Worker may execute: a deployment name plus a Build ID.',
      lines: [6],
    },
    {
      label: 'Default Versioning Behavior',
      description:
        'Optional. This TypeScript example does not set a default; set Versioning Behavior on each Workflow, or add a default when your SDK supports it on Worker options.',
      lines: [],
    },
  ]}
>
```ts
const myWorker = await Worker.create({
  workflowsPath: require.resolve('./workflows'),
  taskQueue,
  workerDeploymentOptions: {
    useWorkerVersioning: true,
    version: { buildId: '1.0', deploymentName: 'llm_srv' },
  },
  connection: nativeConnection,
});
```

**.NET**

  annotations={[
    {
      label: 'UseVersioning',
      description:
        'Enables Worker Versioning for this Worker so Tasks are matched to Deployment Versions.',
      lines: [5],
    },
    {
      label: 'Version',
      description:
        'Identifies the revision this Worker may execute: a deployment name plus a Build ID.',
      lines: [5],
    },
    {
      label: 'Default Versioning Behavior',
      description:
        'Optional. If unset, you must set the Versioning Behavior on each Workflow. Otherwise default to Pinned or Auto-Upgrade.',
      lines: [7],
    },
  ]}
>
```csharp
var myWorker = new TemporalWorker(
    Client,
    new TemporalWorkerOptions(taskQueue)
    {
      DeploymentOptions = new(new("llm_srv", "1.0"), true)
      {
        DefaultVersioningBehavior = VersioningBehavior.Unspecified,
      },
    }.AddWorkflow<MyWorkflow>());
```

**Ruby**

  annotations={[
    {
      label: 'UseVersioning',
      description:
        'Enables Worker Versioning for this Worker so Tasks are matched to Deployment Versions.',
      lines: [10],
    },
    {
      label: 'Version',
      description:
        'Identifies the revision this Worker may execute: a deployment name plus a Build ID.',
      lines: [6, 7, 8, 9],
    },
    {
      label: 'Default Versioning Behavior',
      description:
        'Optional. If unset, you must set the Versioning Behavior on each Workflow. Otherwise default to Pinned or Auto-Upgrade.',
      lines: [11],
    },
  ]}
>
```ruby
worker = Temporalio::Worker.new(
  client: client,
  task_queue: task_queue,
  workflows: [MyWorkflow],
  deployment_options: Temporalio::Worker::DeploymentOptions.new(
      version: Temporalio::WorkerDeploymentVersion.new(
          deployment_name: 'llm_srv',
          build_id: '1.0'
      ),
      use_worker_versioning: true,
      default_versioning_behavior: Temporalio::VersioningBehavior::UNSPECIFIED
  )
)
```
