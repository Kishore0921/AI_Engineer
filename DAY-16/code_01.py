#Make sure you have the required library installed:
#pip install sentence-transformers
from sentence_transformers import SentenceTransformer

def main():
    # 1. Load MiniLM model
    model_name = 'all-MiniLM-L6-v2'
    print(f"Loading model: {model_name}...")
    model = SentenceTransformer(model_name)

    # 2. Enter multiple sentences
    sentences = [
        "Artificial intelligence is transforming software development.",
        "Python is a versatile programming language for data science.",
        "Machine learning models rely on numerical vector representations."
    ]

    # 3. Generate embeddings
    embeddings = model.encode(sentences)

    # 4. Display vector dimensions and output
    print(f"\nOverall Embeddings Matrix Shape: {embeddings.shape}")
    print("-" * 50)
    
    for idx, (sentence, embedding) in enumerate(zip(sentences, embeddings)):
        print(f"Sentence {idx + 1}: '{sentence}'")
        print(f"Vector Shape: {embedding.shape}")
        print(f"First 5 dimensions: {embedding[:5]}\n")

if __name__ == "__main__":
    main()
