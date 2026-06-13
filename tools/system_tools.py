import os


def shutdown_pc():
    os.system("shutdown /s /t 0")
    return "Shutdown command executed."


def restart_pc():
    os.system("shutdown /r /t 0")
    return "Restart command executed."


def sleep_pc():
    os.system(
        "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
    )
    return "Sleep command executed."