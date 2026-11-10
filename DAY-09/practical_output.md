# Day 9 Practical — Create prompt-injection test cases and an AI risk register

## Practical objective
Document how an AI feature may fail or be misused, and create safe, non-destructive tests for its behavior.

## Exact practical output
**Create prompt-injection test cases and an AI risk register.**

## Tasks
1. Define a hypothetical or local-only AI feature and its intended behavior.
2. Write benign test cases that check whether untrusted input can override task instructions or request disclosure of protected context; do not target real services or use real secrets.
3. Record expected safe behavior and observed model behavior separately.
4. Create a risk register with risk, affected asset/user, likelihood, impact, mitigation, and a way to validate the mitigation.
5. Include security/privacy, bias/fairness, and broader AI safety risks relevant to the feature.

## Expected result
A bounded, safe set of prompt-injection tests and a prioritized, actionable AI risk register.

## Completion checklist
- [x] Feature scope and intended behavior are stated.
- [x] Test cases use no real secrets or external target.
- [x] Expected and observed behavior are distinguished.
- [x] Risk register covers relevant security, privacy, bias, fairness, and safety concerns.
- [x] Mitigations have validation ideas.

## Save to GitHub
Save the test cases and risk register in `DAY-09`. Commit with a message such as `Day 09: document AI risks and injection tests`.