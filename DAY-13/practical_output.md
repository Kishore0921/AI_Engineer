# Day 13 Practical — Run a local LLM using Ollama and call it from Python

## Practical objective
Exercise a local model through Ollama and connect to it from a small Python client.

## Exact practical output
**Run a local LLM using Ollama and call it from Python.**

## Tasks
1. Install/use Ollama only if already permitted by the environment and follow its official setup instructions; no repository dependency installation is required for this documentation task.
2. Select an available model tag that fits local hardware and note its size and source.
3. Start the model and send a simple, non-sensitive prompt through the Ollama interface.
4. Use the documented Ollama Python SDK or local API to send a prompt from Python and display the result.
5. Record hardware, response behavior, and any download/runtime limitations; handle a stopped service or missing model as an error.

## Expected result
A local model responds through Ollama and through a Python call, with setup and environment details documented.

## Completion checklist
- [ ] Model and local runtime are identified.
- [ ] Ollama run succeeds or blocker is documented.
- [ ] Python call uses the documented local interface.
- [ ] Service/model errors are visible.
- [ ] No private prompt data is included in committed logs.

## Save to GitHub
Save the Python client in `DAY-13/code_*.py` and the run instructions/results here. Commit with a message such as `Day 13: call a local Ollama model`.