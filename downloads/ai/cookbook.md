# AI Cookbook

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Step-by-step recipes for building reliable AI systems with Temporal, covering LLM integrations, agentic loops, tool calling, and production patterns.

- [Hello world](/ai/cookbook/hello-world-openai-responses-python) — Call an LLM from a durable Temporal Workflow in Python using the OpenAI API library.
- [Hello world with LiteLLM](/ai/cookbook/hello-world-litellm-python) — Integrate LiteLLM into a durable Temporal Workflow in Python to call and switch between LLM providers.
- [Durable agent with tools using the AI SDK by Vercel](/ai/cookbook/ai-sdk-by-vercel-typescript) — Build a durable AI agent with the AI SDK by Vercel and Temporal that chooses tools to answer user questions.
- [Structured outputs with Temporal and OpenAI](/ai/cookbook/structured-output-openai-responses-python) — Use Temporal and the OpenAI Responses API to reliably request output conforming to a specific data structure.
- [Retry policy from HTTP responses](/ai/cookbook/http-retry-enhancement-python) — Extract retry information from HTTP response headers and pass it to Temporal's retry mechanisms in Python.
- [Basic agentic loop with Claude and tool calling](/ai/cookbook/agentic-loop-tool-call-claude-python) — Build a durable agentic loop in Python with Claude tool calling and Temporal.
- [Basic agentic loop with OpenAI and tool calling](/ai/cookbook/agentic-loop-tool-call-openai-python) — Build a durable agentic loop in Python that calls a dynamic set of tools with Temporal and the OpenAI Responses API.
- [Durable MCP weather server](/ai/cookbook/hello-world-durable-mcp-server) — Build a durable MCP server in Python that runs weather tools reliably with Temporal Workflows.
- [Tool calling agent](/ai/cookbook/tool-call-openai-python) — Build a simple, non-looping Python agent that lets the LLM choose tools and then invokes the chosen tools with Temporal and OpenAI.
- [Durable agent with MCP and Activity-backed tools using the Strands Agents SDK](/ai/cookbook/strands-agents-python) — Build a durable AI agent in Python with Temporal and the Strands Agents SDK plugin, combining an MCP server tool with an Activity-backed tool that calls a live HTTP feed.
- [Durable agent with tools using the OpenAI Agents SDK](/ai/cookbook/openai-agents-sdk-python) — Build a durable AI agent with the OpenAI Agents SDK and Temporal that chooses tools to answer user questions.
- [Human-in-the-loop AI agent](/ai/cookbook/human-in-the-loop-python) — Add human-in-the-loop approval to a durable AI agent using Temporal Signals in Python.
- [Multi-Agent Orchestration — Google ADK + Temporal](/ai/cookbook/multi-agent-adk-python) — Build a multi-agent pipeline (parallel + sequential) with Google ADK on Temporal — every LLM call and every I/O tool call runs as a durable activity.
- [Post-LLM guardrail with hard-rule overrides](/ai/cookbook/guardrails-hard-rules-python) — Build a durable content-moderation guardrail in Python with Temporal and Claude that layers deterministic hard rules over an LLM's verdict for auditable overrides.
- [Claim check pattern with Temporal](/ai/cookbook/claim-check-pattern-python) — Use the Claim Check pattern with Temporal to keep large payloads out of Event History by offloading them to S3.
- [Deep research](/ai/cookbook/basic-openai-python) — Build a multi-agent deep research system in Python with Temporal and the OpenAI Responses API.
