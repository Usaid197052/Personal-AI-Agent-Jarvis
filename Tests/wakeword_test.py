import sounddevice as sd
import numpy as np

from openwakeword.model import Model


SAMPLE_RATE = 16000
CHUNK_SIZE = 1280


print("Loading wake word model...")

model = Model(
    wakeword_models=["hey_jarvis"],
    inference_framework="onnx"
)

print("Model loaded successfully.")


def audio_callback(
    indata,
    frames,
    time,
    status
):

    if status:
        print(status)

    audio = (
        indata
        .flatten()
        .astype(np.int16)
    )

    predictions = model.predict(
        audio
    )

    for wakeword, score in predictions.items():

        if score > 0.5:

            print(
                f"\nDetected: {wakeword} "
                f"({score:.2f})"
            )


print("\nWake Word Test Started")
print("Say: 'Hey Jarvis'")
print("Press CTRL+C to stop.\n")


with sd.InputStream(
    channels=1,
    samplerate=SAMPLE_RATE,
    dtype="int16",
    blocksize=CHUNK_SIZE,
    callback=audio_callback
):

    try:

        while True:
            pass

    except KeyboardInterrupt:

        print(
            "\nWake word test stopped."
        )