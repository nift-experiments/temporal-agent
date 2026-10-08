# Continue-As-New - .NET SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Use Temporal's Continue-As-New in .NET to manage large Event Histories by atomically creating new Workflow Executions with the same Workflow Id and fresh parameters.

This page covers the following for .NET developers:

- [What is Continue-As-New?](#what)
- [Use Continue-As-New](#how)
- [When is it right to Continue-As-New?](#when)
- [Test Continue-As-New](#how-to-test)

## What is Continue-As-New? 

[Continue-As-New](/workflow-execution/continue-as-new) lets a Workflow Execution close successfully and creates a new Workflow Execution.
You can think of it as a checkpoint when your Workflow gets too long or approaches certain scaling limits.

The new Workflow Execution is in the same [chain](/workflow-execution#workflow-execution-chain); it keeps the same Workflow Id but gets a new Run Id and a fresh Event History.
It also receives your Workflow's usual parameters.

## Use Continue-As-New with the .NET SDK 

First, design your Workflow parameters so that you can pass in the "current state" when you Continue-As-New into the next Workflow run.
This state is typically set to `None` for the original caller of the Workflow.

[View the source code](https://github.com/temporalio/samples-dotnet/blob/main/src/SafeMessageHandlers/ClusterManagerWorkflow.workflow.cs) in the context of the rest of the application code.

```csharp
public record Input
    {
        public State State { get; init; } = new();

        public bool TestContinueAsNew { get; init; }
    }

[WorkflowInit]
public ClusterManagerWorkflow(Input input)

````
The test hook in the above snippet is covered [below](#how-to-test).

Inside your Workflow, throw a [`CreateContinueAsNewException`](https://dotnet.temporal.io/api/Temporalio.Workflows.ContinueAsNewException.html) exception.
This stops the Workflow right away and starts a new one.

[View the source code](https://github.com/temporalio/samples-dotnet/blob/main/src/SafeMessageHandlers/ClusterManagerWorkflow.workflow.cs) in the context of the rest of the application code.

```csharp
throw Workflow.CreateContinueAsNewException((ClusterManagerWorkflow wf) => wf.RunAsync(new()
{
    State = CurrentState,
    TestContinueAsNew = input.TestContinueAsNew,
}));
````

### Considerations for Workflows with message handlers 

If you use Updates or Signals, don't call Continue-as-New from the handlers.
Instead, wait for your handlers to finish in your main Workflow before you throw `CreateContinueAsNewException`.
See the [`AllHandlersFinished`](message-passing#wait-for-message-handlers) example for guidance.

## When is it right to Continue-As-New with the .NET SDK? 

Use Continue-as-New when your Workflow might hit [Event History Limits](/workflow-execution/event#event-history).

Temporal tracks your Workflow's progress against these limits to let you know when you should Continue-as-New.
Call `Workflow.ContinueAsNewSuggested` to check if it's time.

## Test Continue-As-New with the .NET SDK 

Testing Workflows that naturally Continue-as-New may be time-consuming and resource-intensive.
Instead, add a test hook to check your Workflow's Continue-as-New behavior faster in automated tests.

For example, when `TestContinueAsNew == true`, this sample creates a test-only variable called `maxHistoryLength` and sets it to a small value.
A helper variable in the Workflow checks it each time it considers using Continue-as-New:

[View the source code](https://github.com/temporalio/samples-dotnet/blob/main/src/SafeMessageHandlers/ClusterManagerWorkflow.workflow.cs) in the context of the rest of the application code.

```csharp
private bool ShouldContinueAsNew =>
    // Don't continue as new while update running
    Workflow.AllHandlersFinished &&
    // Continue if suggested or, for ease of testing, max history reached
    (Workflow.ContinueAsNewSuggested || Workflow.CurrentHistoryLength > maxHistoryLength);
```
