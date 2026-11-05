# Day 10 — Building Safer AI Applications

## Learning objective
Explore practical safety controls for application inputs and outputs, moderation, adversarial testing, and user identification.

## Topics and subtopics
1. OpenAI Moderation API.
2. End-user IDs.
3. Adversarial testing.
4. Robust prompting.
5. Constraining inputs and outputs.
6. AI safety best practices.

## Important concepts
- A moderation API can help classify certain content; it is one signal, not a complete safety guarantee.
- End-user identifiers can support provider-side abuse monitoring where supported; use privacy-conscious, non-identifying values as appropriate.
- Adversarial tests probe unexpected or harmful inputs in a controlled environment.
- Input validation, output constraints, robust prompts, and human review can reduce risks but do not replace authorization or application logic.
- Fail safely and surface errors rather than silently treating a failed check as approval.

## Key terminology
Moderation, end-user ID, adversarial testing, input validation, output constraint, safety control, false positive, false negative.

## Learning outcomes
- Explain what moderation and end-user IDs can and cannot do.
- Design input and output checks for a small AI feature.
- Prototype and document a safety filter with explicit failure behavior.