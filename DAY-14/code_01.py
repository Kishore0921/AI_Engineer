#Prerequisites & Setup
#pip install google-genai ollama
'''import os
import time
import json
from datetime import datetime
from google import genai
from google.genai.errors import APIError

LOG_FILE = "hosted_ai_logs.json"
MODEL_NAME = "gemini-2.5-flash"

def save_log(entry):
    """Appends the API interaction log to a JSON file."""
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
    logs.append(entry)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4)

def main():
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable not found.")
        print("Please set it before running this script.")
        return

    client = genai.Client()
    print(f"=== Hosted AI Integration ({MODEL_NAME}) ===")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("Enter prompt: ").strip()
        if prompt.lower() == 'exit':
            break
        if not prompt:
            continue

        start_time = time.perf_counter()
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
            )
            elapsed_time = round(time.perf_counter() - start_time, 2)
            output_text = response.text.strip()

            print(f"\nResponse ({elapsed_time}s):\n{output_text}\n")

            save_log({
                "timestamp": datetime.now().isoformat(),
                "model": MODEL_NAME,
                "prompt": prompt,
                "response": output_text,
                "execution_time_sec": elapsed_time,
                "status": "success"
            })
            print(f"[Logged to {LOG_FILE}]\n")

        except APIError as e:
            elapsed_time = round(time.perf_counter() - start_time, 2)
            print(f"\n[API Error {e.code}]: {e.message}\n")
            save_log({
                "timestamp": datetime.now().isoformat(),
                "model": MODEL_NAME,
                "prompt": prompt,
                "error": str(e),
                "execution_time_sec": elapsed_time,
                "status": "api_error"
            })
        except Exception as e:
            print(f"\n[Unexpected Error]: {e}\n")

if __name__ == "__main__":
    main()
'''