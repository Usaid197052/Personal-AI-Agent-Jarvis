from brain.action_parser import parse_action
from executor.action_executor import execute_action


while True:

    request = input("\nYou: ")

    if request.lower() == "exit":
        break

    action = parse_action(request)

    print("\nParsed Action:")
    print(action)

    if action.get("tool") is None:
        print("\nError:")
        print(action["error"])
        print(action["raw_response"])
        continue

    result = execute_action(
        action["tool"],
        action["arguments"]
    )

    print("\nResult:")
    print(result)