from typing import Dict, Any, List

# Define static enterprise catalog metadata
MODEL_CATALOG = {
    "Reasoning": {
        "Recommended_Family": "o1 / o3-mini / Claude 3.5 Sonnet",
        "Key_Attribute": "Deep multi-step planning, complex math, logical synthesis",
        "Best_Fit": "Closed-Source Reasoning APIs"
    },
    "Coding": {
        "Recommended_Family": "Claude 3.5 Sonnet / Qwen2.5-Coder / DeepSeek-Coder",
        "Key_Attribute": "Syntax correctness, repo-level context, structural generation",
        "Best_Fit": "Hybrid (Specialized Open-Weight or Tier-1 Closed APIs)"
    },
    "Summarization": {
        "Recommended_Family": "Llama-3.1-8B / GPT-4o-mini",
        "Key_Attribute": "High throughput, low latency, processing long context spans cheaply",
        "Best_Fit": "Commodized Open-Weight or Ultra-Low-Cost Closed APIs"
    }
}

def model_selection_engine(task_type: str, constraints: List[str]) -> Dict[str, Any]:
    """Matches workload requirements to optimal architecture profiles."""
    if task_type not in MODEL_CATALOG:
        return {"Error": "Unsupported task category specified."}
        
    specs = MODEL_CATALOG[task_type]
    
    # Rule-based routing engine evaluating explicit operational constraints
    if "strict-privacy" in constraints:
        selected_architecture = "Deploy specialized Open-Weight alternative (e.g., Llama/Qwen) locally."
    elif "low-budget" in constraints and task_type == "Summarization":
        selected_architecture = "Utilize lightweight Open-Weight or subsidized tier-2 API options."
    else:
        selected_architecture = f"Utilize industry baseline: {specs['Recommended_Family']} ({specs['Best_Fit']})"
        
    return {
        "Task Category": task_type,
        "Target Focus": specs["Key_Attribute"],
        "Deployment Recommendation": selected_architecture
    }

# --- Execute Selection Evaluation ---
if __name__ == "__main__":
    print("==================================================")
    print("02. COMPREHENSIVE MODEL SELECTION REPORT")
    print("==================================================")
    
    test_workloads = [
        {"task": "Reasoning", "constraints": ["high-accuracy"]},
        {"task": "Coding", "constraints": ["strict-privacy"]},
        {"task": "Summarization", "constraints": ["low-budget", "high-volume"]}
    ]
    
    for idx, workload in enumerate(test_workloads, 1):
        decision = model_selection_engine(workload["task"], workload["constraints"])
        print(f"\nWorkload Scenario #{idx}:")
        print(f"  Requested Task : {decision['Task Category']}")
        print(f"  User Constraints: {workload['constraints']}")
        print(f"  Evaluation Area : {decision['Target Focus']}")
        print(f"  👉 Final Vector : {decision['Deployment Recommendation']}")
