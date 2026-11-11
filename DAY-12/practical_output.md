# Day 12 Practical — Download and run a suitable open-source model

## Practical objective
Use the Hub to select a documented model and perform one local inference run where the environment supports it.

## Exact practical output
**Download and run a suitable open-source model.**

## Tasks
1. Pick a small, appropriate model for a supported task; review its model card, license, files, and hardware needs.
2. Record the model identifier and selection rationale before downloading.
3. Download it using the documented Hub/Transformers workflow or another documented supported method.
4. Run one safe sample input and record the output and runtime/hardware context.
5. If the machine cannot run it, document the specific storage/hardware/runtime blocker and preserve the model-selection and run instructions without claiming a successful run.

## Expected result
A documented model selection and actual inference output, or a transparent, actionable record of the environment blocker.

## Completion checklist
- [x] Model task, card, license, and requirements were checked.
- [x] Download/run was performed or the exact blocker is recorded.
- [x] Sample input and output are saved when run.
- [x] Model files and generated artifacts are handled appropriately.

## Save to GitHub
Save the run notes and, where appropriate, a small script in `DAY-12/code_*.py`; do not commit large weights. Commit with a message such as `Day 12: run a Hugging Face model`.