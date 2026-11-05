# Day 20 — Retrieval-Augmented Generation (RAG)

## Learning objective
Understand the basic RAG pipeline and how retrieval can provide source material to a language model at answer time.

## Topics and subtopics
1. What is RAG?
2. RAG use cases.
3. RAG vs fine-tuning.
4. Document chunking.
5. Embedding generation.
6. Vector databases.
7. Retrieval.
8. Generation.
9. Basic RAG architecture.

## Important concepts
- RAG retrieves relevant external content and supplies it to a model for generating a response.
- A basic pipeline includes document chunking, embedding, indexing, retrieval, prompt/context assembly, and generation.
- RAG can ground answers in provided sources, but poor retrieval or unsupported generation can still produce errors.
- Fine-tuning changes model behavior through training; RAG supplies potentially updateable information at inference.
- Chunk size and overlap affect context and retrieval; validate choices on representative questions.

## Key terminology
Retrieval-Augmented Generation (RAG), chunk, embedding, vector database, retriever, context, generation, grounding.

## Learning outcomes
- Draw and explain a basic RAG architecture.
- Distinguish RAG from fine-tuning.
- Build a basic pipeline and inspect retrieval and answer quality.