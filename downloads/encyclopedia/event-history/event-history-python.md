# Event History walkthrough with the Python SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

In order to understand how Workflow Replay works, this page will go through the following walkthroughs:

1. [How Workflow code maps to Commands](#How-Workflow-Code-Maps-To-Commands)
2. [How Workflow Commands map to Events](#How-Workflow-Commands-Map-To-Events)
3. [How History Replay provides Durable Execution](#How-History-Replay-Provides-Durable-Execution)
4. [Example of a non-deterministic Workflow Definition](#Example-of-Non-Deterministic-Workflow)

## How Workflow code maps to Commands 

This walkthrough will cover how the Workflow code maps to Commands that get sent to the Temporal Service, letting the
Temporal Service know what to do.

Step through the Workflow Definition below. Each step highlights the statements the Worker is running and shows the
Commands it has issued so far.

```python
@workflow.defn
class PizzaOrderWorkflow:
    @workflow.run
    async def order_pizza(self, order: PizzaOrder) -> OrderConfirmation:
        total_price = sum(pizza.price for pizza in order.items)

        distance = await workflow.execute_activity_method(
            PizzaOrderActivities.get_distance,
            order.address,
            start_to_close_timeout=timedelta(seconds=5),
        )

        if order.is_delivery and distance.kilometers > 25:
            error_message = "customer lives outside the service area"
            raise ApplicationError(error_message)

        # Wait 30 minutes before billing the customer
        await asyncio.sleep(timedelta(minutes=30).total_seconds())

        bill = Bill(
            customer_id=order.customer.customer_id,
            order_number=order.order_number,
            description="Pizza order",
            amount=total_price,
        )

        confirmation = await workflow.execute_activity_method(
            PizzaOrderActivities.send_bill,
            bill,
            start_to_close_timeout=timedelta(seconds=5),
        )

        return confirmation
```
#### Step 1: A basic Workflow Definition

This Workflow Definition takes a pizza order and does the work listed here. Step through it to see which
statements the Worker handles on its own and which ones send a Command to the Temporal Service.

- Calculates the total price of the pizzas
- Determines the distance to the customer
- Fails if the customer is too far away for delivery
- Sleeps for 30 minutes
- Populates a data structure with billing information
- Sends a bill to the customer

#### Step 2: Internal steps

*Internal step*

These steps are internal to the Workflow. The Worker runs them in your process and never contacts the Temporal
Service.

#### Step 3: Steps that reach the Temporal Service

*Sends a Command*

These steps do involve the Temporal Service. Requesting an Activity Execution generates a Command to schedule
the Activity Task, and returning from the Workflow tells the Temporal Service that the Workflow Execution is
complete.

#### Step 4: Total the price of the order

*Internal step*

The walkthrough starts here. Calculating the total price of the pizzas is an internal step, so it doesn't
require any interaction with the Temporal Service.

#### Step 5: Request the GetDistance Activity

*Sends a Command*

The Worker reaches a statement that requires the Temporal Service: a request to execute an Activity. It issues
a ScheduleActivityTask Command with the details the Temporal Service needs, such as the Task Queue name, the
Activity Type, and the input values. An Activity can take hours or days to complete, and the Worker holds no
resources while it waits.

**Commands issued:** `ScheduleActivityTask` ("pizza-tasks", GetDistance, { Line1: "123 Oak St.", Line2: "", ... })

#### Step 6: Evaluate the distance

*Internal step*

The Worker evaluates the distance returned by the Activity. If the customer lived too far away, the Workflow
would raise an exception, which sends a Command asking the Temporal Service to fail the Workflow Execution.
This order is going to a nearby customer, so execution continues.

#### Step 7: Start a Timer

*Sends a Command*

The call to sleep is another statement that involves the Temporal Service. The Worker issues a StartTimer
Command that includes the duration, and this Workflow Execution pauses for 30 minutes until the Timer fires.

**Commands issued:** `StartTimer` (30 minutes)

#### Step 8: Populate the bill

*Internal step*

The Timer fires and execution resumes. These lines create and populate the data structure that holds the input
for the next Activity. The structure relates to an Activity, but building it doesn't involve the Temporal
Service.

#### Step 9: Request the SendBill Activity

*Sends a Command*

The next statement requests execution of an Activity, so the Worker issues another ScheduleActivityTask
Command to the Temporal Service.

**Commands issued:** `ScheduleActivityTask` ("pizza-tasks", SendBill, { Amount: 2750, Description: "Pizzas", ... })

#### Step 10: Return from the Workflow

*Sends a Command*

Returning from the Workflow method also results in a Command. The Worker issues CompleteWorkflowExecution to
the Temporal Service, which includes the value returned from the method.

**Commands issued:** `CompleteWorkflowExecution` ({ ConfirmationNumber: "TPD-26074139" })

Four statements in this Workflow Definition produce a Command:

| Statement                                             | Command                     |
| ----------------------------------------------------- | --------------------------- |
| `workflow.execute_activity_method(get_distance, ...)` | `ScheduleActivityTask`      |
| `asyncio.sleep(timedelta(minutes=30)...)`             | `StartTimer`                |
| `workflow.execute_activity_method(send_bill, ...)`    | `ScheduleActivityTask`      |
| `return confirmation`                                 | `CompleteWorkflowExecution` |

Everything else is an internal step. Totaling the order price, evaluating the distance, and populating the bill all run
in the Worker without contacting the Temporal Service.

## How Workflow Commands map to Events 

The Commands that are sent to the Temporal Service are then turned into Events, which build up the Event History. The
Event History is a detailed log of Events that occur during the lifecycle of a Workflow Execution, such as the execution
of Workflow Tasks or Activity Tasks. Event Histories are persisted to the database used by the Temporal Service, so
they're durable, and will even survive a crash of the Temporal Service itself.

These Events are what are used to recreate a Workflow Execution's state in the case of failure.

Step through the same Workflow Definition to see each Command the Worker issues and the Events the Temporal Service
records in response.

```python
@workflow.defn
class PizzaOrderWorkflow:
    @workflow.run
    async def order_pizza(self, order: PizzaOrder) -> OrderConfirmation:
        total_price = sum(pizza.price for pizza in order.items)

        distance = await workflow.execute_activity_method(
            PizzaOrderActivities.get_distance,
            order.address,
            start_to_close_timeout=timedelta(seconds=5),
        )

        if order.is_delivery and distance.kilometers > 25:
            error_message = "customer lives outside the service area"
            raise ApplicationError(error_message)

        # Wait 30 minutes before billing the customer
        await asyncio.sleep(timedelta(minutes=30).total_seconds())

        bill = Bill(
            customer_id=order.customer.customer_id,
            order_number=order.order_number,
            description="Pizza order",
            amount=total_price,
        )

        confirmation = await workflow.execute_activity_method(
            PizzaOrderActivities.send_bill,
            bill,
            start_to_close_timeout=timedelta(seconds=5),
        )

        return confirmation
```
#### Step 1: Commands and the Events they produce

This walkthrough keeps a running list of the Commands the Worker issues and the Events the Temporal Service records in response. Blue Events are the direct result of a Command. Pink Events are an indirect result.

#### Step 2: The GetDistance Activity is scheduled

*Sends a Command*

The call to the Activity is the first line of code in the Workflow that causes a Command to be issued. In response, the Temporal Service creates an Activity Task, adds it to the Task Queue, and appends the ActivityTaskScheduled Event to the Event History.

**Commands:** `ScheduleActivityTask` (GetDistance)

**Events:** `ActivityTaskScheduled` (GetDistance)

#### Step 3: A Worker polls for the Activity Task

*Temporal Service*

The Temporal Service dispatches this Activity Task to an available Worker. It responds to the poll request with the Task, and the Worker begins executing the code needed to complete it. Nothing is recorded in the Event History yet.

#### Step 4: The Activity Task closes

*Temporal Service*

The ActivityTaskStarted Event is not written to the Event History until the Task closes, because the number of retry attempts is an attribute of that Event. It is an indirect result of the Command. The Start-to-Close Timeout sets how long the Activity has to complete.

**Events:** `ActivityTaskStarted`

#### Step 5: The Activity reports its result

*Temporal Service*

When the Activity Definition returns a result, the Worker sends a message to the Temporal Service to say the Task is complete. This is a notification, not a Command, because it does not ask the Temporal Service to do anything that lets the Workflow Execution progress. The Temporal Service records ActivityTaskCompleted.

**Events:** `ActivityTaskCompleted` (distance = 15)

#### Step 6: The Worker starts a Timer

*Sends a Command*

The next statement that results in a Command is the call to start a Timer. The Temporal Service starts a 30-minute Timer and records a TimerStarted Event, a direct result of the StartTimer Command.

**Commands:** `StartTimer` (30 minutes)

**Events:** `TimerStarted` (30 minutes)

#### Step 7: The Timer fires

*Temporal Service*

After 30 minutes elapse, the Timer fires on the Temporal Service, which records a TimerFired Event. The Workflow Execution continues with the next statement, but populating the bill is an internal step that does not interact with the Temporal Service.

**Events:** `TimerFired`

#### Step 8: The SendBill Activity is scheduled

*Sends a Command*

The Worker reaches the call to the SendBill Activity and issues another ScheduleActivityTask Command. The Temporal Service adds an Activity Task to the Task Queue and records an ActivityTaskScheduled Event.

**Commands:** `ScheduleActivityTask` (SendBill)

**Events:** `ActivityTaskScheduled` (SendBill)

#### Step 9: A Worker dequeues the Activity Task

*Temporal Service*

The Temporal Service dispatches this Activity Task to the Worker. The Worker removes the Task from the Task Queue and begins working on it, and the Temporal Service records an ActivityTaskStarted Event to signify that the Task was dequeued.

**Events:** `ActivityTaskStarted`

#### Step 10: The bill is sent

*Temporal Service*

When the Activity returns, the Task is complete and the Worker notifies the Temporal Service, which records the ActivityTaskCompleted Event. Execution continues until the Workflow completes. The next walkthrough covers the full Event History, including the Workflow Task Events.

**Events:** `ActivityTaskCompleted`

Blue Events are the direct result of a Command. Pink Events are an indirect result, such as the Events the Temporal
Service records when a Worker starts or finishes a Task:

| Command                | Direct Event            | Indirect Events                                |
| ---------------------- | ----------------------- | ---------------------------------------------- |
| `ScheduleActivityTask` | `ActivityTaskScheduled` | `ActivityTaskStarted`, `ActivityTaskCompleted` |
| `StartTimer`           | `TimerStarted`          | `TimerFired`                                   |

## How History Replay provides Durable Execution 

Now that you have seen how code maps to Commands, and how Commands map to Events, this next walkthrough will take a look
at how Temporal uses Replay with the Events to provide Durable Execution and restore a Workflow Execution in the case of
a failure.

This code walkthrough will begin by walking through a Workflow Execution, describing how the code maps to Commands and
Events. There will then be a Worker crash halfway through, explaining how Temporal uses Replay to recover the state of
the Workflow Execution, ultimately resulting in a completed execution that's identical to one that had not crashed.

```python
@workflow.defn
class PizzaOrderWorkflow:
    @workflow.run
    async def order_pizza(self, order: PizzaOrder) -> OrderConfirmation:
        total_price = sum(pizza.price for pizza in order.items)

        distance = await workflow.execute_activity_method(
            PizzaOrderActivities.get_distance,
            order.address,
            start_to_close_timeout=timedelta(seconds=5),
        )

        if order.is_delivery and distance.kilometers > 25:
            error_message = "customer lives outside the service area"
            raise ApplicationError(error_message)

        # Wait 30 minutes before billing the customer
        await asyncio.sleep(timedelta(minutes=30).total_seconds())

        bill = Bill(
            customer_id=order.customer.customer_id,
            order_number=order.order_number,
            description="Pizza order",
            amount=total_price,
        )

        confirmation = await workflow.execute_activity_method(
            PizzaOrderActivities.send_bill,
            bill,
            start_to_close_timeout=timedelta(seconds=5),
        )

        return confirmation
```
### Original execution

#### Step 1: A Client requests the Workflow Execution

*Temporal Service*

The walkthrough begins with a request to execute this Workflow Definition with input data about the customer and the pizzas ordered. The Temporal Service records WorkflowExecutionStarted, always the first Event of a Workflow Execution, and that Event holds the input data.

**Event History:** `WorkflowExecutionStarted` (customer, pizzas ordered)

#### Step 2: A Workflow Task is queued

*Temporal Service*

The Temporal Service adds a Workflow Task to the Task Queue and records a WorkflowTaskScheduled Event.

**Event History:** `WorkflowTaskScheduled`

#### Step 3: A Worker accepts the Workflow Task

*Temporal Service*

The Temporal Service dispatches the Task to a Worker that is polling the Task Queue. The Worker accepts it, and the Temporal Service records a WorkflowTaskStarted Event.

**Event History:** `WorkflowTaskStarted`

#### Step 4: The Worker runs the Workflow code

*Internal step*

The Worker invokes the Workflow code and runs it one statement at a time. The first few lines are internal steps that do not interact with the Temporal Service.

#### Step 5: The Worker completes the Workflow Task

*Sends a Command*

The Worker encounters a request to execute an Activity, so it completes the current Workflow Task. It makes a single gRPC call, RespondWorkflowTaskCompleted, that signals completion of the Workflow Task and carries any Commands with it, so WorkflowTaskCompleted and the Command that follows are technically one call.

**Event History:** `WorkflowTaskCompleted`

#### Step 6: The GetDistance Activity Task is scheduled

*Sends a Command*

In response to the ScheduleActivityTask Command, the Temporal Service queues an Activity Task and records an ActivityTaskScheduled Event, a direct result of the Command.

**Commands:** `ScheduleActivityTask` (GetDistance)

**Event History:** `ActivityTaskScheduled` (GetDistance)

#### Step 7: A Worker starts the Activity Task

*Temporal Service*

The Temporal Service dispatches the Activity Task to an available Worker, which starts running the code in the GetDistance Activity. ActivityTaskStarted is an indirect result of the Command, and it is not written to the Event History until the Task closes, because the number of retry attempts is an attribute of that Event.

**Event History:** `ActivityTaskStarted`

#### Step 8: The Activity returns a distance of 15

*Temporal Service*

When the Activity returns, the Worker notifies the Temporal Service that the Activity Execution is complete. The Temporal Service records an ActivityTaskCompleted Event, which contains the result of the Activity.

**Event History:** `ActivityTaskCompleted` (distance = 15)

#### Step 9: The result goes back to the Workflow

*Temporal Service*

To deliver the result to the Workflow, the Temporal Service creates another Workflow Task that includes it. A Worker dequeues that Task, resumes execution, and evaluates the distance. This order is going to a nearby customer, so execution continues.

**Event History:**
- `WorkflowTaskScheduled`
- `WorkflowTaskStarted`

#### Step 10: The Worker starts a Timer

*Sends a Command*

The Worker reaches the request to start a Timer, so it completes the current Workflow Task and sends the StartTimer Command with it. The Temporal Service starts the Timer and records TimerStarted. The Workflow does not progress until the Timer fires.

**Commands:** `StartTimer` (30 minutes)

**Event History:**
- `WorkflowTaskCompleted`
- `TimerStarted` (30 minutes)

#### Step 11: The Timer fires

*Temporal Service*

After 30 minutes elapse, the Timer fires and the Temporal Service records TimerFired. It then queues a new Workflow Task to deliver that Event to the Workflow and drive progress forward.

**Event History:**
- `TimerFired`
- `WorkflowTaskScheduled`

### Worker crash

#### Step 12: The Worker crashes

*Worker crash*

The Worker polls for the Task, dequeues it, and continues executing the Workflow code — and then crashes right here. How does Temporal recover the state of this Workflow Execution? First, how does the Temporal Service know the Worker crashed?

**Event History:** `WorkflowTaskStarted`

#### Step 13: The Workflow Task times out

*Worker crash*

Once a Worker accepts a Task, it is expected to complete it within a predefined duration. That Workflow Task Timeout, 10 seconds by default, is how a crashed Worker is recognized. The Worker failed to complete the Task in time, so the Temporal Service records WorkflowTaskTimedOut.

**Event History:** `WorkflowTaskTimedOut`

#### Step 14: A new Workflow Task is scheduled

*Temporal Service*

The Temporal Service schedules a new Workflow Task. The Worker that polls for it might be another Worker in the fleet or a new Worker process created by restarting the one that crashed. Everything above the line is the Event History as it stood when the Worker crashed.

**Event History:**
- `WorkflowTaskScheduled`
- *— Event History at the time of the crash —*

### History Replay

#### Step 15: The Worker requests the Event History

*Replay*

Either way, the Worker needs the current Event History for this Workflow Execution, so it requests it from the Temporal Service. The Temporal Service provides the History.

#### Step 16: Replay re-executes the code

*Replay*

The Worker begins re-executing the code with the same input, which was stored in the WorkflowExecutionStarted Event. Because the Workflow code is deterministic, the state of every variable encountered so far is identical to what it was before the crash. For example, totalPrice holds the same value.

#### Step 17: The Activity result comes from the History

*Replay*

When Replay reaches the call to schedule GetDistance, it creates a ScheduleActivityTask Command but does not issue it. Instead, the Worker inspects the Event History and finds ActivityTaskScheduled for this Activity Type, ActivityTaskStarted showing a Worker dequeued the Task, and ActivityTaskCompleted with a result of 15. The Activity already ran, so the Command is not issued.

**Commands:** ✓ `ScheduleActivityTask` (GetDistance) — created during Replay, not issued

#### Step 18: Replay assigns the stored result

*Replay*

The Worker assigns the value stored in the ActivityTaskCompleted Event, 15, to the distance variable. The Activity is not re-executed, so there is no way for it to behave differently during Replay than it did during the original execution. The conditional evaluates to false, just as it did before.

#### Step 19: The Timer is already done

*Replay*

The Worker reaches the request to start a Timer and creates a StartTimer Command, which again it does not issue. The Event History contains TimerStarted and TimerFired, so the Worker knows the Timer already started and fired during the previous execution.

**Commands:** ✓ `StartTimer` (30 minutes) — created during Replay, not issued

#### Step 20: State is restored to the point of the crash

*Replay*

The Worker has reached the point where the crash occurred, and replaying the code has completely restored the state of the Workflow Execution. Every variable, including totalPrice, holds the value it held before the crash.

### Execution resumes

#### Step 21: Execution moves past the crash

*Sends a Command*

The Worker reaches a statement beyond where the crash occurred, which is evident because the Event History contains no Events for the SendBill Activity. Execution continues as if the crash never happened: the Worker completes the current Workflow Task and includes the Command with it.

**Event History:** `WorkflowTaskCompleted`

#### Step 22: The SendBill Activity runs

*Sends a Command*

The Worker issues the Command, the Temporal Service queues the Activity Task, and a Worker dequeues and runs it. When the Activity returns, the Worker notifies the Temporal Service, which records ActivityTaskCompleted with the result from SendBill.

**Commands:** `ScheduleActivityTask` (SendBill)

**Event History:**
- `ActivityTaskScheduled` (SendBill)
- `ActivityTaskStarted`
- `ActivityTaskCompleted`

#### Step 23: One more Workflow Task delivers the result

*Temporal Service*

The Temporal Service has not received a Command saying the Workflow Execution completed or failed, so it schedules another Workflow Task to continue progress. A Worker accepts it and resumes the Workflow code.

**Event History:**
- `WorkflowTaskScheduled`
- `WorkflowTaskStarted`

#### Step 24: The Workflow Execution completes

*Sends a Command*

The Workflow returns, so the Worker completes the current Workflow Task and issues a CompleteWorkflowExecution Command that contains the result. The Temporal Service records WorkflowExecutionCompleted as the final Event. The result is identical to an execution that never crashed.

**Commands:** `CompleteWorkflowExecution` ({ ConfirmationNumber: "TPD-26074139" })

**Event History:**
- `WorkflowTaskCompleted`
- `WorkflowExecutionCompleted`

The walkthrough covers four phases:

1. **Original execution**: the Client starts the Workflow Execution, and the Commands the Worker issues become Events in
   the Event History.
2. **Worker crash**: the Worker dies partway through a Workflow Task. When the Workflow Task Timeout elapses, 10 seconds
   by default, the Temporal Service records `WorkflowTaskTimedOut` and schedules a new Workflow Task.
3. **History Replay**: a Worker requests the Event History and re-executes the Workflow code with the original input,
   which the `WorkflowExecutionStarted` Event stores. Commands the Worker creates during Replay are matched against the
   Event History instead of being issued, so Activities don't run again. The Worker uses the results stored in the
   `ActivityTaskCompleted` Events.
4. **Execution resumes**: past the point of the crash, the Event History holds no matching Events, so the Worker issues
   Commands for real again until the Workflow Execution completes. The result is identical to an execution that never
   crashed.

## Example of a non-deterministic Workflow Definition 

Now that Replay has been covered, this section will explain why a Workflow Definition needs to be
[deterministic](/workflow-definition#deterministic-constraints) in order for Replay to work.

A Workflow Definition is deterministic if every execution of it produces the same Commands in the same
sequence given the same input.

As mentioned in the [`How History Replay Provides Durable Execution`](#How-History-Replay-Provides-Durable-Execution)
walkthrough, in the case of a failure, a Worker requests the Event History to replay it. During Replay, the Worker runs
the Workflow code again to produce a set of Commands which is compared against the sequence of Commands in the Event
History. When there’s a mismatch between the expected sequence of Commands the Worker expects based on the Event History
and the actual sequence produced during Replay (due to non-determinism), Replay will be unable to continue.

To better understand why a Workflow Definition needs to be deterministic, it's helpful to look at one that violates
it. In this case, this code will walk through a Workflow Definition that breaks the determinism constraint with a random
number generator.

```python
@workflow.defn
class GenerateDailyReport:
    @workflow.run
    async def run(self) -> str:
        sales_data = await workflow.execute_activity_method(
            ReportActivities.import_sales_data,
            start_to_close_timeout=timedelta(minutes=45),
        )

        if non_deterministic_number_generator(100) >= 50:
            # sleep for 4 hours
            await asyncio.sleep(timedelta(hours=4).total_seconds())

        workflow.logger.info("Preparing to run daily report")

        return await workflow.execute_activity_method(
            ReportActivities.run_daily_report,
            sales_data,
            start_to_close_timeout=timedelta(minutes=45),
        )
```
### First execution

#### Step 1: The import_sales_data Activity runs

*Sends a Command*

As this Workflow executes step by step, the first line that results in a Command is the call to the import_sales_data Activity. The Activity Execution succeeds, so the Temporal Service logs three Events to the Event History.

**Commands created:** `ScheduleActivityTask` (import_sales_data)

**Relevant History Events:**
- `ActivityTaskScheduled` (import_sales_data)
- `ActivityTaskStarted`
- `ActivityTaskCompleted`

#### Step 2: A random number decides the next branch

*Internal step*

The Worker reaches a conditional statement that evaluates a randomly generated number. The random number generator returns 84 during this execution, so the expression evaluates to true and execution continues with the next line.

#### Step 3: The Workflow starts a 4-hour Timer

*Sends a Command*

The next line requests a Timer, so the Worker issues a StartTimer Command. The Temporal Service starts the Timer and records TimerStarted, then records TimerFired when the Timer fires.

**Commands created:** `StartTimer` (4 hours)

**Relevant History Events:**
- `TimerStarted` (4 hours)
- `TimerFired`

#### Step 4: The Worker crashes

*Worker crash*

The Worker crashes once it reaches the next line, so another Worker takes over. That Worker uses Replay to restore the current state before continuing execution of the lines that follow.

### History Replay

#### Step 5: Replay establishes the expected Commands

*Replay*

The Worker requests the Event History and determines the sequence of Commands needed to restore the current state. Based on the History, it expects to encounter ScheduleActivityTask (import_sales_data) and then StartTimer (4 hours).

#### Step 6: The first Command matches

*Replay*

As the Worker executes the code during Replay, it reaches the first call to execute an Activity and creates a ScheduleActivityTask Command. It is the right type of Command and it occurs at the right position in the expected sequence, so Replay proceeds.

**Commands created:** ✓ `ScheduleActivityTask` (import_sales_data) — created during Replay

#### Step 7: The random number returns something different

*Replay*

The Worker reaches the conditional statement again. This time the random number generator returns 14, so the expression evaluates to false and execution skips the call that starts the Timer.

#### Step 8: The next Command does not match

*Worker crash*

The Worker reaches the request to execute the run_daily_report Activity and creates another ScheduleActivityTask Command. That is not the Command it expected at this position in the sequence, so the Worker cannot restore the previous state.

**Commands created:** ✗ `ScheduleActivityTask` (run_daily_report) — created during Replay (expected: StartTimer (4 hours))

#### Step 9: Replay fails with a non-determinism error

*Worker crash*

The Workflow produced a different sequence of Commands during Replay than the Event History recorded before the crash, so the Workflow Execution cannot be replayed. The random number generator is the source of the non-determinism.

During the first execution, the random number is 84, so the Workflow starts a Timer and the Event History records
`TimerStarted` and `TimerFired`. During Replay, the random number is 14, so the Workflow skips the Timer and produces a
`ScheduleActivityTask` Command where the Event History expects `StartTimer`. That mismatch is what makes Replay fail.

Note that non-deterministic failures do not fail the Workflow Execution by default. A non-deterministic failure is
considered a [Workflow Task Failure](/references/failures#workflow-task-failures) which is considered a transient
failure, meaning it retries over and over. Users can also fix the source of non-determinism, perhaps by removing the
Activity, and then restart the Workers. This means that this type of failure can recover by itself. You can also use a
strategy called versioning to address this non-determinism error. See [versioning](/develop/python/workflows/versioning)
to learn more.

For more information on how Temporal handles Durable Execution or to see these walkthroughs in video format with more
explanation, check out our free, self-paced courses: [Temporal 102](https://learn.temporal.io/courses/temporal_102/) and
[Versioning Workflows](https://learn.temporal.io/courses/versioning/).

## Temporal Applications support non-deterministic operations

We want to emphasize that although your Workflow Definition needs to be deterministic, your application itself does not!

Remember that pretty much anything that interacts with the external world is inherently non-deterministic:

- Calling LLM APIs
- Querying databases
- Reading or writing files
- Making HTTP requests to external services

**Good news**: Your Temporal application can absolutely handle all of these operations. While your Workflow Definition must be
deterministic, your application absolutely can handle any type of non-deterministic operation, including those listed
above. This gives you the best of both worlds—the crash-proof reliability of a Workflow and the resiliency of Activities
which have built-in support for retries.
