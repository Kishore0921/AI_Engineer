import os
from openai import OpenAI

def main():
    print("Launching Persistent Terminal Chatbot Engine...")
    client = OpenAI()

    # Active conversation thread window memory stack
    conversation_history = [
        {"role": "developer", "content": "You are a helpful, conversational programming learning assistant."}
    ]

    print("\nChatbot active! Type 'exit' or 'quit' to terminate the session.")
    print("-" * 60)

    while True:
        try:
            # Capture user interaction input stream
            user_input = input("\nYou: ").strip()
            
            # Termination guard conditions
            if not user_input:
                continue
            if user_input.lower() in ['exit', 'quit']:
                print("\nShutting down active session context window. Goodbye!")
                break

            # Append the fresh user input directly to the memory stack
            conversation_history.append({"role": "user", "content": user_input})

            print("AI is thinking...")
            
            # Send the complete, growing history sequence to maintain accurate chat state context
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=conversation_history,
                temperature=0.7
            )

            # Isolate and capture the new reply context block
            ai_reply = response.choices[0].message.content
            
            print(f"\nAI: {ai_reply}")

            # Append the model response back to conversation memory to complete the loop
            conversation_history.append({"role": "assistant", "content": ai_reply})

        except KeyboardInterrupt:
            print("\nSession interrupted via terminal command. Exiting.")
            break
        except Exception as e:
            print(f"\nAn error occurred processing the chat stream: {e}")
            break

if __name__ == "__main__":
    main()
