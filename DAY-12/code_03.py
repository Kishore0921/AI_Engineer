from transformers import pipeline, set_seed


def run_text_generator():
    print("Loading local text-generation model (distilgpt2)...")
    # distilgpt2 is lightweight (~330MB) and runs well on standard CPUs
    generator = pipeline("text-generation", model="distilgpt2")
    set_seed(42)  # Optional: ensures reproducible results if sampling is off

    print("\nModel ready!")
    print("=" * 55)

    prompt = input("Enter a starting sentence: ").strip()
    if not prompt:
        prompt = "In the future, artificial intelligence will"
        print(f"Using default prompt: '{prompt}'")

    # Get optional generation settings
    try:
        max_len = int(
            input(
                "Enter max output length in tokens (default 60): "
            ).strip()
            or 60
        )
        temp = float(
            input(
                "Enter temperature 0.1 - 1.5 (default 0.7): "
            ).strip()
            or 0.7
        )
    except ValueError:
        print("Invalid input detected. Using default settings.")
        max_len = 60
        temp = 0.7

    print("\nGenerating text...\n")

    # Generate output using sampling settings
    outputs = generator(
        prompt,
        max_new_tokens=max_len,
        do_sample=True,  # Enables creative sampling rather than greedy decoding
        temperature=temp,  # Higher = more random/creative, Lower = more focused
        top_k=50,  # Limits sampling to top 50 likely next words
        top_p=0.95,  # Nucleus sampling for natural phrasing
        num_return_sequences=1,
        pad_token_id=50256,  # Suppresses warning for GPT-2 open-end generation
    )

    print("=" * 55)
    print("GENERATED OUTPUT:")
    print("=" * 55)
    print(outputs[0]["generated_text"])
    print("=" * 55)


if __name__ == "__main__":
    run_text_generator()
