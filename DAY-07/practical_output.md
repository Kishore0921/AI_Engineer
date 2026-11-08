# Day 7 Practical — Working AI chatbot using an API

## Practical objective
Integrate the week's concepts in a small chatbot that exchanges user messages with an API-backed model.

## Exact practical output
**Working AI chatbot using an API.**

## Tasks
1. Sketch the flow: user input → application/API request → model response → displayed answer.
2. Implement a minimal chat loop or single-turn chat UI using the documented API.
3. Preserve only the conversation context needed for the exercise and handle API errors clearly.
4. Test a normal question, a follow-up that needs context, empty input, and an API failure path where safely possible.
5. Write a short Week 1 review listing one concept learned, one open question, and one chatbot limitation.

## Expected result
A working, basic API chatbot with a short test record and a Week 1 revision note.

## Completion checklist
- [x] Chatbot sends user input to the API and shows a response.
- [x] Relevant context is handled intentionally.
- [x] Empty input and failures do not appear as successful answers.
- [x] Credentials remain outside source control.
- [x] Week 1 review is saved.

## Save to GitHub
Save code in `DAY-07/code_*.py` and add a run/setup note without secrets. Commit with a message such as `Day 07: integrate a basic API chatbot`.