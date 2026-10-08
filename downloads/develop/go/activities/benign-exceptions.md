# Benign exceptions - Go SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Mark expected or non-severe Activity errors as benign in Go to reduce noise in logs, metrics, and OpenTelemetry traces.

When Activities return errors that are expected or not severe, they can create noise in your logs, metrics, and OpenTelemetry traces, making it harder to identify real issues.
By marking these errors as benign, you can exclude them from your observability data while still handling them in your Workflow logic.

To mark an error as benign, use [`temporal.NewApplicationErrorWithOptions`](https://pkg.go.dev/go.temporal.io/sdk/temporal#NewApplicationErrorWithOptions) and set the `Category` field to `temporal.ApplicationErrorCategoryBenign` in the `ApplicationErrorOptions`.

Benign errors:
- Have Activity failure logs downgraded to DEBUG level
- Do not emit Activity failure metrics
- Do not set the OpenTelemetry failure status to ERROR

```go
import (
	"go.temporal.io/sdk/activity"
	"go.temporal.io/sdk/temporal"
)

func MyActivity(ctx context.Context) (string, error) {
	result, err := callExternalService()
	if err != nil {
		// Mark this error as benign since it's expected
		return "", temporal.NewApplicationErrorWithOptions(
			err.Error(),
			"",
			temporal.ApplicationErrorOptions{
				Category: temporal.ApplicationErrorCategoryBenign,
			},
		)
	}
	return result, nil
}
```

Use benign exceptions for Activity errors that occur regularly as part of normal operations, such as polling an external service that isn't ready yet, or handling expected transient failures that will be retried.
