   
        log_request(
            transcription
        )

        intent = classify_intent(
            transcription
        )

        print(
            f"\nIntent: {intent}"
        )

        # ==========================
        # CHAT REQUEST
        # ==========================
        if intent["intent"] == "chat":

            response = chat_with_jarvis(
                transcription
            )

            print(
                f"\nJarvis: {response}"
            )

            speak(
                response
            )

            log_result(
                response
            )

            continue

        # ==========================
        # ACTION REQUEST
        # ==========================
        action = parse_action(
            transcription
        )

        print(
            "\nParsed Action:"
        )

        print(
            action
        )

        if action.get("tool") is None:

            message = (
                "Unable to determine action."
            )

            print(
                f"\n{message}"
            )

            speak(
                message
            )

            continue

        tool_name = action["tool"]

        log_action(
            tool_name,
            action["arguments"]
        )

        if requires_confirmation(
            tool_name
        ):

            approval = input(
                f"\nJarvis wants to execute '{tool_name}'. Proceed? (Y/N): "
            )

            if approval.lower() != "y":

                message = (
                    "Action cancelled."
                )

                print(
                    f"\n{message}"
                )

                speak(
                    message
                )

                log_result(
                    "Action cancelled by user."
                )

                continue

        result = execute_action(
            tool_name,
            action["arguments"]
        )

        print(
            f"\nResult:\n{result}"
        )

        speak(
            result
        )

        log_result(
            result
        )


if __name__ == "__main__":
    main()