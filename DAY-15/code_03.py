#Prerequisites & Setup
#pip install openai numpy
import os
import time
from openai import OpenAI

# Standard OpenAI pricing per 1,000,000 tokens
MODELS = {
    "text-embedding-3-small": {"price_per_1m": 0.02},
    "text-embedding-3-large": {"price_per_1m": 0.13},
}

REPORT_FILE = "embedding_model_comparison.md"

def evaluate_model(client, model_name, text):
    start_time = time.perf_counter()
    response = client.embeddings.create(
        input=text,
        model=model_name
    )
    elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)

    vector = response.data[0].embedding
    tokens = response.usage.total_tokens
    price_per_1m = MODELS[model_name]["price_per_1m"]
    estimated_cost = (tokens / 1_000_000) * price_per_1m

    return {
        "model": model_name,
        "dimensions": len(vector),
        "tokens": tokens,
        "cost_usd": estimated_cost,
        "latency_ms": elapsed_ms,
        "sample_values": [round(x, 6) for x in vector[:3]]
    }

def save_report(text, results):
    small = results["text-embedding-3-small"]
    large = results["text-embedding-3-large"]
    cost_multiplier = round(large["cost_usd"] / small["cost_usd"], 1) if small["cost_usd"] > 0 else 6.5

    report = f"""# OpenAI Embedding Model Comparison Report

## 1. Input Text
> "{text}"

## 2. Quantitative Comparison

| Metric | `text-embedding-3-small` | `text-embedding-3-large` |
| :--- | :--- | :--- |
| **Vector Dimensions** | {small['dimensions']} | {large['dimensions']} |
| **Tokens Used** | {small['tokens']} | {large['tokens']} |
| **Estimated Cost (USD)** | ${small['cost_usd']:.8f} | ${large['cost_usd']:.8f} |
| **API Latency** | {small['latency_ms']} ms | {large['latency_ms']} ms |
| **First 3 Vector Values** | `{small['sample_values']}` | `{large['sample_values']}` |

## 3. Key Trade-Offs & Observations
* **Storage & Memory:** `text-embedding-3-large` produces **2x** as many dimensions ({large['dimensions']} vs. {small['dimensions']}), requiring double the vector database storage and memory bandwidth.
* **Cost Efficiency:** `text-embedding-3-large` is **{cost_multiplier}x** more expensive per token ($0.13 vs. $0.02 per 1M tokens).
* **Tokenization:** Both models use the same `cl100k_base` tokenizer, resulting in identical token counts ({small['tokens']} tokens) for the same input.
* **Recommendation:** Use `text-embedding-3-small` for general semantic search and RAG pipelines; reserve `text-embedding-3-large` for high-precision domain retrieval where retrieval accuracy outweighs storage and API costs.
"""
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

def main():
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not found.")
        return

    client = OpenAI()
    print("=== OpenAI Embedding Model Comparison ===")
    text = input("Enter text to benchmark across models: ").strip()
    if not text:
        return

    results = {}
    for model_name in MODELS:
        print(f"Testing {model_name}...")
        results[model_name] = evaluate_model(client, model_name, text)

    save_report(text, results)
    print(f"\nComparison complete! Report saved to '{REPORT_FILE}'.")

if __name__ == "__main__":
    main()
