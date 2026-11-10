from tabulate import tablefmt, tabulate  # Uses standard library dictionary or tabulate if installed

def generate_model_comparison_report():
    """Generates a structured overview comparing Open-Weight vs Closed-Source LLMs."""
    
    # Structural metric database
    comparison_data = [
        {
            "Metric": "Deployment",
            "Open-Weight Models": "Self-hosted (AWS, GCP, local hardware, vLLM/Ollama). Requires DevOps overhead.",
            "Closed-Source Models": "Managed API endpoints (OpenAI, Anthropic). Zero infrastructure management."
        },
        {
            "Metric": "Data Privacy",
            "Open-Weight Models": "Absolute control. Data never leaves your private cloud network infrastructure.",
            "Closed-Source Models": "Requires trusting vendor data processing agreements (DPAs) and compliance policies."
        },
        {
            "Metric": "Accessibility",
            "Open-Weight Models": "Gated by hardware capacity (GPUs) but unrestricted usage limits once deployed.",
            "Closed-Source Models": "Instant access globally via API, subject to rate limits and vendor terms of service."
        },
        {
            "Metric": "Customization",
            "Open-Weight Models": "Full fine-tuning access to all weights, layer parameters, and architecture.",
            "Closed-Source Models": "Limited to vendor-provided fine-tuning pipelines or context-window RAG."
        },
        {
            "Metric": "Primary Risk",
            "Open-Weight Models": "High upfront capital expenditure and infrastructure maintenance overhead.",
            "Closed-Source Models": "Vendor lock-in, API deprecation risks, and dynamic runtime pricing shifts."
        }
    ]
    
    print("==================================================================================")
    print("01. OPEN-WEIGHT VS CLOSED-SOURCE MODELS ANALYSIS")
    print("==================================================================================")
    
    # Format structural data output
    headers = ["Evaluation Axis", "Open-Weight Architecture", "Closed-Source API Ecosystem"]
    table_rows = [[item["Metric"], item["Open-Weight Models"], item["Closed-Source Models"]] for item in comparison_data]
    
    print(tabulate(table_rows, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    # Fallback to manual print if tabulate package isn't actively installed in current env
    try:
        generate_model_comparison_report()
    except ImportError:
        # Structured plain-text layout engine
        print("Evaluation Axis | Open-Weight Architecture | Closed-Source API Ecosystem\n" + "-"*80)
        print("Deployment: Self-hosted (Private Cloud/Hardware) vs Managed Third-Party Web API")
        print("Data Privacy: Absolute local data perimeter control vs Contractual DPA Vendor Trust")
        print("Accessibility: Gated by bare-metal computing resources vs Gated by Web API Rate Limits")
