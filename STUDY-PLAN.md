# 30-Day AI Engineering Study Plan

This roadmap follows the supplied original day-wise syllabus. Keep the order: each day's practical builds on earlier foundations. Provider interfaces, model names, and pricing can change, so consult current documentation before use.

## Week 1: AI and LLM Foundations (Days 1–7)

**Weekly objective:** Understand modern AI applications and work with pre-trained models, APIs, prompts, and basic chatbot integration.

**Weekly milestone:** Explain AI engineering and LLM basics, compare representative models, connect a Python application to an API, and finish a basic AI chatbot.

### Day 1 — Introduction to AI Engineering
- **Topics:** What is an AI Engineer?; roles and responsibilities of an AI Engineer; AI Engineer vs ML Engineer; AI vs AGI; impact of AI on product development; AI ecosystem.
- **Practical output:** AI ecosystem notes and a one-page AI Engineering role map.

### Day 2 — Understanding Large Language Models
- **Topics:** What are Large Language Models (LLMs)?; how LLMs work; inference; training; pre-trained models; benefits and limitations of LLMs; considerations when using LLMs.
- **Practical output:** Run a pre-trained model and record its inputs, outputs, and limitations.

### Day 3 — Understanding the AI Model Ecosystem
- **Topics:** OpenAI; Anthropic Claude; Google Gemini; Mistral; Cohere; model capabilities and differences.
- **Practical output:** Compare five AI models using the same small set of tasks.

### Day 4 — OpenAI API Fundamentals
- **Topics:** OpenAI platform; API fundamentals; Chat Completions; context length; knowledge cut-off dates; model capabilities; connecting Python applications to LLM APIs.
- **Practical output:** Build your first Python LLM application using an API.

### Day 5 — Prompt Engineering Fundamentals
- **Topics:** What is a prompt?; writing effective prompts; prompt structure; maximum tokens; token counting; API pricing; managing tokens.
- **Practical output:** Build a prompt-testing application with token and response comparisons.

### Day 6 — OpenAI Playground and Fine-Tuning
- **Topics:** OpenAI Playground; fine-tuning concepts; model capabilities; model limitations; experimenting with prompts and parameters; understanding output changes.
- **Practical output:** Experiment with different prompts and parameters, and document the output changes.

### Day 7 — Week 1 Revision and Integration
- **Topics:** Revise AI and LLM fundamentals; revise API concepts; practice API integration; combine concepts learned during the week; build a basic AI chatbot.
- **Practical output:** Working AI chatbot using an API.

## Week 2: Prompt Engineering, AI Safety and Open-Source Models (Days 8–14)

**Weekly objective:** Learn advanced prompting, AI security and safety, and local/open-source models and deployment options.

**Weekly milestone:** Produce a tested reusable prompt library, document and test risks, prototype a safety filter, run an open-source/local model, and compare hosted and local AI options.

### Day 8 — Advanced Prompt Engineering
- **Topics:** Prompt engineering roadmap; prompt engineering terminology; prompt patterns; advanced prompting techniques; reusable prompt structures; prompt testing.
- **Practical output:** Create a reusable prompt library with tested examples.

### Day 9 — AI Safety and Security
- **Topics:** Prompt injection attacks; security and privacy; bias in AI systems; fairness; AI safety; potential risks of AI applications.
- **Practical output:** Create prompt-injection test cases and an AI risk register.

### Day 10 — Building Safer AI Applications
- **Topics:** OpenAI Moderation API; end-user IDs; adversarial testing; robust prompting; constraining inputs and outputs; AI safety best practices.
- **Practical output:** Build an AI safety filter prototype with input checks and moderation experiments.

### Day 11 — Open-Source vs Closed-Source Models
- **Topics:** Open-source models; closed-source models; popular open-source models; model selection; quality considerations; speed and cost; privacy and hardware requirements.
- **Practical output:** Create a model comparison sheet covering quality, speed, cost, privacy, and hardware.

### Day 12 — Hugging Face Fundamentals
- **Topics:** Hugging Face Hub; finding models; understanding model tasks; using open-source models; downloading models; running suitable models.
- **Practical output:** Download and run a suitable open-source model.

### Day 13 — Running Local LLMs with Ollama
- **Topics:** Inference SDK; Transformers; Ollama; Ollama models; Ollama SDK; running local LLMs; calling local models from Python.
- **Practical output:** Run a local LLM using Ollama and call it from Python.

### Day 14 — Cloud AI Platforms and Revision
- **Topics:** Azure AI; AWS SageMaker; Replicate; Mistral; Cohere; hosted AI models; local AI models; Week 2 revision.
- **Practical output:** Compare hosted and local AI options and complete the Week 2 revision checkpoint.

## Week 3: Embeddings, Vector Databases and RAG (Days 15–21)

**Weekly objective:** Learn how AI applications represent, search, and retrieve information from data.

**Weekly milestone:** Generate and compare embeddings, build semantic and document search, select a vector database, and deliver an end-to-end source-grounded document chatbot.

### Day 15 — Understanding Embeddings
- **Topics:** What are embeddings?; how embeddings work; OpenAI embedding models; embedding API; embedding pricing; vector dimensions; generating embeddings.
- **Practical output:** Generate embeddings and inspect their dimensions.

