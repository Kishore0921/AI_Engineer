import os
import json
from openai import OpenAI

def query_variant(prompt_string):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt_string}],
        temperature=0.0
    )
    return response.choices.message.content.strip()

def main():
    print("Launching Comparative Prompt Testing Pipeline...")
    
    # Task context: Writing a structural regular expression function safely
    variant_a = "write a regex tool in python to find email strings"
    
    variant_b = (
        "Task: Write a Python function using the `re` library to extract valid email addresses from text.\n"
        "Requirements: Provide a clean regular expression pattern pattern matching standard forms.\n"
        "Output: Return code alongside an example usage snippet block."
    )
    
    variant_c = (
        "Role: Security Analyst & Data Validation Engineer\n"
        "Task: Write a robust, production-grade Python regular expression function to scan and parse emails safely.\n"
        "Constraints: Account for subdomains and avoid catastrophic backtracking structural issues.\n"
        "Output Format: Clean code output blocks followed by a concise 2-sentence structural explanation."
    )

    testing_pool = [
        {"variant_id": "A (Minimalist)", "prompt": variant_a},
        {"variant_id": "B (Structured)", "prompt": variant_b},
        {"variant_id": "C (Role + Constraints)", "prompt": variant_c}
    ]

    evaluation_report = []

    for item in testing_pool:
        print(f" -> Evaluating Strategy Variant: Configuration {item['variant_id']}")
        model_output = query_variant(item["prompt"])
        
        # Evaluation score targets based on clarity, structural metrics, and requirement alignment
        report_record = {
            "variant_id": item["variant_id"],
            "engineered_prompt": item["prompt"],
            "model_response": model_output,
            "metric_assessment": "Check if output strictly adheres to constraints, includes sample validation, and maintains logic integrity."
        }
        evaluation_report.append(report_record)

    print("\n========================= PROMPT PERFORMANCE EVALUATION REPORT =========================")
    for record in evaluation_report:
        print(f"\n[ TEST VARIANT: Variant {record['variant_id']} ]")
        print(f"Prompt Input: {record['engineered_prompt'].replace('\n', ' | ')}")
        print(f"Generated Output Preview:\n{record['model_response'][:250]}...")
        print(f"Automated Evaluation Audit Step: {record['metric_assessment']}")
        print("." * 85)

    with open("prompt_evaluation_matrix_report.json", "w") as f:
        json.dump(evaluation_report, f, indent=4)
    print("\nEvaluation reports captured successfully to 'prompt_evaluation_matrix_report.json'.")

if __name__ == "__main__":
    main()
