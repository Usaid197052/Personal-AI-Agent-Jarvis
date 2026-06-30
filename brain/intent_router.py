import json

from brain.ollama_client import ask_jarvis


def classify_intent(user_request):

    prompt = f"""
You are an intent classifier.

Your task is to classify a user request.

Possible intents:

1. action
   - Open applications
   - Create files
   - Delete files
   - Move files
   - Run scripts
   - Run commands
   - Perform system actions

2. chat
   - General questions
   - Explanations
   - Conversation
   - Math questions
   - Knowledge questions

Return ONLY JSON.

Examples:

User:
Open Notepad

Response:
{{"intent":"action"}}

User:
Create a file called notes.txt

Response:
{{"intent":"action"}}

User:
What is 1 + 1?

Response:
{{"intent":"chat"}}

User:
Who created Python?

Response:
{{"intent":"chat"}}

User:
Tell me a joke

Response:
{{"intent":"chat"}}

User Request:
{user_request}
"""

    response = ask_jarvis(prompt)

    try:

        return json.loads(response)

    except Exception:

        return {
            "intent": "chat"
        }