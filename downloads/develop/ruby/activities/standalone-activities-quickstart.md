# Standalone Activities Ruby Quickstart

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Execute a Standalone Activity with the Temporal Ruby SDK without writing a Workflow.

# Quickstart

Standalone Activities are Activities that run independently, without being orchestrated by a
Workflow. Instead of starting an Activity from within a Workflow Definition, you start a Standalone
Activity directly from a [`Temporalio::Client`](https://ruby.temporal.io/Temporalio/Client.html).

The way you write the Activity and register it with a Worker is identical to [Workflow
Activities](/develop/ruby/activities/basics). The only difference is that you execute a Standalone
Activity directly from your Temporal Client.

> **📝 Note:**
>
> This documentation uses source code from the
> [standalone_activity](https://github.com/temporalio/samples-ruby/tree/main/standalone_activity)
> sample.
>

## Get started with Standalone Activities 

Prerequisites:

- **Ruby** 3.3+

- **Temporal Ruby SDK** (v1.9.0 or higher). See the [Ruby Quickstart](/develop/ruby/set-up-local-ruby) for
  install instructions.

- **Temporal CLI** v1.9.1 or higher. Install with Homebrew, or see the [Temporal CLI install guide](/cli/setup-cli) for other platforms. Verify the installation with `temporal --version`.

Start the Temporal development server with `temporal server start-dev`.

This command automatically starts the Temporal development server with the Web UI, and creates the `default` Namespace.
It uses an in-memory database, so do not use it for real use cases.

The Temporal Server will now be available for client connections on `localhost:7233`, and the
Temporal Web UI will now be accessible at [http://localhost:8233](http://localhost:8233).

```bash
brew install temporal
```

```bash
temporal --version
```

```bash
temporal server start-dev
```

## Clone the sample

Clone the [samples-ruby](https://github.com/temporalio/samples-ruby) repository to follow along:

```bash
git clone https://github.com/temporalio/samples-ruby.git
cd samples-ruby
bundle install
```

The sample consists of separate programs in the `standalone_activity` directory:

```
standalone_activity/
├── my_activities.rb      # Activity definition
├── worker.rb             # Worker that processes activity tasks
├── execute_activity.rb   # Starts an activity and waits for the result
├── start_activity.rb     # Starts an activity without blocking
├── list_activities.rb    # Lists activity executions
└── count_activities.rb   # Counts activity executions
```

## Define your Activity 

An Activity in the Temporal Ruby SDK is a subclass of [`Temporalio::Activity::Definition`](https://ruby.temporal.io/Temporalio/Activity/Definition.html) that
implements an `execute` method. The way you define a Standalone Activity is identical to how you
define an Activity orchestrated by a Workflow. In fact, the same Activity can be executed both as a
Standalone Activity and as a Workflow Activity.

[my_activities.rb](https://github.com/temporalio/samples-ruby/blob/main/standalone_activity/my_activities.rb)

```ruby
require 'temporalio/activity'

module StandaloneActivity
  module MyActivities
    class ComposeGreeting < Temporalio::Activity::Definition
      def execute(greeting, name)
        "#{greeting}, #{name}!"
      end
    end
  end
end
```

## Run a Worker with the Activity registered 

Running a Worker for Standalone Activities is the same as running a Worker for Workflow Activities —
you create a [`Temporalio::Worker`](https://ruby.temporal.io/Temporalio/Worker.html), register the Activity class, and call `worker.run`. The Worker
doesn't need to know whether the Activity will be invoked from a Workflow or as a Standalone
Activity. See [Run a Worker](/develop/ruby/workers/run-worker-process) for more details on
Worker setup and configuration options.

[worker.rb](https://github.com/temporalio/samples-ruby/blob/main/standalone_activity/worker.rb)

Open a new terminal, navigate to the `samples-ruby` directory, and run the Worker.
Leave this terminal running — the Worker needs to stay up to process activities.

```ruby
args, kwargs = Temporalio::EnvConfig::ClientConfig.load_client_connect_options
args[0] ||= 'localhost:7233'
args[1] ||= 'default'

client = Temporalio::Client.connect(*args, **kwargs)

worker = Temporalio::Worker.new(
  client:,
  task_queue: 'standalone-activity-sample',
  activities: [StandaloneActivity::MyActivities::ComposeGreeting]
)

puts 'Starting worker (ctrl+c to exit)'
worker.run(shutdown_signals: ['SIGINT'])
```

```bash
bundle exec ruby standalone_activity/worker.rb
```

## Execute a Standalone Activity 

Use [`Temporalio::Client#execute_activity`](https://ruby.temporal.io/Temporalio/Client.html#execute_activity-instance_method) to execute a
Standalone Activity and block until it completes. Call this from your application code, not from
inside a Workflow Definition. This durably enqueues your Standalone Activity in the Temporal Server,
waits for it to be executed on your Worker, and then returns the result.

[execute_activity.rb](https://github.com/temporalio/samples-ruby/blob/main/standalone_activity/execute_activity.rb)

The first argument is the Activity to run. It can be the [`Activity::Definition`](https://ruby.temporal.io/Temporalio/Activity/Definition.html) subclass, an
instance of one, or a string/symbol name. Positional arguments after it are passed to the Activity's
`execute` method. The call requires `id`, `task_queue`, and at least one of `start_to_close_timeout`
or `schedule_to_close_timeout`.

To run it:

1. Make sure the Temporal Server is running (from the [Get Started](#get-started) step above).
2. Make sure the Worker is running (from the [Run a Worker](#run-worker) step above).
3. Open a new terminal, navigate to the `samples-ruby` directory, and run:
    ```
    bundle exec ruby standalone_activity/execute_activity.rb
    ```

Or use the Temporal CLI.

```ruby
result = client.execute_activity(
  StandaloneActivity::MyActivities::ComposeGreeting,
  'Hello', 'World',
  id: 'standalone-activity-id',
  task_queue: 'standalone-activity-sample',
  start_to_close_timeout: 10
)
puts "Activity result: #{result}"
```

```bash
bundle exec ruby standalone_activity/execute_activity.rb
```

```bash
temporal activity execute \\
  --type ComposeGreeting \\
  --activity-id standalone-activity-id \\
  --task-queue standalone-activity-sample \\
  --start-to-close-timeout 10s \\
  --input '"Hello"' \\
  --input '"World"'
```

## Run with Temporal Cloud

All code samples on this page use
[`Temporalio::EnvConfig::ClientConfig.load_client_connect_options`](https://ruby.temporal.io/Temporalio/EnvConfig/ClientConfig.html#load_client_connect_options-class_method)
to configure the Temporal Client connection. It responds to [environment
variables](/references/client-environment-configuration) and [TOML configuration
files](/references/client-environment-configuration), so the same code works against a local dev
server and Temporal Cloud without changes. See [Run Standalone Activities with Temporal
Cloud](/develop/ruby/activities/standalone-activities#run-standalone-activities-temporal-cloud) in the Feature Guide
for mTLS and API key setup.

## Next steps

- **[Standalone Activities Feature Guide](/develop/ruby/activities/standalone-activities)**: Start without waiting, get handles, list and count Activities, and connect to Temporal Cloud.
- **[Activity basics](/develop/ruby/activities/basics)**: Write and register Activities with the Ruby SDK.
