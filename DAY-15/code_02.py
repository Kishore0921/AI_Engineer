#Prerequisites & Setup
#pip install openai numpy
import os
import numpy as np
from openai import OpenAI

def cosine_similarity(vec_a, vec_b):
    """Calculates cosine similarity between two 1D NumPy arrays."""
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    return dot_product / (norm_a * norm_b)

def main():
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not found.")
        return

    client = OpenAI()
    model_name = "text-embedding-3-small"

    # Anchor sentence followed by semantically similar and unrelated sentences
    sentences = [
        "The software engineer deployed the Python application to the cloud server.",  # [0] Anchor
        "A developer pushed the backend code to production hosting.",                 # [1] Semantically similar
        "Machine learning models require clean datasets for accurate training.",      # [2] Moderately related (Tech)
        "Freshly baked sourdough bread smells wonderful in the morning."              # [3] Completely unrelated
    ]

    print("Generating embeddings for sentences...")
    response = client.embeddings.create(
        input=sentences,
        model=model_name
    )

    # Convert embeddings to NumPy arrays
    vectors = [np.array(item.embedding) for item in response.data]
    anchor_vec = vectors[0]

    print(f"\nAnchor Sentence:\n  \"{sentences[0]}\"\n")
    print("Cosine Similarity Scores (1.0 = Identical, 0.0 = Unrelated):")
    print("-" * 70)

    for i in range(1, len(sentences)):
        score = cosine_similarity(anchor_vec, vectors[i])
        print(f"Score: {score:.4f} | \"{sentences[i]}\"")

    print("-" * 70)

if __name__ == "__main__":
    main()
