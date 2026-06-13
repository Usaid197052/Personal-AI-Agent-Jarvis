from permissions.permissions import requires_confirmation


print("shutdown_pc:",
      requires_confirmation("shutdown_pc"))

print("open_notepad:",
      requires_confirmation("open_notepad"))