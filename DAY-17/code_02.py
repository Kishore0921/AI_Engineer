#Make sure you have the required library installed:
#pip install sentence-transformers
import torch
from sentence_transformers import SentenceTransformer, util

def main():
    # Load model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # 1. Create categories (descriptive labels improve zero-shot accuracy)
    categories = {
        "Technology": "Technology, software, artificial intelligence, computers, and gadgets",
        "Sports": "Sports, athletics, cricket, football, tournaments, and fitness",
        "Education": "Education, universities, studying, exams, teaching, and academic learning",
        "Finance": "Finance, stock market, banking, investments, and economy"
    }

    category_names = list(categories.keys())
    category_descriptions = list(categories.values())

    # 2. Generate embeddings for category labels
    category_embeddings = model.encode(category_descriptions, convert_to_tensor=True)

    # 3. Accept user sentences
    print("Enter sentences to classify (type 'exit' to quit):")
    print("-" * 60)

    while True:
        user_sentence = input("\nInput Sentence: ").strip()
        if user_sentence.lower() == 'exit':
            break
        if not user_sentence:
            continue

        # Generate embedding for the input sentence
        sentence_embedding = model.encode(user_sentence, convert_to_tensor=True)

        # 4. Predict the closest category
        scores = util.cos_sim(sentence_embedding, category_embeddings)[0]
        best_idx = torch.argmax(scores).item()
        best_category = category_names[best_idx]
        confidence = scores[best_idx].item()

        print(f"Predicted Category: {best_category} (Similarity Score: {confidence:.4f})")

if __name__ == "__main__":
    main()
