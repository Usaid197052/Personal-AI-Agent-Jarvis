from tools.tool_registry import TOOLS


def execute_action(tool_name, arguments):

    if tool_name not in TOOLS:
        return f"Tool '{tool_name}' not found."

    tool_function = TOOLS[tool_name]

    try:
        return tool_function(**arguments)

    except Exception as e:
        return f"Execution Error: {e}"