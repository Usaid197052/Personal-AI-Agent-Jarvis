from pathlib import Path
import tempfile
import subprocess
import wave

from piper.voice import PiperVoice


MODEL_PATH = (
    Path(__file__).parent
    / "models"
    / "en_US-lessac-medium.onnx"
)

CONFIG_PATH = (
    Path(__file__).parent
    / "models"
    / "en_US-lessac-medium.onnx.json"
)


voice = PiperVoice.load(
    str(MODEL_PATH),
    config_path=str(CONFIG_PATH)
)


def speak(text):

    if not text:
        return

    print(
        f"\nJarvis Speaking: {text}"
    )

    try:

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as temp_file:

            wav_path = temp_file.name

        with wave.open(
            wav_path,
            "wb"
        ) as wav_file:

            voice.synthesize_wav(
                text,
                wav_file
            )

        subprocess.run(
            [
                "powershell",
                "-c",
                (
                    f'(New-Object Media.SoundPlayer '
                    f'"{wav_path}").PlaySync();'
                )
            ],
            check=False
        )

    except Exception as error:

        print(
            f"TTS Error: {error}"
        )