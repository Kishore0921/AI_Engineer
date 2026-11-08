import os
import json
from openai import OpenAI

def main():
    print("Initializing Playground Behavior Experiment...")
    client = OpenAI()
    
    # Keeping the core request uniform across tests
    user_prompt = "Explain what an index is in a relational database."
    
    # Varying the instructions to observe structural variations in execution quality
    system_variants = {
        "Technical Expert": "You are a senior database administrator. Explain concepts concisely with correct technical terms.",
        "Middle School Teacher": "You are a patient teacher. Explain concepts using basic language and easy real-world analogies.",
        "Minimalist JSON": "You are a data extraction tool. Respond only in valid raw JSON with two keys: 'definition' and 'analogy'."
    }
    
    experiment_log = {}
    
    for identity, instruction in system_variants.items():
        print(f" -> Querying model using instruction configuration: [{identity}]")
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "developer", "content": instruction},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )
        
        experiment_log[identity] = response.choices.message.content.strip()
        
    print("\n======================= PLAYGROUND EXPERIMENT RESULTS =======================")
    for identity, output in experiment_log.items():
        print(f"\n[ SYSTEM INSTRUCTION PROFILE: {identity} ]")
        print("-" * (len(identity) + 30))
        print(output)
        print("." * 77)

    with open("playground_experiment.json", "w") as f:
        json.dump({"prompt": user_prompt, "variants": experiment_log}, f, indent=4)

if __name__ == "__main__":
    main()
