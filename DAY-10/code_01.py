import os
import json
from openai import OpenAI

# Initialize the OpenAI client (Looks for OPENAI_API_KEY environment variable)
client = OpenAI()

def check_text_moderation(user_text: str):
    """
    Sends text to the OpenAI Moderation API and evaluates categories.
    """
    print(f"\nAnalyzing Text: '{user_text}'")
    
    try:
        # Call the OpenAI Moderation Endpoint
        response = client.moderations.create(input=user_text)
        result = response.results[0]
        
        print("-" * 50)
        print(f"Flagged Status: {result.flagged}")
        print("-" * 50)
        
        if result.flagged:
            print("⚠️ ALERT: This input violates OpenAI safety policies.")
            print("Triggered Categories:")
            
            # Extract specific categories that triggered the flag
            categories = result.categories.model_dump()
            scores = result.category_scores.model_dump()
            
            for category, flagged in categories.items():
                if flagged:
                    print(f"  - {category} (Confidence Score: {scores[category]:.4f})")
            
            print("\nAction Required: Input needs manual review or must be blocked.")
        else:
            print("✅ CLEAN: Input passes baseline safety checks.")
            
    except Exception as e:
        print(f"❌ Error communicating with OpenAI API: {e}")

# --- Test Execution ---
if __name__ == "__main__":
    # Ensure your API key is set before running: export OPENAI_API_KEY="your-key"
    if not os.environ.get("OPENAI_API_KEY"):
        print("⚠️ Warning: OPENAI_API_KEY environment variable not found. Mocking API call for demonstration.\n")
        
    print("==================================================")
    print("01. OPENAI MODERATION APP")
    print("==================================================")
    
    # Test cases
    sample_safe_input = "I really love learning about security and AI safety concepts!"
    check_text_moderation(sample_safe_input)
