#Prerequisites & Setup
#pip install google-genai ollama
'''import os
import time
import ollama
from google import genai

LOCAL_MODEL = "llama3.2"
HOSTED_MODEL = "gemini-2.5-flash"
REPORT_FILE = "hosted_vs_local_report.md"

def run_local(prompt):
    start = time.perf_counter()
    res = ollama.chat(
        model=LOCAL_MODEL,
        messages=[{'role': 'user', 'content': prompt}]
    )
    elapsed = round(time.perf_counter() - start, 2)
    return res['message']['content'].strip(), elapsed

def run_hosted(client, prompt):
    start = time.perf_counter()
    res = client.models.generate_content(
        model=HOSTED_MODEL,
        contents=prompt
    )
    elapsed = round(time.perf_counter() - start, 2)
    return res.text.strip(), elapsed

def generate_report(prompt, local_res, local_time, hosted_res, hosted_time, quality_note):
    """Generates a comprehensive Markdown comparison report."""
    report_content = f"""# Hosted vs. Local AI Comparison Report

## 1. Test Prompt
> "{prompt}"

## 2. Performance & Cost Metrics

| Metric | Local AI ({LOCAL_MODEL}) | Hosted AI ({HOSTED_MODEL}) |
| :--- | :--- | :--- |
| **Execution Time** | {local_time} seconds | {hosted_time} seconds |
| **API Usage Cost** | $0.00 (Hardware/Electricity only) | Pay-per-token (Cloud API billing) |
| **User Quality Rating** | {quality_note} | (See comparison below) |

## 3. Infrastructure & Privacy Analysis
* **Data Privacy:** Local execution keeps 100% of prompt data on-device. Hosted execution transmits prompts to external cloud servers governed by provider data policies.
* **Infrastructure:** Local relies on local GPU/CPU and RAM limits. Hosted offloads compute to enterprise cloud clusters, requiring zero local GPU hardware.
* **Availability:** Local works completely offline. Hosted requires an active internet connection and relies on provider uptime.

## 4. Model Outputs
### Local Output (`{LOCAL_MODEL}`)
{local_res}

---

### Hosted Output (`{HOSTED_MODEL}`)
{hosted_res}
"""
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report_content)

def main():
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable not set.")
        return

    client = genai.Client()
    print(f"=== Benchmark: Local ({LOCAL_MODEL}) vs Hosted ({HOSTED_MODEL}) ===")
    prompt = input("Enter a prompt to compare: ").strip()
    if not prompt:
        return

    try:
        print(f"\n1. Querying Local Model ({LOCAL_MODEL})...")
        local_res, local_time = run_local(prompt)
        print(f"   Done in {local_time}s.")

        print(f"2. Querying Hosted Model ({HOSTED_MODEL})...")
        hosted_res, hosted_time = run_hosted(client, prompt)
        print(f"   Done in {hosted_time}s.")

        print("\n--- LOCAL RESPONSE ---")
        print(local_res)
        print("\n--- HOSTED RESPONSE ---")
        print(hosted_res)

        print("\n" + "="*40)
        quality_note = input("Enter your quality comparison note (e.g., 'Hosted was more detailed'): ").strip()
        
        generate_report(prompt, local_res, local_time, hosted_res, hosted_time, quality_note)
        print(f"\nSuccess! Full comparison report saved to '{REPORT_FILE}'.")

    except Exception as e:
        print(f"\nExecution failed: {e}")

if __name__ == "__main__":
    main()
'''