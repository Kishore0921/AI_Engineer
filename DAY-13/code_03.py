'''import time
import csv
import os
import ollama

# Configure the two local models you want to compare
MODEL_A = "llama3.2"
MODEL_B = "mistral"
OUTPUT_FILE = "model_comparison_results.csv"

def benchmark_model(model_name, prompt):
    """Sends a prompt to a model and measures generation time."""
    start_time = time.perf_counter()
    
    response = ollama.chat(
        model=model_name,
        messages=[{'role': 'user', 'content': prompt}]
    )
    
    end_time = time.perf_counter()
    elapsed_time = round(end_time - start_time, 2)
    output_text = response['message']['content'].strip()
    
    return output_text, elapsed_time

def record_to_csv(prompt, res_a, time_a, res_b, time_b):
    """Appends the comparison results to a CSV file."""
    file_exists = os.path.isfile(OUTPUT_FILE)
    
    with open(OUTPUT_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                "Prompt", 
                f"{MODEL_A} Time (s)", f"{MODEL_A} Response", 
                f"{MODEL_B} Time (s)", f"{MODEL_B} Response"
            ])
        writer.writerow([prompt, time_a, res_a, time_b, res_b])

def main():
    print(f"=== Local LLM Benchmark: {MODEL_A} vs {MODEL_B} ===")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("Enter test prompt: ").strip()
        
        if prompt.lower() == 'exit':
            break
        if not prompt:
            continue

        try:
            print(f"\nRunning {MODEL_A}...")
            res_a, time_a = benchmark_model(MODEL_A, prompt)
            
            print(f"Running {MODEL_B}...")
            res_b, time_b = benchmark_model(MODEL_B, prompt)

            # Display Comparison
            print("\n" + "="*50)
            print(f"MODEL A: {MODEL_A} | Time: {time_a}s")
            print("-" * 50)
            print(res_a)
            
            print("\n" + "="*50)
            print(f"MODEL B: {MODEL_B} | Time: {time_b}s")
            print("-" * 50)
            print(res_b)
            print("="*50 + "\n")

            # Save results
            record_to_csv(prompt, res_a, time_a, res_b, time_b)
            print(f"Results saved to {OUTPUT_FILE}\n")

        except Exception as e:
            print(f"\nError during execution: {e}")
            print(f"Ensure both '{MODEL_A}' and '{MODEL_B}' are installed via 'ollama pull'.\n")

if __name__ == "__main__":
    main()
'''


# prerequisites
#pip install transformers torch ollama