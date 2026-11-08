import os
from openai import OpenAI

def query_llm(prompt):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0 # Kept at 0 to focus on prompt structural difference rather than randomness
    )
    return response.choices.message.content

def main():
    # Scenario A: Asking for code help
    weak_prompt_1 = "write a function to find duplicate numbers"
    effective_prompt_1 = (
        "Role: Expert Python Developer\n"
        "Task: Write a function named `find_duplicates(nums)` that takes a list of integers.\n"
        "Constraints: Do not use built-in functions like `set()`. Optimize for O(N) time complexity.\n"
        "Output Format: Return a list of duplicates. Include exactly two lines of docstrings explaining the logic."
    )

    # Scenario B: Summarization task
    weak_prompt_2 = "summarize transfer learning"
    effective_prompt_2 = (
        "Task: Summarize the concept of Transfer Learning in machine learning.\n"
        "Target Audience: A first-year computer science student.\n"
        "Format: Provide exactly 3 bullet points. Max 20 words per bullet point."
    )

    test_cases = [
        {"name": "Coding Task", "weak": weak_prompt_1, "effective": effective_prompt_1},
        {"name": "Summarization Task", "weak": weak_prompt_2, "effective": effective_prompt_2}
    ]

    print("==========================================================================")
    print("                      PROMPT ENGINEERING TEST BENCHMARK                   ")
    print("==========================================================================")

    for case in test_cases:
        print(f"\n[ RUNNING EXPERIMENT: {case['name']} ]")
        print("-" * 50)
        
        print("-> Querying Weak Prompt...")
        weak_res = query_llm(case["weak"])
        
        print("-> Querying Effective Prompt...")
        effective_res = query_llm(case["effective"])
        
        print("\n[ WEAK PROMPT OUTPUT ]:")
        print(weak_res.strip())
        print("\n[ EFFECTIVE PROMPT OUTPUT ]:")
        print(effective_res.strip())
        print("=" * 74)

if __name__ == "__main__":
    # Ensure OPENAI_API_KEY environment variable is configured prior to execution
    main()
