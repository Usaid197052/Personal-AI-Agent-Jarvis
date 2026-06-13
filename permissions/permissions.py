DANGEROUS_TOOLS = {
    "shutdown_pc",
    "restart_pc",
    "sleep_pc",
    "delete_file"
}


def requires_confirmation(tool_name):
    """
    Returns True if a tool requires user approval.
    """

    return tool_name in DANGEROUS_TOOLS