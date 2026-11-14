# Day 15 Practical — Generate embeddings and inspect their dimensions

## Practical objective
Generate vector representations of sample text and inspect the returned vector shape.

## Exact practical output
**Generate embeddings and inspect their dimensions.**

## Tasks
1. Choose a documented OpenAI embedding model and check current API requirements, dimensions, and pricing.
2. Prepare a few short, non-sensitive sentences and request embeddings.
3. Inspect the returned vector length/dimensions and record the exact model identifier.
4. Verify that every vector in the test uses the same expected dimension; do not print or commit unnecessarily large vectors.
5. Record the approximate input size and pricing assumptions/source/date.

## Expected result
A reproducible small embedding experiment with model name, text samples, dimension count, and pricing notes.

## Completion checklist
- [x] Embedding model/API is identified.
- [x] Embeddings are generated or an access limitation is documented.
- [x] Vector dimensions are inspected.
- [x] Pricing source and date are recorded.
- [x] Test data is non-sensitive.

## Save to GitHub
Save code in `DAY-15/code_*.py` and concise results in this folder. Commit with a message such as `Day 15: inspect text embedding dimensions`.