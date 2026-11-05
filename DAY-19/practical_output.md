# Day 19 Practical — Build a document search engine

## Practical objective
Create a search workflow that stores document embeddings and returns the most relevant source passages.

## Exact practical output
**Build a document search engine.**

## Tasks
1. Prepare a small set of shareable documents or text passages and assign each a source identifier.
2. Generate embeddings and store vectors with the text and relevant metadata in the selected index/database.
3. Embed a user query and retrieve the top relevant stored items by similarity.
4. Display matched text with its source identifier; test several queries and inspect retrieval quality.
5. Record the chosen metric, index/database, limitations, and how the index can be rebuilt.

## Expected result
A small document search engine that finds and displays relevant passages with source references.

## Completion checklist
- [ ] Documents are associated with source metadata.
- [ ] Embeddings are indexed and queryable.
- [ ] Search returns ranked source-linked passages.
- [ ] Several test queries and limitations are documented.

## Save to GitHub
Save code in `DAY-19/code_*.py`, plus safe sample documents or a reconstruction note. Commit with a message such as `Day 19: index and search documents`.