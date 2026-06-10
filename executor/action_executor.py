from tools.tool_registry import TOOLS


def execute_action(action_name):

    if action_name not in TOOLS:
        return f"Tool '{action_name}' not found."

    return TOOLS[action_name]()