# Day 20 Practical — Build a basic RAG system

## Practical objective
Connect a small document collection to an LLM through chunking, embedding, retrieval, and answer generation.

## Exact practical output
**Build a basic RAG system.**

## Tasks
1. Select a small, non-sensitive document set and record its sources.
2. Split documents into manageable chunks and retain source metadata.
3. Generate embeddings and index chunks in the chosen vector store.
4. For a test question, retrieve relevant chunks and pass them with the question to the model.
5. Ask the model to answer from supplied context and say when evidence is insufficient; show retrieved sources.
6. Test supported and unsupported questions, then record retrieval and answer failures separately.

## Expected result
A basic RAG pipeline that retrieves document passages and generates a response grounded in that context, with sources exposed for review.

## Completion checklist
- [ ] Chunking preserves source references.
- [ ] Embeddings and index are created.
- [ ] Retrieval context is passed to the generator.
- [ ] Supported and unsupported queries are tested.
- [ ] Source evidence and limitations are visible.

## Save to GitHub
Save code in `DAY-20/code_*.py` and setup/rebuild instructions here. Commit with a message such as `Day 20: build a basic RAG pipeline`.