# 30 Days of AI Engineering

Welcome to my learning repository for a structured, beginner-friendly 30-day journey through AI engineering. It documents my learning journey with daily topic notes, practical deliverables, exercises, and progress tracking. It is a study plan—not a claim that I have completed the roadmap or its projects.

## Learning objectives

- Understand AI engineering, large language models, and the model ecosystem.
- Connect applications to hosted and local models and write effective prompts.
- Apply safety practices and compare model and deployment options.
- Generate and use embeddings, semantic search, vector databases, and RAG.
- Build controlled AI agents, use tools, and explore vision, audio, video, and multimodal workflows.
- Document, test, and present an integrated AI engineering project.

## What I will learn

The roadmap progresses from AI/LLM foundations to prompt engineering and safe model use, then embeddings and retrieval-augmented generation, and finally agents, tool calling, multimodal applications, and deployment. The exact day-wise syllabus and practical outputs are in [STUDY-PLAN.md](./STUDY-PLAN.md).

## 30-day roadmap overview

| Days | Focus |
|---|---|
| 1–7 | AI and LLM Foundations |
| 8–14 | Prompt Engineering, AI Safety and Open-Source Models |
| 15–21 | Embeddings, Vector Databases and RAG |
| 22–30 | AI Agents and Multimodal AI |

## Technologies and tools

The plan introduces Python, OpenAI APIs and Playground, Anthropic Claude, Google Gemini, Mistral, Cohere, Azure AI, AWS SageMaker, Replicate, Hugging Face Hub and Transformers, Ollama, Sentence Transformers, embedding APIs, Chroma, Pinecone, Weaviate, FAISS, LanceDB, Qdrant, Supabase, MongoDB Atlas, LangChain, LlamaIndex, OpenAI moderation and tool/function APIs, DALL-E, Vision APIs, Whisper, AI code editors, Git, and GitHub. These are learning options to evaluate; not every service requires an account or paid usage.

## Weekly milestones

- **Week 1 (Days 1–7):** Explain AI engineering and LLM fundamentals, compare models, make an API call, and integrate a basic API chatbot.
- **Week 2 (Days 8–14):** Create tested prompts, identify safety risks, build a safety-filter prototype, compare and run models, and review hosted/local choices.
- **Week 3 (Days 15–21):** Generate and compare embeddings, build semantic and document search, select a vector database, and create a source-grounded document chatbot.
- **Week 4 (Days 22–30):** Build controlled tool-using agents, explore image/audio/video and multimodal workflows, freeze and test an integrated project, and prepare its documentation, architecture, demo, and deployment.

## Daily learning methodology

Each day follows this sequence:

1. Study the day's topics.
2. Understand the concepts and terminology in `notes.md`.
3. Perform the day-specific activity in `practical_output.md`.
4. Complete 2–3 small Python coding exercises where applicable.
5. Save code in the provided `code_01.py`, `code_02.py`, and `code_03.py` files as appropriate.
6. Update [PROGRESS-TRACKER.md](./PROGRESS-TRACKER.md).
7. Commit the day's work to GitHub using a clear, day-specific commit message.

Use API keys through environment variables or a secret manager, never commit them. Check current provider documentation, pricing, model availability, and data-handling terms before sending data to an external service. Local and API exercises should be run only when the required tools and access are available.

## Practical projects

The daily outputs build incrementally: model comparisons and a chatbot; a prompt library and safety experiments; local model runs; embedding comparisons, semantic/document search, and a RAG document chatbot; then tool-using agents, image and voice prototypes, a multimodal prototype, and a final AI engineering project. Each day's target is recorded in the corresponding `DAY-XX/practical_output.md`.

## Repository structure

```text
30-Days-of-AI-Engineering/
├── README.md
├── STUDY-PLAN.md
├── PROGRESS-TRACKER.md
├── DAY-01/ ... DAY-30/
│   ├── notes.md
│   ├── practical_output.md
│   ├── code_01.py
│   ├── code_02.py
│   └── code_03.py
```

Daily notes are a concise syllabus reference; practical files contain actionable steps and completion checks. The Python files are reserved for exercises.

## Progress tracking

All work starts unchecked in `PROGRESS-TRACKER.md`. After studying, mark only the tasks actually completed, add a short note about challenges or discoveries, and review the weekly milestone. Do not mark the roadmap complete until the work and evidence exist.

## GitHub contribution and commit methodology

Keep commits small and attributable to the day's work. A suggested pattern is `Day 03: compare five model responses`. Include the relevant notes, practical output, and code together when appropriate; do not commit credentials, private data, large model files, or generated artifacts that are not needed. Review the diff before committing, and use the tracker to record the commit reference.

