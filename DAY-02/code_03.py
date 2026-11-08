import torch
import json
from transformers import AutoModelForCausalLM, AutoTokenizer

def query_model(model, tokenizer, prompt):
    messages = [{"role": "user", "content": prompt}]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=120,
        temperature=0.1,  # Low temperature makes it deterministic to reliably trace limitations
        do_sample=False
    )
    
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

def main():
    model_name = "Qwen/Qwen2.5-0.5B-Instruct"
    
    print(f"Loading {model_name} for boundaries and limitations testing...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")
    
    # Specific edge cases designed to test factual reliability, ambiguity handling, and knowledge gaps
    test_cases = [
        {
            "category": "Factual Verification / Temporal Logic",
            "prompt": "Who is the current Prime Minister of the United Kingdom right now?"
        },
        {
            "category": "Ambiguous / Lacking Context",
            "prompt": "How much does it cost to buy a nice one?"
        },
        {
            "category": "Beyond Known Limits / Future / Unknowable",
            "prompt": "What specific technical updates were introduced in the latest version of PyTorch released exactly two weeks ago?"
        }
    ]
    
    limitation_records = []
    
    print("\n--- Executing Limitations Benchmark ---")
    for test in test_cases:
        print(f"Testing Category: {test['category']}")
        response = query_model(model, tokenizer, test['prompt'])
        
        record = {
            "test_category": test["category"],
            "tested_prompt": test["prompt"],
            "model_response": response,
            "reliability_assessment": "Verify whether the output exhibits hallucination, structural confusion, or a refusal to answer due to real-time information gaps."
        }
        limitation_records.append(record)
        
    print("\n================ LIMITATIONS TESTING RESULTS ================")
    for record in limitation_records:
        print(f"\nCategory: {record['test_category']}")
        print(f"Prompt Given: {record['tested_prompt']}")
        print(f"Model Assessment:\n{record['model_response']}")
        print(f"Analysis Step: {record['reliability_assessment']}")
        print("=" * 60)
        
    # Write the limitations assessment data out to disk
    report_filename = "llm_limitations_report.json"
    with open(report_filename, "w") as f:
        json.dump(limitation_records, f, indent=4)
    print(f"\nLimitations test logging finished. Output saved to '{report_filename}'.")

if __name__ == "__main__":
    main()
