# Day 23 Practical — Build an AI agent that calls at least two useful tools

## Practical objective
Connect a model to two bounded tools and implement the tool-execution loop in application code.

## Exact practical output
**Build an AI agent that calls at least two useful tools.**

## Tasks
1. Choose two safe, useful tools for a simple task (for example, a deterministic calculator and a lookup over local sample data).
2. Define each tool's name, arguments, validation rules, and return shape.
3. Ask the model for a tool call using the current documented functions/tool-calling interface.
4. Validate the requested tool and arguments in Python, execute only allowed operations, and return the result to the model.
5. Test both tools, invalid arguments, and an unknown tool request; record the interaction sequence.

## Expected result
A manual tool-using agent that invokes at least two useful tools through validated application-side execution.

## Completion checklist
- [ ] Two tools have clear, bounded contracts.
- [ ] Tool requests and arguments are validated.
- [ ] Both tools are exercised in tests.
- [ ] Unknown tools and tool failures are handled visibly.
- [ ] No unsafe external side effects occur without explicit approval.

## Save to GitHub
Save the implementation in `DAY-23/code_*.py` and record test interactions here. Commit with a message such as `Day 23: add two validated agent tools`.