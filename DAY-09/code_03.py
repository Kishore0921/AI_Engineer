from typing import Dict, Any

# --- 1. Scenario Simulation ---
def mock_loan_approval_model(profile: Dict[str, Any]) -> Dict[str, Any]:
    """
    Simulates a flawed loan approval model scoring engine.
    Demonstrates historical proxy bias via zip codes/background metrics.
    """
    base_score = 600
    
    # Financial metrics (Fair factors)
    base_score += int(profile['income'] / 1000)
    
    # Proxy / Biased metrics (Unfair real-world correlations)
    # Fictional Profile A lives in an affluent tech hub zip code
    if profile['zip_code'] == "94025": 
        base_score += 150
    # Fictional Profile B lives in an historically underfunded industrial zip code
    elif profile['zip_code'] == "48201":
        base_score -= 50
        
    status = "Approved" if base_score >= 700 else "Denied"
    
    return {"score": base_score, "status": status}

# --- 2. Build Fictional Profiles ---
profiles = {
    "Profile_A_TechHub": {
        "name": "Alex",
        "income": 80000,
        "zip_code": "94025",
        "demographic_group": "Group X"
    },
    "Profile_B_Industrial": {
        "name": "Jordan",
        "income": 80000, 
        "zip_code": "48201",
        "demographic_group": "Group Y"
    }
}

# --- 3. Generate Evaluation Report ---
print("==================================================")
print("03. AI BIAS AND FAIRNESS EVALUATION REPORT")
print("==================================================")

results = {}
for key, profile in profiles.items():
    results[key] = mock_loan_approval_model(profile)
    print(f"\nUser Profile: {profile['name']} ({profile['demographic_group']})")
    print(f"  Attributes: Income: ${profile['income']}, Zip Code: {profile['zip_code']}")
    print(f"  Model Output: Score: {results[key]['score']}, Decision: {results[key]['status']}")

print("\n--------------------------------------------------")
print("FAIRNESS ANALYSIS")
print("--------------------------------------------------")

score_gap = abs(results["Profile_A_TechHub"]["score"] - results["Profile_B_Industrial"]["score"])
print(f"Disparity Identified: Credit score gap of {score_gap} points between identical incomes.")

if results["Profile_A_TechHub"]["status"] != results["Profile_B_Industrial"]["status"]:
    print("Conclusion: ❌ UNFAIR OUTCOME DETECTED.")
    print("Reasoning: Zip code parameters act as an active proxy bias, creating systemic disparities for equal income brackets.")
else:
    print("Conclusion: ✅ Fair systemic outcome observed across target groups.")
