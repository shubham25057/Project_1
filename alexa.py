import speech_recognition as sr
import pyttsx3

listener=sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Lisnenig...")
        voice=listener.listen(source)
        command=listener.recognitize_google(voice)
        command=command.lower()
        if "adam" in command:
            print(command)


except:
    pass

