import json

from brain.ollama_client import ask_jarvis
from tools.tool_registry import TOOLS


def parse_action(user_request):

    available_tools = "\n".join(TOOLS.keys())

    prompt = f"""
You are Jarvis, a desktop AI assistant.

Available tools:

{available_tools}

Your job is to convert the user's request into JSON.

Rules:
- Return ONLY valid JSON.
- No explanations.
- No markdown.
- No extra text.
- Always return a tool and arguments object.
- If no arguments are required, return an empty arguments object.

Examples:

User:
Open Visual Studio

Response:
{{"tool":"open_visual_studio","arguments":{{}}}}

User:
Open Notepad

Response:
{{"tool":"open_notepad","arguments":{{}}}}

User:
Open Calculator

Response:
{{"tool":"open_calculator","arguments":{{}}}}

User:
Open Command Prompt

Response:
{{"tool":"open_cmd","arguments":{{}}}}

User:
Open PowerShell

Response:
{{"tool":"open_powershell","arguments":{{}}}}

User:
Create a file called notes.txt

Response:
{{"tool":"create_file","arguments":{{"file_path":"notes.txt"}}}}

User:
Create a file called report.csv

Response:
{{"tool":"create_file","arguments":{{"file_path":"report.csv"}}}}

User:
Read notes.txt

Response:
{{"tool":"read_file","arguments":{{"file_path":"notes.txt"}}}}

User:
Read requirements.txt

Response:
{{"tool":"read_file","arguments":{{"file_path":"requirements.txt"}}}}

User:
List files in D:\\Projects\\Jarvis

Response:
{{"tool":"list_files","arguments":{{"folder_path":"D:\\\\Projects\\\\Jarvis"}}}}

User Request:
{user_request}
"""

    response = ask_jarvis(prompt)

    try:
        return json.loads(response)

    except Exception as e:

        return {
            "tool": None,
            "arguments": {},
            "error": f"JSON Parse Error: {e}",
            "raw_response": response
        }