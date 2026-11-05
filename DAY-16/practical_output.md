# Day 16 Practical — Generate embeddings and compare different models

## Practical objective
Run at least two suitable embedding models on shared sentence examples and compare their outputs meaningfully.

## Exact practical output
**Generate embeddings and compare different models.**

## Tasks
1. Select two documented Sentence Transformers/Hugging Face embedding models and review their task descriptions and licenses.
2. Create a small set of non-sensitive sentences, including a paraphrase pair and an unrelated pair.
3. Generate embeddings with each model and record dimensions and runtime context.
4. Compare similarity relationships within each model's vector space; do not compare raw vector coordinates across models.
5. Summarize which model seems suitable for a stated use case and note limits of the small sample.

## Expected result
A model comparison record with examples, dimensions, similarity observations, and a use-case-based conclusion.

## Completion checklist
- [ ] Two models and their documentation are recorded.
- [ ] The same sentences are encoded by each model.
- [ ] Dimensions and within-model similarity observations are included.
- [ ] Conclusion and sample limitations are stated.

## Save to GitHub
Save scripts in `DAY-16/code_*.py` and results here. Commit with a message such as `Day 16: compare open-source embeddings`.