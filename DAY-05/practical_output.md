# Day 5 Practical — Build a prompt-testing application with token and response comparisons

## Practical objective
Create a small test harness that compares prompt variants and makes token/response differences visible.

## Exact practical output
**Build a prompt-testing application with token and response comparisons.**

## Tasks
1. Choose one task and write two or three prompt variants that differ in a deliberate way.
2. Use the same model and test input for every variant.
3. Build a small application that submits each prompt and records its response; include token counts when the chosen API or tokenizer makes them available.
4. Record the model's current pricing source and calculate or estimate usage only from that source.
5. Compare response usefulness and token/output differences; note any measurement limitations.

## Expected result
A runnable prompt comparison tool and a compact report showing prompt variants, responses, token counts where available, and pricing assumptions.

## Completion checklist
- [x] Task and prompt variants are saved.
- [x] Test conditions are comparable.
- [x] Responses and token measurements are recorded.
- [x] Pricing source/date and assumptions are documented.
- [x] Credentials are not saved in code.

## Save to GitHub
Save the app in `DAY-05/code_*.py` and the test results in this folder. Commit with a message such as `Day 05: compare prompts and token usage`.