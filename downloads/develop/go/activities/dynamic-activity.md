# Dynamic Activity - Go SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Register one Dynamic Activity per Worker with RegisterDynamicActivity to handle Activity Types that match no other registered Activity.

## Set a Dynamic Activity 

A Dynamic Activity in Temporal is an Activity that is invoked dynamically at runtime if no other Activity with the same name is registered.
An Activity can be registered as dynamic by using `worker.RegisterDynamicActivity()`.
You must register the Activity with the Worker before it can be invoked.
Only one Dynamic Activity can be present on a Worker.

The Activity Definition must then accept a single argument of type `converter.EncodedValues`.
This code snippet is taken from the [Dynamic Workflow example from samples-go](https://github.com/temporalio/samples-go/tree/main/dynamic-workflows).

```go
func DynamicActivity(ctx context.Context, args converter.EncodedValues) (string, error) {
	var arg1, arg2 string
	err := args.Get(&arg1, &arg2)
	if err != nil {
		return "", fmt.Errorf("failed to decode arguments: %w", err)
	}

	info := activity.GetInfo(ctx)
	result := fmt.Sprintf("%s - %s - %s", info.WorkflowType.Name, arg1, arg2)

	return result, nil
}
```
