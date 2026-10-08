# What is Temporal?

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Temporal is a scalable platform that ensures the Durable Execution of application code, allowing reliable and resilient Workflow Executions even in the face of failures like network outages or server crashes.

Temporal is a scalable and reliable runtime for durable function executions called [Temporal Workflow Executions](/workflow-execution).

Said another way, it's a platform that guarantees the [Durable Execution](#durable-execution) of your application code.

It enables you to develop as if failures don't even exist.
Your application will run reliably even if it encounters problems, such as network outages or server crashes, which would be catastrophic for a typical application.
The Temporal Platform handles these types of problems, allowing you to focus on the business logic, instead of writing application code to detect and recover from failures.

![The Temporal System](/diagrams/temporal-system-simple.svg)

## Durable Execution 

Durable Execution in the context of Temporal refers to the ability of a Workflow Execution to maintain its state and progress even in the face of failures, crashes, or server outages.
This is achieved through Temporal's use of an [Event History](/workflow-execution/event#event-history), which records the state of a Workflow Execution at each step.
If a failure occurs, the Workflow Execution can resume from the last recorded event, ensuring that progress isn't lost.

## What is the Temporal Platform? 

> **💡 Tip:**
>
> Watch a short overview of the Temporal Platform:
>
> [Watch: What is the Temporal Platform?](https://www.youtube.com/watch?v=EwweiH2rd7M)
>

The Temporal Platform consists of supervising software called the [Temporal Service](/temporal-service) and application code bundled as [Worker Processes](/workers#worker-process).
Together these components create a runtime for your [Temporal Application](/temporal#temporal-application).

![The Temporal Platform](/diagrams/temporal-platform-simple.svg)

A Temporal Service consists of the [Temporal Server](https://github.com/temporalio/temporal), written in Go, and a database.

Our software as a service (SaaS) offering, Temporal Cloud, offers an alternative to hosting the Temporal Service yourself.

Worker Processes are hosted and operated by you and execute your code. Workers run using one of our SDKs.

## What is a Temporal Application? 

A Temporal Application is a set of [Temporal Workflow Executions](/workflow-execution).
Each Temporal Workflow Execution has exclusive access to its local state, executes concurrently to all other Workflow Executions, and communicates with other Workflow Executions and the environment via message passing.

Therefore, a Temporal Workflow Execution executes a [Temporal Workflow Definition](/workflow-definition), also called a Temporal Workflow Function, your application code, exactly once and to completion—whether your code executes for seconds or years, in the presence of arbitrary load and arbitrary failures.

## Next steps 

- [Quickstarts](/quickstarts): Build a Hello World Workflow in your language.
- [Developer guides](/develop): SDK feature guides and API references.
- [Develop with AI](/with-ai): Give your coding agent Temporal expertise.
- [Temporal Cloud](/cloud): Deploy and run on Temporal Cloud.
- [Temporal architecture](/encyclopedia/architecture/temporal-architecture): How the platform works under the hood.
- [Understanding Temporal](/evaluate/understanding-temporal): A short overview of Temporal concepts.
