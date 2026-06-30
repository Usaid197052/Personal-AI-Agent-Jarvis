import sounddevice as sd
from scipy.io.wavfile import write

from faster_whisper import WhisperModel


SAMPLE_RATE = 16000
RECORD_SECONDS = 5

MODEL_SIZE = "small"


model = WhisperModel(
    MODEL_SIZE,
    device="cpu",
    compute_type="int8"
)


def record_audio():

    print(
        "\nRecording... Speak now."
    )

    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(
        "recording.wav",
        SAMPLE_RATE,
        audio
    )

    print(
        "Recording complete."
    )

    return "recording.wav"


def transcribe_audio(audio_path):

    segments, info = model.transcribe(
        audio_path
    )

    text = ""

    for segment in segments:

        text += segment.text + " "

    return text.strip()