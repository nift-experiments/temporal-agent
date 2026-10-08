# Benign exceptions - Python SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Mark expected or non-severe Activity errors as benign in Python to reduce noise in logs, metrics, and OpenTelemetry traces.

When Activities throw errors that are expected or not severe, they can create noise in your logs, metrics, and OpenTelemetry traces, making it harder to identify real issues.
By marking these errors as benign, you can exclude them from your observability data while still handling them in your Workflow logic.

To mark an error as benign, set the `category` parameter to `ApplicationErrorCategory.BENIGN` when raising an [`ApplicationError`](https://python.temporal.io/temporalio.exceptions.ApplicationError.html).

Benign errors:
- Have Activity failure logs downgraded to DEBUG level
- Do not emit Activity failure metrics
- Do not set the OpenTelemetry failure status to ERROR

```python
from temporalio import activity
from temporalio.exceptions import ApplicationError, ApplicationErrorCategory

@activity.defn
async def my_activity() -> str:
    try:
        return await call_external_service()
    except Exception as err:
        raise ApplicationError(
            message=str(err),
            # Mark this error as benign since it's expected
            category=ApplicationErrorCategory.BENIGN,
        )
```

Use benign exceptions for Activity errors that occur regularly as part of normal operations, such as polling an external service that isn't ready yet, or handling expected transient failures that will be retried.
