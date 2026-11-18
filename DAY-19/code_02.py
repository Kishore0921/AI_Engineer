#Prerequisites
#pip install chromadb
'''import chromadb

def main():
    client = chromadb.Client()
    collection = client.get_or_create_collection(name="similarity_search_demo")

    documents = [
        "Bananas are rich in potassium and dietary fiber.",
        "The Eiffel Tower is a wrought-iron lattice tower in Paris, France.",
        "Photosynthesis is the process plants use to convert sunlight into energy.",
        "Football is the most popular sport in the world.",
        "Strawberries and blueberries are packed with antioxidants.",
        "Mount Everest is Earth's highest mountain above sea level.",
        "Oranges and lemons are citrus fruits high in Vitamin C.",
        "The Pacific Ocean is the largest and deepest ocean on Earth.",
        "Tennis can be played individually against a single opponent or between two teams.",
        "Apples are nutritious fruits that come in many varieties like Fuji and Gala."
    ]
    ids = [f"item_{i+1}" for i in range(len(documents))]

    # Index the documents
    collection.add(documents=documents, ids=ids)

    # Accept a search query from the user
    query = input("Enter your search query (e.g., 'healthy fruits with vitamins'): ").strip()
    if not query:
        query = "healthy fruits with vitamins"
        print(f"Using default query: '{query}'")

    # Perform similarity search for the top 3 results
    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    print("\nTop 3 Ranked Search Results:")
    print("-" * 60)
    for rank, (doc, dist) in enumerate(zip(results["documents"][0], results["distances"][0]), start=1):
        print(f"Rank #{rank} | Distance: {dist:.4f}")
        print(f"Document: {doc}\n")

if __name__ == "__main__":
    main()
'''