# Dynamic Workflow - .NET SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> This section explains Dynamic Workflows with the .NET SDK

## Set a Dynamic Workflow 

A Dynamic Workflow in Temporal is a Workflow that is invoked dynamically at runtime if no other Workflow with the same name is registered.
A Workflow can be made dynamic by setting `Dynamic` as `true` on the `[Workflow]` attribute.
You must register the Workflow with the Worker before it can be invoked.
Only one Dynamic Workflow can be present on a Worker.

The Workflow Definition must then accept a single argument of type `Temporalio.Converters.IRawValue[]`.
The [Workflow.PayloadConverter](https://dotnet.temporal.io/api/Temporalio.Workflows.Workflow.html#Temporalio_Workflows_Workflow_PayloadConverter) property is used to convert an `IRawValue` object to the desired type using extension methods in the `Temporalio.Converters` namespace.

```csharp
[Workflow(Dynamic = true)]
public class DynamicWorkflow
{
    [WorkflowRun]
    public async Task<string> RunAsync(IRawValue[] args)
    {
        var name = Workflow.PayloadConverter.ToValue<string>(args.Single());
        var param = MyActivityParams("Hello", name);
        return await Workflow.ExecuteActivityAsync(
            (MyActivities a) => a.MyActivity(param),
            new() { StartToCloseTimeout = TimeSpan.FromMinutes(5) });
    }
}
```
