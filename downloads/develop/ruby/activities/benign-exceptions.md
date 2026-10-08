# Benign exceptions - Ruby SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Mark expected or non-severe Activity errors as benign in Ruby to reduce noise in logs, metrics, and OpenTelemetry traces.

When Activities throw errors that are expected or not severe, they can create noise in your logs, metrics, and OpenTelemetry traces, making it harder to identify real issues.
By marking these errors as benign, you can exclude them from your observability data while still handling them in your Workflow logic.

To mark an error as benign, set the `category` parameter to `Temporalio::Error::ApplicationError::Category::BENIGN` when raising an `ApplicationError`.

Benign errors:
- Have Activity failure logs downgraded to DEBUG level
- Do not emit Activity failure metrics
- Do not set the OpenTelemetry failure status to ERROR

```ruby
require 'temporalio/activity'

class MyActivity < Temporalio::Activity::Definition
  def execute
    begin
      call_external_service
    rescue StandardError => e
      # Mark this error as benign since it's expected
      raise Temporalio::Error::ApplicationError.new(
        e.message,
        category: Temporalio::Error::ApplicationError::Category::BENIGN
      )
    end
  end
end
```

Use benign exceptions for Activity errors that occur regularly as part of normal operations, such as polling an external service that isn't ready yet, or handling expected transient failures that will be retried.
