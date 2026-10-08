# Entity pattern - TypeScript SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Implement the Single-Entity Design Pattern in TypeScript to manage Workflow iterations and handle Signals, ensuring efficient Workflow Execution with updates.

### Single-entity design pattern in TypeScript 

The following is a simple pattern that represents a single entity.
It tracks the number of iterations regardless of frequency, and calls `continueAsNew` while properly handling pending updates from Signals.

```ts
interface Input {
  /* Define your Workflow input type here */
}
interface Update {
  /* Define your Workflow update type here */
}

const MAX_ITERATIONS = 1;

export async function entityWorkflow(
  input: Input,
  isNew = true,
): Promise<void> {
  try {
    const pendingUpdates = Array<Update>();
    setHandler(updateSignal, (updateCommand) => {
      pendingUpdates.push(updateCommand);
    });

    if (isNew) {
      await setup(input);
    }

    for (let iteration = 1; iteration <= MAX_ITERATIONS; ++iteration) {
      // Ensure that we don't block the Workflow Execution forever waiting
      // for updates, which means that it will eventually Continue-As-New
      // even if it does not receive updates.
      await condition(() => pendingUpdates.length > 0, '1 day');

      while (pendingUpdates.length) {
        const update = pendingUpdates.shift();
        await runAnActivityOrChildWorkflow(update);
      }
    }
  } catch (err) {
    if (isCancellation(err)) {
      await CancellationScope.nonCancellable(async () => {
        await cleanup();
      });
    }
    throw err;
  }
  await continueAsNew<typeof entityWorkflow>(input, false);
}
```