### Day 16 — Sentence Transformers and Open-Source Embeddings
- **Topics:** Sentence Transformers; Hugging Face embeddings; open-source embedding models; generating sentence embeddings; comparing embedding models.
- **Practical output:** Generate embeddings and compare different models.

### Day 17 — Semantic Search and Embedding Applications
- **Topics:** Semantic search; data classification; recommendation systems; anomaly detection; embedding use cases; similarity between text representations.
- **Practical output:** Build a semantic search engine using a small text collection.

### Day 18 — Vector Databases
- **Topics:** What is a vector database?; purpose of vector databases; vector database functionality; Chroma; Pinecone; Weaviate; FAISS; LanceDB; Qdrant; Supabase; MongoDB Atlas.
- **Practical output:** Compare vector databases and select one for your project.

### Day 19 — Vector Search and Indexing
- **Topics:** Vector search; indexing embeddings; similarity search; retrieving relevant information; searching stored document embeddings.
- **Practical output:** Build a document search engine.

### Day 20 — Retrieval-Augmented Generation (RAG)
- **Topics:** What is RAG?; RAG use cases; RAG vs fine-tuning; document chunking; embedding generation; vector databases; retrieval; generation; basic RAG architecture.
- **Practical output:** Build a basic RAG system.

### Day 21 — Building Complete RAG Applications
- **Topics:** RAG alternatives; RAG implementation; direct SDKs; LangChain; LlamaIndex; end-to-end testing; source-grounded answers.
- **Practical output:** Build a complete document chatbot that answers questions using retrieved source documents.

## Week 4: AI Agents and Multimodal AI (Days 22–30)

**Weekly objective:** Build controlled agents, integrate tools, explore multimodal capabilities, and test, document, and deploy a final project.

**Weekly milestone:** Build traceable tool-using workflows and image, voice, and multimodal prototypes; freeze the final system's features; then test, debug, document, deploy, and present it.

### Day 22 — Introduction to AI Agents
- **Topics:** What are AI agents?; AI agent use cases; agent prompting; ReAct framework; agent reasoning and actions; controlled agent workflows.
- **Practical output:** Build a basic controlled AI agent.

### Day 23 — Building AI Agents Manually
- **Topics:** Manual agent implementation; OpenAI functions; tools and tool calling; tool execution; agent interactions; connecting agents to external tools.
- **Practical output:** Build an AI agent that calls at least two useful tools.

### Day 24 — Advanced AI Agent Workflows
- **Topics:** OpenAI Assistant API concepts; agent workflows; LangChain agent concepts; LlamaIndex agent concepts; tool-using agents; error handling; traceable workflows.
- **Practical output:** Build a tool-using agent with error handling and a traceable workflow.

### Day 25 — Introduction to Multimodal AI
- **Topics:** What is multimodal AI?; multimodal AI use cases; image understanding; image generation; AI applications involving images.
- **Practical output:** Build an image-understanding application.

### Day 26 — Vision and Image Generation APIs
- **Topics:** OpenAI Vision API; DALL-E API; Hugging Face multimodal models; image-based AI applications; comparing multimodal models.
- **Practical output:** Build an image-based application and compare models.

### Day 27 — Audio and Video AI
- **Topics:** Audio processing; Whisper API; speech-to-text; text-to-speech; video understanding; audio AI applications.
- **Practical output:** Build a voice AI prototype.

### Day 28 — Building Multimodal AI Applications
- **Topics:** LangChain multimodal applications; LlamaIndex multimodal applications; multimodal integration; combining different modalities; multimodal application workflows.
- **Practical output:** Build a multimodal prototype using at least two modalities.

### Day 29 — AI Engineering Tools and Final Revision
- **Topics:** AI code editors; code completion tools; AI development tools; full AI Engineering roadmap revision; integrated system feature freeze; code review; revision notes.
- **Practical output:** Freeze the final system's features, review code, and prepare revision notes.

### Day 30 — Final Project and Deployment
- **Topics:** Final project testing; debugging; documentation; deployment; GitHub presentation; project architecture; final demonstration.
- **Practical output:** Complete the final AI Engineering project, README, architecture diagram, and demo.

## Technologies and tools introduced

Python; OpenAI platform, APIs, Chat Completions, Playground, Moderation API, functions, and Assistant API concepts; Anthropic Claude; Google Gemini; Mistral; Cohere; Azure AI; AWS SageMaker; Replicate; Hugging Face Hub and Transformers; Ollama and its SDK; Sentence Transformers; OpenAI and open-source embedding models; Chroma, Pinecone, Weaviate, FAISS, LanceDB, Qdrant, Supabase, and MongoDB Atlas; LangChain; LlamaIndex; DALL-E; Vision APIs; Whisper; AI code editors and code completion tools; Git and GitHub.

## Daily study routine

For each day, study the syllabus in `DAY-XX/notes.md`, understand the concepts, complete the specified activity in `DAY-XX/practical_output.md`, do 2–3 small Python exercises where applicable, save code only in the provided Python files, update the tracker, and commit the day's work. Keep credentials and private data out of source control.