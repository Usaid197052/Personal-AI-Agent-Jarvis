from pathlib import Path


def create_file(file_path):
    """
    Creates an empty file.
    """

    try:

        Path(file_path).touch(exist_ok=True)

        return f"File created: {file_path}"

    except Exception as e:

        return f"Error creating file: {e}"


def read_file(file_path):
    """
    Reads file contents.
    """

    try:

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except Exception as e:

        return f"Error reading file: {e}"


def list_files(folder_path):
    """
    Lists files in a folder.
    """

    try:

        folder = Path(folder_path)

        files = [item.name for item in folder.iterdir()]

        return "\n".join(files)

    except Exception as e:

        return f"Error listing files: {e}"