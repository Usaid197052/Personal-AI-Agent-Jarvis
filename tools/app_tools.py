import subprocess

# Used to force applications to open in a new window
NEW_CONSOLE = subprocess.CREATE_NEW_CONSOLE


def open_visual_studio():
    """
    Opens Microsoft Visual Studio 2026.
    """

    try:

        subprocess.Popen(
            r"C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\devenv.exe"
        )

        return "Visual Studio opened successfully."

    except Exception as e:

        return f"Error opening Visual Studio: {e}"


def open_notepad():
    """
    Opens Windows Notepad.
    """

    try:

        subprocess.Popen("notepad.exe")

        return "Notepad opened successfully."

    except Exception as e:

        return f"Error opening Notepad: {e}"


def open_calculator():
    """
    Opens Windows Calculator.
    """

    try:

        subprocess.Popen("calc.exe")

        return "Calculator opened successfully."

    except Exception as e:

        return f"Error opening Calculator: {e}"


def open_cmd():
    """
    Opens a NEW Command Prompt window.
    """

    try:

        subprocess.Popen(
            ["cmd.exe"],
            creationflags=NEW_CONSOLE
        )

        return "Command Prompt opened successfully."

    except Exception as e:

        return f"Error opening Command Prompt: {e}"


def open_powershell():
    """
    Opens a NEW PowerShell window.
    """

    try:

        subprocess.Popen(
            ["powershell.exe"],
            creationflags=NEW_CONSOLE
        )

        return "PowerShell opened successfully."

    except Exception as e:

        return f"Error opening PowerShell: {e}"