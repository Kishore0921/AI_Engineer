#install the Chroma library via your terminal:
#pip install chromadb
'''
import chromadb

# 1. Initialize the Chroma client (in-memory for quick testing)
client = chromadb.Client()

# 2. Create a collection
collection = client.get_or_create_collection(name="my_basic_collection")

# 3. Prepare documents, IDs, and custom embeddings
documents = [
    "Python is a versatile programming language.",
    "Vector databases store high-dimensional embeddings.",
    "Chroma is an open-source embedding database.",
]
ids = ["doc_1", "doc_2", "doc_3"]

# Using simple 3-dimensional dummy embeddings for demonstration
embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]

# Store sentences with IDs and embeddings
collection.add(documents=documents, embeddings=embeddings, ids=ids)

# 4. Retrieve stored records
retrieved_records = collection.get(ids=["doc_1", "doc_3"])

print("--- Retrieved Records ---")
for doc_id, doc_text in zip(
    retrieved_records["ids"], retrieved_records["documents"]
):
  print(f"ID: {doc_id} | Text: {doc_text}")

print("\nExpected Output: Successfully stored and retrieved documents.")
'''