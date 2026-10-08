# Timeouts and Retry Policies

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Detect Workflow and Activity failures with timeouts, then mitigate them with automatic retries. Configuration guides for every Temporal SDK.

In Temporal, timeouts detect application failures.
The system can then automatically mitigate these failures through retries.
Both major application function primitives, **[Workflows](/workflows)** and **[Activities](/activities)**, have dedicated **timeout configurations** and can be configured with a **[Retry Policy](/encyclopedia/retry-policies)**.

Follow one of our tutorials to [Get started](https://learn.temporal.io/getting_started/) exploring timeouts and Retry Policies.

## Workflow timeouts

Each Workflow timeout limits a different aspect of a [Workflow Execution](/workflow-execution), and you set them when you start the Workflow Execution.

- **[Workflow Execution Timeout](/encyclopedia/detecting-workflow-failures#workflow-execution-timeout)**: the maximum time a Workflow Execution can stay Open, including retries and any use of [Continue-As-New](/workflow-execution/continue-as-new). The default is infinite.
- **[Workflow Run Timeout](/encyclopedia/detecting-workflow-failures#workflow-run-timeout)**: the maximum duration of a single [Workflow Run](/workflow-execution/workflowid-runid#run-id), which excludes retries and Continue-As-New. The default matches the Workflow Execution Timeout.
- **[Workflow Task Timeout](/encyclopedia/detecting-workflow-failures#workflow-task-timeout)**: the maximum time a [Worker](/workers#worker) has to execute a [Workflow Task](/tasks#workflow-task) after picking it up from the [Task Queue](/task-queue). The default is 10 seconds, with a maximum of 120 seconds.

Workflows are built to run for long periods and to survive failures, so most applications don't need a Workflow Execution Timeout or Workflow Run Timeout.
A timeout limits how long a Workflow can absorb delays. To act after a set period inside a Workflow, use a [Timer](/workflow-execution/timers-delays) instead.
Workflow Execution and Workflow Run Timeouts are most often used to bound a [Temporal Cron Job](/cron-job).

Set Workflow timeouts and Retry Policies in your language:

- [.NET SDK](/develop/dotnet/workflows/timeouts): Set Workflow timeouts and Retry Policies in C# and .NET.
- [Go SDK](/develop/go/workflows/timeouts): Set Workflow timeouts and Retry Policies in Go.
- [Java SDK](/develop/java/workflows/timeouts): Set Workflow timeouts and Retry Policies in Java and other JVM languages.
- [PHP SDK](/develop/php/workflows/timeouts): Set Workflow timeouts and Retry Policies in PHP.
- [Python SDK](/develop/python/workflows/timeouts): Set Workflow timeouts and Retry Policies in Python.
- [Ruby SDK](/develop/ruby/workflows/timeouts): Set Workflow timeouts and Retry Policies in Ruby.
- [Rust SDK](/develop/rust/workflows/timeouts): Set Workflow timeouts and Retry Policies in Rust.
- [TypeScript SDK](/develop/typescript/workflows/timeouts): Set Workflow timeouts and Retry Policies in TypeScript and JavaScript.

## Activity timeouts

Activity timeouts tell the caller — a Workflow, or the Client for a [Standalone Activity](/standalone-activity) — which kind of Activity failure occurred, and the Activity's [Retry Policy](/encyclopedia/retry-policies) decides what happens next.

- **[Schedule-To-Start Timeout](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout)**: the maximum time an [Activity Task](/tasks#activity-task) can sit in the Task Queue before a Worker picks it up. The default is infinite, and this timeout never triggers a retry, because a retry would return the Activity Task to the same Task Queue.
- **[Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout)**: the maximum time for a single [Activity Task Execution](/tasks#activity-task-execution). It has no default of its own. If you set only a Schedule-To-Close Timeout, Start-To-Close uses that value.
- **[Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout)**: the maximum time for the whole [Activity Execution](/activity-execution), from the first Activity Task being scheduled to the last one closing. The default is infinite.
- **[Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout)**: the maximum time between [Activity Heartbeats](/encyclopedia/detecting-activity-failures#activity-heartbeat), the pings a Worker sends to report that an Activity Execution is still making progress.

Every Activity Execution needs either a Start-To-Close or a Schedule-To-Close Timeout.
Set Start-To-Close: the [Temporal Service](/temporal-service) can't tell when a Worker crashes or loses contact, so it relies on this timeout to retry the Activity.
Long-running Activities should also Heartbeat and set a Heartbeat Timeout, which detects a lost Worker sooner than a long Start-To-Close Timeout can.

Set Activity timeouts and Retry Policies in your language:

- [.NET SDK](/develop/dotnet/activities/timeouts): Set Activity timeouts and Retry Policies in C# and .NET.
- [Go SDK](/develop/go/activities/timeouts): Set Activity timeouts and Retry Policies in Go.
- [Java SDK](/develop/java/activities/timeouts): Set Activity timeouts and Retry Policies in Java and other JVM languages.
- [PHP SDK](/develop/php/activities/timeouts): Set Activity timeouts and Retry Policies in PHP.
- [Python SDK](/develop/python/activities/timeouts): Set Activity timeouts and Retry Policies in Python.
- [Ruby SDK](/develop/ruby/activities/timeouts): Set Activity timeouts and Retry Policies in Ruby.
- [Rust SDK](/develop/rust/activities/timeouts): Set Activity timeouts and Retry Policies in Rust.
- [TypeScript SDK](/develop/typescript/activities/timeouts): Set Activity timeouts and Retry Policies in TypeScript and JavaScript.

## Resources

For a deep dive into timeouts and Retry Policies visit the following Temporal Encyclopedia pages or enroll in one of [our courses](https://learn.temporal.io/courses/).

- [Detecting Workflow failures](/encyclopedia/detecting-workflow-failures): Workflow Execution, Workflow Run, and Workflow Task Timeouts in detail, plus how to find Workflows with failed Workflow Tasks.
- [Detecting Activity failures](/encyclopedia/detecting-activity-failures): Schedule-To-Start, Start-To-Close, Schedule-To-Close, and Heartbeat Timeouts in detail, plus which Activities should Heartbeat.
- [Retry Policies](/encyclopedia/retry-policies): How attempts, intervals, backoff coefficients, and non-retryable errors shape a retry.
