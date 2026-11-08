import os
import json
from openai import OpenAI

def query_llm(prompt):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )
    return response.choices.message.content.strip()

def main():
    print("Executing Prompt Patterns Benchmark Matrix...")

    # Pattern 1: Zero-Shot vs Few-Shot (Task: Sentiment Extraction)
    zero_shot_prompt = (
        "Classify the sentiment of this text as POSITIVE, NEGATIVE, or NEUTRAL.\n"
        "Text: The engine works well enough, but the noisy fan makes long rides uncomfortable."
    )
    
    few_shot_prompt = (
        "Classify the sentiment of the text as POSITIVE, NEGATIVE, or NEUTRAL.\n\n"
        "Text: The brakes are perfectly responsive and smooth.\nSentiment: POSITIVE\n\n"
        "Text: The display console flickers non-stop during night commutes.\nSentiment: NEGATIVE\n\n"
        "Text: The engine works well enough, but the noisy fan makes long rides uncomfortable.\nSentiment:"
    )

    # Pattern 2: Standard Task Description vs Role-Based System Structure
    standard_prompt = "Explain why high-end distinct motorcycle styling matters to consumers."
    role_based_prompt = (
        "Role: Luxury Product & Automotive Styling Designer\n"
        "Context: Speaking to an enthusiast audience looking for premium aesthetics that stand out.\n"
        "Task: Explain why distinct, premium vehicle aesthetics matter to buyers. Max 3 sentences."
    )

    # Pattern 3: Unstructured vs Specific JSON Output Structure
    unstructured_prompt = "List 3 key maintenance safety points for high-performance engines."
    structured_json_prompt = (
        "Task: List 3 key maintenance safety points for high-performance engines.\n"
        "Output Format: Return valid raw JSON only. Use the keys: 'item_number', 'component', 'action_required'."
    )

    patterns = [
        {"category": "Zero-Shot Setup", "prompt": zero_shot_prompt},
        {"category": "Few-Shot Setup", "prompt": few_shot_prompt},
        {"category": "Standard Strategy", "prompt": standard_prompt},
        {"category": "Role-Based Strategy", "prompt": role_based_prompt},
        {"category": "Unstructured Output", "prompt": unstructured_prompt},
        {"category": "Structured JSON Format", "prompt": structured_json_prompt}
    ]

    results = {}
    for entry in patterns:
        print(f" -> Querying Pattern Block: [{entry['category']}]")
        results[entry["category"]] = query_llm(entry["prompt"])

    print("\n========================= PROMPT PATTERN COMPARISON =========================")
    print("\n[ APPROACH 1: ZERO-SHOT VS FEW-SHOT ]")
    print(f"-> Zero-Shot Response: {results['Zero-Shot Setup']}")
    print(f"-> Few-Shot Response: {results['Few-Shot Setup']}")
    
    print("\n[ APPROACH 2: ROLE-BASED DESIGN VARIATION ]")
    print(f"-> Role-Based Output:\n{results['Role-Based Strategy']}")
    
    print("\n[ APPROACH 3: STRUCTURED OUTPUT ENFORCEMENT ]")
    print(f"-> JSON Output Response:\n{results['Structured JSON Format']}")
    print("=" * 77)

    with open("prompt_patterns_output.json", "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    main()
