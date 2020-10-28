import datetime
import shutil

import pyttsx3
import speech_recognition as sr

MALE_VOICE = 0
FEMALE_VOICE = 1

VOICE = 1
TEXT = 0
ASSISTANT_STATE = VOICE
ASSISTANT_NAME = "RORA"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetings():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    assistant_name = ASSISTANT_NAME
    speak("I am your Assistant {}".format(assistant_name))


def user_name():
    speak("What should i call you?")
    uname = takeCommand()
    speak("Welcome {}".format(uname))
    columns = shutil.get_terminal_size().columns
    print("Welcome", uname.center(columns))
    speak("How can i Help you")


def takeCommand():
    if ASSISTANT_STATE == VOICE:
        r = sr.Recognizer()
        query: str
        with sr.Microphone() as source:

            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-US')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Unable to Recognizing your voice.")
            return "None"
    else:
        print("Waiting...")
        query = input("Type here: ")
        print(f"User said: {query}\n")

    return query
