from tools.app_tools import (
    open_visual_studio,
    open_notepad,
    open_calculator,
    open_cmd,
    open_powershell
)

from tools.file_tools import (
    create_file,
    read_file,
    list_files,
    delete_file,
    rename_file,
    move_file,
    copy_file
)

from tools.terminal_tools import (
    run_python_script,
    run_cmd_command,
    run_powershell_command
)

from tools.system_tools import (
    shutdown_pc,
    restart_pc,
    sleep_pc
)


TOOLS = {

    # Application Tools
    "open_visual_studio": open_visual_studio,
    "open_notepad": open_notepad,
    "open_calculator": open_calculator,
    "open_cmd": open_cmd,
    "open_powershell": open_powershell,

    # File Tools
    "create_file": create_file,
    "read_file": read_file,
    "list_files": list_files,
    "delete_file": delete_file,
    "rename_file": rename_file,
    "move_file": move_file,
    "copy_file": copy_file,

    # Terminal Tools
    "run_python_script": run_python_script,
    "run_cmd_command": run_cmd_command,
    "run_powershell_command": run_powershell_command,

    # System Tools
    "shutdown_pc": shutdown_pc,
    "restart_pc": restart_pc,
    "sleep_pc": sleep_pc
}