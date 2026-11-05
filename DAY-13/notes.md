# Day 13 — Running Local LLMs with Ollama

## Learning objective
Understand common inference tooling and run a local LLM through Ollama from both its interface and Python.

## Topics and subtopics
1. Inference SDK.
2. Transformers.
3. Ollama.
4. Ollama models.
5. Ollama SDK.
6. Running local LLMs.
7. Calling local models from Python.

## Important concepts
- An inference SDK or runtime provides a programmatic way to load or call a model.
- Transformers provides model and tokenizer tooling; Ollama manages local model runs through its own runtime/interface.
- Local inference avoids sending prompts to a hosted model provider, but local files, logs, and machine access still require care.
- Hardware, memory, model size, and quantization affect whether and how quickly a model runs.
- The local Python client must target the running local service and report connection/model errors clearly.

## Key terminology
Inference SDK, Transformers, Ollama, model tag, local LLM, runtime, Ollama SDK, quantization.

## Learning outcomes
- Distinguish model tooling from the model itself.
- Run an available local model with Ollama.
- Call the local model from Python and describe hardware/runtime limits.