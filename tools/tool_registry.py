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
    list_files
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
    "list_files": list_files

}