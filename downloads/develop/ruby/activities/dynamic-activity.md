# Dynamic Activities - Ruby SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Register one Dynamic Activity per Worker with activity_dynamic to handle Activity Types that match no other registered Activity.

## Set a Dynamic Activity 

A Dynamic Activity in Temporal is an Activity that is invoked dynamically at runtime if no other Activity with the same name is registered.
An Activity can be made dynamic by invoking `activity_dynamic` class method at the top of the definition.
You must register the Activity with the Worker before it can be invoked.
Only one Dynamic Activity can be present on a Worker.

Often, dynamic is used in conjunction with `activity_raw_args` which does not convert arguments but instead passes them
through as a splatted array of `Temporalio::Converters::RawValue` instances.

```ruby
class MyDynamicActivity < Temporalio::Activity::Definition
  # Make this the dynamic activity and accept raw args
  activity_dynamic
  activity_raw_args

  def execute(*raw_args)
    raise Temporalio::Error::ApplicationError, 'One arg expected' unless raw_args.size == 1

    # Use payload converter to convert it
    input = Temporalio::Activity::Context.current.payload_converter.from_payload(raw_args.first.payload)
    "#{input['greeting']}, #{input['name']}!"
  end
end
```
