"""
Filename: program_02_ai_vs_ml.py
Description: Compares AI Engineers and ML Engineers and allows interactive exploration.
"""


def get_role_data():
    return {
        "AI Engineer": [
            "Integrates third-party AI APIs (like OpenAI or Gemini) into software products.",
            "Designs orchestration architectures using patterns like RAG, agents, and MCP.",
            "Optimises runtime parameters like temperature, top_p, and system prompts.",
            "Focuses heavily on application logic, user context parsing, and developer tooling.",
        ],
        "ML Engineer": [
            "Designs, trains, and fine-tunes custom neural network architectures.",
            "Handles fundamental mathematical modeling, feature engineering, and data cleaning.",
            "Manages raw data processing layers, term frequency indexing, and tokenization setups.",
            "Focuses deeply on model validation, mathematical metrics, and physical infrastructure.",
        ],
    }


def compare_roles(roles):
    print("\n" + "=" * 80)
    print(f"{'CORE DIFFERENCES AT A GLANCE':^80}")
    print("=" * 80)
    print(f"{'Attribute':<20} | {'AI Engineer':<28} | {'ML Engineer':<28}")
    print("-" * 80)
    print(
        f"{'Primary Focus':<20} | {'Application & Integration':<28} | {'Model Creation & Training':<28}"
    )
    print(
        f"{'Core Toolkit':<20} | {'APIs, Orchestrators, VectorDBs':<28} | {'PyTorch, Hardware, Algorithms':<28}"
    )
    print(
        f"{'Data Handling':<20} | {'Context Retrieval & Prompts':<28} | {'Preprocessing & Tokenization':<28}"
    )
    print("=" * 80 + "\n")


def interactive_explorer():
    roles = get_role_data()

    print("=" * 50)
    print(f"{'ROLE COMPARISON EXPLORER':^50}")
    print("=" * 50)

    compare_roles(roles)

    while True:
        print("Select a role to inspect its core responsibilities:")
        print("1. AI Engineer")
        print("2. ML Engineer")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            print(f"\n--- Responsibilities of an AI Engineer ---")
            for resp in roles["AI Engineer"]:
                print(f" * {resp}")
            print("-" * 50 + "\n")
        elif choice == "2":
            print(f"\n--- Responsibilities of an ML Engineer ---")
            for resp in roles["ML Engineer"]:
                print(f" * {resp}")
            print("-" * 50 + "\n")
        elif choice == "3":
            print("\nExiting explorer. Goodbye!")
            break
        else:
            print("\n[!] Invalid input. Please select 1, 2, or 3.\n")


if __name__ == "__main__":
    interactive_explorer()
