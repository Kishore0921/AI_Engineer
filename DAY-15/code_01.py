#Prerequisites & Setup
#pip install openai numpy
import os
from openai import OpenAI

def main():
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not found.")
        return

    client = OpenAI()
    model_name = "text-embedding-3-small"

    print(f"=== OpenAI Text Embedding Generator ({model_name}) ===")
    print("Type 'exit' to quit.\n")

    while True:
        user_text = input("Enter text to embed: ").strip()
        
        if user_text.lower() == 'exit':
            break
        if not user_text:
            continue

        try:
            response = client.embeddings.create(
                input=user_text,
                model=model_name
            )

            embedding_vector = response.data[0].embedding
            dimensions = len(embedding_vector)
            prompt_tokens = response.usage.prompt_tokens
            total_tokens = response.usage.total_tokens

            print("\n--- Embedding Result ---")
            print(f"Vector Dimensions : {dimensions}")
            print(f"First 5 Values    : {embedding_vector[:5]}")
            print(f"Prompt Tokens     : {prompt_tokens}")
            print(f"Total Tokens      : {total_tokens}\n")

        except Exception as e:
            print(f"\nAPI Error: {e}\n")

if __name__ == "__main__":
    main()
