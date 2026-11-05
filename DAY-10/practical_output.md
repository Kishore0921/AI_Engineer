# Day 10 Practical — Build an AI safety filter prototype with input checks and moderation experiments

## Practical objective
Prototype a layered safety check for a small AI interaction and observe moderation behavior.

## Exact practical output
**Build an AI safety filter prototype with input checks and moderation experiments.**

## Tasks
1. Define the prototype's intended use and a small set of allowed and disallowed input examples.
2. Add basic input checks appropriate to that scope (for example, empty/oversized input handling); keep them separate from content moderation.
3. If an authorized moderation API is available, test representative, non-sensitive examples and record categories/results. Otherwise document the unavailable dependency and retain a mock-free manual experiment plan.
4. Handle moderation/API failure explicitly; do not treat a failed check as safe approval.
5. Document end-user ID handling where supported, privacy considerations, false-positive/negative limits, and follow-up adversarial tests.

## Expected result
A small safety-filter prototype or clearly bounded experiment record showing input checks, moderation observations, and failure behavior.

## Completion checklist
- [ ] Intended use and test examples are documented.
- [ ] Input checks are implemented or specified.
- [ ] Moderation behavior or access limitation is recorded accurately.
- [ ] Failures are not silently allowed through.
- [ ] Privacy and moderation limitations are noted.

## Save to GitHub
Save prototype code in `DAY-10/code_*.py` and the experiment notes here. Commit with a message such as `Day 10: prototype AI safety checks`.