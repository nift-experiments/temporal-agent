# Durable AI

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Build durable AI agents and systems on Temporal, with runnable cookbook recipes, SDK integrations, and design patterns for agent workloads.

Temporal gives AI applications and agents Durable Execution: a Workflow resumes automatically after a crash, a
network timeout, or a multi-day wait for a human to approve a step. Temporal shows up in four recurring types of AI
system:

**Agents.** Long-running, stateful agent loops that call LLMs and tools, wait on humans, and pick up exactly where
they left off after a failure. Start with the [AI Cookbook](/ai/cookbook) and the
[Approval](/design-patterns/approval) and [Entity Workflow](/design-patterns/entity-workflow) patterns.

**Processing pipelines.** Multi-step data and document pipelines, such as extraction, embedding, or batch inference,
that need to fan out, retry failed steps in isolation, and resume without reprocessing completed work. When pipelines
share Workers across models, tenants, or urgency levels, use
[Task Queue Priority and Fairness](/develop/task-queue-priority-fairness) to run urgent work ahead of bulk work and
keep one tenant from starving the others. See the [batch processing](/design-patterns#batch-processing-patterns) and
[QoS and throughput](/design-patterns/qos-throughput-patterns) patterns.

**Internal agent platforms.** Teams building a shared runtime for many agents reuse Temporal's Worker and Task Queue
primitives instead of building their own scheduler. See the
[worker configuration patterns](/design-patterns#worker-configuration-patterns) for routing and isolating agent
workloads.

**Model training.** Long-running training and fine-tuning jobs coordinated across GPU resources, with checkpointing
and recovery handled by Temporal's Event History instead of custom orchestration code. Start with the [long-running activity](/design-patterns/long-running-activity) and [parallel-execution](/design-patterns/parallel-execution) patterns. 

> Looking to use an AI coding assistant to write Temporal code instead? See [Develop with AI](/with-ai).

## AI Cookbook

Runnable, step-by-step recipes for building AI systems and agents with Temporal: tool calling, MCP, structured
output, human-in-the-loop, and more.

<!-- CookbookPreview (no recipes found) -->

## Agent framework integrations

Temporal integrations for the SDKs and frameworks teams use to build agents. This view is pre-filtered to agent
frameworks — browse [every integration](/integrations) for the full catalog.

- [AI SDK by Vercel](/develop/typescript/integrations/ai-sdk) — Build AI-powered applications with Durable Execution using the Vercel AI SDK. _(TypeScript · Agent framework)_
- [Deep Agents](/develop/python/integrations/deepagents) — Make LangChain Deep Agents durable with Temporal Workflows and Activities. _(Python · Agent framework)_
- [Google ADK](/develop/python/integrations/google-adk) — Run Google ADK agents as durable Temporal Workflows. _(Python · Agent framework)_
- [Google ADK](/develop/go/integrations/google-adk) — Run Google ADK agents as durable Temporal Workflows. _(Go · Agent framework)_
- [Google ADK](/develop/typescript/integrations/google-adk-agents) — Run Google ADK agents as durable Temporal Workflows. _(TypeScript · Agent framework)_
- [Google GenAI](/develop/python/integrations/google-genai) — Call Google Gemini models durably from Temporal Workflows with the Google Gen AI SDK. _(Python · Agent framework)_
- [LangGraph](/develop/python/integrations/langgraph) — Run LangGraph agent graphs as durable, resumable Temporal Workflows. _(Python · Agent framework)_
- [Mastra](https://mastra.ai/guides/deployment/temporal) — Build durable AI agents and workflows with the Mastra TypeScript framework. _(TypeScript · Agent framework)_
- [OpenAI Agents SDK](/develop/python/integrations/openai-agents) — Run OpenAI Agents with Durable Execution using Temporal. _(Python · Agent framework)_
- [OpenAI Agents SDK](/develop/typescript/integrations/openai-agents) — Run OpenAI Agents with Durable Execution using Temporal. _(TypeScript · Agent framework)_
- [Pydantic AI](https://ai.pydantic.dev/durable_execution/temporal/) — Build type-safe AI agents with Durable Execution through Pydantic AI. _(Python · Agent framework)_
- [Spring AI](/develop/java/integrations/spring-ai) — Build AI-powered Java applications with durable Spring AI tool calls. _(Java · Agent framework)_
- [Strands Agents](/develop/python/integrations/strands-agents) — Orchestrate AWS Strands Agents with durable Temporal Workflows. _(Python · Agent framework)_
- [Strands Agents](/develop/typescript/integrations/strands-agents) — Orchestrate AWS Strands Agents with durable Temporal Workflows. _(TypeScript · Agent framework)_

## Featured from the Code Exchange

A hand-picked look at samples built with Temporal and AI. Browse the full
[Code Exchange](https://temporal.io/code-exchange) for more.

- [AI enhanced e-commerce application](https://temporal.io/code-exchange/ai-enhanced-e-commerce-application): A sample e-commerce gift shop with hybrid full-text and vector search plus an AI-powered chat shopping assistant, built with Stripe and Temporal Workflows. _(Dotnet · Hybrid search)_
- [Temporal AI Question Planetarium](https://temporal.io/code-exchange/ai-question-planetarium): Runs a Hugging Face model inside Temporal Activities and Workers, streaming updates to the browser over WebSockets in real time. _(Python · Demo)_
- [Document Processing w/ AI](https://temporal.io/code-exchange/document-processing-w-ai): A mortgage underwriting demo that uses Gemini OCR and policy-grounded AI analysis, with human-in-the-loop review and full traceability. _(Python · Gemini · Mortgage)_
- [Rust Confessional: a durable AI agent demo](https://temporal.io/code-exchange/rust-confessional): A live demo where an AI agent judges audience programming confessions, its progress surviving a Worker crash mid-task. _(Rust · Demo)_

## Design patterns for AI agents

- [Approval](/design-patterns/approval): Human-in-the-loop Workflows that block until external approval decisions are made. Uses Signals to capture approval data with metadata.
- [Saga Pattern](/design-patterns/saga-pattern): Manages distributed transactions with compensating actions. Each step has a compensation that undoes its effects if subsequent steps fail.
- [Long-Running Activity](/design-patterns/long-running-activity): Long-running Activities report progress via heartbeats and enable resumption after failures with cancellation support.
- [Entity Workflow](/design-patterns/entity-workflow): A long-lived business entity — a user account, device, or order — gets one Workflow per instance, with Signals and Updates driving every state transition.
- [Local Activities](/design-patterns/local-activities): Local Activities run inside the Worker process, skipping server round-trips for short, idempotent Activities on a latency-sensitive path.

Browse the full [Design Patterns catalog](/design-patterns) for more, or jump straight into the
[AI Cookbook](/ai/cookbook) for runnable code.
