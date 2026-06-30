from brain.intent_router import classify_intent


while True:

    request = input("\nYou: ")

    if request.lower() == "exit":
        break

    result = classify_intent(
        request
    )

    print(result)