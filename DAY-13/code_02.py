'''import ollama

def main():
    # Replace with any model you have pulled locally (e.g., 'llama3.2', 'gemma2', 'mistral')
    MODEL_NAME = "llama3.2" 
    
    print(f"Starting chat session with '{MODEL_NAME}'...")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    # Stores conversation history for context
    messages = []

    while True:
        user_prompt = input("You: ").strip()
        
        if user_prompt.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
            
        if not user_prompt:
            continue

        # Append user message to history
        messages.append({'role': 'user', 'content': user_prompt})

        try:
            print("AI: ", end="", flush=True)
            full_response = ""
            
            # Stream the response for a better CLI experience
            stream = ollama.chat(
                model=MODEL_NAME,
                messages=messages,
                stream=True,
            )
            
            for chunk in stream:
                content = chunk['message']['content']
                print(content, end="", flush=True)
                full_response += content
                
            print("\n")
            
            # Append assistant response to history
            messages.append({'role': 'assistant', 'content': full_response})

        except ollama.ResponseError as e:
            print(f"\nError: {e.error}")
            print(f"Make sure Ollama is running and you have pulled '{MODEL_NAME}'.\n")
            messages.pop() # Remove failed prompt from history

if __name__ == "__main__":
    main()
'''

# prerequisites
#pip install transformers torch ollama