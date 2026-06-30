from brain.chat import chat_with_jarvis


while True:

    request = input("\nYou: ")

    if request.lower() == "exit":
        break

    response = chat_with_jarvis(
        request
    )

    print(
        f"\nJarvis: {response}"
    )