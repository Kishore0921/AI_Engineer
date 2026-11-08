import os
import json
from openai import OpenAI

def main():
    print("Initializing Capability Boundaries and Model Limitations Benchmark...")
    client = OpenAI()
    
    # Stress tests across distinct boundary categories (Temporal Knowledge, Ambiguity, Reasoning)
    limitation_challenges = [
        {
            "category": "Factual / Temporal Knowledge Boundary",
            "prompt": "Who won the men's singles tennis final at the absolute most recent US Open tournament?"
        },
        {
            "category": "Ambiguity Handling",
            "prompt": "Why did it fail to open when I clicked it?"
        },
        {
            "category": "Complex Logical / Constraint Reasoning",
            "prompt": "Write a short sentence about programming where every word must start with the letter 'P'."
        }
    ]
    
    report = []
    
    print("\nExecuting stress metrics...")
    for test in limitation_challenges:
        print(f" -> Processing Category: {test['category']}")
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": test["prompt"]}],
            temperature=0.0 # Standardize randomness to clearly measure systematic failure
        )
        
        output = response.choices.message.content.strip()
        report.append({
            "category": test["category"],
            "prompt": test["prompt"],
            "model_response": output
        })
        
    print("\n======================= MODEL LIMITATIONS REPORT =======================")
    for entry in report:
        print(f"\n[ Category ]: {entry['category']}")
        print(f"[ Prompt Provided ]: {entry['prompt']}")
        print(f"[ Raw Response ]:\n{entry['model_response']}")
        print("." * 72)
        
    with open("model_limitations_report.json", "w") as f:
        json.dump(report, f, indent=4)
    print("\nReport logged out smoothly to 'model_limitations_report.json'.")

if __name__ == "__main__":
    main()
