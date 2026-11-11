from transformers import pipeline


def run_sentiment_analyzer():
    print("Loading pre-trained sentiment-analysis model...")
    # Using DistilBERT fine-tuned on SST-2 (fast and accurate)
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    classifier = pipeline("sentiment-analysis", model=model_name)

    print("\nModel loaded! Type 'exit' or 'quit' to stop.\n")
    print("=" * 50)

    while True:
        user_text = input("Enter text to analyze: ").strip()

        if user_text.lower() in ["exit", "quit"]:
            print("Exiting application.")
            break

        if not user_text:
            print("Please enter some valid text.\n")
            continue

        # Run prediction
        result = classifier(user_text)[0]
        label = result["label"]
        confidence = result["score"] * 100

        print(f" -> Sentiment:  {label}")
        print(f" -> Confidence: {confidence:.2f}%\n")


if __name__ == "__main__":
    run_sentiment_analyzer()
