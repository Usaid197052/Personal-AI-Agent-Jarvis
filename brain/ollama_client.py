from ollama import chat


def ask_jarvis(prompt):
    """
    Sends a prompt to Ollama and returns the response.
    """

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]