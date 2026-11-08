import os
from openai import OpenAI, AuthenticationError, APIConnectionError, APIError

def main():
    print("Initializing Resilient Chatbot Engine with Advanced Exception Handling...")
    
    # Pre-flight check: Verify if key variable exists prior to client compilation
    if not os.environ.get("OPENAI_API_KEY"):
        print("\n[CRITICAL ERROR]: The 'OPENAI_API_KEY' environment variable is missing.")
        print("Please resolve this by running: export OPENAI_API_KEY='your_actual_key'")
        return

    try:
        client = OpenAI()
    except Exception as e:
        print(f"[INITIALIZATION ERROR]: System failed to bootstrap the OpenAI client: {e}")
        return

    # Fixed operational constraints
    system_instruction = "You are a concise, helpful tutor. Keep explanations short and structured."
    max_token_bound = 150 
    
    conversation_history = [{"role": "developer", "content": system_instruction}]

    print(f"\nChatbot Active. Safety bounds set to max_tokens={max_token_bound}. Type 'exit' to quit.")
    print("-" * 75)

    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
            if user_input.lower() in ['exit', 'quit']:
                print("Graceful exit complete.")
                break

            conversation_history.append({"role": "user", "content": user_input})
            print("AI is processing request...")
            
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=conversation_history,
                max_tokens=max_token_bound, # Enforcement of maximum output length constraint
                timeout=15.0                # Drops hanging socket connections if network slows down
            )

            ai_reply = response.choices.message.content
            print(f"\nAI: {ai_reply}")
            conversation_history.append({"role": "assistant", "content": ai_reply})

        except AuthenticationError:
            print("\n[API ERROR]: Refused connection. Your API key appears invalid or revoked.")
            break
        except APIConnectionError:
            print("\n[NETWORK ERROR]: Handshake failed. Check your internet connection status.")
        except APIError as e:
            print(f"\n[SERVER ERROR]: OpenAI platform error occurred: {e}")
        except KeyboardInterrupt:
            print("\nInterrupted by terminal key bind signals. Exiting.")
            break
        except Exception as e:
            print(f"\n[UNEXPECTED SYSTEM FAULT]: {e}")

if __name__ == "__main__":
    main()
