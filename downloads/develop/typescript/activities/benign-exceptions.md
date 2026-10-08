# Benign exceptions - TypeScript SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Mark expected or non-severe Activity errors as benign in TypeScript to reduce noise in logs, metrics, and OpenTelemetry traces.

When Activities throw errors that are expected or not severe, they can create noise in your logs, metrics, and OpenTelemetry traces, making it harder to identify real issues.
By marking these errors as benign, you can exclude them from your observability data while still handling them in your Workflow logic.

To mark an error as benign, set the `category` field to `ApplicationFailureCategory.BENIGN` when creating an [`ApplicationFailure`](https://typescript.temporal.io/api/classes/common.ApplicationFailure).

Benign errors:
- Have Activity failure logs downgraded to DEBUG level
- Do not emit Activity failure metrics
- Do not set the OpenTelemetry failure status to ERROR

```typescript
import {
  ApplicationFailure,
  ApplicationFailureCategory,
} from '@temporalio/common';

export async function myActivity(): Promise<string> {
  try {
    return await callExternalService();
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    throw ApplicationFailure.create({
      message,
      // Mark this error as benign since it's expected
      category: ApplicationFailureCategory.BENIGN,
    });
  }
}
```

Use benign exceptions for Activity errors that occur regularly as part of normal operations, such as polling an external service that isn't ready yet, or handling expected transient failures that will be retried.
