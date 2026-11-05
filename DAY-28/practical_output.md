# Day 28 Practical — Build a multimodal prototype using at least two modalities

## Practical objective
Combine two or more modalities in one user workflow and demonstrate how information passes between them.

## Exact practical output
**Build a multimodal prototype using at least two modalities.**

## Tasks
1. Choose two available modalities (for example, image plus text question, or speech input plus text response).
2. Draw the workflow and identify preprocessing, model/API, and output for each modality.
3. Implement a minimal end-to-end path using available components; use LangChain or LlamaIndex concepts where appropriate and document framework choice.
4. Test valid inputs and one missing/invalid modality case; ensure the failure is reported rather than silently ignored.
5. Record component versions/models, sample results, compatibility limits, and privacy/consent considerations.

## Expected result
A working or clearly bounded two-modality prototype with an understandable workflow diagram and test notes.

## Completion checklist
- [ ] At least two modalities are genuinely used in one workflow.
- [ ] Integration path and component choices are documented.
- [ ] Valid and failure-path tests are recorded.
- [ ] Privacy/consent and model limitations are addressed.

## Save to GitHub
Save code in `DAY-28/code_*.py` and a small workflow diagram or text description here. Commit with a message such as `Day 28: integrate two AI modalities`.