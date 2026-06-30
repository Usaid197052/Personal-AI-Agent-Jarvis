
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

for index, voice in enumerate(voices):

    print(f"\nVoice #{index}")

    print(f"Name: {voice.name}")

    print(f"ID: {voice.id}")