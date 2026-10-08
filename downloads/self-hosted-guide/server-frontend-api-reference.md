# Server frontend API reference

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

While it's usually easiest to interact with [Temporal Server](/temporal-service/temporal-server) via a
[Client SDK](/encyclopedia/temporal-client) or the [Temporal CLI](/cli), you can
also use its gRPC API.

Our Client and Worker SDKs use the gRPC API. The API reference is located here:

[`api-docs.temporal.io`](https://api-docs.temporal.io/)

## Use with code

Usually you interact with the API via high-level methods like `client.workflow.start()`. However, Client SDKs also
expose the underlying gRPC services. For instance, the TypeScript SDK has:

- WorkflowService:
  [`Client.connection.workflowService`](https://typescript.temporal.io/api/classes/client.Connection#workflowservice)
- OperatorService:
  [`Client.connection.operatorService`](https://typescript.temporal.io/api/classes/client.Connection/#operatorservice)
- HealthService:
  [`Client.connection.healthService`](https://typescript.temporal.io/api/classes/client.Connection/#healthservice)

If you're not using an SDK Client (rare), you can generate gRPC client stubs by:

- Cloning [`temporalio/api`](https://github.com/temporalio/api) (repo with the protobuf files)
- Generating code in [your language](https://grpc.io/docs/languages/)

## Use manually

To query the API manually via command line or a GUI, first:

- If you don't already have a Server to connect to, run [`temporal server start-dev`](/cli/command-reference/server#start-dev)
- Clone this repo:

```shell
git clone https://github.com/temporalio/api.git
cd api
```

### With command line

Install [`evans`](https://github.com/ktr0731/evans#installation).

```shell
cd /path/to/api
evans --proto temporal/api/workflowservice/v1/service.proto --port 7233
```

To connect to Temporal Cloud, set the host, cert, cert key, and TLS flag:

```shell
evans --proto temporal/api/workflowservice/v1/service.proto --host devrel.a2dd6.tmprl.cloud --port 7233 --tls --cert /Users/me/certs/temporal.pem --certkey /Users/me/certs/temporal.key
```

Once inside the evans prompt, you can run commands like `help`, `show service` to list available methods, and
`call ListWorkflowExecutions`.

### With a GUI

- Install [BloomRPC](https://github.com/bloomrpc/bloomrpc#installation).
- Open the app
- Select "Import Paths" button on the top-left and enter the path to the cloned repo: `/path/to/api`
- Select the "Import protos" + button and select this file:

```shell
/path/to/api/temporal/api/workflowservice/v1/service.proto
```

- A list of methods should appear in the sidebar. Select one.
- Edit the JSON in the left pane.
- Hit `Cmd/Ctrl-Enter` or click the play button to get a response from the server on the right.

![ListWorkflowExecutions](/img/proto/ListWorkflowExecutions.png)

One downside compared to [command line](#with-command-line) is it doesn't show enum names, just numbers like
`"task_queue_type": 1`.

![DescribeTaskQueue](/img/proto/DescribeTaskQueue.png)
