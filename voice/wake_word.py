import time

import sounddevice as sd
import numpy as np

from openwakeword.model import Model

from logs.logger import (
    log_wakeword
)


SAMPLE_RATE = 16000
CHUNK_SIZE = 1280

DETECTION_THRESHOLD = 0.85

COOLDOWN_SECONDS = 3


LAST_TTS_TIME = 0


print(
    "Loading wake word model..."
)

model = Model(
    wakeword_models=["hey_jarvis"],
    inference_framework="onnx"
)

print(
    "Wake word model loaded."
)


def pause_wake_word(seconds=5):

    global LAST_TTS_TIME

    LAST_TTS_TIME = (
        time.time() + seconds
    )


def wait_for_wake_word():

    print(
        "\nListening for wake word..."
    )

    last_detection = 0

    detected = False

    def audio_callback(
        indata,
        frames,
        time_info,
        status
    ):

        nonlocal detected
        nonlocal last_detection

        if status:
            return

        # Ignore microphone while
        # Jarvis has recently spoken
        if time.time() < LAST_TTS_TIME:
            return

        audio = (
            indata
            .flatten()
            .astype(np.int16)
        )

        predictions = model.predict(
            audio
        )

        score = predictions.get(
            "hey_jarvis",
            0
        )

        if score > 0.3:

            print(
                f"Wake score: {score:.2f}"
            )

        current_time = time.time()

        if (
            score > DETECTION_THRESHOLD
            and current_time - last_detection
            > COOLDOWN_SECONDS
        ):

            print(
                f"\nWake word detected "
                f"({score:.2f})"
            )

            log_wakeword(
                score
            )

            last_detection = current_time

            detected = True

    with sd.InputStream(
        channels=1,
        samplerate=SAMPLE_RATE,
        dtype="int16",
        blocksize=CHUNK_SIZE,
        callback=audio_callback
    ):

        while not detected:
            time.sleep(0.1)