import os
from openai import OpenAI

def main():
    print("Initializing OpenAI structured completion pipeline...")
    client = OpenAI()

    # Formulating structural roles using developer guidelines and user tasks
    system_instruction = (
        "You are an elite, highly concise technical code reviewer. "
        "Review the user's code only for structural execution safety and space complexity. "
        "Provide your review in three short bullet points max."
    )
    
    user_prompt = (
        "def fetch_data(items):\n"
        "    result = []\n"
        "    for item in items:\n"
        "        if item not in result:\n"
        "            result.append(item)\n"
        "    return result"
    )

    print("\nSending structural payload with role profiles...")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": system_instruction},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2 # Lower temperature for stable, predictable analysis outputs
    )

    # Clean extraction pattern of the assistant response node
    assistant_review = response.choices[0].message.content

    print("\n================ ASSISTANT CODE REVIEW ================")
    print(assistant_review)
    print("=======================================================")

if __name__ == "__main__":
    main()
