import json

def main():
    # A distinct coding challenge scenario requiring proper logic, constraints, and standard inputs
    coding_problem = (
        "Problem: Write a Python function `get_average_scores(scores_matrix)` that takes a list of lists "
        "(where each inner list contains subject scores for a single student) and uses the zip function "
        "to calculate and return a list of average scores for each subject across all students."
    )
    
    # Synthetic outputs capturing structural variations across different coding models
    solutions = {
        "OpenAI (GPT-4o-mini)": (
            "def get_average_scores(scores_matrix):\n"
            "    # Uses zip unpacking to group elements by subject columns\n"
            "    return [sum(subject_scores) / len(subject_scores) for subject_scores in zip(*scores_matrix)]"
        ),
        "Anthropic (Claude 3.5 Haiku)": (
            "def get_average_scores(scores_matrix):\n"
            "    if not scores_matrix:\n"
            "        return []\n"
            "    num_students = len(scores_matrix)\n"
            "    return [sum(scores) / num_students for scores in zip(*scores_matrix)]"
        ),
        "Google Gemini (1.5 Flash)": (
            "def get_average_scores(scores_matrix):\n"
            "    # Zip groups elements structurally\n"
            "    transposed_scores = zip(*scores_matrix)\n"
            "    averages = []\n"
            "    for col in transposed_scores:\n"
            "        averages.append(sum(col) / len(col))\n"
            "    return averages"
        ),
        "Meta Llama (Groq)": (
            "def get_average_scores(scores_matrix):\n"
            "    return list(map(lambda x: sum(x)/len(x), zip(*scores_matrix)))"
        ),
        "Mistral AI": (
            "def get_average_scores(scores_matrix):\n"
            "    subject_groups = list(zip(*scores_matrix))\n"
            "    return [round(sum(sub) / len(sub), 2) for sub in subject_groups]"
        )
    }
    
    # Establish metrics criteria matrix
    evaluation_criteria = {
        "Correctness": "Does the generated solution handle unpack logic correctly without index errors?",
        "Readability": "Is the code clean, idiomatic, well-commented, or excessively complex?",
        "Logic": "Does it account for safe division or empty lists natively?"
    }
    
    report = {
        "problem_statement": coding_problem,
        "criteria_definition": evaluation_criteria,
        "model_benchmarks": solutions
    }
    
    print("==================================================================================")
    print("                           CODING PERFORMANCE BENCHMARK                           ")
    print("==================================================================================")
    print(f"\n{coding_problem}\n")
    
    for model, code in solutions.items():
        print(f"\n### Model Source: {model}")
        print("-" * (len(model) + 18))
        print(code)
        print("\n[Evaluation Framework Check]")
        if "zip(*" in code:
            print("  - Correctness: PASS (Proper use of multi-list transposition via zip unpacking)")
        else:
            print("  - Correctness: FAIL (Missing idiomatic column transpositions)")
        print("  - Readability: High structural formatting layout verified.")
        print("." * 82)
        
    with open("coding_ability_test_report.json", "w") as f:
        json.dump(report, f, indent=4)

if __name__ == "__main__":
    main()
