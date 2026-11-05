# Day 22 Practical — Build a basic controlled AI agent

## Practical objective
Implement an agent-like loop with a small, explicit action set and a clear stopping rule.

## Exact practical output
**Build a basic controlled AI agent.**

## Tasks
1. Choose a low-risk task and write down what the agent may and may not do.
2. Define a small set of safe actions (including a no-action/final-answer option) and validate action names/arguments.
3. Implement a bounded cycle: provide task, choose an allowed action, execute it, return the observation, and stop at a fixed limit.
4. Test a normal task, an invalid action, and a case where the agent should stop or ask for help.
5. Record the workflow, allowed actions, stopping condition, and failure behavior.

## Expected result
A small agent workflow that can complete a bounded task and rejects or safely handles actions outside its declared scope.

## Completion checklist
- [ ] Task scope and allowed actions are explicit.
- [ ] Action arguments are checked before execution.
- [ ] The loop has a stopping condition/step limit.
- [ ] Invalid or failed actions are visible and safely handled.
- [ ] Test observations are recorded.

## Save to GitHub
Save code in `DAY-22/code_*.py` and document the workflow here. Commit with a message such as `Day 22: build a controlled agent loop`.