from transformers import pipeline

def main():
    print("Loading pre-trained sentiment analysis model...")
    # Loads a default fine-tuned DistilBERT model for sentiment analysis
    classifier = pipeline(
        "sentiment-analysis", 
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )
    print("Model loaded successfully! Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter text to analyze: ").strip()
        
        if user_input.lower() == 'exit':
            print("Exiting application.")
            break
            
        if not user_input:
            continue

        # Perform prediction
        result = classifier(user_input)[0]
        label = result['label']
        confidence = result['score'] * 100

        print(f"Prediction: {label} (Confidence: {confidence:.2f}%)\n")

if __name__ == "__main__":
    main()
