def calculate_api_cost(input_tokens, output_tokens, price_in_per_million, price_out_per_million):
    # Perform math conversion safely to scale counts down from per-million brackets
    input_cost = (input_tokens / 1_000_000) * price_in_per_million
    output_cost = (output_tokens / 1_000_000) * price_out_per_million
    total_cost = input_cost + output_cost
    
    return input_cost, output_cost, total_cost

def main():
    print("==========================================================================")
    print("                      LLM API COST ESTIMATION CALCULATOR                  ")
    print("==========================================================================")

    # Simulated profile configuration (pricing targets modeled on typical gpt-4o-mini rates)
    model_name = "gpt-4o-mini"
    price_in_m = 0.15   # $0.15 per 1M tokens
    price_out_m = 0.60  # $0.60 per 1M tokens

    # Sample batch workloads processing profiles
    workloads = [
        {"name": "Small Script Execution", "in_tokens": 1500, "out_tokens": 450},
        {"name": "Large Data Pipeline Batch", "in_tokens": 4_500_000, "out_tokens": 1_200_000}
    ]

    print(f"Target Model Configured: {model_name}")
    print(f"Pricing Tiers: Input: ${price_in_m}/1M | Output: ${price_out_m}/1M\n")

    for run in workloads:
        in_c, out_c, total_c = calculate_api_cost(
            run["in_tokens"], run["out_tokens"], price_in_m, price_out_m
        )
        print(f"Workload Profile: {run['name']}")
        print(f"  - Tokens Consumed -> Input: {run['in_tokens']:,} | Output: {run['out_tokens']:,}")
        print(f"  - Input Cost:  ${in_c:.6f}")
        print(f"  - Output Cost: ${out_c:.6f}")
        print(f"  - Total Cost:  ${total_c:.6f}")
        print("-" * 60)

if __name__ == "__main__":
    main()
