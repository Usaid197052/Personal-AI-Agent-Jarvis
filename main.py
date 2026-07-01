    if any(
        phrase in text
        for phrase in explicit_phrases
    ):
        return True

    if (
        "jarvis" in text
        and (
            "shutdown" in text
            or "shut down" in text
            or "exit" in text
            or "quit" in text
        )
    ):
        return True

    return False


def main():

    print(
        "Jarvis Voice Assistant"
    )

    print(
        "Waiting for wake word..."
    )

    wait_for_wake_word()

    print(
        "\nJarvis Activated"
    )

    speak(
        "Jarvis is online."
    )

    while True:

        audio_file = record_audio()

        transcription = transcribe_audio(
            audio_file
        )

        print(
            f"\nYou said: {transcription}"
        )

        if not transcription.strip():

            print(
                "No speech detected."
            )

            continue

        normalized_text = (
            transcription
            .lower()
            .strip()
        )

        if is_exit_request(
            normalized_text
        ):

            shutdown_message = (
                "Jarvis shutting down."
            )

            print(
                f"\n{shutdown_message}"
            )

            speak(
                shutdown_message
            )

            log_result(
                "Voice session terminated."
            )

            break

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