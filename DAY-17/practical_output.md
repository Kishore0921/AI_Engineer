# Day 17 Practical — Build a semantic search engine using a small text collection

## Practical objective
Represent a small collection and query with embeddings, then rank the most semantically relevant items.

## Exact practical output
**Build a semantic search engine using a small text collection.**

## Tasks
1. Collect or write a small set of non-sensitive text snippets with known subject matter.
2. Generate an embedding for each item and for a natural-language query using the same model.
3. Compute a documented similarity score and rank the collection.
4. Test several queries, including paraphrases and queries with no good match; inspect whether the ranking makes sense.
5. Document the model, metric, results, and one possible extension to classification, recommendation, or anomaly detection.

## Expected result
A runnable small semantic search workflow that returns ranked text snippets for natural-language queries.

## Completion checklist
- [ ] Text collection is saved and appropriate for sharing.
- [ ] Query and items use the same embedding model.
- [ ] Similarity ranking is implemented and tested.
- [ ] Results and limitations are documented.

## Save to GitHub
Save implementation in `DAY-17/code_*.py` and sample collection/results here. Commit with a message such as `Day 17: build a semantic text search`.