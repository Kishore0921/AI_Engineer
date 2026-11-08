import os
from openai import OpenAI

def main():
    # Make sure you set your environment variable first: export OPENAI_API_KEY="your-key-here"
    # The client automatically picks up the API key from the environment variable.
    print("Initializing OpenAI client connection...")
    client = OpenAI()

    prompt = "Give me a single, catchy, motivational motto for a computer programmer."

    print(f"Sending prompt to model: '{prompt}'")
    
    # Standard single request endpoint using a cost-effective, fast model
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    # Extract the generated text response
    ai_response = response.choices[0].message.content
    
    print("\n================ AI RESPONSE ================")
    print(ai_response)
    print("=============================================")

if __name__ == "__main__":
    main()
