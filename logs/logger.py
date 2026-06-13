from datetime import datetime
from pathlib import Path


LOG_FILE = Path("logs/jarvis.log")


def write_log(message):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    log_entry = f"[{timestamp}] {message}\n"

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as log_file:

        log_file.write(log_entry)


def log_request(user_request):

    write_log(
        f"REQUEST: {user_request}"
    )


def log_action(tool_name, arguments):

    write_log(
        f"ACTION: {tool_name} | ARGS: {arguments}"
    )


def log_result(result):

    write_log(
        f"RESULT: {result}"
    )