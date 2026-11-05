# Day 23 — Building AI Agents Manually

## Learning objective
Implement tool calling directly and understand the boundary between a model's proposed tool request and application-side execution.

## Topics and subtopics
1. Manual agent implementation.
2. OpenAI functions.
3. Tools and tool calling.
4. Tool execution.
5. Agent interactions.
6. Connecting agents to external tools.

## Important concepts
- A model can return a structured request for a function/tool; the application must validate and execute it.
- Tool schemas describe names and arguments but are not authorization controls.
- Restrict available tools and arguments; treat model-provided values as untrusted input.
- Return bounded tool results to the model and handle malformed requests, timeouts, and failures.

## Key terminology
Manual agent, function calling, tool schema, tool call, tool execution, argument validation, external tool.

## Learning outcomes
- Explain tool-calling request and execution flow.
- Build a manual agent that uses at least two useful tools.
- Validate tool arguments and report execution errors clearly.