#Prerequisites
#pip install chromadb
'''import chromadb

def main():
    # Initialize an in-memory Chroma client
    client = chromadb.Client()

    # Create or get a collection
    collection = client.get_or_create_collection(name="sample_documents")

    # 12 sample documents
    documents = [
        "Python is a high-level, interpreted programming language.",
        "Machine learning is a subset of artificial intelligence.",
        "Chroma is an open-source AI-native vector database.",
        "Neural networks are inspired by the human brain.",
        "SQL is used for managing relational databases.",
        "HTML and CSS are the core technologies for building web pages.",
        "Git is a distributed version control system for tracking code changes.",
        "Docker allows developers to package applications into containers.",
        "APIs enable different software applications to communicate with each other.",
        "Cloud computing delivers computing services over the internet.",
        "Cybersecurity protects systems and networks from digital attacks.",
        "Data science combines statistics, programming, and domain expertise."
    ]

    # Metadata and unique IDs for each document
    metadatas = [
        {"category": "programming", "level": "beginner"},
        {"category": "ai", "level": "intermediate"},
        {"category": "database", "level": "intermediate"},
        {"category": "ai", "level": "advanced"},
        {"category": "database", "level": "beginner"},
        {"category": "web", "level": "beginner"},
        {"category": "devops", "level": "beginner"},
        {"category": "devops", "level": "intermediate"},
        {"category": "software", "level": "beginner"},
        {"category": "cloud", "level": "beginner"},
        {"category": "security", "level": "intermediate"},
        {"category": "data", "level": "intermediate"}
    ]
    ids = [f"doc_{i+1}" for i in range(len(documents))]

    # Add documents (Chroma generates and indexes embeddings automatically)
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    # Retrieve stored items to verify indexing
    stored_data = collection.get()

    print(f"Successfully indexed {len(stored_data['ids'])} documents.\n")
    print("Stored Document IDs and Metadata:")
    print("-" * 50)
    for doc_id, meta in zip(stored_data["ids"], stored_data["metadatas"]):
        print(f"ID: {doc_id:<8} | Metadata: {meta}")

if __name__ == "__main__":
    main()
'''