import os
from openai import OpenAI

class PromptLibrary:
    def __init__(self):
        # Base reusable templates with variable insertion fields
        self.templates = {
            "coding": (
                "Role: Senior Python Software Engineer\n"
                "Task: Implement a function to solve this task: {task}\n"
                "Constraints: {constraints}\n"
                "Format: Return executable python code inside blocks. Include line comments."
            ),
            "summarization": (
                "Role: Academic Editor\n"
                "Context: Processing core content fields for student revision modules.\n"
                "Task: Summarize the following core text block details down to a punchy, structured format.\n"
                "Length Limit: Max {max_bullets} bullet points.\n"
                "Source Text: {text}"
            ),
            "explanation": (
                "Role: Specialized Subject Expert Instructor\n"
                "Topic: {topic}\n"
                "Target Audience Skill Level: {audience}\n"
                "Task: Explain the core mechanics clearly using an intuitive everyday analogy."
            )
        }

    def generate_prompt(self, template_key, **kwargs):
        if template_key not in self.templates:
            raise KeyError(f"Template '{template_key}' not found in configuration library.")
        return self.templates[template_key].format(**kwargs)

def run_pipeline(prompt_text):
    client = OpenAI()
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt_text}],
        temperature=0.2
    )
    return res.choices.message.content.strip()

def main():
    library = PromptLibrary()
    print("Initializing Prompt Template Engine Tests...\n")

    # Example 1: Testing the Code Generation Template
    code_prompt = library.generate_prompt(
        "coding",
        task="Calculate historical cumulative rolling averages from a numerical matrix stream.",
        constraints="Do not use external dependencies outside standard math modules. Keep it O(N)."
    )
    print("--- Executing Coding Template Generation ---")
    print(run_pipeline(code_prompt))
    print("-" * 70)

    # Example 2: Testing the Summarization Template
    summary_prompt = library.generate_prompt(
        "summarization",
        max_bullets=3,
        text="A Generative Adversarial Network architecture utilizes an adversary strategy pairing two core networks. The Generator network generates synthetically modeled data objects starting out directly from seed noise metrics, whereas the Discriminator runs evaluation matrices verifying real vs fake inputs."
    )
    print("\n--- Executing Academic Summarization Template ---")
    print(run_pipeline(summary_prompt))
    print("-" * 70)

if __name__ == "__main__":
    main()
