#Prerequisites
#pip install chromadb sentence-transformers openai
'''import chromadb
from sentence_transformers import SentenceTransformer

def split_text(text, chunk_size=220, chunk_overlap=40):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + chunk_size].strip())
        start += (chunk_size - chunk_overlap)
    return chunks

def main():
    # Sample knowledge base document
    document_content = (
        "Solar energy is radiant light and heat from the Sun harnessed using technologies such as solar panels. "
        "Photovoltaic (PV) cells convert sunlight directly into electricity using semiconducting materials like silicon. "
        "Wind energy captures kinetic energy from air currents using large turbines to generate clean electrical power. "
        "Hydroelectric power generates electricity by using flowing water to spin turbines connected to generators. "
        "Battery storage systems store excess renewable energy so power remains available when the sun is not shining or wind is calm. "
        "Transitioning to renewable energy reduces greenhouse gas emissions and lowers dependence on fossil fuels."
    )

    # 1. Split document into chunks
    chunks = split_text(document_content, chunk_size=220, chunk_overlap=40)
    print(f"Document split into {len(chunks)} chunks.")

    # 2. Generate embeddings using Sentence Transformers
    print("Loading SentenceTransformer model ('all-MiniLM-L6-v2')...")
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = embedder.encode(chunks).tolist()

    # 3. Store chunks and embeddings in a persistent Chroma database
    client = chromadb.PersistentClient(path="./chroma_rag_db")
    collection = client.get_or_create_collection(name="renewable_energy_rag")

    ids = [f"chunk_{i+1}" for i in range(len(chunks))]
    metadatas = [{"source": "Renewable_Energy_Guide.txt", "chunk_index": i+1} for i in range(len(chunks))]

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"\nSuccessfully indexed {collection.count()} document chunks into Chroma ('./chroma_rag_db').")

if __name__ == "__main__":
    main()
'''