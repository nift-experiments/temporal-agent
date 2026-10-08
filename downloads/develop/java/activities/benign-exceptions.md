# Benign exceptions - Java SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Mark expected or non-severe Activity errors as benign in Java to reduce noise in logs, metrics, and OpenTelemetry traces.

When Activities throw errors that are expected or not severe, they can create noise in your logs, metrics, and OpenTelemetry traces, making it harder to identify real issues.
By marking these errors as benign, you can exclude them from your observability data while still handling them in your Workflow logic.

To mark an error as benign, set the category to `ApplicationErrorCategory.BENIGN` using the [`ApplicationFailure`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/failure/ApplicationFailure.html) builder.

Benign errors:
- Have Activity failure logs downgraded to DEBUG level
- Do not emit Activity failure metrics
- Do not set the OpenTelemetry failure status to ERROR

```java
import io.temporal.activity.ActivityInterface;
import io.temporal.activity.ActivityMethod;
import io.temporal.failure.ApplicationErrorCategory;
import io.temporal.failure.ApplicationFailure;

@ActivityInterface
public interface MyActivities {
  @ActivityMethod
  String myActivity();
}

public class MyActivitiesImpl implements MyActivities {
  @Override
  public String myActivity() {
    try {
      return callExternalService();
    } catch (Exception e) {
      // Mark this error as benign since it's expected
      throw ApplicationFailure.newBuilder()
          .setMessage(e.getMessage())
          .setType(e.getClass().getName())
          .setCause(e)
          .setCategory(ApplicationErrorCategory.BENIGN)
          .build();
    }
  }
}
```

Use benign exceptions for Activity errors that occur regularly as part of normal operations, such as polling an external service that isn't ready yet, or handling expected transient failures that will be retried.
