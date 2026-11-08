import os
import json
from openai import OpenAI

def main():
    print("Initializing Hyperparameter Temperature Experiment...")
    client = OpenAI()
    
    creative_prompt = "Write a unique, abstract title and a one-sentence tagline for a sci-fi book about time travel."
    
    # Test discrete temperature thresholds to observe creativity vs. predictability
    temperature_settings = [0.0, 0.7, 1.4]
    experiment_log = []
    
    for temp in temperature_settings:
        print(f" -> Generating with temperature set to: {temp}")
        
        # We run the generation twice per temperature setting to check for consistency/variance
        runs = []
        for run_id in range(1, 3):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "developer", "content": "You are a creative novelist."},
                    {"role": "user", "content": creative_prompt}
                ],
                temperature=temp,
                max_tokens=60
            )
            runs.append(response.choices.message.content.strip())
            
        experiment_log.append({
            "temperature": temp,
            "iteration_1": runs[0],
            "iteration_2": runs[1]
        })
        
    print("\n======================= TEMPERATURE VARIANCE ANALYSIS =======================")
    for record in experiment_log:
        print(f"\n[ Temperature: {record['temperature']} ]")
        print(f"  Run 1: {record['iteration_1']}")
        print(f"  Run 2: {record['iteration_2']}")
        print("-" * 77)

    with open("temperature_experiment.json", "w") as f:
        json.dump(experiment_log, f, indent=4)

if __name__ == "__main__":
    main()
