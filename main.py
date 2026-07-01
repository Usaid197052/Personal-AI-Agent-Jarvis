 
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