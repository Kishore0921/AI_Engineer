import re
from typing import Dict, Any

# --- 1. Core Logic ---
EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
PHONE_REGEX = r'\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}'

def check_and_mask_input(user_input: str) -> Dict[str, Any]:
    """Detects PII patterns, masks them, and logs warnings."""
    warnings = []
    masked_text = user_input
    
    # Find emails
    emails = re.findall(EMAIL_REGEX, user_input)
    if emails:
        warnings.append(f"Detected {len(emails)} email address(es).")
        for email in emails:
            masked_text = masked_text.replace(email, "[MASKED_EMAIL]")
            
    # Find phone numbers (basic filter to avoid matching short standard numbers/IDs)
    phones = re.findall(PHONE_REGEX, user_input)
    # Filter out short strings that regex might catch but aren't phones
    valid_phones = [p for p in phones if len(re.sub(r'\D', '', p)) >= 7]
    
    if valid_phones:
        warnings.append(f"Detected {len(valid_phones)} phone number(s).")
        for phone in valid_phones:
            masked_text = masked_text.replace(phone, "[MASKED_PHONE]")
            
    return {
        "original": user_input,
        "masked": masked_text,
        "warnings": warnings,
        "risk_detected": len(warnings) > 0
    }

# --- 2. Test Inputs ---
sample_inputs = [
    "Hello, my name is John Doe. Can you look up my account?",
    "Hey, I need help fast. Email me at sarah.smith@example.com or call my cell +1-555-019-2834.",
    "The client told me to update their primary contact to contact@startup.io and primary phone to 555.234.5678 instantly."
]

# --- 3. Execute and Run Report ---
print("==================================================")
print("02. PRIVACY RISK CHECKER REPORT")
print("==================================================")

for idx, current_input in enumerate(sample_inputs, 1):
    result = check_and_mask_input(current_input)
    print(f"\nScenario #{idx}")
    print(f"Raw Input:      {result['original']}")
    print(f"Masked Output:  {result['masked']}")
    
    if result['risk_detected']:
        print("Privacy Alerts:")
        for warning in result['warnings']:
            print(f"  ⚠️  {warning}")
    else:
        print("Privacy Alerts: ✅ Clean input. No PII detected.")
