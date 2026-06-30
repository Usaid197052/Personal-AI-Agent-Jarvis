import pyttsx3

while True:

    text = input("\nText: ")

    if text.lower() == "exit":
        break

    engine = pyttsx3.init()

    engine.say(text)

    engine.runAndWait()

    print("Done")
