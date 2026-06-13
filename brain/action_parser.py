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
- Use only the tools listed above.

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
Read notes.txt

Response:
{{"tool":"read_file","arguments":{{"file_path":"notes.txt"}}}}

User:
List files in D:\\Projects\\Jarvis

Response:
{{"tool":"list_files","arguments":{{"folder_path":"D:\\\\Projects\\\\Jarvis"}}}}

User:
Delete notes.txt

Response:
{{"tool":"delete_file","arguments":{{"file_path":"notes.txt"}}}}

User:
Rename hello.py to test.py

Response:
{{"tool":"rename_file","arguments":{{"old_name":"hello.py","new_name":"test.py"}}}}

User:
Move report.csv to D:\\Reports

Response:
{{"tool":"move_file","arguments":{{"source_path":"report.csv","destination_path":"D:\\\\Reports"}}}}

User:
Copy data.csv to backup.csv

Response:
{{"tool":"copy_file","arguments":{{"source_path":"data.csv","destination_path":"backup.csv"}}}}

User:
Run hello.py

Response:
{{"tool":"run_python_script","arguments":{{"script_path":"hello.py"}}}}

User:
Run ipconfig

Response:
{{"tool":"run_cmd_command","arguments":{{"command":"ipconfig"}}}}

User:
Get all running processes

Response:
{{"tool":"run_powershell_command","arguments":{{"command":"Get-Process"}}}}

User:
Shutdown my computer

Response:
{{"tool":"shutdown_pc","arguments":{{}}}}

User:
Restart my computer

Response:
{{"tool":"restart_pc","arguments":{{}}}}

User:
Put my computer to sleep

Response:
{{"tool":"sleep_pc","arguments":{{}}}}

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