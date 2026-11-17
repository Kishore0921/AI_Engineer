#install the Chroma library via your terminal:
#pip install chromadb
'''
def generate_comparison_report():
  # Structured comparison data
  vector_dbs = [
      {
          "name": "Chroma",
          "architecture": (
              "Embedded or Client-Server; uses SQLite + ClickHouse/DuckDB"
              " under the hood."
          ),
          "deployment": (
              "In-memory, local persistent file, or self-hosted Docker."
          ),
          "features": (
              "Built-in default embeddings, metadata filtering, simple Python"
              " API."
          ),
          "best_for": (
              "Local Development & Prototyping (zero-setup, runs directly in"
              " Python)."
          ),
      },
      {
          "name": "Pinecone",
          "architecture": (
              "Cloud-native, distributed, proprietary serverless/pod-based"
              " engine."
          ),
          "deployment": "Fully managed SaaS (AWS, GCP, Azure).",
          "features": (
              "Auto-scaling, high availability, hybrid search, zero"
              " infrastructure maintenance."
          ),
          "best_for": (
              "Enterprise Production (hands-off scaling and high reliability)."
          ),
      },
      {
          "name": "Qdrant",
          "architecture": (
              "Written in Rust; uses custom HNSW index with payload storage."
          ),
          "deployment": (
              "Local mode, self-hosted Docker/Kubernetes, or Qdrant Cloud."
          ),
          "features": (
              "Rich JSON payload filtering, quantization for memory"
              " efficiency, high throughput."
          ),
          "best_for": (
              "High-Performance Production & Hybrid Cloud (great balance of"
              " speed and control)."
          ),
      },
      {
          "name": "FAISS",
          "architecture": (
              "C++ core library with Python bindings; pure vector similarity"
              " index."
          ),
          "deployment": "In-memory library embedded inside your application.",
          "features": (
              "Blazingly fast GPU acceleration, dozens of indexing algorithms"
              " (IVF, HNSW, PQ)."
          ),
          "best_for": (
              "Local Research & Static Datasets (lacks built-in metadata DB or"
              " CRUD APIs)."
          ),
      },
  ]

  print("=" * 75)
  print(f"{'VECTOR DATABASE COMPARISON REPORT':^75}")
  print("=" * 75)

  for db in vector_dbs:
    print(f"\nDatabase: {db['name']}")
    print(f"  - Architecture : {db['architecture']}")
    print(f"  - Deployment   : {db['deployment']}")
    print(f"  - Key Features : {db['features']}")
    print(f"  - Best Fit     : {db['best_for']}")

  print("\n" + "=" * 75)
  print("FINAL ENVIRONMENT RECOMMENDATIONS")
  print("=" * 75)
  print(
      "* Local Development : Chroma (fastest setup, requires no external"
      " server)."
  )
  print(
      "* Production        : Qdrant (if self-hosting/high filtering) or"
      " Pinecone (if fully managed)."
  )
  print(
      "* Raw Math/GPU Speed: FAISS (best when you only need pure vector search"
      " without metadata)."
  )
  print("=" * 75)


if __name__ == "__main__":
  generate_comparison_report()

'''