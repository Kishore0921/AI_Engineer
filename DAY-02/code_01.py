import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def main():
    # Define a lightweight, high-performing open-source model
    model_name = "Qwen/Qwen2.5-0.5B-Instruct"
    
    print(f"Loading pretrained model and tokenizer: {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, 
        torch_dtype="auto", 
        device_map="auto"
    )
    
    # Define the text prompt
    prompt = "Explain the core concept of Transfer Learning in machine learning in two sentences."
    
    # Format the prompt using the model's standard chat template
    messages = [{"role": "user", "content": prompt}]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    
    print("\n--- Generating Response ---")
    print(f"Prompt: {prompt}\n")
    
    # Tokenize input and move to the same device as the model
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    
    # Generate text output
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=150,
        temperature=0.7,
        do_sample=True
    )
    
    # Trim the input tokens out of the generation history to isolate the response
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    
    # Decode and display the result
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    print(f"Model Response:\n{response}")

if __name__ == "__main__":
    main()