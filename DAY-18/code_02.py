#install the Chroma library via your terminal:
#pip install chromadb
'''import chromadb

# 1. Initialize client and create collection
client = chromadb.Client()
collection = client.get_or_create_collection(name="educational_docs")

# 2. Store sample educational documents (Chroma auto-generates embeddings)
edu_documents = [
    (
        "Photosynthesis is the process by which green plants convert sunlight"
        " into chemical energy."
    ),
    (
        "The Pythagorean theorem states that in a right triangle, the square of"
        " the hypotenuse equals the sum of the squares of the other two sides."
    ),
    (
        "World War II was a global conflict that lasted from 1939 to 1945"
        " involving most of the world's nations."
    ),
    (
        "Mitochondria are double-membrane-bound organelles found in most"
        " eukaryotic organisms, often called the powerhouse of the cell."
    ),
    (
        "Newton's second law of motion states that Force equals mass times"
        " acceleration (F = ma)."
    ),
]
edu_ids = ["bio_1", "math_1", "hist_1", "bio_2", "phys_1"]

collection.add(documents=edu_documents, ids=edu_ids)

# 3. Enter a natural-language search query
query_text = "How do cells and plants produce energy?"
print(f"Search Query: '{query_text}'\n")

# 4. Retrieve the top 3 similar documents
results = collection.query(query_texts=[query_text], n_results=3)

# 5. Display their similarity distances (Lower L2 distance = higher similarity)
print("--- Top 3 Relevant Documents Ranked by Similarity ---")
for i in range(len(results["ids"][0])):
  doc_id = results["ids"][0][i]
  distance = results["distances"][0][i]
  document = results["documents"][0][i]
  print(f"Rank {i+1} [ID: {doc_id} | Distance: {distance:.4f}]: {document}")
'''