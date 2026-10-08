# Schedules

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> A Schedule starts Workflows on an interval or calendar expression, with Overlap Policy, Catchup Window, backfill, and pause controls the Temporal Service runs for you.

A [Schedule](/schedule) starts a [Workflow Execution](/workflow-execution) at times you define: on an interval, on a calendar expression, or on a combination of both.

A Schedule is its own object in the Temporal Service with its own Id, separate from the Workflow Executions it starts.
You can update, pause, backfill, or trigger it without changing or redeploying the Workflow code it runs.

That separation is what you get instead of running a scheduler alongside your application.
There's no second system to deploy, monitor, and reconcile with your Workers, and every start the Schedule makes is an ordinary Workflow Execution with the same durability, retries, and [Event History](/workflow-execution/event#event-history) as one you start by hand.

## What a Schedule controls

- **Spec.** When Actions happen: an interval (`45m`, or `6h/5h` for every six hours offset into the fifth hour) or a calendar expression, given as a cron string (`0 8 * * 1-5`, weekdays at 8:00 UTC) or as JSON with named fields (`{"dayOfMonth": "1,15", "hour": "11-14"}`). One Spec can combine several of each and add start and end times, exclusions, jitter, and a time zone. Exclusions and embedded time zone data are available through the SDKs and API, but not the CLI or Web UI.
- **[Overlap Policy](/schedule#overlap-policy).** What happens when it's time to start and the previous Execution is still running: `Skip` (the default), `BufferOne`, `BufferAll`, `CancelOther`, `TerminateOther`, or `AllowAll`.
- **[Catchup Window](/schedule#catchup-window).** Which missed Actions to take when the Temporal Service was unavailable at the scheduled time. The default is one year; the minimum is ten seconds.
- **[Pause-on-failure](/schedule#pause-on-failure).** Pause the Schedule automatically when a scheduled Execution ends in failure or timeout.
- **[Backfill](/schedule#backfill).** Run every Action for a past time range now, including a range from before the Schedule existed.
- **[Action limit](/schedule#limit-number-of-actions).** Stop after a set number of scheduled Actions, after which the Schedule behaves as paused.

Every Execution a Schedule starts carries the `TemporalScheduledStartTime` and `TemporalScheduledById` [Search Attributes](/search-attribute), so you can query scheduled runs with a [List Filter](/list-filter) the same way you query anything else.

## What a Schedule doesn't do

- **Pausing a Schedule doesn't pause what's already running.** It stops future Actions. Executions the Schedule already started keep going.
- **A Paused Workflow Execution still counts as running.** When the Schedule evaluates its Overlap Policy, a Paused Execution is an open Execution, so `Skip` skips and `BufferOne` buffers behind it. See [Interaction with Workflow Pause](/schedule#workflow-pause).
- **Listing Schedules is eventually consistent.** `ListSchedules` and `CountSchedules` are served by [Visibility](/visibility#operations-that-use-visibility) and share its rate limit, so a Schedule you just created or deleted may not appear right away.

## How to choose between a Schedule, a Cron Job, and Start Delay

- **Use a Schedule when the same Workflow has to run more than once.** It's the right choice as soon as you need to pause the series during an incident, change the timing without a deploy, or run the Actions an outage skipped. Use it for new applications even when the timing is a plain cron expression, because you get those controls whether or not you need them yet.
- **Use [Start Delay](/workflow-execution/timers-delays#delay-workflow-execution) when there's exactly one run, at a time you know when you start it.** A trial expiry, a cancellation deadline, a reminder. It isn't recurring, and it's incompatible with both Schedules and Cron Jobs, so it's not a way to hold off the first Action of a Schedule. Set a start time on the Schedule Spec for that.
- **Keep a [Temporal Cron Job](/cron-job) if you have one running, but don't write new ones.** A cron string is a property of the Workflow Execution rather than a separate object, so the next Run starts only after the current one closes, and changing or stopping the series means terminating the Workflow. A Schedule covers the same cases and lets you update it in place.

If the waiting happens inside a Workflow that's already running, none of these apply. Use a [Timer](/workflow-execution/timers-delays#timer).

## Resources

- [Schedule](/schedule): Full reference for Spec, Policies, Backfill, last completion result, and the limitations of Schedules.
- [Temporal Cron Job](/cron-job): How Cron Schedules behave, the supported cron syntax, time zone caveats, and how to stop a Cron Job.
- [Timers and Start Delay](/workflow-execution/timers-delays): Durable Timers inside a Workflow, and Start Delay for a one-time start at a future point.
- [temporal schedule](/cli/command-reference/schedule): CLI commands to create, backfill, delete, describe, list, pause, trigger, and update a Schedule.
- [Missed Schedule Actions](/troubleshooting/schedule-missed-actions): Alert on the missed catchup window metric, then narrow down which Schedule skipped an Action and why.

Or jump straight to the SDK feature guide for implementation details:

- [.NET SDK](/develop/dotnet/workflows/schedules): Create, backfill, delete, describe, list, pause, trigger, and update Schedules in C# and .NET.
- [Go SDK](/develop/go/workflows/schedules): Create, backfill, delete, describe, list, pause, trigger, and update Schedules in Go.
- [Java SDK](/develop/java/workflows/schedules): Create, backfill, delete, describe, list, pause, trigger, and update Schedules in Java and other JVM languages.
- [PHP SDK](/develop/php/workflows/schedules): Create, backfill, delete, describe, list, pause, trigger, and update Schedules in PHP.
- [Python SDK](/develop/python/workflows/schedules): Create, backfill, delete, describe, list, pause, trigger, and update Schedules in Python.
- [Ruby SDK](/develop/ruby/workflows/schedules): Create, backfill, delete, describe, list, pause, trigger, and update Schedules in Ruby.
- [TypeScript SDK](/develop/typescript/workflows/schedules): Create, backfill, delete, describe, list, pause, trigger, and update Schedules in TypeScript.
