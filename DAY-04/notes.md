# Day 4 — OpenAI API Fundamentals

## Learning objective
Understand the basic API request/response flow and how a Python application can communicate with an LLM.

## Topics and subtopics
1. OpenAI platform.
2. API fundamentals.
3. Chat Completions.
4. Context length.
5. Knowledge cut-off dates.
6. Model capabilities.
7. Connecting Python applications to LLM APIs.

## Important concepts
- An API lets an application send a structured request and receive a model response.
- Chat Completions represents a conversation as role-labelled messages; check current platform guidance because APIs evolve.
- Context length bounds the material a model can consider in one request.
- A model's training knowledge has limits and may not include current events.
- Keep keys out of source code; handle network, authentication, rate-limit, and response errors visibly.

## Key terminology
API, endpoint, request, response, SDK, Chat Completions, message role, context length, knowledge cut-off, API key.

## Learning outcomes
- Describe a basic LLM API exchange.
- Connect a Python application to an API using the documented client pattern.
- Identify context and knowledge limits and protect credentials.