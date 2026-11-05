# Day 21 Practical — Build a complete document chatbot that answers questions using retrieved source documents

## Practical objective
Integrate document ingestion, retrieval, and generation into an end-to-end chatbot that shows its evidence.

## Exact practical output
**Build a complete document chatbot that answers questions using retrieved source documents.**

## Tasks
1. Select the implementation path (direct SDK, LangChain, or LlamaIndex) and note why it fits the small project.
2. Ingest the document set, chunk it, generate embeddings, and retain source metadata.
3. Implement a user question flow that retrieves relevant passages and generates a context-grounded answer.
4. Display citations/source references and handle no-relevant-source and API/store failure cases clearly.
5. Test representative supported, ambiguous, and unsupported questions end to end; record whether each answer is grounded in retrieved text.

## Expected result
A working document chatbot with retrieved source references, clear failure behavior, and an end-to-end test record.

## Completion checklist
- [ ] Documents are ingested with source metadata.
- [ ] Chatbot retrieves relevant evidence before generation.
- [ ] Answers expose their source documents.
- [ ] Unsupported questions and failures are tested.
- [ ] Implementation choice and test results are documented.

## Save to GitHub
Save code in `DAY-21/code_*.py`, sample data or rebuild instructions, and test results. Commit with a message such as `Day 21: build a source-grounded document chatbot`.