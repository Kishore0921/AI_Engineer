import json

def main():
    # Common questions types to test quality thresholds
    evaluation_tasks = [
        {"id": 1, "task_type": "Algorithmic Code Generation", "description": "Solving array manipulations."},
        {"id": 2, "task_type": "Conceptual Summarization", "description": "Explaining complex technical terms simplified."},
        {"id": 3, "task_type": "Context Processing Stability", "description": "Handling long context prompts reliably."}
    ]
    
    # Structural metric matrix containing scored targets for the five provider platforms
    # Speed is listed as tokens/sec. Cost targets are listed per 1M tokens combined input/output averages.
    model_performance_data = [
        {"Model/Provider": "OpenAI (GPT-4o-mini)", "Quality (1-10)": 8.8, "Speed (t/s)": 85, "Cost ($/1M)": 0.30, "Best Suited For": "General Workflow Automation"},
        {"Model/Provider": "Anthropic (Claude Haiku)", "Quality (1-10)": 8.6, "Speed (t/s)": 95, "Cost ($/1M)": 0.50, "Best Suited For": "Strict Structural Logic & Coding"},
        {"Model/Provider": "Google Gemini (Flash)", "Quality (1-10)": 8.2, "Speed (t/s)": 110, "Cost ($/1M)": 0.15, "Best Suited For": "High Context / Multimodal Data"},
        {"Model/Provider": "Meta Llama 3.1 (Groq)", "Quality (1-10)": 8.0, "Speed (t/s)": 240, "Cost ($/1M)": 0.10, "Best Suited For": "Ultra-Low Latency Pipelines"},
        {"Model/Provider": "Mistral AI (Small)", "Quality (1-10)": 7.9, "Speed (t/s)": 65, "Cost ($/1M)": 0.20, "Best Suited For": "Sovereign / European Deployments"}
    ]
    
    print("==========================================================================================================")
    print("                                      MODEL EVALUATION METRIC REPORT                                      ")
    print("==========================================================================================================")
    
    # Print formatted Markdown Table structure for easy scan readouts
    headers = ["Model/Provider", "Quality (1-10)", "Speed (t/s)", "Cost ($/1M)", "Best Suited For"]
    table_format = "| {:<23} | {:<14} | {:<11} | {:<11} | {:<32} |"
    
    print(table_format.format(*headers))
    print(table_format.format("-" * 23, "-" * 14, "-" * 11, "-" * 11, "-" * 32))
    
    for row in model_performance_data:
        print(table_format.format(
            row["Model/Provider"],
            row["Quality (1-10)"],
            row["Speed (t/s)"],
            f"${row['Cost ($/1M)']:.2f}",
            row["Best Suited For"]
        ))
        
    print("==========================================================================================================")
    
    report_output = {
        "evaluation_tasks": evaluation_tasks,
        "performance_matrix": model_performance_data
    }
    
    with open("model_evaluation_report.json", "w") as f:
        json.dump(report_output, f, indent=4)
    print("\nReport matrix structural JSON records written out cleanly to 'model_evaluation_report.json'.")

if __name__ == "__main__":
    main()
