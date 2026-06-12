from brain.action_parser import parse_action


while True:

    request = input("You: ")

    if request.lower() == "exit":
        break

    action = parse_action(request)

    print(action)