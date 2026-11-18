#Prerequisites
#pip install chromadb sentence-transformers openai
'''import os
import chromadb
from sentence_transformers import SentenceTransformer
from openai import OpenAI

# Set your API key in your terminal before running:
# export OPENAI_API_KEY="your-api-key-here"
# (Or point base_url="http://localhost:11434/v1" and api_key="ollama" for local Ollama)
llm_client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", "your-api-key-here")
)

def main():
    print("Loading embedding model and connecting to ChromaDB...")
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    chroma_client = chromadb.PersistentClient(path="./chroma_rag_db")
    collection = chroma_client.get_collection(name="renewable_energy_rag")

    print("\nRAG Chatbot Ready! Ask a question about your indexed documents (type 'exit' to quit).\n")

    while True:
        user_question = input("You: ").strip()
        if user_question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if not user_question:
            continue

        # 1. Embed the user's question and retrieve top 2 relevant chunks
        query_embedding = embedder.encode([user_question]).tolist()
        results = collection.query(
            query_embeddings=query_embedding,
            n_results=2
        )

        retrieved_chunks = results["documents"]
        context = "\n\n".join(retrieved_chunks)

        # 2. Construct prompt with retrieved context
        system_prompt = (
            "You are a helpful assistant. Answer the user's question using ONLY the provided context. "
            "If the answer is not contained in the context, say 'I do not have enough information in the documents to answer that.'"
        )
        user_prompt = f"Context:\n{context}\n\nQuestion: {user_question}"

        # 3. Send question and context to the LLM
        try:
            response = llm_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.2
            )
            answer = response.choices[0].message.content
            print(f"\nBot: {answer}\n")
        except Exception as e:
            print(f"\n[LLM Error]: {e}")
            print("Retrieved Context was:\n" + context + "\n")

if __name__ == "__main__":
    main()
'''