# Timers - PHP SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Set a durable Timer in PHP with Workflow::timer(). Timers persist across Worker downtime, and a single Worker can run millions of them.

## What is a Timer? 

A Workflow can set a durable timer for a fixed time period.
In some SDKs, the function is called `sleep()`, and in others, it's called `timer()`.

A Workflow can sleep for months.
Timers are persisted, so even if your Worker or Temporal Service is down when the time period completes, as soon as your Worker and Temporal Service are back up, the `sleep()` call will resolve and your code will continue executing.

Sleeping is a resource-light operation: it does not tie up the process, and you can run millions of Timers off a single Worker.

To set a Timer in PHP, use `Workflow::timer()` and pass the number of seconds you want to wait before continuing.

The following example yields a sleep method for 5 minutes.

```php
yield Workflow::timer(300); // sleep for 5 minutes
```

You cannot set a Timer invocation inside the `await` or `awaitWithTimeout` methods.
