import torch
import json
from transformers import AutoModelForCausalLM, AutoTokenizer

def run_inference(model, tokenizer, prompt):
    messages = [{"role": "user", "content": prompt}]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=100,
        temperature=0.7,
        do_sample=True
    )
    
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

def main():
    model_name = "Qwen/Qwen2.5-0.5B-Instruct"
    
    print(f"Initializing inference environment with {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")
    
    # A set of varied prompts to test and compare outputs
    prompts = [
        "Write a formal one-sentence reminder about submitting code challenges.",
        "Write a casual, enthusiastic one-sentence text about completing code challenges.",
        "Explain what a Discriminator does in a GAN framework in brief."
    ]
    
    experiment_log = []
    
    print("\n--- Running Inference Experiment ---")
    for idx, prompt in enumerate(prompts, 1):
        print(f"Processing Prompt {idx}/{len(prompts)}...")
        response = run_inference(model, tokenizer, prompt)
        
        record = {
            "prompt_id": idx,
            "input_prompt": prompt,
            "generated_output": response
        }
        experiment_log.append(record)
        
    # Compare outputs visually
    print("\n================ EXPERIMENT SUMMARY & COMPARISON ================")
    for record in experiment_log:
        print(f"\n[Prompt {record['prompt_id']}]: {record['input_prompt']}")
        print(f"[Generated Output]:\n{record['generated_output']}")
        print("-" * 50)
        
    # Save the experimental results to a JSON file
    log_filename = "inference_experiment_log.json"
    with open(log_filename, "w") as f:
        json.dump(experiment_log, f, indent=4)
    print(f"\nExperiment data recorded successfully to '{log_filename}'.")

if __name__ == "__main__":
    main()
