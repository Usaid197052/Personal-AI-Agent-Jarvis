import subprocess


def run_python_script(script_path):
    """
    Runs a Python script and captures its output.
    """

    try:

        result = subprocess.run(
            ["python", script_path],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return result.stdout

        return result.stderr

    except Exception as e:

        return f"Error running Python script: {e}"


def run_cmd_command(command):
    """
    Runs a CMD command and returns output.
    """

    try:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        return result.stdout or result.stderr

    except Exception as e:

        return f"Error running CMD command: {e}"


def run_powershell_command(command):
    """
    Runs a PowerShell command and returns output.
    """

    try:

        result = subprocess.run(
            ["powershell", "-Command", command],
            capture_output=True,
            text=True
        )

        return result.stdout or result.stderr

    except Exception as e:

        return f"Error running PowerShell command: {e}"