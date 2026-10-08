# Dynamic Workflow - Go SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> This section explains Dynamic Workflows with the Go SDK

## Set a Dynamic Workflow 

A Dynamic Workflow in Temporal is a Workflow that is invoked dynamically at runtime if no other Workflow with the same name is registered.
A Workflow can be registered as dynamic by using `worker.RegisterDynamicWorkflow()`.
You must register the Workflow with the Worker before it can be invoked.
Only one Dynamic Workflow can be present on a Worker.

The Workflow Definition must then accept a single argument of type `converter.EncodedValues`.
This code snippet is taken from the [Dynamic Workflow example from samples-go](https://github.com/temporalio/samples-go/tree/main/dynamic-workflows).

```go
func DynamicWorkflow(ctx workflow.Context, args converter.EncodedValues) (string, error) {
	var result string
	info := workflow.GetInfo(ctx)

	var arg1, arg2 string
	err := args.Get(&arg1, &arg2)
	if err != nil {
		return "", fmt.Errorf("failed to decode arguments: %w", err)
	}

	if info.WorkflowType.Name == "dynamic-activity" {
		ctx = workflow.WithActivityOptions(ctx, workflow.ActivityOptions{StartToCloseTimeout: 10 * time.Second})
		err := workflow.ExecuteActivity(ctx, "random-activity-name", arg1, arg2).Get(ctx, &result)
		if err != nil {
			return "", err
		}
	} else {
		result = fmt.Sprintf("%s - %s - %s", info.WorkflowType.Name, arg1, arg2)
	}

	return result, nil
}
```
