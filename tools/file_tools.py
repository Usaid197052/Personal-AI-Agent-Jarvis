from pathlib import Path
import shutil


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


def delete_file(file_path):
    """
    Deletes a file.
    """

    try:

        Path(file_path).unlink()

        return f"File deleted: {file_path}"

    except Exception as e:

        return f"Error deleting file: {e}"


def rename_file(old_name, new_name):
    """
    Renames a file.
    """

    try:

        Path(old_name).rename(new_name)

        return f"Renamed '{old_name}' to '{new_name}'"

    except Exception as e:

        return f"Error renaming file: {e}"


def move_file(source_path, destination_path):
    """
    Moves a file.
    """

    try:

        shutil.move(source_path, destination_path)

        return f"Moved '{source_path}' to '{destination_path}'"

    except Exception as e:

        return f"Error moving file: {e}"


def copy_file(source_path, destination_path):
    """
    Copies a file.
    """

    try:

        shutil.copy2(source_path, destination_path)

        return f"Copied '{source_path}' to '{destination_path}'"

    except Exception as e:

        return f"Error copying file: {e}"