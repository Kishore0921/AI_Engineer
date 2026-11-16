#Make sure you have the required library installed:
#pip install sentence-transformers
import torch
from sentence_transformers import SentenceTransformer, util

def main():
    # Load model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # 1. Create a small collection of documents
    documents = [
        "Python is widely used in data science, web development, and automation.",
        "Photosynthesis is the process by which green plants convert sunlight into chemical energy.",
        "The Indian Space Research Organisation (ISRO) launched Chandrayaan-3 to explore the lunar south pole.",
        "Regular cardiovascular exercise improves heart health and boosts daily energy levels.",
        "Quantum computing uses qubits to perform complex calculations exponentially faster than classical computers.",
        "Sourdough bread relies on natural wild yeast and lactobacilli for fermentation.",
        "Bengaluru is widely recognized as the primary technology and startup hub of India."
    ]

    # 2. Generate embeddings for the document collection
    print("Indexing documents...")
    doc_embeddings = model.encode(documents, convert_to_tensor=True)

    # 3. Accept a user search query
    query = input("\nEnter your search query: ").strip()
    if not query:
        query = "space exploration and moon missions"
        print(f"Using default query: '{query}'")

    query_embedding = model.encode(query, convert_to_tensor=True)

    # 4. Return the top 3 most relevant documents
    cosine_scores = util.cos_sim(query_embedding, doc_embeddings)[0]
    top_results = torch.topk(cosine_scores, k=min(3, len(documents)))

    print(f"\nTop 3 Search Results for: '{query}'")
    print("-" * 60)
    for rank, (score, idx) in enumerate(zip(top_results.values, top_results.indices), start=1):
        print(f"Rank {rank} [Score: {score.item():.4f}]")
        print(f"Document: {documents[idx]}\n")

if __name__ == "__main__":
    main()
