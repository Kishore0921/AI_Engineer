# Day 4 Practical — Build your first Python LLM application using an API

## Practical objective
Build a minimal Python program that sends a user prompt to an LLM API and displays the returned response.

## Exact practical output
**Build your first Python LLM application using an API.**

## Tasks
1. Review the provider's current API and Python SDK documentation; choose an available model.
2. Configure the API key outside the source file using an environment variable or approved secret store.
3. Write a small program that accepts or defines a non-sensitive prompt, sends the documented request, and prints the response.
4. Handle missing credentials and API failures with clear messages; do not print or commit the key.
5. Run one successful request and record the model, prompt, and a short result summary.

## Expected result
A working, reproducible Python LLM application with credentials kept outside the repository and a recorded successful test.

## Completion checklist
- [x] Current API documentation and model are recorded.
- [x] Python app sends a prompt and displays the response.
- [x] Missing key or API failure is reported clearly.
- [x] No key or sensitive data is stored in the repository.

## Save to GitHub
Save the application in an appropriate `DAY-04/code_*.py` file and document setup without secrets. Commit with a message such as `Day 04: build a Python LLM API app`.