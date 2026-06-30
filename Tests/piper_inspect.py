from piper.voice import PiperVoice

print("PiperVoice methods:\n")

for item in dir(PiperVoice):

    if not item.startswith("_"):

        print(item)
