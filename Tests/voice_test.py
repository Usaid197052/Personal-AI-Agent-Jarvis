from voice.speech_to_text import (
    record_audio,
    transcribe_audio
)


def main():

    print(
        "Voice Test"
    )

    input(
        "\nPress ENTER to start recording..."
    )

    audio_file = record_audio()

    text = transcribe_audio(
        audio_file
    )

    print(
        "\nTranscription:"
    )

    print(text)


if __name__ == "__main__":
    main()