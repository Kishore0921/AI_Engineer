# Day 24 Practical — Build a tool-using agent with error handling and a traceable workflow

## Practical objective
Improve the manual agent with workflow structure, observable steps, and deliberate failure handling.

## Exact practical output
**Build a tool-using agent with error handling and a traceable workflow.**

## Tasks
1. Choose an approach (direct workflow, Assistant API concepts, LangChain, or LlamaIndex) and document the relevant abstraction.
2. Define the workflow states, tools, step limit, and completion conditions.
3. Record each step's event type, safe input summary, tool/action, result status, and timing where practical.
4. Handle malformed tool requests, tool exceptions, model/API errors, and exhausted limits without returning a success-shaped answer.
5. Test a successful run and at least two failure cases; redact keys and sensitive data from traces.

## Expected result
A bounded tool-using agent with clear error paths and a useful redacted execution trace.

## Completion checklist
- [ ] Workflow and termination rules are documented.
- [ ] Tool execution and errors are traceable.
- [ ] At least one successful and two failing cases are tested.
- [ ] Secrets and sensitive content are excluded from logs.
- [ ] Framework/API choice is identified.

## Save to GitHub
Save implementation in `DAY-24/code_*.py` and example redacted traces here. Commit with a message such as `Day 24: trace and harden an agent workflow`.