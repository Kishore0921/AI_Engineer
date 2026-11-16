#Make sure you have the required library installed:
#pip install sentence-transformers
import time
from sentence_transformers import SentenceTransformer, util

def evaluate_model(model_name, sentences):
    # Load model
    model = SentenceTransformer(model_name)
    
    # Measure execution time for generating embeddings
    start_time = time.perf_counter()
    embeddings = model.encode(sentences, convert_to_tensor=True)
    end_time = time.perf_counter()
    
    exec_time_ms = (end_time - start_time) * 1000
    dimensions = embeddings.shape[1]
    
    # Calculate similarity between the two identical-intent sentences
    similarity_score = util.cos_sim(embeddings[0], embeddings[1]).item()
    
    return {
        "name": model_name,
        "dimensions": dimensions,
        "time_ms": exec_time_ms,
        "similarity": similarity_score
    }

def main():
    # Identical test sentences for both models
    test_sentences = [
        "How do I reset my forgotten account password?",
        "I need help recovering access to my profile because I forgot my login credentials."
    ]

    print("Running benchmark (first run may take a moment to download models)...\n")
    
    # 1. Load and evaluate MiniLM and MPNet
    minilm_results = evaluate_model('all-MiniLM-L6-v2', test_sentences)
    mpnet_results = evaluate_model('all-mpnet-base-v2', test_sentences)

    results = [minilm_results, mpnet_results]

    # 2. Output Comparison Table
    header = f"{'Model Name':<22} | {'Dimensions':<12} | {'Exec Time (ms)':<16} | {'Cosine Similarity':<18}"
    print(header)
    print("-" * len(header))
    
    for res in results:
        print(f"{res['name']:<22} | {res['dimensions']:<12} | {res['time_ms']:<16.2f} | {res['similarity']:<18.4f}")

if __name__ == "__main__":
    main()
