# Workflow cache tuning

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Tune Workflow cache size and thread limits to balance Worker memory use against replay latency.

When the number of cached Workflow Executions reported by `sticky_cache_size` hits `workflowCacheSize` _or_ the number of threads reported by the `workflow_active_thread_count` metrics gauge hits `maxWorkflowThreadCount`, Workflow Executions will start to be evicted from the cache.
An evicted Workflow Execution will need to be replayed when it gets any action that may advance it.

If the Workflow Cache limits described above are hit, and Worker hosts have enough free RAM and are not close to reasonable thread limits, then you may choose to increase `workflowCacheSize` and `maxWorkflowThreadCount` limits to decrease the overall latency and cost of the Replays in the system.
If the opposite occurs, consider decreasing the limits.

> **📝 Note:**
>
> In CoreSDK based SDKs, like TypeScript, this metric works differently and should be monitored and adjusted on a per Worker and Task Queue basis.
>
> The `maxWorkflowThreadCount` and `workflow_active_thread_count` parameters are for the Java SDK only.
>
