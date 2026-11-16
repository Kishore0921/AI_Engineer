#Make sure you have the required library installed:
#pip install sentence-transformers
import torch
from sentence_transformers import SentenceTransformer, util

def main():
    # Load model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # 1. Create a small course dataset
    courses = [
        {"title": "Python for Data Science", "desc": "Learn Python programming, Pandas, NumPy, and data visualization for analytics."},
        {"title": "Deep Learning & Neural Networks", "desc": "Build artificial neural networks, CNNs, and transformers using PyTorch."},
        {"title": "Full-Stack Web Development", "desc": "Master HTML, CSS, JavaScript, React, and Node.js to build modern web apps."},
        {"title": "Natural Language Processing (NLP)", "desc": "Work with text embeddings, sentiment analysis, and large language models."},
        {"title": "Digital Marketing Masterclass", "desc": "Learn SEO, social media advertising, content strategy, and brand growth."},
        {"title": "Financial Accounting Basics", "desc": "Understand balance sheets, income statements, cash flow, and corporate finance."},
        {"title": "UI/UX Design Fundamentals", "desc": "Design user-friendly interfaces, wireframes, and interactive prototypes in Figma."}
    ]

    # Combine title and description for richer embeddings
    course_texts = [f"{c['title']}: {c['desc']}" for c in courses]

    # 2. Generate embeddings for item descriptions
    course_embeddings = model.encode(course_texts, convert_to_tensor=True)

    # Display available courses
    print("Available Courses:")
    print("-" * 60)
    for i, course in enumerate(courses, start=1):
        print(f"{i}. {course['title']}")

    # 3. Accept a user's preferred item
    try:
        choice = int(input("\nSelect a course number you liked (1-7): ")) - 1
        if choice < 0 or choice >= len(courses):
            raise ValueError
    except ValueError:
        choice = 0
        print(f"Invalid input. Defaulting to: {courses[choice]['title']}")

    selected_course = courses[choice]
    selected_embedding = course_embeddings[choice]

    # 4. Recommend the top 3 similar items (excluding the selected item itself)
    cosine_scores = util.cos_sim(selected_embedding, course_embeddings)[0]
    cosine_scores[choice] = -1.0  # Mask out the chosen course

    top_recommendations = torch.topk(cosine_scores, k=3)

    print(f"\nBecause you liked '{selected_course['title']}', we recommend:")
    print("-" * 60)
    for rank, (score, idx) in enumerate(zip(top_recommendations.values, top_recommendations.indices), start=1):
        rec = courses[idx]
        print(f"{rank}. {rec['title']} [Similarity: {score.item():.4f}]")
        print(f"   Description: {rec['desc']}\n")

if __name__ == "__main__":
    main()
