"""
Filename: program_01_ai_ecosystem.py
Description: Displays the major components of the AI ecosystem and their purposes.
"""


def display_ecosystem():
    # 8 major components of the AI ecosystem stored as tuples in a list
    ecosystem_components = [
        (
            "Hardware Infrastructure",
            "GPUs, TPUs, and AI accelerators that provide computational power.",
        ),
        (
            "Data Engineering Tools",
            "Pipelines, storage (Data Lakes), and preprocessing engines like Spark.",
        ),
        (
            "Foundational Models",
            "Large pre-trained neural networks (LLMs, Diffusion models) acting as base engines.",
        ),
        (
            "ML Frameworks",
            "Core development libraries like PyTorch, TensorFlow, and JAX.",
        ),
        (
            "MLOps & Orchestration",
            "Platforms for tracking experiments, versioning data, and deployments (MLflow).",
        ),
        (
            "Vector Databases",
            "Specialised storage for managing semantic embeddings used in RAG systems.",
        ),
        (
            "Deployment Frameworks",
            "High-performance serving engines and API frameworks like FastAPI and vLLM.",
        ),
        (
            "Application Layer",
            "The interfaces, agents, and user-facing clients powered by underlying AI.",
        ),
    ]

    print("=" * 75)
    print(f"{'THE AI ECOSYSTEM EXPLORER':^75}")
    print("=" * 75)

    for i, (component, purpose) in enumerate(ecosystem_components, 1):
        print(f"{i}. {component:<25} | {purpose}")
        if i < len(ecosystem_components):
            print("-" * 75)

    print("=" * 75)


if __name__ == "__main__":
    display_ecosystem()
