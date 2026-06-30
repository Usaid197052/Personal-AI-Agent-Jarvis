from piper.voice import PiperVoice
import inspect

print(
    inspect.signature(
        PiperVoice.synthesize_wav
    )
)
