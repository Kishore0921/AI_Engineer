#Make sure you have the required library installed:
#pip install sentence-transformers
from sentence_transformers import SentenceTransformer, util

def main():
    # Load MiniLM model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # 1. Take three different sentences
    sentences = [
        "The cat is sleeping peacefully on the warm sofa.",
        "A feline is taking a nap on the couch.",
        "Stock markets experienced high volatility during the trading session."
    ]

    # 2. Generate embeddings
    embeddings = model.encode(sentences, convert_to_tensor=True)

    # 3. Calculate cosine similarity
    cosine_scores = util.cos_sim(embeddings, embeddings)

    print("Pairwise Cosine Similarity Scores:")
    print("-" * 50)
    
    pairs = []
    num_sentences = len(sentences)
    
    for i in range(num_sentences):
        for j in range(i + 1, num_sentences):
            score = cosine_scores[i][j].item()
            pairs.append((score, i, j))
            print(f"Sentence {i+1} vs Sentence {j+1}: {score:.4f}")

    # 4. Identify the most similar pair
    best_score, idx1, idx2 = max(pairs, key=lambda x: x[0])
    
    print("\nMost Similar Pair:")
    print("-" * 50)
    print(f"Score: {best_score:.4f}")
    print(f"1: '{sentences[idx1]}'")
    print(f"2: '{sentences[idx2]}'")

if __name__ == "__main__":
    main()
