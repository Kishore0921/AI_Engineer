#Prerequisites & Setup
#pip install google-genai ollama
import random

QUIZ_BANK = [
    {
        "day": "Day 8",
        "question": "Which Hugging Face function automatically loads a pre-trained model and tokenizer for tasks like sentiment analysis?",
        "options": ["A) AutoModel()", "B) pipeline()", "C) load_hub()", "D) tokenizer()"],
        "answer": "B",
        "explanation": "The pipeline() API abstracts away preprocessing and postprocessing for quick inference."
    },
    {
        "day": "Day 9",
        "question": "What is the primary benefit of running LLMs locally using tools like Ollama?",
        "options": ["A) Unlimited context windows", "B) Zero local RAM usage", "C) Complete data privacy and offline access", "D) Faster training speeds"],
        "answer": "C",
        "explanation": "Local models run entirely on your own hardware without sending sensitive data to external APIs."
    },
    {
        "day": "Day 10",
        "question": "Which CLI command downloads a model in Ollama without immediately starting an interactive chat session?",
        "options": ["A) ollama fetch", "B) ollama get", "C) ollama pull", "D) ollama install"],
        "answer": "C",
        "explanation": "'ollama pull <model>' downloads the model weights locally so Python scripts can call it."
    },
    {
        "day": "Day 11",
        "question": "When comparing two local LLMs on identical hardware, what metric best measures raw generation speed?",
        "options": ["A) Tokens per second (TPS)", "B) Model file size in GB", "C) Number of layers", "D) Temperature setting"],
        "answer": "A",
        "explanation": "Tokens per second measures how quickly the model generates text after processing the prompt."
    },
    {
        "day": "Day 12",
        "question": "Why is exception handling (try/except) critical when integrating hosted AI APIs?",
        "options": ["A) To make the model smarter", "B) To handle rate limits, network drops, and invalid API keys gracefully", "C) To reduce token costs", "D) To convert JSON to CSV"],
        "answer": "B",
        "explanation": "Cloud APIs can fail due to network issues, quota limits (HTTP 429), or server downtime."
    },
    {
        "day": "Day 13",
        "question": "Which factor is typically a disadvantage of hosted AI models compared to local models?",
        "options": ["A) Requires expensive local GPUs", "B) Ongoing per-token costs and external data transmission", "C) Inability to scale", "D) Hard to update models"],
        "answer": "B",
        "explanation": "Hosted models charge per input/output token and require sending data over the internet."
    },
    {
        "day": "Day 14",
        "question": "In Python, which module provides the highest-resolution timer for benchmarking AI execution latency?",
        "options": ["A) datetime.now()", "B) time.sleep()", "C) time.perf_counter()", "D) calendar.timegm()"],
        "answer": "C",
        "explanation": "time.perf_counter() uses the highest available system clock resolution for accurate duration measurement."
    }
]

def run_quiz():
    print("==========================================")
    print("   WEEK 2 AI ENGINEERING REVISION QUIZ    ")
    print("             (Days 8 - 14)                ")
    print("==========================================\n")

    questions = QUIZ_BANK.copy()
    random.shuffle(questions)
    
    score = 0
    missed = []

    for idx, q in enumerate(questions, 1):
        print(f"Question {idx}/{len(questions)} [{q['day']}]:")
        print(q["question"])
        for opt in q["options"]:
            print(f"  {opt}")
        
        while True:
            user_ans = input("\nYour answer (A/B/C/D): ").strip().upper()
            if user_ans in ["A", "B", "C", "D"]:
                break
            print("Invalid input. Please enter A, B, C, or D.")

        if user_ans == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer is {q['answer']}.")
            print(f"💡 Note: {q['explanation']}\n")
            missed.append(q)

    percentage = round((score / len(questions)) * 100, 1)
    print("==========================================")
    print(f"QUIZ COMPLETE! Final Score: {score}/{len(questions)} ({percentage}%)")
    print("==========================================")

    if missed:
        print("\nTopics to review:")
        for item in missed:
            print(f"- {item['day']}: {item['explanation']}")
    else:
        print("\nPerfect score! You are ready for Week 3.")

if __name__ == "__main__":
    run_quiz()
