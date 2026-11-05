# Day 21 — Building Complete RAG Applications

## Learning objective
Extend a basic RAG pipeline into an end-to-end document chatbot and compare implementation approaches.

## Topics and subtopics
1. RAG alternatives.
2. RAG implementation.
3. Direct SDKs.
4. LangChain.
5. LlamaIndex.
6. End-to-end testing.
7. Source-grounded answers.

## Important concepts
- Frameworks can simplify orchestration but add abstractions; understand the retrieval/generation flow they implement.
- Direct SDKs provide a more explicit integration path; choose based on project complexity and maintainability.
- End-to-end testing should cover ingestion, retrieval, generation, errors, and unsupported questions.
- Source-grounded responses should expose retrieved evidence and avoid claiming unsupported facts.

## Key terminology
RAG alternative, direct SDK, LangChain, LlamaIndex, end-to-end test, source grounding, ingestion, retrieval.

## Learning outcomes
- Compare direct SDKs, LangChain, and LlamaIndex at a practical level.
- Build a document chatbot that answers using retrieved source documents.
- Test source grounding and identify retrieval or generation failures.