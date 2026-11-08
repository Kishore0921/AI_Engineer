import os
from openai import OpenAI

def main():
    # Make sure you set your environment variable first: export OPENAI_API_KEY="your-key-here"
    print("Initializing Single-Turn Chatbot Engine...")
    client = OpenAI()

    print("\nChatbot active! Type 'exit' or 'quit' to close.")
    print("-" * 50)

    while True:
        user_input = input("\nYou: ").strip()
        
        if not user_input:
            continue
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting session. Goodbye!")
            break

        print("AI is thinking...")
        
        # Single-turn transaction: Only sends the current prompt
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        ai_response = response.choices.message.content
        print(f"\nAI: {ai_response}")

if __name__ == "__main__":
    main()
