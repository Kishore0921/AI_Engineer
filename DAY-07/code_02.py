import os
from openai import OpenAI

def main():
    print("Initializing Multi-Turn Context-Aware Chatbot...")
    client = OpenAI()

    # The dynamic list that grows to keep the conversational context alive
    conversation_history = [
        {"role": "developer", "content": "You are a helpful, direct conversational programming learning assistant."}
    ]

    print("\nChatbot active! Context retention enabled. Type 'exit' or 'quit' to close.")
    print("-" * 65)

    while True:
        user_input = input("\nYou: ").strip()
        
        if not user_input:
            continue
        if user_input.lower() in ['exit', 'quit']:
            print("Context cleared. Goodbye!")
            break

        # Append new user statement directly to history stack
        conversation_history.append({"role": "user", "content": user_input})
        print("AI is thinking...")
        
        # Pass full cumulative history payload so the model can track context loops
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history
        )

        ai_reply = response.choices.message.content
        print(f"\nAI: {ai_reply}")

        # Append the assistant's reply back to history to finish the chain
        conversation_history.append({"role": "assistant", "content": ai_reply})

if __name__ == "__main__":
    main()
